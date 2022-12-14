# from dataclasses import fields
# from pyexpat import model
# from django.db import models
# from django.forms import fields
from django import forms
from .models import Section, HeadingLogoNameShortDescrip, ImageWithDescription, IconWithHeading, HeadingWithDescription, HeadingWithMultipleImageUpload, LandingPageAssets, Slide, VideosUrls, Faq #ClientDataSubmit


class LandingPageAssetsForm(forms.ModelForm):

    class Meta():
        model = LandingPageAssets
        fields = "__all__"


class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = "__all__"



class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = "__all__"
   

class HeadingLogoNameShortDescripForm(forms.ModelForm):
    class Meta:
        model = HeadingLogoNameShortDescrip
        fields = "__all__"
 

class ImageWithDescriptionForm(forms.ModelForm):
    class Meta:
        model = ImageWithDescription
        fields = "__all__"


class IconWithHeadingForm(forms.ModelForm):
    class Meta:
        model = IconWithHeading
        fields = "__all__"



class HeadingWithDescriptionForm(forms.ModelForm):
    class Meta:
        model = HeadingWithDescription
        fields = "__all__"



class HeadingWithMultipleImageUploadForm(forms.ModelForm):
    class Meta:
        model = HeadingWithMultipleImageUpload
        fields = "__all__" 

        

class VideosUrlsForm(forms.ModelForm):
    class Meta:
        model = VideosUrls
        fields = "__all__"


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = "__all__"


# class ClientDataForm(forms.ModelForm):
#     class Meta:
#         model = ClientDataSubmit
#         fields = "__all__"
