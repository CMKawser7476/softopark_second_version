# Generated by Django 3.1.7 on 2022-04-03 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0016_auto_20220403_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headinglogonameshortdescrip',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='headingwithdescription',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='imagewithdescription',
            name='button_text',
        ),
    ]