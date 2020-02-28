from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# create a
# sender and receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """

    Create automatically a profile every time a user is created

    :param sender:
    :param instance: the instance of the user
    :param created: if the user was created
    :param kwargs:
    :return:
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    """

    Save the profile everytime a user is saved

    :param sender:
    :param instance: the instance of the user
    :param created: if the user was created
    :param kwargs:
    :return:
    """
    instance.profile.save()
