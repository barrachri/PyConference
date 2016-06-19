from django.contrib import admin
from pycon.volunteers.models import Volunteer


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')


admin.site.register(Volunteer, VolunteerAdmin)
