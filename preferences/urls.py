from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'account-settings', views.AccountSettingViewSet, basename='account-settings')
router.register(r'notification-settings', views.NotificationSettingViewSet, basename='notification-settings')
router.register(r'theme-settings', views.ThemeSettingViewSet, basename='theme-settings')
router.register(r'privacy-settings', views.PrivacySettingViewSet, basename='privacy-settings')

urlpatterns = [
    path('', include(router.urls)),
]
