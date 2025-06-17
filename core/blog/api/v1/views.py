from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from ...models import Post, Category
from . serializers import PostSerializer, CategorySerializer
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import PostPagination





'''
@api_view(["GET", "POST"])
# age vorodi line paeein IsAuthenticated vared konim faghat kesaei ke login kardan mitonan bebinan 
# age vorodi line paeein IsAdminUser vared konim faghat kesaei ke admin hastan mitonan bebinan
# age vorodi line paeein IsAuthenticatedOrReadOnly vared konim faghat kesaei ke login kardan dastresi be sakht post va edit daran va baghie mitonan faghat bebinan
@permission_classes([IsAuthenticatedOrReadOnly])
def PostListView(request):
    if request.method == 'GET':
        post = Post.objects.filter(status=True)
        # serializer default faght yek object ro json mikone age bishtar az yeki bashe baiad begim many=true
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data) # request.data mige data e ke ersal shode ro bede
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''



'''
# list kardan post ha ba estefade az classbase va APIView
class PostList(APIView):

    # age vorodi line paeein IsAuthenticated vared konim faghat kesaei ke login kardan mitonan bebinan 
    # age vorodi line paeein IsAdminUser vared konim faghat kesaei ke admin hastan mitonan bebinan
    # age vorodi line paeein IsAuthenticatedOrReadOnly vared konim faghat kesaei ke login kardan
    # dastresi be sakht post va edit daran va baghie mitonan faghat bebinan
    permission_classes = [IsAuthenticatedOrReadOnly]
    # line paeein mesle form class hast, miad form ba input haye PostSerializer misaze
    serializer_class = PostSerializer



    def get(self, request):
        post = Post.objects.filter(status=True)
        # serializer default faght yek object ro json mikone age bishtar az yeki bashe baiad begim many=true
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data) # request.data mige data e ke ersal shode ro bede
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
'''


'''
# list kardan post ha ba estefade az option haye generic APIView
# dakhel ListCreateAPIView khodesh query haye get va post ro dare baraye hamin nesbat be code haye bala besyar kotah tar shode
class PostList(ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

'''








'''
@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticatedOrReadOnly])
def PostDetailView(request, id):
    post = get_object_or_404(Post, pk=id, status=True)

    if request.method == 'GET':

        # serializer karesh ine ke vaghti ma az model yek object e migirim ono tabdil kone be json ke betonim dar page bebinim.
        # agar az api estefade nakonim vaghti object e az model begirim khodesh tabdil be json mishe ama dar api ba estefade az serializer
        # mitonim be json tablin konim. dakhel file serializers baiad class e besazim ke che field haei tabdil be json beshan 
        # line paeein post ro ferstadim be class serializer va in class tebghe field haei ke behesh goftim
        # field haye post ro be json tabdil mikone
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    # request PUT baraye update kardan hast
    elif request.method == 'PUT':
        serializer = PostSerializer(post, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response({'message':'itme removed successfully'}, status=status.HTTP_204_NO_CONTENT)
'''



'''
class PostDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)

        # serializer karesh ine ke vaghti ma az model yek object e migirim ono tabdil kone be json ke betonim dar page bebinim.
        # agar az api estefade nakonim vaghti object e az model begirim khodesh tabdil be json mishe ama dar api ba estefade az serializer
        # mitonim be json tablin konim. dakhel file serializers baiad class e besazim ke che field haei tabdil be json beshan 
        # line paeein post ro ferstadim be class serializer va in class tebghe field haei ke behesh goftim
        # field haye post ro be json tabdil mikone
        serializer = PostSerializer(post)
        return Response(serializer.data)
    

    # request PUT baraye update kardan hast
    def put(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)

        serializer = PostSerializer(post, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)

        post.delete()
        return Response({'message':'itme removed successfully'}, status=status.HTTP_204_NO_CONTENT)
'''
    

'''
# dakhel RetrieveUpdateDestroyAPIView khodesh function haye get, put, patch, delete ro dare
class PostDetail(RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

'''





'''
# ba estefade az Viewsets mishe bejaye inke class haye joda baraye post-list va post-detail besazim ba yek class handle konim
# vali nemishe function list va retrieve be yek url vasl beshan chon retrieve niaz be ersal pk dare ama list nadare baraye hamin baiad be
# url haye motafavet vasl beshan ama function destroy(delete) baiad be url retrieve vasl she 
class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


    def list(self, request):
        serializer = PostSerializer(self.queryset, many=True)
        return Response(serializer.data)
    

    # manzor az retrieve(get), gerfatan yekdone object hast
    def retrieve(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = PostSerializer(post_object)
        return Response(serializer.data)
    
    def destroy(self, request, pk=None):

        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = PostSerializer(post_object) 
        post_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, pk=None):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = PostSerializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



    def partial_update(self, request, pk=None, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

'''




# class bala az ViewSet estefade shode bod ke az mixin haye GenericAPIView estefade nakarde bod baraye hamin majbor bodim tamome
# function hayesh ro khodemon tarif konim, ama ModelViewSet az mixin haye GenericAPIView ers bari karde
# va niazi be neveshtan function ha nist
class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    # ba ezafe kardan line haye paeein mitonim filter kardan va search va sort kardan ro ezafe konim 
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]


    # line paeein baraye filter ha vaghti 'exact' mizarim yani faghat yek filter mishe entekhab kard va vaghti kenaresh 'in' 
    # mizarim yani mishe 2 ta filter select kard   
    filterset_fields = {'category':['exact', 'in'], 'author':['exact'], 'status':['exact']}
    search_fields = ['title', 'content']
    ordering_fields = ['published_date']
    pagination_class = PostPagination

    
    # mishe dakhel file filters.py khodemon filter besazim. age bekhaim filter e besazim ke range gheymat ro filter kone mitonim
    # az code zir estefade konim
    '''
        from rest_framework import generics
        from django_filters import rest_framework as filters
        from myapp import Product


        class ProductFilter(filters.FilterSet):
            min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
            max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

            class Meta:
                model = Product
                fields = ['category', 'in_stock']


        class ProductList(generics.ListAPIView):
            queryset = Product.objects.all()
            serializer_class = ProductSerializer
            filter_backends = (filters.DjangoFilterBackend,)
            filterset_class = ProductFilter
    '''



    # code paeein extra action hast. methods age khali bashe default get hast.
    # age karbar pk az url nafreste detail=False age karbar pk befreste baiad True bashe 
    # esme function ham mishe esme url.
    @action(methods=['get'], detail=False)
    def get_ok(self, request):
        return Response({'detail':'ok'})
    



class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()