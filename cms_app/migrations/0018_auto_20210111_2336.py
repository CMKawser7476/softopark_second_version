# Generated by Django 3.1.4 on 2021-01-11 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0017_auto_20210111_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='section_type',
            field=models.CharField(choices=[('container_fluid', 'Container Fluid'), ('container', 'Container'), ('heading_border_name_by_4', 'Heading Border Name By 4'), ('heading_descrip_container', ' Heading Descrip Container'), ('heading_icon _short_descrip_name_border_container_by_4', 'Heading Icon Short Descrip Name Border Container By 4'), ('heading_icon_border_name_by_3', 'Heading Icon Border Name By 3'), ('heading_icon_border_name_by_4', 'Heading Icon Border Name By 4'), ('heading_icon_name_border_container_by_4', 'Heading Icon Name Border Container By 4'), ('heading_icon_name_border_container_by_6', 'Heading Icon Name Border Container By 6'), ('heading_icon_name_container_by_4', 'Heading Icon Name Container By 4'), ('heading_icon_name_short_descrip_without_border_container_by_3', 'Heading Icon Name Short Descrip Without Border Container by 3'), ('heading_img_by_3', 'Heading img by 3'), ('heading_lft_cards_rght_img_container_by_2', 'Heading lft Cards rght img container by 2'), ('heading_logo_name_border_container_by_6', 'Heading logo name border container by 6'), ('heading_logo_name_short_descrip_border_container_by_3', 'Heading logo name short descrip border container by 3'), ('heading_logo_name_short_descrip_with_border_container_by_4', 'Heading logo name short descrip with border container by 4'), ('heading_logo_name_short_descrip_with_border_container_by_5', 'Heading logo name short descrip with border container by 5'), ('heading_media_with_border_container_by_2', 'Heading media with border container by 2'), ('heading_media_without_border_container_by_2', 'Heading media without border container by 2'), ('heading_name_short_descrip_border_container_by_4', 'Heading name short descrip border container by 4'), ('heading_social_media_container_by_2', 'Heading social media container by 2'), ('heading_sub_heading_icon_media_by_3', 'Heading sub heading icon media by 3')], max_length=200),
        ),
    ]
