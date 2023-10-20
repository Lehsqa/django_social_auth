from django.contrib.admin.apps import AdminConfig


# Define a custom AdminConfig class named AccountsAdminConfig.
class AccountsAdminConfig(AdminConfig):
    # Specify a custom admin site to be used as the default for the AccountsAdminConfig.
    # In this case, it's set to 'admin.SocialAuthAdminSite'.
    default_site = 'admin.SocialAuthAdminSite'
