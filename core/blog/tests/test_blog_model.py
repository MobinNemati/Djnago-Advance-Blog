from ..models import Post, Category
from django.contrib.auth import get_user_model
from accounts.models import User, Profile
from django.test import SimpleTestCase, TestCase
from datetime import datetime


class TestBlogModel(TestCase):

    # vaghti bekhaim code e ro to test haye mokhtalef estefade konim bejaye inke har bar
    # biaim on code ro benevisim to func haye mokhatlef. miaim yebar to func setUp minevisim 
    # va harvaght khastim mitonim az on estefade mikonim to test haye mokhtalef
    # code paeen ma omadim yebar ye user sakhtim.
    # hala harvaght bekhaim mitonim in user ro seda konim to test haye mokhtalef
    def setUp(self):
        self.user = User.objects.create_user(email='test@gmail.com', password='a/@1234567')



    def test_create_post_with_valid_data(self):

        post =  Post.objects.create(
            author = self.user.profile,
            title = 'test',
            content = 'test dec',
            status = True,
            category = None,
            published_date = datetime.now(),
        )
        # baraye inke befahmim post skahte shode ya na assertEqual ro seda misazim 
        # migim check kon title be esm 'test' sakhte shode? age na error bede
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEquals(post.title, 'test')