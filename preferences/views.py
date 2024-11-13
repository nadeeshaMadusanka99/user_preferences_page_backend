from rest_framework import viewsets
from .models import AccountSetting, NotificationSetting
from .serializers import AccountSettingSerializer, NotificationSettingSerializer


class AccountSettingViewSet(viewsets.ModelViewSet):
    queryset = AccountSetting.objects.all()
    serializer_class = AccountSettingSerializer


class NotificationSettingViewSet(viewsets.ModelViewSet):
    queryset = NotificationSetting.objects.all()
    serializer_class = NotificationSettingSerializer
