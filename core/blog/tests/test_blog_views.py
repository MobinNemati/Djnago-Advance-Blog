from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..models import Post, Category
from datetime import datetime


User = get_user_model()


class TestBlogView(TestCase):



    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            email='mobin@gmail.com',
            password='testpass123'
        )

        post =  Post.objects.create(
            author = self.user.profile,
            title = 'test',
            content = 'test dec',
            status = True,
            category = None,
            published_date = datetime.now(),
        )

    def test_blog_post_list_url_successful_response(self):
        self.client.force_login(self.user)
        url = reverse('blog:post-list')
        # client, to line paeen kare request zadan ro anjam mide
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='blog/post_list.html')


    def test_blog_post_list_url_unsuccessful_response(self):
        url = reverse('blog:post-list')
        # client, to line paeen kare request zadan ro anjam mide
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)
