from django import forms

from rsvp.models import Rsvp


class RsvpModelForm(forms.ModelForm):
    class Meta:
        model = Rsvp
        fields = ["dietary_restrictions", "shirt_size", "transport_type", "notes"]
