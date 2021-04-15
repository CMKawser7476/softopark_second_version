from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PageListView, SignupView, DashboardView, PostCreateView, PostListView, PostUpdateView, post_draft_view, CategoryCreateView, CategoryUpdateView, CategoryListView

app_name = "dashboard"

urlpatterns = [
    path('', DashboardView.as_view(), name="dashboard"),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('pages/', PageListView.as_view(), name="page_list"),
    path('posts/', PostListView.as_view(), name="post_list"),
    path('posts/new/', PostCreateView.as_view(), name="post_create"),
    path("<str:slug>/edit/", PostUpdateView.as_view(), name="post_update"),
    path("<str:slug>/draft/", post_draft_view, name="post_draft"),
    path("<str:slug>/draft/", post_draft_view, name="post_draft"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/new/", CategoryCreateView.as_view(), name="category_create"),
    path("categories/<str:slug>/edit/", CategoryUpdateView.as_view(), name="category_update"),
]