# Generated by Django 3.1.7 on 2022-04-20 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0005_auto_20220420_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headinglogonameshortdescrip',
            name='button_allignment',
        ),
    ]