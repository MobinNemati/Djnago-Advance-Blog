from django.test import SimpleTestCase, TestCase
from datetime import datetime
from ..forms import PostForm
from ..models import Category



class TestBlogForm(TestCase):
    

    def test_post_form_with_valid_data(self):

        # line paeen darim ye category misazim baraye test kardan form
        # to in test ma darim ba database kar mikonim(sakht category) baraye hamin
        # baiad az TestCase estefade konim bejaye SimpleTestCase
        category_obj = Category.objects.create(name='test')

        form = PostForm(data={
            'title':'test',
            'content':'testjbhjdec',
            'status':True,
            'category':category_obj,
            'published_date':datetime.now()
        })
        # assert shabih if hast ama if edame peida mikone ama assert motavaghef mishe
        # assertTrue yani baiad form.is_valid() True bashe age nabashe assertTrue error barmigardone
        self.assertTrue(form.is_valid())



    def test_post_form_with_no_data(self):
        form = PostForm(data={})
        # assertFalse yani baiad form.is_valid False bargardone vagarna assert error mide
        self.assertFalse(form.is_valid())
