from rest_framework import serializers
from .models import AccountSetting, NotificationSetting, ThemeSetting, PrivacySetting


class AccountSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountSetting
        fields = ['id', 'username', 'email', 'password', 'bio', 'created', 'updated']


class NotificationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSetting
        fields = ['id', 'email_notifications', 'push_notifications', 'notification_frequency']


class ThemeSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeSetting
        fields = ['id', 'color', 'font', 'layout']


class PrivacySettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacySetting
        fields = ['id', 'profile_visibility', 'data_sharing']
