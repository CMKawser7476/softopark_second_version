# Generated by Django 3.1.7 on 2022-03-31 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0008_headinglogonameshortdescrip_button_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='headingwithdescription',
            name='button_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='imagewithdescription',
            name='button_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
