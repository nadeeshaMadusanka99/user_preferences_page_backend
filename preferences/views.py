from rest_framework import viewsets
from .models import AccountSettings, NotificationSettings
from .serializers import AccountSettingsSerializer, NotificationSettingsSerializer


class AccountSettingsViewSet(viewsets.ModelViewSet):
    queryset = AccountSettings.objects.all()
    serializer_class = AccountSettingsSerializer


class NotificationSettingsViewSet(viewsets.ModelViewSet):
    queryset = NotificationSettings.objects.all()
    serializer_class = NotificationSettingsSerializer
