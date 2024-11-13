from rest_framework import viewsets
from .models import AccountSetting, NotificationSetting, ThemeSetting, PrivacySetting
from .serializers import AccountSettingSerializer, NotificationSettingSerializer, ThemeSettingSerializer, \
    PrivacySettingSerializer


class AccountSettingViewSet(viewsets.ModelViewSet):
    queryset = AccountSetting.objects.all()
    serializer_class = AccountSettingSerializer


class NotificationSettingViewSet(viewsets.ModelViewSet):
    queryset = NotificationSetting.objects.all()
    serializer_class = NotificationSettingSerializer


class ThemeSettingViewSet(viewsets.ModelViewSet):
    queryset = ThemeSetting.objects.all()
    serializer_class = ThemeSettingSerializer


class PrivacySettingViewSet(viewsets.ModelViewSet):
    queryset = PrivacySetting.objects.all()
    serializer_class = PrivacySettingSerializer
