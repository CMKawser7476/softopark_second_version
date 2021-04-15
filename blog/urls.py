from django.urls import path
from .views import CategoryCreateView, CategoryUpdateView, BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView

app_name = "blog"

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("<str:slug>/details/", BlogDetailView.as_view(), name="blog_detail"),
    path("<str:slug>/edit/", BlogUpdateView.as_view(), name="blog_update"),
    path("new/", BlogCreateView.as_view(), name="blog_create"),
    path("categories/new/", CategoryCreateView.as_view(), name="category_create"),
    path("categories/<str:slug>/update/", CategoryUpdateView.as_view(), name="category_update"),
]