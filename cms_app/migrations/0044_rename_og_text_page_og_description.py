# Generated by Django 3.2 on 2021-04-27 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0043_auto_20210412_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='og_text',
            new_name='og_description',
        ),
    ]