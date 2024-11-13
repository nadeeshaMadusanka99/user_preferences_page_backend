from django.db import models
from django.contrib.auth.models import User


# Base model for preference categories
class PreferenceCategory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AccountSettings(PreferenceCategory):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    bio = models.TextField()


class NotificationSettings(PreferenceCategory):
    email_notifications = models.BooleanField(default=True)
    push_notifications = models.BooleanField(default=True)
    notification_frequency = models.CharField(max_length=50)

@receiver(post_save, sender=User)
def create_user_preferences(sender, instance, created, **kwargs):
    if created:
        AccountSettings.objects.create(user=instance)
        NotificationSettings.objects.create(user=instance)
        print('User preferences created!')