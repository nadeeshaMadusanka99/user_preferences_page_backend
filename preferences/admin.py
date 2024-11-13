from django.contrib import admin
from .models import AccountSetting, NotificationSetting, ThemeSetting, PrivacySetting


class AccountSettingAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio']


class NotificationSettingAdmin(admin.ModelAdmin):
    list_display = ['email_notifications', 'push_notifications', 'notification_frequency']


class ThemeSettingAdmin(admin.ModelAdmin):
    list_display = ['color', 'font', 'layout']


class PrivacySettingAdmin(admin.ModelAdmin):
    list_display = ['profile_visibility', 'data_sharing']


admin.site.register(AccountSetting, AccountSettingAdmin)
admin.site.register(NotificationSetting, NotificationSettingAdmin)
admin.site.register(ThemeSetting, ThemeSettingAdmin)
admin.site.register(PrivacySetting, PrivacySettingAdmin)
