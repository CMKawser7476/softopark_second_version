# Generated by Django 3.1.5 on 2021-01-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0026_auto_20210116_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headinglogonameshortdescrip',
            name='logo_icon',
            field=models.ImageField(upload_to='logo_icons'),
        ),
    ]