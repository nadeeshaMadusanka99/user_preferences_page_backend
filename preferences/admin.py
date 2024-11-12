from django.contrib import admin
from .models import AccountSettings, NotificationSettings

admin.site.register(AccountSettings)
admin.site.register(NotificationSettings)