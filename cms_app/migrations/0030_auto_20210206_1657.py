# Generated by Django 3.1.5 on 2021-02-06 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0029_auto_20210206_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headinglogonameshortdescrip',
            name='logo_icon',
            field=models.ImageField(blank=True, null=True, upload_to='logo_icons'),
        ),
    ]