# Generated by Django 3.1.7 on 2022-03-30 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0007_auto_20220330_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='headinglogonameshortdescrip',
            name='button_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]