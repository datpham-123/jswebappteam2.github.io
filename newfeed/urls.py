from django.urls import path
from .views import  (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CfsListView,
    CfsDetailView,
UserListView,
  )
from . import views

urlpatterns = [
    path('home', PostListView.as_view(), name='newfeed-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='newfeed-about'),
    path('event1/', views.Event1, name='Event1'),
    path('event2/', views.Event2, name='Event2'),
    path('event3/', views.Event3, name='Event3'),
    path('event4/', views.Event4, name='Event4'),
    path('training/', views.training, name='training'),
    path('document/', views.document, name='document'),
    path('confession/', views.sentconfession,name='sent-confession'),
    path('post/<int:pk>/', views.post , name='post'),
    path('', views.JSclub, name='JS_club'),
    path('confession_home', CfsListView.as_view(), name='home-confession'),
    path('post_confession/<int:pk>/', views.post_confession, name='post_confession'),
    path('user_home', UserListView.as_view(), name='home-user'),
]

#video 10: looking for:
# <app>/<model>_<viewtype>.html
