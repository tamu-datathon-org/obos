from django import test
from django.core import exceptions as django_exceptions
from hacker import models as hacker_models

# Create your tests here.


class HackerModelTestCase(test.TestCase):

    def setUp(self):
        self.hacker_fields = {
            'admitted': None,
            'checked_in': None,
            'admitted_datetime': None,
            'checked_in_datetime': None,
            'first_name': 'First',
            'last_name': 'Last',
            'email': 'some@email.com'
        }

    def test_first_name_required(self):
        del self.hacker_fields['first_name']

        hacker_without_first = hacker_models.Hacker(**self.hacker_fields)
        with self.assertRaises(django_exceptions.ValidationError):
            # Runs validation on the model before saving it.
            hacker_without_first.full_clean()

    def test_last_name_required(self):
        del self.hacker_fields['last_name']
        hacker_without_last = hacker_models.Hacker(**self.hacker_fields)

        with self.assertRaises(django_exceptions.ValidationError):
            # Runs validation on the model
            hacker_without_last.full_clean()

    def test_email_required(self):
        del self.hacker_fields['email']
        hacker_without_email = hacker_models.Hacker(**self.hacker_fields)

        with self.assertRaises(django_exceptions.ValidationError):
            # Runs validation on the model
            hacker_without_email.full_clean()
