from django.contrib.admin.apps import AdminConfig


class AccountsAdminConfig(AdminConfig):
    default_site = 'admin.SocialAuthAdminSite'
