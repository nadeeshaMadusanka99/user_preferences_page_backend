from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'account-settings', views.AccountSettingsViewSet)
router.register(r'notification-settings', views.NotificationSettingsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]