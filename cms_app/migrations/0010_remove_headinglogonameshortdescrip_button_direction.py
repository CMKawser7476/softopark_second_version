# Generated by Django 3.1.7 on 2022-05-31 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0009_auto_20220420_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headinglogonameshortdescrip',
            name='button_direction',
        ),
    ]
