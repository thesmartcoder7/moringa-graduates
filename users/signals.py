from django.db.models.signals import post_save
from django.contrib.auth.models import User
from users.models import Profile
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(instance, created, **kwargs):
    """
    Signal receiver function to create a profile for a newly created user.

    Args:
        instance (User): The newly created User instance.
        created (bool): Flag indicating if the User instance was created or updated.
        **kwargs: Additional keyword arguments.

    Returns:
        None

    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Signal receiver function to save the profile of a user.

    Args:
        sender (User): The User model.
        instance (User): The User instance.
        **kwargs: Additional keyword arguments.

    Returns:
        None

    """
    instance.profile.save()
