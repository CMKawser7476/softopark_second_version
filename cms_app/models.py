from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import json
from tinymce import HTMLField
# Create your models here. 


SECTION_TYPE_CHOICES = [
    ("book_an_appointment", "Book An Appointment"),
    ("call_to_action", "Call To Action"),
    ("call_to_action2", "Call To Action 2"),
    ("image_with_cards_by_2", "Image With Cards By 2"),
    ("testimonials", "Testimonials"),
    ("video_with_full_container", "Video With Full Container"),
    ("video_with_description_by_2", "Video With Description By 2"),
    ("video_with_description_by_3", "Video With Description By 2"),
    ("image_with_description", "Image With Description"),
    ("heading_border_name_by_4", "Heading Border Name By 4"),
    ("heading_descrip_container", " Heading Descrip Container"),
    ("heading_icon_short_descrip_name_border_container_by_4", "Heading Icon Short Descrip Name Border Container By 4"),
    ("heading_icon_border_name_by_3", "Heading Icon Border Name By 3"),
    ("heading_icon_border_name_by_4", "Heading Icon Border Name By 4"),
    ("heading_icon_name_border_container_by_4", "Heading Icon Name Border Container By 4"),
    ("heading_icon_name_border_container_by_6", "Heading Icon Name Border Container By 6"),
    ("heading_icon_name_container_by_4", "Heading Icon Name Container By 4"),
    ("heading_icon_name_short_descrip_without_border_container_by_3", "Heading Icon Name Short Descrip Without Border Container by 3"),
    ("heading_img_by_3", "Heading img by 3"),
    ("heading_logo_name_border_container_by_6", "Heading logo name border container by 6"),
    ("heading_logo_name_short_descrip_border_container_by_3", "Heading logo name short descrip border container by 3"),
    ("heading_logo_name_short_descrip_with_border_container_by_4", "Heading logo name short descrip with border container by 4"),
    ("heading_logo_name_short_descrip_with_border_container_by_5", "Heading logo name short descrip with border container by 5"),
    ("heading_media_with_border_container_by_2", "Heading media with border container by 2"),
    ("heading_media_without_border_container_by_2", "Heading media without border container by 2"),
    ("heading_social_media_container_by_2", "Heading social media container by 2"),
    ("heading_sub_heading_icon_media_by_3", "Heading sub heading icon media by 3"),
    ("slider", "Slider"),
    ("heading_short_des_svg_png_video_2", "heading short descrip with svg or videos")
    

]


CONTAINER_TYPE_CHOICES = [
    ("container", "Container"),
    ("container-fluid", "Container Fluid")
]


IMAGE_ALIGNMENT_CHOICES = [
    ("left", "Left Image"),
    ("right", "Right Image")
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
    keywords = models.TextField(null=True, blank=True) # please enter keywords separated by comma here
    
    twitter_description = models.TextField(null=True, blank=True)
    twitter_title = models.CharField(max_length=260 ,null=True, blank=True)
    twitter_image = models.ImageField(upload_to="twitter_images", null=True, blank=True)


    # OG issues for properties
    og_title = models.CharField(max_length=255, null=True, blank=True)
    og_description = models.TextField(null=True, blank=True)
    og_type = models.CharField(max_length=260 , null=True, blank=True)
    og_url = models.URLField(null=True, blank=True)
    og_image = models.ImageField(upload_to="og_images", null=True, blank=True)
    
    
 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.page_name)
        super(Page, self).save(*args, **kwargs)

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





# heading_social_media_container_by_2
# heading_media_with_border_container_by_2
# heading_logo_name_short_descrip_with_border_container_by_5
# heading_icon_name_short_descrip_without_border_container_by_3
# heading_sub_heading_icon_media_by_3
# heading_media_without_border_container_by_2
# heading_logo_name_short_descrip_with_border_container_by_4
# heading_logo_name_short_descrip_border_container_by_3
# heading_icon_short_descrip_name_border_container_by_4
# heading_name_short_descrip_border_container_by_4

 
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
    short_description = HTMLField("Short_description", null=True, blank=True)
    target_url = models.URLField(blank=True, null=True)

    
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
    # description = models.TextField( blank=True, null=True)
    description = HTMLField("Description", null=True, blank=True)
    target_url = models.URLField(blank=True, null=True)


    
    def __str__(self):
        return self.heading



class IconWithHeading(models.Model):
    section = models.ForeignKey(Section, related_name="icon_with_heading", on_delete=models.CASCADE)
    heading = models.CharField(max_length=255, blank=True, null=True)
    sub_heading = models.TextField(null=True, blank=True)
    icon = models.ImageField()
    target_url = models.URLField(blank=True, null=True)

    
    def __str__(self):
        return self.heading




class HeadingWithDescription(models.Model):
    section = models.ForeignKey(Section, related_name="heading_with_description", on_delete=models.CASCADE)
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255, blank=True, null=True)
    description = HTMLField("Description", null=True, blank=True)
    target_url = models.URLField(blank=True, null=True)


    
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
    description = HTMLField("Description", null=True, blank=True) 


    def __str__(self):
        return self.heading