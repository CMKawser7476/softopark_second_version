from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
from accounts.models import User
from ckeditor_uploader.fields import RichTextUploadingField

import random
import string

class Category(models.Model):
    parent = models.ForeignKey('Category', related_name="child_categories", null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=270, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    cover_photo = models.ImageField(upload_to="blog_categories", null=True, blank=True)

    def save(self, *args, **kwargs):
        obj = None
        if self.id:
            obj = Category.objects.get(id=self.id)
        if (obj and (obj.name != self.name)) or not obj:
            random_string = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(7))
            self.slug = f"{slugify(self.name)}-{random_string}"
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name



class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=270, null=True, blank=True)
    description = RichTextUploadingField(blank=True, null=True, config_name='default')
    photo = models.ImageField(upload_to="blog_post_photos", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    publish_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name="blog_posts")

  # seo related fields for name
    blog_title_tag = models.TextField(null=True, blank=True)
    blog_meta_description = models.TextField(null=True, blank=True)
    blog_keywords = models.TextField(null=True, blank=True) # please enter keywords separated by comma here
    
    blog_twitter_description = models.TextField(null=True, blank=True)
    blog_twitter_title = models.CharField(max_length=260 ,null=True, blank=True)
    blog_twitter_image = models.ImageField(upload_to="twitter_images", null=True, blank=True)


    # OG issues for properties
    blog_og_title = models.CharField(max_length=255, null=True, blank=True)
    blog_og_type = models.CharField(max_length=260 ,null=True, blank=True)
    blog_og_description = models.TextField(null=True, blank=True)
    blog_og_url = models.URLField(null=True, blank=True)
    blog_og_image = models.ImageField(upload_to="og_images", null=True, blank=True)


    def save(self, *args, **kwargs):
        obj = None
        if self.id:
            obj = Blog.objects.get(id=self.id)
        if (obj and (obj.title != self.title)) or not obj:
            new_slug = slugify(self.title)
            post = Blog.objects.filter(slug=new_slug)
            self.slug = new_slug
            if post.exists():
                random_string = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(7))
                self.slug = f"{new_slug}-{random_string}"
        super(Blog, self).save(*args, **kwargs)
 
    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title