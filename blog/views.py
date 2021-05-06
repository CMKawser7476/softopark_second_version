from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic
from django.contrib.sitemaps import Sitemap
from django.utils import timezone
from .models import Category, Blog
from cms_app.models import Page
from django.db.models import Q

# Create your views here.
class CategoryCreateView(generic.CreateView):
    model = Category
    fields = ['parent', 'name', 'description', 'cover_photo']
    success_url = "/blog"


class CategoryUpdateView(generic.UpdateView):
    model = Category
    fields = ['parent', 'name', 'description', 'cover_photo']
    success_url = "/blog"

    def get_object(self, queryset=None):
        category_slug = self.kwargs.get("slug")
        category = get_object_or_404(Category, slug=category_slug)
        return category

class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ['title', 'description', 'photo', 'publish_at', 'featured', 'categories', 'blog_title_tag', 'blog_og_type', 'blog_meta_description', 'blog_keywords', 'blog_twitter_description', 'blog_twitter_title', 'blog_twitter_image', 'blog_og_title', 'blog_og_description', 'blog_og_url', 'blog_og_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ['title', 'description', 'photo', 'publish_at', 'featured', 'categories', 'blog_title_tag', 'blog_og_type', 'blog_meta_description', 'blog_keywords', 'blog_twitter_description', 'blog_twitter_title', 'blog_twitter_image', 'blog_og_title', 'blog_og_description', 'blog_og_url', 'blog_og_image']

    def get_object(self, queryset=None):
        post_slug = self.kwargs.get("slug")
        post = get_object_or_404(Blog, slug=post_slug)
        return post



class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        queryset = Blog.objects.filter(deleted_at__isnull=True).filter(publish_at__lt=timezone.now())
        category_slug = self.request.GET.get('category', '')
        search = self.request.GET.get('search', '')
        if category_slug:
            category_obj = get_object_or_404(Category, slug=category_slug)
            queryset = category_obj.blog_posts.filter(deleted_at__isnull=True).filter(publish_at__lt=timezone.now())
        if search:
            queryset = Blog.objects.filter(Q(title__icontains=search) | Q(description__icontains=search)).distinct()
        return queryset


    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['pages'] = Page.objects.filter(parent_page__isnull=True, content="")
        context['categories'] = Category.objects.all()
        return context


class BlogDetailView(generic.DetailView):
    model = Blog

    def get_object(self, queryset=None):
        post_slug = self.kwargs.get("slug")
        post = get_object_or_404(Blog, slug=post_slug)
        return post

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['pages'] = Page.objects.filter(parent_page__isnull=True, content="")
        return context


class BlogSitemap(Sitemap):
    
    def items(self):
        return Blog.objects.filter(deleted_at__isnull=True).filter(publish_at__lt=timezone.now())