from django.contrib import admin


# Define a custom admin site by extending the AdminSite class.
class SocialAuthAdminSite(admin.AdminSite):
    # Customize the title displayed in the admin site's header.
    title_header = 'Social Auth Admin'
    # Customize the text displayed in the browser's title bar.
    site_header = 'Social Auth administration'
    # Customize the title displayed on the admin site's index page.
    index_title = 'Social Auth site admin'
