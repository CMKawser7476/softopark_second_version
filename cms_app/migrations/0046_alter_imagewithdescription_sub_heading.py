# Generated by Django 3.2 on 2021-06-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0045_auto_20210506_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagewithdescription',
            name='sub_heading',
            field=models.TextField(blank=True, null=True),
        ),
    ]