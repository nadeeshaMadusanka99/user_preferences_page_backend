from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import authenticate
from rest_framework import status

from ..models import AccountSetting, PrivacySetting, NotificationSetting, ThemeSetting, User
from rest_framework.test import APIClient


class AccountSettingFunctionalTest(TestCase):

    # Set up the user and the notification settings instance
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            email='testuser@example.com'
        )
        self.client.login(username='testuser', password='password123')

    # Test the account settings page loads correctly
    def test_account_settings_page_load(self):
        url = reverse('account-settings-list')
        response = self.client.get(url)

        # Check if the page loads successfully (status code 200)
        self.assertEqual(response.status_code, 200)

        # Parse JSON response and check content
        response_data = response.json()
        self.assertIsInstance(response_data, list)
        self.assertGreater(len(response_data), 0)

        # Check specific fields in the first account setting
        account_setting = response_data[0]
        self.assertEqual(account_setting['username'], 'testuser')
        self.assertEqual(account_setting['email'], 'testuser@example.com')

    # Test updating the account settings
    def test_account_settings_update(self):
        self.account_setting = AccountSetting.objects.get(user=self.user)

        url = reverse('account-settings-detail', args=[self.account_setting.id])

        # Update data for the account settings
        data = {
            'username': 'newtestuser',
            'email': 'newtestuser@example.com',
            'password': 'newpassword123',
            'bio': 'This is a test bio',
        }

        # Send a PUT request to update the account settings
        response = self.client.put(url, data, content_type='application/json')

        # Check if the account settings were updated successfully (status code 200)
        self.assertEqual(response.status_code, 200)

        # Fetch the updated user from the database
        account_settings = AccountSetting.objects.get(user=self.user)

        # Check if the username and email were updated
        self.assertEqual(account_settings.username, 'newtestuser')
        self.assertEqual(account_settings.email, 'newtestuser@example.com')
        self.assertEqual(account_settings.check_password('newpassword123'), True)
        self.assertEqual(account_settings.bio, 'This is a test bio')

    # Test deleting a user account and it should delete the all the related settings
    def test_user_deletion_cascades_settings(self):
        # Ensure related settings exist
        self.assertEqual(AccountSetting.objects.filter(user=self.user).count(), 1)
        self.assertEqual(NotificationSetting.objects.filter(user=self.user).count(), 1)
        self.assertEqual(ThemeSetting.objects.filter(user=self.user).count(), 1)
        self.assertEqual(PrivacySetting.objects.filter(user=self.user).count(), 1)

        user_before_delete = User.objects.get(username='testuser')

        self.user.delete()

        # Check that all related settings are deleted
        self.assertEqual(AccountSetting.objects.filter(user=user_before_delete).count(), 0)
        self.assertEqual(NotificationSetting.objects.filter(user=user_before_delete).count(), 0)
        self.assertEqual(ThemeSetting.objects.filter(user=user_before_delete).count(), 0)
        self.assertEqual(PrivacySetting.objects.filter(user=user_before_delete).count(), 0)

    # Test that an unauthorized user cannot access the account settings
    def test_unauthorized_user_cannot_access_settings(self):
        # Log out the user
        self.client.logout()

        response = self.client.get("/api/v1/account-settings/")
        self.assertEqual(response.status_code, 403)

    # Test that the POST method is disabled for all settings
    def test_post_method_disabled(self):
        self.endpoints = {
            "account": "/api/v1/account-settings/",
            "notification": "/api/v1/notification-settings/",
            "theme": "/api/v1/theme-settings/",
            "privacy": "/api/v1/privacy-settings/",
        }
        for setting_type, endpoint in self.endpoints.items():
            with self.subTest(setting=setting_type):
                data = {"dummy_field": "dummy_value"}  # Data to test POST

                response = self.client.post(endpoint, data=data, format="json")

                self.assertEqual(
                    response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED,
                    f"POST should be disabled for {setting_type}, but got {response.status_code}"
                )
