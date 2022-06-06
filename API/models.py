from pickle import TRUE
from django.db import models

# Create your models here.
class Book(models.Model):
    author=models.CharField(max_length=30)
    title=models.CharField(max_length=30)
    pub_date=models.DateField()
    ISBN_no=models.IntegerField()
    
    def __str__(self) -> str:
        return self.title

class User(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    employee_number = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=255)
    is_staff = models.BooleanField(null=False, blank=True)
    is_admin = models.BooleanField(null=False, blank=True)
    is_student = models.BooleanField(null=False, blank=True)
    books=models.ManyToManyField(Book,verbose_name="assigned books")
    
    def __str__(self) -> str:
        return self.first_name + " "+ self.last_name
    
    

    