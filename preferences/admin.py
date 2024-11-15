from django.contrib import admin
from .models import AccountSetting, NotificationSetting, ThemeSetting, PrivacySetting
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# Custom method to get the user's name in every setting
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

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(AccountSetting, AccountSettingAdmin)
admin.site.register(NotificationSetting, NotificationSettingAdmin)
admin.site.register(ThemeSetting, ThemeSettingAdmin)
admin.site.register(PrivacySetting, PrivacySettingAdmin)
admin.site.register(User, CustomUserAdmin)
