from django.contrib import admin
from pycon.schedule.models import *


class SlotRoomInline(admin.TabularInline):
    model = SlotRoom
    extra = 1


class SlotAdmin(admin.ModelAdmin):
    list_filter = ("day", "kind")
    list_display = ("day", "start", "end", "kind", "proposal")
    #inlines = [SlotRoomInline]


class RoomAdmin(admin.ModelAdmin):
    list_display = ["name", "order"]
    #inlines = [SlotRoomInline]


class PresentationAdmin(admin.ModelAdmin):
    model = Proposal
    list_display = ("title", "speaker", "duration", "level", "language", "status", "cancelled")
    list_filter = ["cancelled", "status"]
    search_fields = ['title']

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "url", "twitter_link")
    search_fields = ('user__email', "user__first_name", "user__last_name")
    #inlines = [SlotRoomInline]

admin.site.register(Day)
admin.site.register(
    SlotKind,
    list_display=["label"],
)
admin.site.register(
    SlotRoom
    #list_display=["slot", "room"]
)
admin.site.register(Room, RoomAdmin)
admin.site.register(Slot, SlotAdmin)
admin.site.register(Session)
admin.site.register(Proposal, PresentationAdmin)
admin.site.register(Speaker, SpeakerAdmin)
