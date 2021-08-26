from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def index(request):
   contacts = Contact.objects.all()
   return render(request, 'index.html', {'contacts':contacts})

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

# get contact info based on id (pk)
def contactProfile(request, pk):
   contact = Contact.objects.get(id=pk)
   return render(request, 'contact-name.html', {'contact': contact})

def editContact(request, pk):
   contact = Contact.objects.get(id=pk)
   
   if request.method == 'POST':
      contact.firstName = request.POST['firstname']
      contact.lastName = request.POST['lastname']
      contact.phoneNumber = request.POST['phonenumber']
      contact.emailAddress = request.POST['emailaddress']
      contact.streetAddress = request.POST['streetaddress']
      contact.save()
      return redirect('/profile/'+str(contact.id))
   return render(request, 'edit-contact.html', {'contact': contact})

def deleteContact(request, pk):
   contact = Contact.objects.get(id=pk)
   if request.method == 'POST':
      contact.delete()
      return redirect('/')
   return render(request, 'delete-contact.html', {'contact': contact})