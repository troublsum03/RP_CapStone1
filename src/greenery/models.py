import random
import os
from django.db import models
from django.db.models.signals import pre_save, post_save

from .utlis import unique_slug_generator


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 999999)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "greenery/{new_filename}/{final_filename}".format(
        new_filename=new_filename, 
        final_filename=final_filename
        )

class GreeneryQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

class GreeneryManager(models.Manager):
    def get_queryset(self):
        return GreeneryQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def features(self):
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Greenery.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

class Greenery(models.Model):
    Strains = models.CharField(max_length=120)
    Name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    Cannabinoids = models.CharField(max_length=120)
    Description = models.TextField()
    Feeling = models.CharField(max_length=120)
    HelpWith = models.CharField(max_length=120)
    Negatives = models.CharField(max_length=120)
    Price = models.DecimalField(decimal_places=2, max_digits=20, default=30.00)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = GreeneryManager()

    def get_absolute_url(self):
        return "/greenery/{slug}/".format(slug=self.slug)
    
    def __str__(self):
        return self.Name
    
    def __unicode__(self):
        return self.Name


def greenery_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(greenery_pre_save_receiver, sender=Greenery)