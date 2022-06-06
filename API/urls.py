from django.urls import path

from API.views import BookDetailView,UserView,BooksList



urlpatterns = [
    path("books/",BooksList.as_view()),
    path("books/<int:pk>",BookDetailView.as_view()),
    path("users/",UserView.as_view()),  
]

    
    