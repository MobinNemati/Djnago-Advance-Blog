from rest_framework import serializers
from ...models import Post, Category
from accounts.models import Profile


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)



#serialize kardan mesle form sakhtan hast. ham Form darim ham ModelForm inja ham Serializer darim ModelSerializer ham darim
class PostSerializer(serializers.ModelSerializer):
    # line paeein goftam ke yek field mikham ezafe konam ke read only hast, va vaslesh kon be function get_snippet ke 
    # dakhel model post tarif kardam
    snippet = serializers.ReadOnlyField(source='get_snippet')

    # line paeein goftam ke yek field mikham ezafe konam ke url hastesh va, vaslesh kon be get_absolute_api_url va readonly ham bokon
    # in field url har post ro dakhel field relative_url minevise
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)

    # line paeein vasle be function get_absolute_url va full url har post ro peida mikone 
    absolute_url = serializers.SerializerMethodField()

    # bedon line paeein vaghti ma vard post-list mishim field category ro be ma id categorish neshon mide
    # vorodi line paeein goftim ke tedad category har post bishtar az 1 nist(many=False), va goftim ke jaye id name category ro 
    # neshon bede, va akhari ham goftim haame category haro biar baraye inke vaghti bekhaim category post ro avaz konim betonim 
    # baghie category haro bebinim
    category = serializers.SlugRelatedField(many=False, slug_field='name', queryset=Category.objects.all())



    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'image', 'category', 'snippet', 'status', 'relative_url', 'absolute_url', 'created_date', 'published_date']
        # dakhel vorodi line paeein har field e ro ezafe konim on field faghat ghabel didan mishe va dige 
        # dakhel form ha vojod nadare va ghabel taghir nist 
        read_only_fields = ['author',] 


    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)

    # function paeein mitone har field ya har chizi ro ghabl az namayesh dadan on taghir bede. mesal paeein:
    def to_representation(self, instance):

        # line paeein request e ke karbar mifreste ro migire. request karbar ro mishe be sorat zir print kard va did che chiz haei
        # ba request ersal mishe
        request = self.context.get('request')
        # print(request.__dict__)

        rep = super().to_representation(instance)

        # line paeein goftam az dakhel request karbar parser_context.kwargs ro begir bebin age pk dasht 
        # yani karbar request be url post-detail zade va field haei ke goftam ro None bezar age dakhel kwargs pk vojod nadasht
        # yani karbar request be url post-list zade va field content ro None bezar
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('snippet', None)
            rep.pop('relative_url', None)
            rep.pop('absolute_url', None)
        else:
            rep.pop('content', None)


        # line paeein migim ke ghabl namayesh, dakhel field category id va name on ro bezar 
        # manzor az instance khode object hast
        rep['category'] = CategorySerializer(instance.category, context={'request':request}).data
        return rep


    def create(self, validated_data):
        validated_data['author'] = Profile.objects.get(user__id = self.context.get('request').user.id)
        return super().create(validated_data)




class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']