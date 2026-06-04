from django.db.models.signals import post_delete
from django.dispatch import receiver
import cloudinary.uploader
from .models import Post

@receiver(post_delete, sender=Post)
def delete_post_image(sender, instance, **kwargs):
    if instance.image:
        cloudinary.uploader.destroy(instance.image.public_id)