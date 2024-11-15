from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.exceptions import PermissionDenied, NotFound, MethodNotAllowed

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

    def check_duplicate_for_user(self, user):
        if self.queryset.filter(user=user).exists():
            raise ValidationError(f"A {self.queryset.model.__name__} already exists for this user.")

    def create(self, request, *args, **kwargs):
        # Disable the POST method by raising an exception
        raise MethodNotAllowed("POST", detail="Creating settings is not allowed via this endpoint.")

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except self.queryset.model.DoesNotExist:
            raise NotFound(detail=f"{self.queryset.model.__name__} not found.")
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


def create_extend_schema_view(model_name: str):
    singular_name = model_name
    plural_name = singular_name + "s"

    return extend_schema_view(
        list=extend_schema(tags=[plural_name], description=f"List all {plural_name.lower()}"),
        create=extend_schema(tags=[plural_name], description=f"Create a new {singular_name.lower()}"),
        retrieve=extend_schema(tags=[plural_name], description=f"Retrieve a {singular_name.lower()}"),
        update=extend_schema(tags=[plural_name], description=f"Update a {singular_name.lower()}"),
        partial_update=extend_schema(tags=[plural_name], description=f"Partially update a {singular_name.lower()}"),
        destroy=extend_schema(tags=[plural_name], description=f"Delete a {singular_name.lower()}")
    )


@create_extend_schema_view("Account Setting")
class AccountSettingViewSet(BasePreferenceSettingViewSet):
    serializer_class = AccountSettingSerializer
    queryset = AccountSetting.objects.all()


@create_extend_schema_view("Notification Setting")
class NotificationSettingViewSet(BasePreferenceSettingViewSet):
    serializer_class = NotificationSettingSerializer
    queryset = NotificationSetting.objects.all()


@create_extend_schema_view("Theme Setting")
class ThemeSettingViewSet(BasePreferenceSettingViewSet):
    serializer_class = ThemeSettingSerializer
    queryset = ThemeSetting.objects.all()


@create_extend_schema_view("Privacy Setting")
class PrivacySettingViewSet(BasePreferenceSettingViewSet):
    serializer_class = PrivacySettingSerializer
    queryset = PrivacySetting.objects.all()
