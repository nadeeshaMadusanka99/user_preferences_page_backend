from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    class Meta:
        db_table = 'auth_user'


# Base model for preference categories
class PreferenceCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AccountSetting(PreferenceCategory):
    username = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=128)
    bio = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        password_value = self.password
        # Hash the password if it's not already hashed
        if not password_value.startswith('pbkdf2'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        # Check raw password matches the hashed password
        return check_password(raw_password, self.password)


class NotificationSetting(PreferenceCategory):
    FREQUENCY_CHOICES = [
        ('instantly', 'Instantly'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
    ]

    email_notifications = models.BooleanField(default=True)
    push_notifications = models.BooleanField(default=True)
    notification_frequency = models.CharField(max_length=50,
                                              choices=FREQUENCY_CHOICES,
                                              default='instantly')


class ThemeSetting(PreferenceCategory):
    THEME_CHOICES = [
        ('light', 'Light'),
        ('dark', 'Dark'),
    ]
    FONT_CHOICES = [
        ('arial', 'Arial'),
        ('serif', 'Serif'),
        ('sans-serif', 'Sans Serif'),
        ('courier', 'Courier New'),
    ]
    LAYOUT_CHOICES = [
        ('fixed', 'Fixed'),
        ('fluid', 'Fluid'),
    ]
    color = models.CharField(max_length=50,
                             choices=THEME_CHOICES,
                             default='light')
    font = models.CharField(max_length=50,
                            choices=FONT_CHOICES,
                            default='arial')
    layout = models.CharField(max_length=50,
                              choices=LAYOUT_CHOICES,
                              default='fixed')


class PrivacySetting(PreferenceCategory):
    PROFILE_VISIBILITY_CHOICES = [
        ('public', 'Public'),
        ('friends', 'Friends'),
        ('private', 'Private'),
    ]
    DATA_SHARING_CHOICES = [
        ('public', 'Public'),
        ('friends', 'Friends'),
        ('none', 'None'),
    ]

    profile_visibility = models.CharField(max_length=50,
                                          choices=PROFILE_VISIBILITY_CHOICES,
                                          default='public')
    data_sharing = models.CharField(max_length=50,
                                    choices=DATA_SHARING_CHOICES,
                                    default='public')


@receiver(post_save, sender=User)
def create_user_preferences(sender, instance, created, **kwargs):
    if created:
        AccountSetting.objects.create(user=instance, username=instance.username, email=instance.email,
                                      password=instance.password)
        NotificationSetting.objects.create(user=instance)
        ThemeSetting.objects.create(user=instance)
        PrivacySetting.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_preferences(sender, instance, **kwargs):
    instance.accountsetting.save()
    instance.notificationsetting.save()
    instance.themesetting.save()
    instance.privacysetting.save()


@receiver(pre_delete, sender=User)
def delete_user_preferences(sender, instance, **kwargs):
    AccountSetting.objects.filter(user=instance).delete()
    NotificationSetting.objects.filter(user=instance).delete()
    ThemeSetting.objects.filter(user=instance).delete()
    PrivacySetting.objects.filter(user=instance).delete()
