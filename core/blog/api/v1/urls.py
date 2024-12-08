from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter



app_name = 'api-v1'


# router yeki az option haye ViewSet hast. karesh ine ke khodesh url haye ViewSet ro automatic dorost mikone 
router = DefaultRouter()
# line paeein baraye register kardan hast ke 3 vorodi migire 1- url chi bashe 2- esme ViewSet 3- basename hamon name hast
router.register('post', views.PostModelViewSet, basename='post')
router.register('category', views.CategoryModelViewSet, basename='category')

# line paeen baraye ine ke url haei ke router sakhte be urlpatterns ezaafe beshan
urlpatterns = router.urls


# urlpatterns = [
#     # path('posts/', views.PostListView, name='post-list'),
#     # path('post/<int:id>/', views.PostDetailView, name='post-detail'),
#     # path('posts/', views.PostList.as_view(), name='post-list'),
#     # path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),

#     # dakhel vorodi as_view goftam ke method get man function list hast
#     path('posts/', views.PostViewSet.as_view({'get':'list', 'post':'create'}), name='post-list'),
#     path('post/<int:pk>/', views.PostViewSet.as_view({'get':'retrieve', 'delete':'destroy', 'put':'update', 'patch':'partial_update'}), name='post-detail')

# ]