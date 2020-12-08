from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import Profile


@receiver(post_save, sender=User)
def callback_save(sender, **kwargs):
    Profile.objects.create()
    post_save.connect(callback_save)