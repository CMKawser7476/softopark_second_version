# Generated by Django 3.1.4 on 2020-12-24 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
