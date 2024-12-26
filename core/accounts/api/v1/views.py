
from rest_framework import generics
from .serializers import RegistrationSerializer, AuthTokenSerializer, CustomTokenObtainPairSerializer, ChangePasswordSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from ...models import Profile
from django.shortcuts import get_object_or_404

User = get_user_model()


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
    

# class paeen hamon class TokenObtainPairView hast.
# man yek class jadid zadam ke class madaresh TokenObtainPairView hast
# va faghat bekhater in class ro zadam ke serializer_classesh ro taghir bedam
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer




class ChangePasswordApiView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [IsAuthenticated]

    # gerftan user e ke request dade
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        # user e ke request dade ro az def get_object bala migire va dakhel self.object mirize
        self.object = self.get_object()
        # data e ke az tarigh request omade ro be serializer mide ke baresi kone
        serializer = self.get_serializer(data=request.data)
        # if serializer.is_valid check mikone ke data ke omade ba ghavanini ke dar serializer tarif shode sazgar hast ya na
        if serializer.is_valid():
            # check old password 
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old_password': ['Wrong password.']}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            return Response({'details':'password changed successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                                              


# neshon dadan profile user
class ProfileApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj