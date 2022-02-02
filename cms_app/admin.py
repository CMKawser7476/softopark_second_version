from django.contrib import admin
from .models import Page, Section, HeadingLogoNameShortDescrip,  ImageWithDescription, IconWithHeading, HeadingWithDescription, HeadingWithMultipleImageUpload, LandingPageAssets, Slide, VideosUrls, Faq, LeadData
     

# Register your models here.
admin.site.register(Page)
admin.site.register(LandingPageAssets)
admin.site.register(Section)
admin.site.register(Slide)
admin.site.register(HeadingLogoNameShortDescrip)
admin.site.register(ImageWithDescription)
admin.site.register(IconWithHeading)
admin.site.register(HeadingWithMultipleImageUpload)
admin.site.register(HeadingWithDescription)
admin.site.register(VideosUrls)
admin.site.register(Faq)
admin.site.register(LeadData)


