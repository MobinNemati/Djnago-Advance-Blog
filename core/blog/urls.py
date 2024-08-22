from django.urls import path
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

    # ba estefade az RedirectView mishe vaghti karbar vard in url mishe redirect beshe be link e ke dadim
    path('go-to-maktabkhooneh', RedirectView.as_view(url='https://www.maktabkhooneh.com/'), name='go-to-maktabkhooneh'),
    path('go-to-index', RedirectView.as_view(pattern_name='blog:cbv-index'), name='go-to-index'),

    path('go-to-maktab/<int:pk>', views.RedirectToMaktab.as_view(), name='go-to-maktab'),
    path('post/', views.PostList.as_view(), name='post-list'),

]