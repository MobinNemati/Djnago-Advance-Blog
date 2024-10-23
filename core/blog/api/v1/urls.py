from django.urls import path, include
from . import views


app_name = 'api-v1'


urlpatterns = [
    # path('posts/', views.PostListView, name='post-list'),
    # path('post/<int:id>/', views.PostDetailView, name='post-detail'),
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('post/<int:id>/', views.PostDetail.as_view(), name='post-detail'),

]