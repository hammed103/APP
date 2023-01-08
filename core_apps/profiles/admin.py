from django.contrib import admin

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["pkid", "id", "user", "phone_number", "country", "city"]
    list_filter = [ "city"]
    list_display_links = ["id", "pkid"]


admin.site.register(Profile, ProfileAdmin)