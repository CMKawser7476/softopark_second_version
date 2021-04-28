from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import SoftoUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from cms_app.models import Page
from blog.models import Blog, Category
from accounts.models import User

# Create your views here.
class PageListView(generic.ListView):
    paginate_by=10
    model = Page
    template_name = 'dashboard/page_list.html'


class SignupView(generic.CreateView):
    model = User
    form_class = SoftoUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('dashboard:login')



class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'dashboard/dashboard.html'
    login_url = reverse_lazy('dashboard:login')

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['total_pages'] = Page.objects.count()
        context['total_posts'] = Blog.objects.count()
        context['total_categories'] = Category.objects.count()
        context['total_users'] = User.objects.count()

        return context



class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Category
    fields = ['parent', 'name', 'description', 'cover_photo']
    template_name = 'dashboard/category_form.html'
    success_url = reverse_lazy('dashboard:category_list')
    login_url = reverse_lazy('dashboard:login')





class CategoryUpdateView(generic.UpdateView):
    model = Category
    fields = ['parent', 'name', 'description', 'cover_photo']
    template_name = 'dashboard/category_form.html'
    success_url = reverse_lazy('dashboard:category_list')

    def get_object(self, queryset=None):
        category_slug = self.kwargs.get("slug")
        category = get_object_or_404(Category, slug=category_slug)
        return category



class CategoryListView(generic.ListView):
    paginate_by = 10
    model = Category
    template_name = 'dashboard/categories_list.html'





class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Blog
    fields = ['title', 'description', 'photo', 'publish_at', 'featured', 'categories', 'blog_title_tag','blog_meta_description', 'blog_keywords', 'blog_twitter_description', 'blog_twitter_title', 'blog_twitter_image', 'blog_og_title', 'blog_og_description', 'blog_og_url', 'blog_og_image']
    template_name = 'dashboard/blog_form.html'
    success_url = reverse_lazy('dashboard:post_list')
    login_url = reverse_lazy('dashboard:login')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostListView(generic.ListView):
    model = Blog
    template_name = 'dashboard/blog_list.html'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        draft = self.request.GET.get('draft', 'false')
        published = self.request.GET.get('published', 'true')
        if draft == 'false' and published == 'true':
            qs = qs.filter(deleted_at__isnull=True).filter(publish_at__lte=timezone.now())
        elif published == 'false':
            qs = qs.filter(publish_at__gte=timezone.now())
        else:
            qs = qs.filter(deleted_at__isnull=False)
        return qs


class PostUpdateView(generic.UpdateView):
    model = Blog
    fields = ['title', 'description', 'photo', 'publish_at', 'featured', 'categories', 'blog_title_tag','blog_meta_description', 'blog_keywords', 'blog_twitter_description', 'blog_twitter_title', 'blog_twitter_image', 'blog_og_title', 'blog_og_description', 'blog_og_url', 'blog_og_image']
    template_name = 'dashboard/blog_form.html'
    success_url = reverse_lazy('dashboard:post_list')

    def get_object(self, queryset=None):
        post_slug = self.kwargs.get("slug")
        post = get_object_or_404(Blog, slug=post_slug)
        return post


def post_draft_view(request, *args, **kwargs):
    post = get_object_or_404(Blog, slug=kwargs.get('slug'))
    if post.deleted_at or post.publish_at > timezone.now():
        post.deleted_at = None
        post.publish_at = timezone.now()
    else:
        post.deleted_at = timezone.now()
    post.save()
    return redirect(reverse_lazy('dashboard:post_list'))