from django.urls import path
from .views import HeadingLogoNameShortDescripUpdateView, IconWithHeadingUpdateView, ImageWithDescriptionUpdateView, HeadingWithDescriptionUpdateView, HeadingWithMultipleImageUploadUpdateView, HeadingLogoNameShortDescripDeleteView, IconWithHeadingDeleteView, ImageWithDescriptionDeleteView, HeadingWithDescriptionDeleteView, HeadingWithMultipleImageUploadDeleteView


app_name = "cms_app"

urlpatterns = [
    # url('', some_text_view, name="varible_pass")
    path('items/heading_logo_name_short_description/<int:pk>/', HeadingLogoNameShortDescripUpdateView.as_view(), name="heading_logo_name_short_descrip_view"),
    # path('items/sliders/<int:pk>/', View.as_view(), name="slide_view"),
    path('items/icon_with_heading/<int:pk>/', IconWithHeadingUpdateView.as_view(), name="icon_with_heading_view"),
    path('items/image_with_description/<int:pk>/', ImageWithDescriptionUpdateView.as_view(), name="image_with_description_view"),
    path('items/heading_with_description/<int:pk>/', HeadingWithDescriptionUpdateView.as_view(), name="heading_with_description_view"),
    path('items/heading_with_multiple_image_upload/<int:pk>/', HeadingWithMultipleImageUploadUpdateView.as_view(), name="heading_with_multiple_image_upload_view"),
    # DeleteView path
    path('items/heading_logo_name_short_description_delete_view/<int:pk>/', HeadingLogoNameShortDescripDeleteView.as_view(), name="heading_logo_name_short_descrip_delete_view"),
    path('items/icon_with_heading_delete_view/<int:pk>/', IconWithHeadingDeleteView.as_view(), name="icon_with_heading_delete_view"),
    path('items/image_with_description_delete_view/<int:pk>/', ImageWithDescriptionDeleteView.as_view(), name="image_with_description_delete_view"),
    path('items/heading_with_description_delete_view/<int:pk>/', HeadingWithDescriptionDeleteView.as_view(), name="heading_with_description_delete_view"),
    path('items/heading_with_multiple_image_upload_delete_view/<int:pk>/', HeadingWithMultipleImageUploadDeleteView.as_view(), name="heading_with_multiple_image_upload_delete_view"),
]