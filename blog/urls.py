from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    NewsListView,
    NewsDetailView,
    NewsCreateView,
    NewsUpdateView,
    NewsDeleteView,
    UserNewsListView
)
from . import views

urlpatterns = [
    #urls correspondientes a las paginas de posteo de los usuarios
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    #urls correspondientes a las paginas de noticias
    path('user/<str:username>', UserNewsListView.as_view(), name='user-news'),
    path('news/news_posted',NewsListView.as_view(),name='blog-news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('news/new/',NewsCreateView.as_view(),name='news-create'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='news-update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news-delete'),

    #url correspondiente a la pagina "sobre nosotros"
    path('about/', views.about, name='blog-about'),
]
