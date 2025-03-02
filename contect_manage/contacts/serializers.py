from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User,Profile,contects
# from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token =super().get_token(user)

        token['name']=user.User.name
        token['email']=user.User.email
        token['address']=user.User.address
        token['number']=user.User.number
        token['verified']=user.User.verified
        return token


    

class RegisterForm(serializers.ModelSerializer):
        # extra_kwargs = {'password': {'write_only': True}}
    password=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2=serializers.CharField(write_only=True,required=True)

    class Meta:
        model=User
        fields=['email','username','password','password2']


    def validate(self,attrs):
        if attrs['password']!=attrs['password2']:
                raise serializers.ValidationError(
                    {"password":"Password fields does not match"}
                )
        return attrs
     
        
    def create(self,validated_data):
        user=User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],

        )
        user.set_password(validated_data['password'])
        user.save()

        return user


# serializers.py





class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contects
        fields = ['id', 'name', 'number', 'address']



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = contects
        fields = ['id','name','number','address','completed']
