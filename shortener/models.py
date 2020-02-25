from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from hashids import Hashids

from users.models import CustomUser


class Link(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    url_original = models.URLField(max_length=1000)
    url_part_short = models.CharField(max_length=20, default='undefined')
    date_created = models.DateTimeField(auto_now_add=True)
    usage_count = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ['user', 'url_original']


hasher = Hashids(salt='qwerty', min_length=5)


@receiver(post_save, sender=Link, dispatch_uid='update_url_part_short_field')
def update_url_part_short_field(sender, instance, **kwargs):
    instance.url_part_short = hasher.encode(instance.id)
    # Avoid recursion
    post_save.disconnect(update_url_part_short_field, sender=Link, dispatch_uid='update_url_part_short_field')
    instance.save()
    post_save.connect(update_url_part_short_field, sender=Link, dispatch_uid='update_url_part_short_field')
