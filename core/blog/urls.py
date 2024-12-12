from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView


app_name = 'blog'

urlpatterns = [
    #path('fbv-index', views.indexView, name='fbv-index'),

    # ba estefade az TemplateView dar url ke mishe mostaghim az yek url vasl shod be template bedon estefade az view 
    # va mishe context ham ferstad
    # path('cbv-index', TemplateView.as_view(template_name='index.html', extra_context={'name':'mobin'})),

    # path('cbv-index', views.IndexView.as_view(), name='cbv-index'),

    # ba estefade az RedirectView mishe vaghti karbar vard in url mishe redirect beshe be link e ke dadim !bedon estefade az view
    # path('go-to-maktabkhooneh/', RedirectView.as_view(url='https://www.maktabkhooneh.com/'), name='go-to-maktabkhooneh'),
    # path('go-to-index/', RedirectView.as_view(pattern_name='blog:cbv-index'), name='go-to-index'),

    path('go-to-maktab/<int:pk>/', views.RedirectToMaktab.as_view(), name='go-to-maktab'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # baraye estefade az api dar appe blog yek url misazim ke maalom she az api estefade mikone in page
    # baad baiad dakhel app blog yek folder besazim be esme api va dakhl on views va url besazim va url paeein ro vasl konim be folder api
    # dakhel folder api ham view haye marbot be api ro misazim
    path('api/v1/', include('blog.api.v1.urls')),

]