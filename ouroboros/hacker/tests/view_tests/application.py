import json

from django.urls import reverse_lazy

from hacker import models as hacker_models
from shared import test


class ApplicationViewTestCase(test.SharedTestCase):

    def test_redirects_when_not_logged_in(self):
        response = self.client.get(reverse_lazy("application"))
        self.assertRedirects(
            response, f"{reverse_lazy('login')}?next={reverse_lazy('application')}"
        )

    def test_redirects_when_no_active_wave(self):
        self.client.force_login(self.hacker)
        response = self.client.get(reverse_lazy("application"))
        self.assertRedirects(response, reverse_lazy("status"))

    def test_rejects_when_no_active_wave(self):
        self.client.force_login(self.hacker)
        response = self.client.post(reverse_lazy("application"), self.application_fields)
        self.assertEqual(response.status_code, 403)

    def test_associates_application_with_user(self):
        self.create_active_wave()
        self.client.force_login(self.hacker)
        response = self.client.post(reverse_lazy("application"), self.application_fields)
        app = hacker_models.Application.objects.get(hacker=self.hacker)
        self.assertEqual(app.hacker, self.hacker)

    def test_user_can_edit_application_once_submitted(self):
        self.create_active_wave()
        self.client.force_login(self.hacker)
        response = self.client.post(reverse_lazy("application"), self.application_fields)

        app_fields = self.application_fields
        new_major = "ABCDEFG"
        app_fields["major"] = new_major
        response = self.client.post(reverse_lazy("application"), app_fields)

        app = hacker_models.Application.objects.get(hacker=self.hacker)
        self.assertEqual(app.major, new_major)