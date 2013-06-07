from django.contrib import admin
from random101.models import Meeting, Chat101


def generate_101_chats(modeladmin, request, queryset):
    for meeting in queryset:
        meeting.generate_101()
generate_101_chats.short_description = " Generate 101 chats"


class MeetingAdmin(admin.ModelAdmin):
    actions = [generate_101_chats]


def users_101(obj):
    if obj.users.all():
        return "{0} & {1}".format(*[user.username for user in obj.users.all()])
    else:
        return ""
users_101.description = "users"


class Chat101Admin(admin.ModelAdmin):
    list_display = ['meeting', users_101]
    list_filter = ['meeting', 'users']


admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Chat101, Chat101Admin)
