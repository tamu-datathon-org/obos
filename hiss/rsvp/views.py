from typing import Union

from django.conf import settings
from django.contrib.auth import mixins
from django.core import exceptions
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from application.models import Application
from rsvp.forms import RsvpModelForm
from rsvp.models import Rsvp
from user.models import User


class CreateRsvpView(mixins.UserPassesTestMixin, generic.CreateView):
    """
    Creates a new Rsvp and links it to a User if one doesn't already exist and the User's been accepted.
    """

    form_class = RsvpModelForm
    template_name = "rsvp/rsvp_form.html"
    success_url = reverse_lazy("status")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event_start_datetime"] = settings.EVENT_START_DATETIME
        context["event_end_datetime"] = settings.EVENT_END_DATETIME
        return context

    def test_func(self) -> bool:
        # Ensure user is logged-in
        user: User = self.request.user
        if not user.is_authenticated:
            return False
        app: Union[Application, None] = user.application_set.first()

        # User hasn't applied
        if not app:
            return False
        # Their application hasn't been approved (or has been rejected)
        if not app.approved:
            return False
        # They don't have (or missed) an RSVP deadline
        if not user.rsvp_deadline or user.rsvp_deadline < timezone.now():
            return False
        return True

    def get(self, request: HttpRequest, *args, **kwargs):
        if request.user.declined_acceptance:
            return redirect(reverse_lazy("status"))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form: RsvpModelForm):
        if Rsvp.objects.filter(user=self.request.user).exists():
            form.add_error(None, "You've already submitted an RSVP.")
            return self.form_invalid(form)
        rsvp: Rsvp = form.save(commit=False)
        rsvp.user = self.request.user
        rsvp.save()
        return redirect(self.success_url)


class UpdateRsvpView(mixins.UserPassesTestMixin, generic.UpdateView):
    """
    Updates a linked Rsvp.
    """

    success_url = reverse_lazy("status")
    queryset = Rsvp.objects.all()
    form_class = RsvpModelForm
    template_name = "rsvp/rsvp_form.html"

    def test_func(self) -> bool:
        # Ensure user is logged-in
        user: User = self.request.user
        if not user.is_authenticated:
            return False
        app: Union[Application, None] = user.application_set.first()

        # User hasn't applied
        if not app:
            return False
        # Their application hasn't been approved (or has been rejected)
        if not app.approved:
            return False
        # They don't have (or missed) an RSVP deadline
        if not user.rsvp_deadline or user.rsvp_deadline < timezone.now():
            return False
        return True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["event_start_datetime"] = settings.EVENT_START_DATETIME
        context["event_end_datetime"] = settings.EVENT_END_DATETIME
        return context

    def get_object(self, queryset=None) -> Rsvp:
        """
        Checks to make sure that the user actually owns the rsvp requested.
        """
        rsvp: Rsvp = super().get_object()
        if rsvp.user != self.request.user:
            raise PermissionDenied("You don't have permission to view this rsvp")
        return rsvp


class DeclineRsvpView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = "rsvp/rsvp_decline.html"

    def post(self, request: HttpRequest, *_args, **_kwargs):
        if not request.user.application_set.exists():
            raise exceptions.PermissionDenied(
                "You can't decline admission without applying first"
            )
        if not request.user.application_set.first().approved:
            raise exceptions.PermissionDenied(
                "You must have been admitted to decline admission."
            )
        if request.user.rsvp_deadline and request.user.rsvp_deadline < timezone.now():
            raise exceptions.PermissionDenied("Your RSVP deadline has passed.")
        request.user.declined_acceptance = True
        request.user.save()
        return redirect(reverse_lazy("status"))
