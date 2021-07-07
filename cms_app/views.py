from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.sitemaps import Sitemap
from .models import Page, Section, HeadingLogoNameShortDescrip, ImageWithDescription, IconWithHeading, HeadingWithDescription, HeadingWithMultipleImageUpload, LandingPageAssets, Slide, VideosUrls, Faq
from .forms import SectionForm, HeadingLogoNameShortDescripForm, ImageWithDescriptionForm, IconWithHeadingForm, HeadingWithDescriptionForm, HeadingWithMultipleImageUploadForm, LandingPageAssetsForm, SlideForm, VideosUrlsForm, FaqForm

SECTION_TYPE_CHOICES = [
    ("accordian", ['heading', 'ordering']),
    ("table_with_tech", ['heading', 'ordering']),
    ("table_with_services", ['heading', 'ordering']),
    ("table_with_services_2", ['heading', 'ordering']),
    ("heading_logo_border_by_6", ['heading', 'ordering']),
    ("call_to_action", ['heading', 'ordering']),
    ("call_to_action2", ['heading', 'ordering']),
    ("image_with_cards_by_2", ['heading', 'ordering']),
    ("testimonials", ['heading', 'ordering']),
    ("cards_3", ['heading', 'ordering']),
    ("cards_3_container_fluid", ['heading', 'ordering']),
    ("cards_4", ['heading', 'ordering']),
    ("cards_4_with_link", ['heading', 'ordering']),
    ("all_logos", ['heading', 'ordering']),
    ("col_sm_3", ['heading', 'ordering']),
    ("col_sm_3_bg_white", ['heading', 'ordering']),
    ("col_sm_4", ['heading', 'ordering']),
    ("col_sm_4_bg_white", ['heading', 'ordering']),
    ("col_sm_4_with_link", ['heading', 'ordering']),
    ("col_sm_4_bg_white_with_link", ['heading', 'ordering']),
    ("img_heading_descrip", ['heading', 'ordering']),
    ("video_with_full_container", ['heading', 'ordering']),
    ("video_with_description_by_2", ['heading', 'ordering']),
    ("video_with_description_by_3", ['heading', 'ordering']),
    ("book_an_appointment", ['heading', 'ordering']),
    ("heading_short_des_svg_png_video_2", ['heading', 'ordering']),
    ("slider", ['heading', 'ordering']),
    ("image_with_description", ['heading', 'ordering']),
    ("heading_border_name_by_4", ['heading', 'ordering']),
    ("heading_descrip_container", ['heading', 'ordering']),
    ("heading_icon_short_descrip_name_border_container_by_4", ['heading', 'ordering']),
    ("heading_icon_border_name_by_3", ['heading', 'sub_heading', 'ordering']),
    ("heading_icon_border_name_by_4", ['heading', 'ordering']),
    ("heading_icon_name_border_container_by_4", ['heading', 'ordering']),
    ("heading_icon_name_border_container_by_6", ['heading', 'ordering']),
    ("heading_icon_name_container_by_4", ['heading', 'ordering']),
    ("heading_icon_name_short_descrip_without_border_container_by_3", ['heading', 'ordering']),
    ("heading_img_by_3", ['heading', 'ordering']),
    ("heading_logo_name_border_container_by_6", ['heading', 'ordering']),
    ("heading_logo_name_short_descrip_border_container_by_3", ['heading', 'ordering']),
    ("heading_logo_name_short_descrip_with_border_container_by_4", ['heading', 'ordering']),
    ("heading_media_with_border_container_by_2", ['heading', 'sub_heading', 'ordering']),
    ("heading_media_without_border_container_by_2", ['heading', 'ordering']),
    ("heading_social_media_container_by_2", ['heading', 'sub_heading', 'ordering']),
    ("heading_sub_heading_icon_media_by_3", ['heading', 'sub_heading', 'ordering'])
]
  

# Create your views here.
class PageCreateView(generic.CreateView):
    model = Page
    fields = ['parent_page', 'page_name', 'heading', 'sub_heading', 'page_banner', 'content','title_tag', 'meta_description', 'keywords', 'twitter_description', 'twitter_title', 'twitter_image', 'og_title', 'og_type', 'og_description', 'og_url', 'og_image',]

    def get_context_data(self, **kwargs):
        context = super(PageCreateView, self).get_context_data(**kwargs)
        context['pages'] = Page.objects.filter(parent_page__isnull=True)
        return context

class PageUpdateView(generic.UpdateView):
    model = Page
    fields = ['parent_page', 'page_name', 'heading', 'sub_heading', 'page_banner', 'content','title_tag', 'meta_description', 'keywords', 'twitter_description', 'twitter_title', 'twitter_image', 'og_title', 'og_type', 'og_description', 'og_url', 'og_image',]

    def get_context_data(self, **kwargs):
        context = super(PageUpdateView, self).get_context_data(**kwargs)
        context['pages'] = Page.objects.filter(parent_page__isnull=True)
        return context




