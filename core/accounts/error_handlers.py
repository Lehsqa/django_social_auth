from rest_framework.views import exception_handler
from allauth.socialaccount.providers.oauth2.client import OAuth2Error
from rest_framework.response import Response


def accounts_exception_handler(exc, context):
    # Check if the exception is an OAuth2Error
    if isinstance(exc, OAuth2Error):
        # Customize the response for OAuth2Error
        response_data = {
            "error": "OAuth2Error",
            "error_description": str(exc),  # Use the exception message as the description
        }
        return Response(response_data, status=400)

    # Handle other exceptions with the default exception handler
    return exception_handler(exc, context)
