from rest_framework import serializers
from .models import AccountSettings, NotificationSettings


class AccountSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountSettings
        fields = ['user', 'username', 'email', 'password', 'bio', 'created', 'updated']


class NotificationSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSettings
        fields = ['user', 'email_notifications', 'push_notifications', 'notification_frequency']
