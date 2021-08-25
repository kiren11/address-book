from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def index(request):
   return render(request, 'index.html')

def addContact(request):
   if request.method == "POST":
      new_contact = Contact(
         firstName = request.POST['firstname'],
         lastName = request.POST['lastname'],
         phoneNumber = request.POST['phonenumber'],
         emailAddress = request.POST['emailaddress'],
         streetAddress = request.POST['streetaddress']
      )
      new_contact.save()
      return redirect('/')
   return render(request, 'new-contact.html')