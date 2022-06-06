from rest_framework import serializers

from API.models import Book, User

       

class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"
        
class CreateBookSerializer(serializers.Serializer):
    title=serializers.CharField()
    author=serializers.CharField()
    pub_date=serializers.DateField()
    ISBN_no=serializers.IntegerField()


class CreateUserProfile(serializers.Serializer):
    first_name = serializers.CharField()
    middle_names = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    phone_number = serializers.CharField()
    employee_number = serializers.CharField()
    registration_number = serializers.CharField()
    


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

    
    