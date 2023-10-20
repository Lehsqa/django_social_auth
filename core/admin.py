from django.contrib import admin


class SocialAuthAdminSite(admin.AdminSite):
    title_header = 'Social Auth Admin'
    site_header = 'Social Auth administration'
    index_title = 'Social Auth site admin'
