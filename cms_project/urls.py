from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from cms_app import views
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView
from cms_app.views import PageView, PageCreateView, PageUpdateView, LandingPageAssetsListCreateView
from django.contrib.sitemaps.views import sitemap
from blog.views import BlogSitemap
from cms_app.views import PageSitemap


sitemaps = {
    'blogs': BlogSitemap,
    'pages': PageSitemap,
}

urlpatterns = [
    path('', PageView.as_view()),
    path('admin/', admin.site.urls),
    path('cms_app/', include("cms_app.urls")),
    path('pages/new/', PageCreateView.as_view(), name="page_create"),
    path('pages/<str:slug>/update/', PageUpdateView.as_view(), name="page_update"),
    path('pages/assets/', LandingPageAssetsListCreateView.as_view(), name="page_assets_list"),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}), 
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', include('blog.urls', 'blog')),
    path('dashboard/', include('dashboard.urls', 'dashboard')),
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('robots.txt/', include('robots.urls')),
    path('<str:slug>/', PageView.as_view(), name="page_detail"),
 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
