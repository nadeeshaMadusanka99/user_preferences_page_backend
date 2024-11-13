from django.contrib import admin
from .models import AccountSetting, NotificationSetting

class AccountSettingAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio']

class NotificationSettingAdmin(admin.ModelAdmin):
    list_display = ['email_notifications', 'push_notifications', 'notification_frequency']

admin.site.register(AccountSetting, AccountSettingAdmin)
admin.site.register(NotificationSetting, NotificationSettingAdmin)