from django.test import TestCase
from ..models import AccountSetting, User


class AccountSettingTest(TestCase):

    # Create a user instance
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            email='testuser@example.com'
        )

    # Test the creation of an AccountSetting instance
    def test_account_setting_creation(self):
        account_setting = AccountSetting.objects.get(user=self.user)

        # Check that the AccountSetting instance was created correctly
        self.assertEqual(account_setting.username, 'testuser')
        self.assertEqual(account_setting.email, 'testuser@example.com')

    # Test the addition of password to an AccountSetting instance
    def test_account_setting_password_add(self):
        account_setting = AccountSetting.objects.get(user=self.user)
        account_setting.password = 'password123'
        account_setting.save()

        # Fetch the updated instance and check the password
        updated_account_setting = AccountSetting.objects.get(user=self.user)
        self.assertTrue(updated_account_setting.check_password('password123'))

    # Test the update of password in an AccountSetting instance
    def test_account_setting_password_update(self):
        account_setting = AccountSetting.objects.get(user=self.user)
        # Update the password and save it
        account_setting.password = 'newpassword123'
        account_setting.save()

        # Fetch the updated instance and check the password
        updated_account_setting = AccountSetting.objects.get(user=self.user)
        self.assertTrue(updated_account_setting.check_password('newpassword123'))

    # Test the addition of bio to an AccountSetting instance
    def test_account_setting_bio_add(self):
        account_setting = AccountSetting.objects.get(user=self.user)
        account_setting.bio = 'Adding test bio'
        account_setting.save()

        # Fetch the updated instance and check the bio
        updated_account_setting = AccountSetting.objects.get(user=self.user)
        self.assertEqual(updated_account_setting.bio, 'Adding test bio')

    # Test the update of bio in an AccountSetting instance
    def test_account_setting_bio_update(self):
        account_setting = AccountSetting.objects.get(user=self.user)
        # Update the bio and save it
        account_setting.bio = 'Updated bio'
        account_setting.save()

        # Fetch the updated instance and check the bio
        updated_account_setting = AccountSetting.objects.get(user=self.user)
        self.assertEqual(updated_account_setting.bio, 'Updated bio')

    # Test username and email fields are updated
    def test_account_setting_username_email_update(self):
        account_setting = AccountSetting.objects.get(user=self.user)
        # Update the username and email fields
        account_setting.username = 'newtestuser'
        account_setting.email = 'newuseremail@gmail.com'
        account_setting.save()

        # Fetch the updated instance and check the username and email fields
        updated_account_setting = AccountSetting.objects.get(user=self.user)

        self.assertEqual(updated_account_setting.username, 'newtestuser')
        self.assertEqual(updated_account_setting.email, 'newuseremail@gmail.com')

    # Test the deletion is restricted if the related User exists
    def test_account_setting_deletion_restricted(self):
        account_setting = AccountSetting.objects.get(user=self.user)

        # Try to delete the AccountSetting instance
        with self.assertRaises(Exception):
            account_setting.delete()
