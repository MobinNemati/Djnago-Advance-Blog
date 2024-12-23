
from rest_framework import generics
from .serializers import RegistrationSerializer, AuthTokenSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated



# Register api class
class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer


    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # dar sorat dorost bodan form register, be user yek dictionary barmigardone ke email: email user
            data = {
                'email':serializer.validated_data['email']
            }
            # return kardan email user ba http response
            return Response(data, status=status.HTTP_201_CREATED)
        # age form eshtebah bashe error ba http response barmigardone
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



# ba class paeen mitonim custom konim ke baad login kardan ba url token/login/ chi bargardone be ma
class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
    

# delete kardan token
class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)