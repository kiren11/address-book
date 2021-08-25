from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def index(request):
   return render(request, 'index.html')

def addContact(request):
   if request.method == "POST":
      new_contact = Contact(
         first_name = request.POST['firstname'],
         last_name = request.POST['lastname'],
         phoen_number = request.POST['phonenumber'],
         email_address = request.POST['emailaddress'],
         street_address = request.POST['streetaddress']
      )
      new_contact.save()
      return redirect('/')
   return render(request, 'new-contact.html')