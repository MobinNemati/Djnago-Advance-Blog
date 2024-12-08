from typing import Any
from django.forms import BaseModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, RedirectView
from accounts.models import User
from blog.models import Post
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView, DeleteView
from .forms import PostForm
# baraye LoginRequired baiad LoginRequiredMixin be on class e ke mikhaim required beshe ezafe konim
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin




# ferestadan context ba function
"""
def indexView(request):
    name = 'obin'
    context = {'name':name}
    return render(request, 'index.html', context)
"""



# ferestadan context ba class
"""
class IndexView(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'mobin'
        context['user'] = Post.objects.all()
        return context
"""



# redirect kardan be maktabkhooneh ba estefade az function
"""
def RedirectToMaktab(requset):
    return redirect('https://maktabkhooneh.com')
"""


# redirect kardan ba estefade az class
class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.com'


    # def paeein pk e ke az url omade ro migire mibine post e ba on pk hast ya na, age bod
    # post ro print mikone dakhel terminal va user redirect mishe be url e ke neveshtim 
    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    

# estefade az ListView dar class
# ListView baraye list kardan object haye model estefade mishe
# baraye avordan object ha baiad az object_list dar template estefade kard
class PostListView(LoginRequiredMixin, ListView):

    # baiad model e ke mikhaim list konim ro moarefi konim
    '''
    model = Post
    queryset = Post.objects.all()
    '''

    # mitonim ba estefade az paginate_by begim dar har safe chand post bashe
    paginate_by = 2

    # ba ordering migim bar che asas post ha list shavand vali code paeein dar sorati kar mikone ke ma az get_queryset estefade nakonim
    # az model ya queryset bala estefade konim
    '''
    ordering = '-id'
    '''

    # mitonim bejaie inke kole model ro moarefi konim, mitonim filter roye posta anjam bedim va baad befrestim mesl code paeein
    def get_queryset(self):
        posts = Post.objects.filter(status=True).order_by('-id')
        return posts

    # ba context_object_name mishe esm context ke ersal mishe be template ra avaz kard 
    context_object_name = 'posts' 



# DetailView baraye neshon dadan object haye yek model hast ke baraye page haye single estefade mishe
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post' 



# neshon dadan form va save on ba FormView
'''
class PostCreateView(FormView):
    # 3 ta field peein ejbarie

    # address template create post
    template_name = 'blog/post_form.html'

    # form e ke baraye create post estefade mikoni
    form_class = PostForm

    # baad az ersal dorost form be url paeein redirect mishi
    success_url = '/blog/posts/'

    # baraye save kardan ya taghir form ersal shode baiad az function paeein estefade konim
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''


# neshon dadan form va save automatic ba CreateView
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # esme default template create view post_form.html hast ke mishe ba template_name esm on ro taghir dad

    # mishe az fields estefade kard baraye neshon dadan fields haye form 
    # ya mitonim az form_class estefade konim ke form e ke az ghabl amade kardim ro neshon bedim
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']
    form_class = PostForm
    success_url = '/blog/posts/'


    def form_valid(self, form):
        # ba har account e login bashi code paeein ba on acc ghesmat author form ro por mikone
        form.instance.author = self.request.user.profile
        return super().form_valid(form)
    

# baraye edit ya update kardan post ha va form ha mitonim az UpdateView estefade konim
class PostEditView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = "blog.change_post"

    model = Post
    form_class = PostForm
    success_url = '/blog/posts/'



# baraye delete kardan post mitonim az DeleteView estefade konim
# va baraye delete kardan baiad safe confrim be karbar neshon bedim ta confrim kone
# va esm template default on post_confirm_delete.html hast ke mitonim ba template_name esm on ro avaz konim
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/blog/posts/'



