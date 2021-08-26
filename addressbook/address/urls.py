from django.urls import path, include
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
   url(r'^login/$', LoginView.as_view(), name='login'),
   url(r'^logout/$', LogoutView.as_view(), name='logout'),
   # path('register/', views.register, name='register'),    
   path('', views.index, name='index'),
   path('add-contact/', views.addContact, name='add-contact'),
   path('profile/<str:pk>', views.contactProfile, name='profile'),
   path('edit/<str:pk>', views.editContact, name='edit-contact'),
   path('delete/<str:pk>', views.deleteContact, name='delete')
]