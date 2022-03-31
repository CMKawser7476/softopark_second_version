# Generated by Django 3.1.7 on 2022-03-23 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0005_auto_20220224_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='section_type',
            field=models.CharField(choices=[('table_with_tech', 'Table With Tech'), ('table_with_services', 'Table With Services'), ('table_with_sercices_2', 'Table With Services 2'), ('heading_logo_border_by_6', 'Heading Logo Border By 6'), ('call_to_action2', 'Call To Action 2'), ('call_to_action_with_slug', 'Call To Action With Slug'), ('image_with_cards_by_2', 'Image With Cards By 2'), ('testimonials', 'Testimonials'), ('cards_3', 'Cards 3'), ('cards_3_container_fluid', 'Cards 3 Container Fluid'), ('cards_4', 'Cards 4'), ('cards_4_with_link', 'Cards 4 With Link'), ('all_logos', 'All Logos'), ('col_sm_3', 'Col sm 3'), ('col_sm_3_bg_white', 'Col sm 3 Bg White'), ('col_sm_4', 'Col sm 4'), ('col_sm_4_bg_white', 'Col sm 4 Bg White'), ('col_sm_4_with_link', 'Col sm 4 with link'), ('col_sm_4_bg_white_with_link', 'Col sm 4 white with link'), ('img_heading_descrip', 'Image heading descriptin'), ('video_with_full_container', 'Video With Full Container'), ('video_with_description_by_2', 'Video With Description By 2'), ('video_with_description_by_3', 'Video With Description By 3'), ('image_with_description', 'Image With Description'), ('heading_border_name_by_4', 'Heading Border Name By 4'), ('heading_descrip_container', ' Heading Descrip Container'), ('heading_icon_short_descrip_name_border_container_by_4', 'Heading icon short descrip name border container by 4'), ('heading_icon_border_name_by_3', 'Heading Icon Border Name By 3'), ('heading_icon_border_name_by_4', 'Heading Icon Border Name By 4'), ('heading_icon_name_border_container_by_4', 'Heading Icon Name Border Container By 4'), ('heading_icon_name_border_container_by_6', 'Heading Icon Name Border Container By 6'), ('heading_icon_name_short_descrip_without_border_container_by_3', 'Heading Icon Name Short Descrip Without Border Container by 3'), ('heading_img_by_3', 'Heading img by 3'), ('heading_logo_name_border_container_by_6', 'Heading logo name border container by 6'), ('heading_logo_name_short_descrip_border_container_by_3', 'Heading logo name short descrip border container by 3'), ('heading_logo_name_short_descrip_with_border_container_by_4', 'Heading logo name short descrip with border container by 4'), ('heading_media_with_border_container_by_2', 'Heading media with border container by 2'), ('heading_media_without_border_container_by_2', 'Heading media without border container by 2'), ('heading_social_media_container_by_2', 'Heading social media container by 2'), ('heading_sub_heading_icon_media_by_3', 'Heading sub heading icon media by 3'), ('slider', 'Slider'), ('heading_short_des_svg_png_video_2', 'heading short descrip with svg or videos'), ('lead_data_form', 'Lead Data Form')], max_length=200),
        ),
    ]
