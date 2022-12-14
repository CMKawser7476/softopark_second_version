# from doctest import BLANKLINE_MARKER
# import email
# from email import message
# from operator import truediv
# from pyexpat import model
# from django.utils.text import slugify
# import json
# from tinymce.models import HTMLField
# from email import message
# from pyexpat import model
# from django.db.models.deletion import CASCADE

from django.db import models
from django.urls import reverse


# Create your models here.
SECTION_TYPE_CHOICES = [
    ("table_with_tech", "Table With Tech"),
    ("table_with_services", "Table With Services"),
    ("table_with_sercices_2", "Table With Services 2"),
    ("heading_logo_border_by_6", "Heading Logo Border By 6"),
    ("call_to_action2", "Call To Action 2"),
    ("call_to_action_with_slug", "Call To Action With Slug"),
    ("image_with_cards_by_2", "Image With Cards By 2"),
    ("testimonials", "Testimonials"),
    ("cards_3", "Cards 3"),
    ("cards_3_container_fluid", "Cards 3 Container Fluid"),
    ("cards_4", "Cards 4"),
    ("cards_4_with_link", "Cards 4 With Link"),
    ("all_logos", "All Logos"),
    ("col_sm_3", "Col sm 3"),
    ("col_sm_3_bg_white", "Col sm 3 Bg White"),
    ("col_sm_4", "Col sm 4"),
    ("col_sm_4_bg_white", "Col sm 4 Bg White"),
    ("col_sm_4_with_link", "Col sm 4 with link"),
    ("col_sm_4_bg_white_with_link", "Col sm 4 white with link"),
    ("img_heading_descrip", "Image heading descriptin"),
    ("video_with_full_container", "Video With Full Container"),
    ("video_with_description_by_2", "Video With Description By 2"),
    ("video_with_description_by_3", "Video With Description By 3"),
    ("image_with_description", "Image With Description"),
    ("heading_border_name_by_4", "Heading Border Name By 4"),
    ("heading_descrip_container", " Heading Descrip Container"),
    ("heading_icon_short_descrip_name_border_container_by_4", "Heading icon short descrip name border container by 4"),
    ("heading_icon_border_name_by_3", "Heading Icon Border Name By 3"),
    ("heading_icon_border_name_by_4", "Heading Icon Border Name By 4"),
    ("heading_icon_name_border_container_by_4", "Heading Icon Name Border Container By 4"),
    ("heading_icon_name_border_container_by_6", "Heading Icon Name Border Container By 6"),
    ("heading_icon_name_short_descrip_without_border_container_by_3", "Heading Icon Name Short Descrip Without Border Container by 3"),
    ("heading_img_by_3", "Heading img by 3"),
    ("heading_logo_name_border_container_by_6", "Heading logo name border container by 6"),
    ("heading_logo_name_short_descrip_border_container_by_3", "Heading logo name short descrip border container by 3"),
    ("heading_logo_name_short_descrip_with_border_container_by_4", "Heading logo name short descrip with border container by 4"),
    ("heading_media_with_border_container_by_2", "Heading media with border container by 2"),
    ("heading_media_without_border_container_by_2", "Heading media without border container by 2"),
    ("heading_social_media_container_by_2", "Heading social media container by 2"),
    ("heading_sub_heading_icon_media_by_3", "Heading sub heading icon media by 3"),
    ("slider", "Slider"),
    ("heading_short_des_svg_png_video_2", "heading short descrip with svg or videos"),
    # ("client_data_submit_form", "Client Data Submit"),


]


CONTAINER_TYPE_CHOICES = [
    ("container", "Container"),
    ("container-fluid", "Container Fluid")
]


IMAGE_ALIGNMENT_CHOICES = [
    ("left", "Left Image"),
    ("right", "Right Image")
]



BUTTON_ALIGNMENT_CHOICES = [
    ("left_button", "Button Left"),
    ("center_button", "Button Center"),
    ("right_button", "Button Right")
]


BUTTON_SIZE = [
    ("small", "Small Button"),
    ("large", "Large Button"),
]


