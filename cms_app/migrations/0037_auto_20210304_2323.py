# Generated by Django 3.1.7 on 2021-03-04 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0036_auto_20210304_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slides')),
                ('heading', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_heading', models.TextField(blank=True, null=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='cms_app.section')),
            ],
        ),
        migrations.DeleteModel(
            name='SlidersWithHeading',
        ),
    ]