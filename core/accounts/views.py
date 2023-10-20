import os

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView


# Define a view for Facebook login by extending the SocialLoginView.
class FacebookLoginView(SocialLoginView):
    # Set the adapter class for Facebook OAuth2 authentication.
    adapter_class = FacebookOAuth2Adapter
    # Define the callback URL for Facebook authentication, with a fallback to 'http://localhost'.
    callback_url = os.environ.get("FACEBOOK_REDIRECT_URL", "http://localhost")
    # Set the client class for OAuth2 authentication.
    client_class = OAuth2Client


# Define a view for Google login by extending the SocialLoginView.
class GoogleLoginView(SocialLoginView):
    # Set the adapter class for Google OAuth2 authentication.
    adapter_class = GoogleOAuth2Adapter
    # Define the callback URL for Google authentication, with a fallback to 'http://localhost'.
    callback_url = os.environ.get("GOOGLE_REDIRECT_URL", "http://localhost")
    # Set the client class for OAuth2 authentication.
    client_class = OAuth2Client
