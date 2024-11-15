from django.test import TestCase
from ..models import ThemeSetting, User


class ThemeSettingTest(TestCase):

    # Create a user instance
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password123',
            email='testuser@example.com')

    # Test the creation of a ThemeSetting instance with default values
    def test_theme_setting_creation(self):
        theme_setting = ThemeSetting.objects.get(user=self.user)

        self.assertEqual(theme_setting.user.username, 'testuser')
        self.assertEqual(theme_setting.color, 'light')
        self.assertEqual(theme_setting.font, 'arial')
        self.assertEqual(theme_setting.layout, 'fixed')

    # Test the update of color in a ThemeSetting instance
    def test_theme_setting_color_update(self):
        theme_setting = ThemeSetting.objects.get(user=self.user)
        theme_setting.color = 'dark'
        theme_setting.save()

        updated_theme_setting = ThemeSetting.objects.get(user=self.user)
        self.assertEqual(updated_theme_setting.color, 'dark')

    # Test the update of font in a ThemeSetting instance
    def test_theme_setting_font_update(self):
        theme_setting = ThemeSetting.objects.get(user=self.user)
        theme_setting.font = 'serif'
        theme_setting.save()

        updated_theme_setting = ThemeSetting.objects.get(user=self.user)
        self.assertEqual(updated_theme_setting.font, 'serif')

    # Test the update of layout in a ThemeSetting instance
    def test_theme_setting_layout_update(self):
        theme_setting = ThemeSetting.objects.get(user=self.user)
        theme_setting.layout = 'fluid'
        theme_setting.save()

        updated_theme_setting = ThemeSetting.objects.get(user=self.user)
        self.assertEqual(updated_theme_setting.layout, 'fluid')

    # Test the update of all fields in a ThemeSetting instance
    def test_theme_setting_all_fields_update(self):
        theme_setting = ThemeSetting.objects.get(user=self.user)
        theme_setting.color = 'dark'
        theme_setting.font = 'sans-serif'
        theme_setting.layout = 'fluid'
        theme_setting.save()

        updated_theme_setting = ThemeSetting.objects.get(user=self.user)
        self.assertEqual(updated_theme_setting.color, 'dark')
        self.assertEqual(updated_theme_setting.font, 'sans-serif')
        self.assertEqual(updated_theme_setting.layout, 'fluid')

    # Test delete restriction for ThemeSetting instance
    def test_theme_setting_delete_restriction(self):
        theme_setting = ThemeSetting.objects.get(user=self.user)

        with self.assertRaises(Exception):
            theme_setting.delete()