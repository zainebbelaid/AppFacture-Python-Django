from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
   
   path('factnp',factnp,name='factnp'),
   path('listfactnp',listfactnp,name='listfactnp'),
   path('add_facture',add_facture,name='add_facture'),
   path('listfactnp/sendemail',sendemail,name='sendemail'),
   path('delete_facture/<int:myid>/',delete_facture,name='delete_facture'),

   

   
] 