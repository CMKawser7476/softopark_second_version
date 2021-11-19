# Generated by Django 3.2.9 on 2021-11-11 08:38

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.CharField(blank=True, max_length=270, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='blog_categories')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_categories', to='blog.category')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(blank=True, max_length=270, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='blog_post_photos')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('publish_at', models.DateTimeField(blank=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('blog_title_tag', models.TextField(blank=True, null=True)),
                ('blog_meta_description', models.TextField(blank=True, null=True)),
                ('blog_keywords', models.TextField(blank=True, null=True)),
                ('blog_twitter_description', models.TextField(blank=True, null=True)),
                ('blog_twitter_title', models.CharField(blank=True, max_length=260, null=True)),
                ('blog_twitter_image', models.ImageField(blank=True, null=True, upload_to='twitter_images')),
                ('blog_og_title', models.CharField(blank=True, max_length=255, null=True)),
                ('blog_og_type', models.CharField(blank=True, max_length=260, null=True)),
                ('blog_og_description', models.TextField(blank=True, null=True)),
                ('blog_og_url', models.URLField(blank=True, null=True)),
                ('blog_og_image', models.ImageField(blank=True, null=True, upload_to='og_images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(related_name='blog_posts', to='blog.Category')),
            ],
        ),
    ]
