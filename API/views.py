
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.shortcuts import get_object_or_404

from API.models import Book, User
from .serializers import Bookserializer, CreateBookSerializer,CreateUserProfile, Userserializer
from django.db import transaction
# from rest_framework.viewsets import GenericViewSet


# Create your views here.
class UserView(APIView):
    serializer_class=CreateUserProfile
    def get(self,request):
         user=User.objects.all()
         serializer=Userserializer(user,many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
     
    def post(self,request):
        serializer=CreateUserProfile(data=request.data)
        serializer.is_valid(raise_exception=True)
         # check if user is duplicate
        if User.objects.filter(
                registration_number=self.request.data.get('registration_number')
        ).exists():
            return Response({'details': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
        else:
           user= User.objects.create(
                first_name=serializer.data.get('first_name'),
                middle_names=serializer.data.get('middle_names'),
                last_name=serializer.data.get('last_name'),
                email=serializer.data.get('email'),
                phone_number=serializer.data.get('phone_number'),
                employee_number=serializer.data.get('employee_number'),
                registration_number=serializer.data.get('registration_number'),
            )
           user.save()
           response=Userserializer(user)
           return Response (response.data,status=status.HTTP_201_CREATED)    
    

class BookDetailView(APIView):
    serializer_class=CreateBookSerializer
    def get(self,request,pk):
         book=get_object_or_404(Book,pk=pk)
         serializer=Bookserializer(book)
         return Response(serializer.data,status=status.HTTP_200_OK)
    def delete(self,request,pk):
         book=get_object_or_404(Book,pk=pk)
         book.objects.delete()         
         return Response(book,status.HTTP_204_NO_CONTENT)
    def put(self,request,pk):
        book=get_object_or_404(Book,pk=pk)
        serializer=Bookserializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
             
        
         
    
class BooksList(APIView):
     serializer_class=CreateBookSerializer
     def post(self,request):
         serializer=CreateBookSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         if Book.objects.filter(ISBN_no=serializer.data.get("ISBN_no")).exists():
             return Response (f"book with isbn no {serializer.data.get('ISBN_no')} already exist")
        
         with transaction.atomic():
            book=Book.objects.create(
                title=serializer.data.get('title'),
                author=serializer.data.get('author'),
                pub_date=serializer.data.get('pub_date'),
                ISBN_no=serializer.data.get('ISBN_no'),
            )
            book.save()
            response=Bookserializer(book)
            return Response (response.data,status=status.HTTP_201_CREATED)
            
             
     def get(self,request):
         books=Book.objects.all()
         serializer=Bookserializer(books,many=True)
         return Response(serializer.data,status=status.HTTP_200_OK)
     