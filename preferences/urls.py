from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'account-settings', views.AccountSettingViewSet)
router.register(r'notification-settings', views.NotificationSettingViewSet)
router.register(r'theme-settings', views.ThemeSettingViewSet)
router.register(r'privacy-settings', views.PrivacySettingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
