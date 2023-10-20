from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.providers.oauth2.client import OAuth2Error


# Define a test case class for FacebookLoginView.
class FacebookLoginViewTestCase(TestCase):
    def setUp(self):
        # Init Facebook object (need to set client_id and secret).
        self.client = APIClient()
        self.facebook_app = SocialApp.objects.create(
            provider='facebook',
            name='Facebook',
            client_id='',
            secret='',
        )

    def test_facebook_login_view(self):
        # Test when there are no errors.
        url = reverse('facebook_login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(self.facebook_app.client_id, response.url)

    def test_facebook_login_view_failure(self):
        # Test when there is an OAuth2Error.
        self.facebook_app.secret = 'invalid-secret'
        self.facebook_app.save()
        url = reverse('facebook_login')
        with self.assertRaises(OAuth2Error):
            self.client.get(url)


# Define a test case class for GoogleLoginView.
class GoogleLoginViewTestCase(TestCase):
    def setUp(self):
        # Init Google object (need to set client_id and secret).
        self.client = APIClient()
        self.google_app = SocialApp.objects.create(
            provider='google',
            name='Google',
            client_id='',
            secret='',
        )

    def test_google_login_view(self):
        # Test when there are no errors.
        url = reverse('google_login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(self.google_app.client_id, response.url)

    def test_google_login_view_failure(self):
        # Test when there is an OAuth2Error.
        self.google_app.secret = 'invalid-secret'
        self.google_app.save()
        url = reverse('google_login')
        with self.assertRaises(OAuth2Error):
            self.client.get(url)