# top_banner_image
class Page(models.Model):
    # page = models.CharField(max_length=255, choices=PAGE_CHOICES)
    parent_page = models.ForeignKey("Page", related_name="page_childs", null=True, blank=True, on_delete=models.CASCADE)
    page_name = models.CharField(max_length=60, unique=True)
    heading = models.CharField(max_length=255, null=True, blank=True)
    page_banner = models.ImageField(upload_to="page_banner", null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    sub_heading = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    # seo related fields for name
    title_tag = models.TextField(null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    # please enter keywords separated by comma here
    keywords = models.TextField(null=True, blank=True)

    twitter_description = models.TextField(null=True, blank=True)
    twitter_title = models.CharField(max_length=260, null=True, blank=True)
    twitter_image = models.ImageField(
    upload_to="twitter_images", null=True, blank=True)

    # OG issues for properties
    og_title = models.CharField(max_length=255, null=True, blank=True)
    og_description = models.TextField(null=True, blank=True)
    og_type = models.CharField(max_length=260, null=True, blank=True)
    og_url = models.URLField(null=True, blank=True)
    og_image = models.ImageField(upload_to="og_images", null=True, blank=True)

    def get_absolute_url(self):
        return reverse('page_detail', kwargs={"slug": self.slug})

    def __str__(self):
        return self.page_name


class LandingPageAssets(models.Model):
    name = models.CharField(max_length=255)
    image_or_file = models.FileField(upload_to="landing_page_assets")

    def __str__(self):
        return str(self.id)


class Section(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    section_type = models.CharField(choices=SECTION_TYPE_CHOICES, max_length=200)
    heading = models.CharField(max_length=255)
    sub_heading = models.TextField(null=True, blank=True)
    background_image = models.ImageField(upload_to="section_backgrounds", null=True, blank=True)
    ordering = models.IntegerField()

    class Meta:
        ordering = ["ordering"]

    def __str__(self):
        return self.heading


class Slide(models.Model):
    section = models.ForeignKey(Section, related_name="slides", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="slides")
    heading = models.CharField(max_length=255, null=True, blank=True)
    sub_heading = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.heading if self.heading else int(self.id)


class HeadingLogoNameShortDescrip(models.Model):
    section = models.ForeignKey(Section, related_name="heading_logo_name_short_descrip", on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255, blank=True, null=True)
    logo_icon = models.ImageField(upload_to="logo_icons", null=True, blank=True)
    short_description = models.TextField( blank=True, null=True)
    # short_description = HTMLField("Description", null=True, blank=True)
    target_url = models.URLField(blank=True, null=True)
    button_text = models.CharField(max_length=255, blank=True, null=True)
    button_direction = models.CharField(choices=BUTTON_ALIGNMENT_CHOICES, default="left_button", max_length=15)
    button_size = models.CharField(choices=BUTTON_SIZE, default="small", max_length=55 )


    def __str__(self):
        return self.heading


class ImageWithDescription(models.Model):
    section = models.ForeignKey(Section, related_name="image_with_description", on_delete=models.CASCADE)
    container_type = models.CharField(choices=CONTAINER_TYPE_CHOICES, default="container", max_length=20)
    image_alignment = models.CharField(choices=IMAGE_ALIGNMENT_CHOICES, default="left", max_length=10)
    background_image = models.ImageField(upload_to="item_backgrounds", blank=True, null=True)
    photo = models.ImageField()
    heading = models.CharField(max_length=255)
    sub_heading = models.TextField(blank=True, null=True)
    description = models.TextField( blank=True, null=True)
    # description = HTMLField("Description", null=True, blank=True)
    target_url = models.URLField(blank=True, null=True)
    # button_text = models.CharField(max_length=255, blank=True, null=True)
    # button_alignment = models.CharField(choices=BUTTON_ALLIGNMENT, default="left", max_length=55)
    # button_size = models.CharField(choices=BUTTON_SIZE, default="small", max_length=55 )


    def __str__(self):
        return self.heading


class IconWithHeading(models.Model):
    section = models.ForeignKey(Section, related_name="icon_with_heading", on_delete=models.CASCADE)
    heading = models.CharField(max_length=275, blank=True, null=True)
    sub_heading = models.TextField(null=True, blank=True)
    icon = models.ImageField()
    target_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.heading


class HeadingWithDescription(models.Model):
    section = models.ForeignKey(Section, related_name="heading_with_description", on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField( blank=True, null=True)
    # description = HTMLField("Description", null=True, blank=True)
    target_url = models.URLField(blank=True, null=True)
    # button_text = models.CharField(max_length=255, blank=True, null=True)
    # button_alignment = models.CharField(choices=BUTTON_ALLIGNMENT, default="left", max_length=55)
    # button_size = models.CharField(choices=BUTTON_SIZE, default="small", max_length=55 )



    def __str__(self):
        return self.heading


class HeadingWithMultipleImageUpload(models.Model):
    section = models.ForeignKey(Section, related_name="heading_with_multiple_image_upload", on_delete=models.CASCADE)
    photo = models.ImageField()

    def __str__(self):
        return f"{self.section.heading} - {self.id}"


class VideosUrls(models.Model):
    section = models.ForeignKey(Section, related_name="videos_urls", on_delete=models.CASCADE)
    heading = models.CharField(max_length=300, blank=True, null=True)
    sub_heading = models.TextField(blank=True, null=True)
    embed_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.heading


class Faq(models.Model):
    section = models.ForeignKey(Section, related_name="all_faqs", on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    answere = models.TextField(blank=True, null=True)
    ordering = models.IntegerField()

    def __str__(self):
        return self.question





# class ClientDataSubmit(models.Model):
#     section = models.ForeignKey(Section, related_name="all_data_submits", on_delete=models.CASCADE)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     email = models.CharField(max_length=255, blank=True, null=True)
#     phone = models.CharField(max_length=255, blank=True, null=True)
#     message = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.name