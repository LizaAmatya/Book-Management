from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

# @receiver(post_save, sender=get_user_model())
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#     instance.profile.save()
