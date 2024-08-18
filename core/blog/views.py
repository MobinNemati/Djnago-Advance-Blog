from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, RedirectView
from accounts.models import User
from blog.models import Post



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


# redirect kardan be maktabkhooneh ba estefade az class

"""

"""
class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.com'

    # def paeein pk e ke az url karbar vard karde ro migire mibine post e ba on pk hast ya na, age bod
    # post ro print mikone dakhel terminal va user redirect mishe be url e ke neveshtim 
    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)