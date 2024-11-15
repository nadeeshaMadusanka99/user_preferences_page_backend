from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.exceptions import PermissionDenied, NotFound

from .models import AccountSetting, NotificationSetting, ThemeSetting, PrivacySetting
from .serializers import AccountSettingSerializer, NotificationSettingSerializer, ThemeSettingSerializer, \
    PrivacySettingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError


class BasePreferenceSettingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if not user.is_authenticated:
            raise PermissionDenied("You do not have permission to view this data.")

        if user.is_superuser:
            queryset = self.queryset.all()
        else:
            queryset = self.queryset.filter(user=user)

        if not queryset.exists():
            raise NotFound(detail=f"No {self.queryset.model.__name__} data found for the user.")

        return queryset

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except Exception as e:
            raise ValidationError(f"Error creating object: {str(e)}")

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except self.queryset.model.DoesNotExist:
            raise NotFound(detail=f"{self.queryset.model.__name__} not found.")
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    list=extend_schema(tags=["Account Settings"], description="List all account settings"),
    create=extend_schema(tags=["Account Settings"], description="Create a new account setting"),
    retrieve=extend_schema(tags=["Account Settings"], description="Retrieve an account setting"),
    update=extend_schema(tags=["Account Settings"], description="Update an account setting"),
    partial_update=extend_schema(tags=["Account Settings"], description="Partially update an account setting"),
    destroy=extend_schema(tags=["Account Settings"], description="Delete an account setting"),
)
class AccountSettingViewSet(BasePreferenceSettingViewSet):
    serializer_class = AccountSettingSerializer
    queryset = AccountSetting.objects.all()


@extend_schema_view(
    list=extend_schema(tags=["Notification Settings"], description="List all notification settings"),
    create=extend_schema(tags=["Notification Settings"], description="Create a new notification setting"),
    retrieve=extend_schema(tags=["Notification Settings"], description="Retrieve a notification setting"),
    update=extend_schema(tags=["Notification Settings"], description="Update a notification setting"),
    partial_update=extend_schema(tags=["Notification Settings"], description="Partially update a notification setting"),
    destroy=extend_schema(tags=["Notification Settings"], description="Delete a notification setting"),
)
class NotificationSettingViewSet(BasePreferenceSettingViewSet):
    serializer_class = NotificationSettingSerializer
    queryset = NotificationSetting.objects.all()


@extend_schema_view(
    list=extend_schema(tags=["Theme Settings"], description="List all theme settings"),
    create=extend_schema(tags=["Theme Settings"], description="Create a new theme setting"),
    retrieve=extend_schema(tags=["Theme Settings"], description="Retrieve a theme setting"),
    update=extend_schema(tags=["Theme Settings"], description="Update a theme setting"),
    partial_update=extend_schema(tags=["Theme Settings"], description="Partially update a theme setting"),
    destroy=extend_schema(tags=["Theme Settings"], description="Delete a theme setting"),
)
class ThemeSettingViewSet(BasePreferenceSettingViewSet):
    serializer_class = ThemeSettingSerializer
    queryset = ThemeSetting.objects.all()


@extend_schema_view(
    list=extend_schema(tags=["Privacy Settings"], description="List all privacy settings"),
    create=extend_schema(tags=["Privacy Settings"], description="Create a new privacy setting"),
    retrieve=extend_schema(tags=["Privacy Settings"], description="Retrieve a privacy setting"),
    update=extend_schema(tags=["Privacy Settings"], description="Update a privacy setting"),
    partial_update=extend_schema(tags=["Privacy Settings"], description="Partially update a privacy setting"),
    destroy=extend_schema(tags=["Privacy Settings"], description="Delete a privacy setting"),
)
class PrivacySettingViewSet(BasePreferenceSettingViewSet):
    serializer_class = PrivacySettingSerializer
    queryset = PrivacySetting.objects.all()
