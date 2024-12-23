from rest_framework import serializers
from ...models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _



class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password1']
        

    # etebar sanji kardan form ersal shode tavasot user
    def validate(self, attrs):
        # check kardan inke aya password ba password1 barabar hast ya na
        if attrs.get('password') != attrs.get('password1'):
            raise serializers.ValidationError({'detail':'passwords doesnt match'})
        try:
            # validate_password dakhel khodesh be sorat pish farz yekseri ghavaedei dare ke amniat password ro check mikone 
            validate_password(attrs.get('password'))

        # age ghavaede amniati ro raaiat nakarde bashe varde except mishe
        # exceptions.ValidationError errore marbot be moshkel password ro barmigardone mesal:
        # This password is entirely numeric.
        # passwords doesnt match.
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'password':list(e.messages)})
        return super().validate(attrs)
    

    # age bala be moshkeli bar nakhore vard function create mishe
    def create(self, validated_data):
        # pop kardan yani delete kardan
        # dar line paeen bekhater inke field password1 dakhel model nadarim baiad on ro hazf konim
        # vagarna be error mikhorim chon def create nemidone field password1 ke karbar ersal karde ro bejaye kodom field model bezare
        validated_data.pop('password1', None)
        # line paeen az create_user estefade kardim bejaye create chon khodemon function create_user ro dakhel model sakhtim
        # va lazim nist ke az create ke default django hast estefade konim
        return User.objects.create_user(**validated_data)
    



# serializer paeen hamon serializer class ObtainAuthToken hast ke copy kardam va bejaye field username be email taghir dadam
class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
