from django.test import TestCase
from ..models import NotificationSetting, User


class NotificationSettingTest(TestCase):

    # Create a user instance
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            email='testuser@example.com')

    # Test the creation of a NotificationSetting instance with default values
    def test_notification_setting_creation(self):
        notification_setting = NotificationSetting.objects.get(user=self.user)

        self.assertEqual(notification_setting.user.username, 'testuser')
        self.assertEqual(notification_setting.email_notifications, True)
        self.assertEqual(notification_setting.push_notifications, True)
        self.assertEqual(notification_setting.notification_frequency, 'instantly')

    # Test the update of email_notifications in a NotificationSetting instance
    def test_notification_setting_email_notifications_update(self):
        notification_setting = NotificationSetting.objects.get(user=self.user)
        notification_setting.email_notifications = False
        notification_setting.save()

        updated_notification_setting = NotificationSetting.objects.get(user=self.user)
        self.assertEqual(updated_notification_setting.email_notifications, False)

    # Test the update of push_notifications in a NotificationSetting instance
    def test_notification_setting_push_notifications_update(self):
        notification_setting = NotificationSetting.objects.get(user=self.user)
        notification_setting.push_notifications = False
        notification_setting.save()

        updated_notification_setting = NotificationSetting.objects.get(user=self.user)
        self.assertEqual(updated_notification_setting.push_notifications, False)

    # Test the update of notification_frequency in a NotificationSetting instance
    def test_notification_setting_notification_frequency_update(self):
        notification_setting = NotificationSetting.objects.get(user=self.user)
        notification_setting.notification_frequency = 'daily'
        notification_setting.save()

        updated_notification_setting = NotificationSetting.objects.get(user=self.user)
        self.assertEqual(updated_notification_setting.notification_frequency, 'daily')

    # Test the update of all fields in a NotificationSetting instance
    def test_notification_setting_all_fields_update(self):
        notification_setting = NotificationSetting.objects.get(user=self.user)
        notification_setting.email_notifications = False
        notification_setting.push_notifications = False
        notification_setting.notification_frequency = 'daily'
        notification_setting.save()

        updated_notification_setting = NotificationSetting.objects.get(user=self.user)
        self.assertEqual(updated_notification_setting.email_notifications, False)
        self.assertEqual(updated_notification_setting.push_notifications, False)
        self.assertEqual(updated_notification_setting.notification_frequency, 'daily')

    # Test deletion of a NotificationSetting instance
    def test_notification_setting_deletion(self):
        notification_setting = NotificationSetting.objects.get(user=self.user)
        notification_setting.delete()

        with self.assertRaises(NotificationSetting.DoesNotExist):
            NotificationSetting.objects.get(user=self.user)
