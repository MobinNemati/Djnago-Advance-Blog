from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from ...models import Post
from . serializers import PostSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


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
