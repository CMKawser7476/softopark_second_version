# Generated by Django 3.1.4 on 2021-01-09 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0010_auto_20210109_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagewithdescription',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='headinglogonameshortdescrip',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heading_logo_name_short_descrip', to='cms_app.section'),
        ),
        migrations.AlterField(
            model_name='section',
            name='section_type',
            field=models.CharField(choices=[('top_banner_image', 'Top banner image')], max_length=200),
        ),
    ]
