from ..views import *
from django.test import TestCase, SimpleTestCase
from django.urls import resolve, reverse



class TestBlogUrl(SimpleTestCase):

    def test_post_list_url_resolve(self):
        url = reverse('blog:post-list')
        self.assertEquals(resolve(url).func.view_class, PostListView)
        


    def test_post_detail_url_resolve(self):
        url = reverse('blog:post-detail', kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class, PostDetailView)


    def test_post_create_url_resolve(self):
        url = reverse('blog:post-create')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)


    def test_post_edit_url_resolve(self):
        url = reverse('blog:post-edit', kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class, PostEditView)


    def test_post_delete_url_resolve(self):
        url = reverse('blog:post-delete', kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)