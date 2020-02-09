from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from greenery.models import Greenery
from backendGS.utils import unique_slug_generator


class Tag(models.Model):
    Name = models.CharField(max_length=120)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    greenery = models.ManyToManyField(Greenery, blank=True)

    def __str__(self):
        return self.Name



def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)
