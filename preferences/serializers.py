from rest_framework import serializers
from .models import AccountSettings, NotificationSettings


class AccountSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountSettings
        fields = ['username', 'email', 'password', 'bio', 'created', 'updated']


class NotificationSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSettings
        fields = ['email_notifications', 'push_notifications', 'notification_frequency']
