from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema
from .models import AccountSetting, NotificationSetting, ThemeSetting, PrivacySetting
from .serializers import AccountSettingSerializer, NotificationSettingSerializer, ThemeSettingSerializer, \
    PrivacySettingSerializer


@extend_schema_view(
    list=extend_schema(tags=["Account Settings"], description="List all account settings"),
    create=extend_schema(tags=["Account Settings"], description="Create a new account setting"),
    retrieve=extend_schema(tags=["Account Settings"], description="Retrieve an account setting"),
    update=extend_schema(tags=["Account Settings"], description="Update an account setting"),
    partial_update=extend_schema(tags=["Account Settings"], description="Partially update an account setting"),
    destroy=extend_schema(tags=["Account Settings"], description="Delete an account setting"),
)
class AccountSettingViewSet(viewsets.ModelViewSet):
    queryset = AccountSetting.objects.all()
    serializer_class = AccountSettingSerializer

@extend_schema_view(
    list=extend_schema(tags=["Notification Settings"], description="List all notification settings"),
    create=extend_schema(tags=["Notification Settings"], description="Create a new notification setting"),
    retrieve=extend_schema(tags=["Notification Settings"], description="Retrieve a notification setting"),
    update=extend_schema(tags=["Notification Settings"], description="Update a notification setting"),
    partial_update=extend_schema(tags=["Notification Settings"], description="Partially update a notification setting"),
    destroy=extend_schema(tags=["Notification Settings"], description="Delete a notification setting"),
)
class NotificationSettingViewSet(viewsets.ModelViewSet):
    queryset = NotificationSetting.objects.all()
    serializer_class = NotificationSettingSerializer

@extend_schema_view(
    list=extend_schema(tags=["Theme Settings"], description="List all theme settings"),
    create=extend_schema(tags=["Theme Settings"], description="Create a new theme setting"),
    retrieve=extend_schema(tags=["Theme Settings"], description="Retrieve a theme setting"),
    update=extend_schema(tags=["Theme Settings"], description="Update a theme setting"),
    partial_update=extend_schema(tags=["Theme Settings"], description="Partially update a theme setting"),
    destroy=extend_schema(tags=["Theme Settings"], description="Delete a theme setting"),
)
class ThemeSettingViewSet(viewsets.ModelViewSet):
    queryset = ThemeSetting.objects.all()
    serializer_class = ThemeSettingSerializer

@extend_schema_view(
    list=extend_schema(tags=["Privacy Settings"], description="List all privacy settings"),
    create=extend_schema(tags=["Privacy Settings"], description="Create a new privacy setting"),
    retrieve=extend_schema(tags=["Privacy Settings"], description="Retrieve a privacy setting"),
    update=extend_schema(tags=["Privacy Settings"], description="Update a privacy setting"),
    partial_update=extend_schema(tags=["Privacy Settings"], description="Partially update a privacy setting"),
    destroy=extend_schema(tags=["Privacy Settings"], description="Delete a privacy setting"),
)
class PrivacySettingViewSet(viewsets.ModelViewSet):
    queryset = PrivacySetting.objects.all()
    serializer_class = PrivacySettingSerializer

    # Assigning a tag to categorize this endpoint under "Privacy Settings"
    @extend_schema(tags=["Privacy Settings"])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
