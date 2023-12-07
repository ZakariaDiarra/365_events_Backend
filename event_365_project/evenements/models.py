from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200, default="Toulouse")
    bio = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    photo = models.ImageField(default="default", upload_to='profile_pictures', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    imageUrl = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    imageUrl = models.ImageField(upload_to='events/', blank=True, null=True)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    tickets = models.IntegerField(default=1)

    def __str__(self):
        return f"Reservation by {self.user} for {self.event}, {self.tickets} tickets"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()