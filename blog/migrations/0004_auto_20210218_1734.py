# Generated by Django 3.1.5 on 2021-02-18 11:34

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210128_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
