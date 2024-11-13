from django.contrib import admin
from .models import AccountSetting, NotificationSetting

admin.site.register(AccountSetting)
admin.site.register(NotificationSetting)