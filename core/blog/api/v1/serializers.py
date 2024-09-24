from rest_framework import serializers
from ...models import Post


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)



#serialize kardan mesle form sakhtan hast ham Form darim ham ModelForm darim inja ham Serializer darim ModelSerializer ham darim
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'status', 'created_date', 'published_date']