class PageView(generic.View):

    forms = {
        'section_form': SectionForm,
        'slider_form':SlideForm,
        'heading_logo_name_short_descrip_form': HeadingLogoNameShortDescripForm,
        'image_with_description_form': ImageWithDescriptionForm,
        'icon_with_heading_form': IconWithHeadingForm,
        'heading_with_description_form': HeadingWithDescriptionForm,
        'heading_with_multiple_image_upload_form': HeadingWithMultipleImageUploadForm,
        'videos_urls_form': VideosUrlsForm
        
    }


    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        if slug == "home":
            return redirect("/")
        if not slug:
            slug = 'home'
        page = get_object_or_404(Page, slug=slug)
        context = {}
        context['page'] = page
        context['pages'] = Page.objects.filter(parent_page__isnull=True, content="")
        context['section_types'] = SECTION_TYPE_CHOICES
        for key, value in self.forms.items():
            context[key] = value()
        return render(request, 'cms_app/page_detail.html', context)


    def post(self, request, *args, **kwargs):
        slug = kwargs.get('slug', "home")
        form_name = request.POST.get('form_name')
        page = get_object_or_404(Page, slug=slug)
        context = {}
        context['page'] = page
        context['pages'] = Page.objects.filter(parent_page__isnull=True, content="")
        context['section_types'] = SECTION_TYPE_CHOICES
        for key, value in self.forms.items():
            context[key] = value()
        form = self.forms[form_name](request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            context[form_name] = form
        return render(request, 'cms_app/page_detail.html', context)



class SectionUpadateView(generic.UpdateView):
    model = Section
    template_name = "cms_app/section_update_form.html"
    fields = ['page', 'section_type', 'heading', 'sub_heading', 'background_image', 'ordering']

    def get_success_url(self):
        return self.get_object().page.get_absolute_url()



class SectionDeleteView(generic.DeleteView):
    model = Section
    template_name = "cms_app/section_delete_form.html"
    fields = ['page', 'section_type', 'heading', 'sub_heading', 'background_image', 'ordering']

    
    def get_success_url(self):
        return self.get_object().page.get_absolute_url()






class LandingPageAssetsListCreateView(generic.View):

    def get(self, request, *args, **kwargs):
        form = LandingPageAssetsForm()
        assets = LandingPageAssets.objects.all()
        return render(request, 'cms_app/landing_page_assets.html', {"form": form, "assets": assets})

    def post(self, request, *args, **kwargs):
        form = LandingPageAssetsForm(request.POST, request.FILES)
        assets = LandingPageAssets.objects.all()
        if form.is_valid():
            form.save()
            return redirect(reverse('page_assets_list'))
        return render(request, 'cms_app/landing_page_assets.html', {"form": form, "assets": assets})


class PageSitemap(Sitemap):

    def items(self):
        return Page.objects.all()





    
class HeadingLogoNameShortDescripUpdateView(generic.UpdateView):
    model = HeadingLogoNameShortDescrip
    template_name = 'cms_app/heading_logo_name_short_descrip_form.html'
    fields = ['heading', 'sub_heading', 'logo_icon', 'short_description', 'target_url']

    def get_success_url(self):
        return self.get_object().section.page.get_absolute_url()



class IconWithHeadingUpdateView(generic.UpdateView):
    model = IconWithHeading
    template_name = 'cms_app/icon_with_heading_form.html'
    fields = ['heading', 'sub_heading', 'icon']
    

    def get_success_url(self):
        return self.get_object().section.page.get_absolute_url()





class ImageWithDescriptionUpdateView(generic.UpdateView):
    model = ImageWithDescription
    template_name = 'cms_app/image_with_description_form.html'
    fields = ['container_type', 'image_alignment', 'background_image', 'photo', 'heading', 'sub_heading', 'description', 'target_url']
   

    def get_success_url(self):
        return self.get_object().section.page.get_absolute_url()


 

 
class HeadingWithDescriptionUpdateView(generic.UpdateView):
    model = HeadingWithDescription
    template_name = 'cms_app/heading_with_description_form.html'
    fields = ['heading', 'sub_heading', 'description']
    

    def get_success_url(self):
        return self.get_object().section.page.get_absolute_url()




class HeadingWithMultipleImageUploadUpdateView(generic.UpdateView):
    model = HeadingWithMultipleImageUpload
    template_name = 'cms_app/heading_with_multiple_image_upload_form.html'
    fields = ['photo']
    
    def get_success_url(self):
        return self.get_object().section.page.get_absolute_url()


class VideosUrlsUpdateView(generic.UpdateView):
    model = VideosUrls
    template_name = 'cms_app/videos_urls.html'
    fields = ['heading', 'sub_heading', 'embed_url', 'description']

    def get_success_url(self):
        return self.get_object().section.page.get_absolute_url()



class FaqUpdateView(generic.UpdateView):
    model = Faq
    template_name = 'cms_app/accordian.html'
    fields = ['question', 'answere', 'ordering']

    def get_success_url(self):
        return self.get_object().section.page.get_absolute_url()





# -----delete view-----

class HeadingLogoNameShortDescripDeleteView(generic.DeleteView):
    model = HeadingLogoNameShortDescrip
    template_name = 'cms_app/heading_logo_name_short_descrip_confirm_delete.html'
    
    def get_success_url(self):
        return self.get_object().section.page.get_absolute_url()



class IconWithHeadingDeleteView(generic.DeleteView):
    model = IconWithHeading
    template_name = 'cms_app/icon_with_heading_form.html'

    def get_success_url(self):
        return self.get_object().section.page.get_absolute_url()
   




class ImageWithDescriptionDeleteView(generic.DeleteView):
    model = ImageWithDescription
    template_name = 'cms_app/image_with_description_form.html'

    def get_success_url(self):
        return self.get_object().section.page.get_absolute_url()
    

 

 
class HeadingWithDescriptionDeleteView(generic.DeleteView):
    model = HeadingWithDescription
    template_name = 'cms_app/heading_with_description_form.html'

    def get_success_url(self):
        return self.get_object().section.page.get_absolute_url()
    



class HeadingWithMultipleImageUploadDeleteView(generic.DeleteView):
    model = HeadingWithMultipleImageUpload
    template_name = 'cms_app/heading_with_multiple_image_upload_form.html'


    def get_success_url(self):
        return self.get_object().section.page.get_absolute_url()
  



class FaqDeleteView(generic.DeleteView):
    model = Faq
    template_name = 'cms_app/accordian.html'

    def get_success_url(self):
        return self.get_object().section.page.get_absolute_url()

