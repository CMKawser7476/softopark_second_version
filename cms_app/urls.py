from django.urls import path
from django.views.generic.edit import UpdateView
from .views import SectionUpadateView, SectionDeleteView, HeadingLogoNameShortDescripUpdateView, IconWithHeadingUpdateView, ImageWithDescriptionUpdateView, HeadingWithDescriptionUpdateView, HeadingWithMultipleImageUploadUpdateView, HeadingLogoNameShortDescripDeleteView, IconWithHeadingDeleteView, ImageWithDescriptionDeleteView, HeadingWithDescriptionDeleteView, HeadingWithMultipleImageUploadDeleteView, VideosUrlsUpdateView, VideourlsDeleteView, FaqUpdateView  
 

app_name = "cms_app"

urlpatterns = [
    # UpdateView path
    path('sections/all_sections/<int:pk>/', SectionUpadateView.as_view(), name="section_update_view"),
    path('items/heading_logo_name_short_description/<int:pk>/', HeadingLogoNameShortDescripUpdateView.as_view(), name="heading_logo_name_short_descrip_view"),
    path('items/icon_with_heading/<int:pk>/', IconWithHeadingUpdateView.as_view(), name="icon_with_heading_view"),
    path('items/image_with_description/<int:pk>/', ImageWithDescriptionUpdateView.as_view(), name="image_with_description_view"),
    path('items/heading_with_description/<int:pk>/', HeadingWithDescriptionUpdateView.as_view(), name="heading_with_description_view"),
    path('items/heading_with_multiple_image_upload/<int:pk>/', HeadingWithMultipleImageUploadUpdateView.as_view(), name="heading_with_multiple_image_upload_view"),
    path('items/video_urls/<int:pk>/', VideosUrlsUpdateView.as_view(), name="video_urls_update_view"),
    # path('items/submit_data/', clientinfosubmit, name="lead_collection_view"),

    
    # DeleteView path
    path('sections/all_section_delete/<int:pk>/', SectionDeleteView.as_view(), name="section_delete_view"),
    path('items/heading_logo_name_short_description_delete_view/<int:pk>/', HeadingLogoNameShortDescripDeleteView.as_view(), name="heading_logo_name_short_descrip_delete_view"),
    path('items/icon_with_heading_delete_view/<int:pk>/', IconWithHeadingDeleteView.as_view(), name="icon_with_heading_delete_view"),
    path('items/image_with_description_delete_view/<int:pk>/', ImageWithDescriptionDeleteView.as_view(), name="image_with_description_delete_view"),
    path('items/heading_with_description_delete_view/<int:pk>/', HeadingWithDescriptionDeleteView.as_view(), name="heading_with_description_delete_view"),
    path('items/heading_with_multiple_image_upload_delete_view/<int:pk>/', HeadingWithMultipleImageUploadDeleteView.as_view(), name="heading_with_multiple_image_upload_delete_view"),
    path('items/video_urls_delete/<int:pk>/', VideourlsDeleteView.as_view(), name="video_urls_delete_view"),

]