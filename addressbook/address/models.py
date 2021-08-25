from django.db import models

class Contact(models.Model):
   firstName = models.CharField(max_length=500)
   lastName = models.CharField(max_length=500)
   phoneNumber = models.IntegerField(max_length=10)
   emailAddress = models.EmailField(max_length=500)
   streetAddress = models.CharField(max_length=150)
   
   def __str__(self):
      return self.firstName