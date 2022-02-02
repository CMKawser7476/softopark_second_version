# Generated by Django 3.2.9 on 2022-02-02 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaddata',
            name='section',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='all_leads', to='cms_app.section'),
            preserve_default=False,
        ),
    ]
