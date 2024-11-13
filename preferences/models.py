from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password, check_password


# Base model for preference categories
class PreferenceCategory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AccountSetting(PreferenceCategory):
    username = models.CharField(max_length=50)
    email = models.EmailField()
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

@receiver(post_save, sender=User)
def create_user_preferences(sender, instance, created, **kwargs):
    if created:
        AccountSetting.objects.create(user=instance, username=instance.username, email=instance.email)
        NotificationSetting.objects.create(user=instance)
        print('User preferences created!')

@receiver(post_save, sender=User)
def save_user_preferences(sender, instance, **kwargs):
    instance.accountsetting.save()
    instance.notificationsetting.save()
    print('User preferences saved!')