from django.test import TestCase
from ..models import PrivacySetting, User


class PrivacySettingTest(TestCase):

    # Create a user instance
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            email='testuser@example.com')

    # Test the creation of a PrivacySetting instance with default values
    def test_privacy_setting_creation(self):
        privacy_setting = PrivacySetting.objects.get(user=self.user)

        self.assertEqual(privacy_setting.user.username, 'testuser')
        self.assertEqual(privacy_setting.profile_visibility, 'public')
        self.assertEqual(privacy_setting.data_sharing, 'public')

    # Test the update of profile_visibility in a PrivacySetting instance
    def test_privacy_setting_profile_visibility_update(self):
        privacy_setting = PrivacySetting.objects.get(user=self.user)
        privacy_setting.profile_visibility = 'private'
        privacy_setting.save()

        updated_privacy_setting = PrivacySetting.objects.get(user=self.user)
        self.assertEqual(updated_privacy_setting.profile_visibility, 'private')

    # Test the update of data_sharing in a PrivacySetting instance
    def test_privacy_setting_data_sharing_update(self):
        privacy_setting = PrivacySetting.objects.get(user=self.user)
        privacy_setting.data_sharing = 'none'
        privacy_setting.save()

        updated_privacy_setting = PrivacySetting.objects.get(user=self.user)
        self.assertEqual(updated_privacy_setting.data_sharing, 'none')

    # Test the update of all fields in a PrivacySetting instance
    def test_privacy_setting_all_fields_update(self):
        privacy_setting = PrivacySetting.objects.get(user=self.user)
        privacy_setting.profile_visibility = 'private'
        privacy_setting.data_sharing = 'none'
        privacy_setting.save()

        updated_privacy_setting = PrivacySetting.objects.get(user=self.user)
        self.assertEqual(updated_privacy_setting.profile_visibility, 'private')
        self.assertEqual(updated_privacy_setting.data_sharing, 'none')

    # Test the delete restriction of a PrivacySetting instance
    def test_privacy_setting_delete_restriction(self):
        privacy_setting = PrivacySetting.objects.get(user=self.user)

        with self.assertRaises(Exception):
            privacy_setting.delete()