# Generated by Django 3.1.7 on 2022-04-20 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0003_auto_20220420_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headinglogonameshortdescrip',
            name='button_alignment',
            field=models.CharField(choices=[('left', 'Button Left'), ('center', 'Button Center'), ('right', 'Button Right')], default='left', max_length=15),
        ),
    ]