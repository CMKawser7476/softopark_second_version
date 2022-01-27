# Generated by Django 3.2.4 on 2021-06-08 08:42

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0052_auto_20210608_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='videosurls',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='video_urls', to='cms_app.section'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='videosurls',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
