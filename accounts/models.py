from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    profile_photo = models.ImageField(upload_to="profile_photos", null=True, blank=True)
    short_bio = models.TextField()
    website = models.URLField(max_length=200,  null=True, blank=True)
    facebook = models.URLField(max_length=200,  null=True, blank=True)
    linkedin = models.URLField(max_length=200,  null=True, blank=True)
    twitter = models.URLField(max_length=200,  null=True, blank=True)
    instagram = models.URLField(max_length=200,  null=True, blank=True)