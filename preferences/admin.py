from django.contrib import admin
from .models import AccountSetting, NotificationSetting, ThemeSetting, PrivacySetting


# Define a custom method to get the user's name

class UserNameAdmin(admin.ModelAdmin):
    def user_name(self, obj):
        return obj.user.username

    user_name.short_description = 'User'


class AccountSettingAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'bio']


class NotificationSettingAdmin(UserNameAdmin, admin.ModelAdmin):
    list_display = ['user_name', 'email_notifications', 'push_notifications', 'notification_frequency']


class ThemeSettingAdmin(UserNameAdmin, admin.ModelAdmin):
    list_display = ['user_name', 'color', 'font', 'layout']


class PrivacySettingAdmin(UserNameAdmin, admin.ModelAdmin):
    list_display = ['user_name', 'profile_visibility', 'data_sharing']


admin.site.register(AccountSetting, AccountSettingAdmin)
admin.site.register(NotificationSetting, NotificationSettingAdmin)
admin.site.register(ThemeSetting, ThemeSettingAdmin)
admin.site.register(PrivacySetting, PrivacySettingAdmin)
