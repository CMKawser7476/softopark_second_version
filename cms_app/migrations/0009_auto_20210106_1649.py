# Generated by Django 3.1.4 on 2021-01-06 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0008_auto_20210106_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeadingLogoNameShortDescrip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('logo_icon', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=255)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_with_logo', to='cms_app.section')),
            ],
        ),
        migrations.RemoveField(
            model_name='iconshortdescriptionwithname',
            name='section',
        ),
        migrations.RemoveField(
            model_name='iconwithmedia',
            name='section',
        ),
        migrations.DeleteModel(
            name='CardWithLogo',
        ),
        migrations.DeleteModel(
            name='IconShortDescriptionWithName',
        ),
        migrations.DeleteModel(
            name='IconWithMedia',
        ),
    ]
