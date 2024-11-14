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
    # queryset = AccountSetting.objects.all()
    serializer_class = AccountSettingSerializer

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            # Superusers can see all account settings
            return AccountSetting.objects.all()
        # Regular users can only see their own account settings
        return AccountSetting.objects.filter(user=user)


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

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return NotificationSetting.objects.all()
        return NotificationSetting.objects.filter(user=user)


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

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return ThemeSetting.objects.all()
        return ThemeSetting.objects.filter(user=user)


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

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return PrivacySetting.objects.all()
        return PrivacySetting.objects.filter(user=user)

