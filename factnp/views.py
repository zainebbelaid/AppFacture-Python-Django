from django.contrib import messages
from django.shortcuts import render
from .models import *
from django.http.response import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from django.core.mail import send_mail
# Create your views here.
def factnp(request):
    
     facture_list = facture.objects.all()
     context ={
        'facture_list' : facture_list
     }
     return render(request,'factnp.html',context)


def listfactnp(request):   
    
    facture_list = facture.objects.all()
    context ={
        'facture_list' : facture_list
     } 
 
    if request.method == "POST":
        numfac = request.POST.getlist('boxes')
        print(numfac)
        messages.info(request,('Pour payer les frais du comsomation du factures numero' , numfac,'Entrez svp les information boncaires '))
    else:
        return redirect('/factnp')
    
    return render(request,'factnp.html',context)
    


def add_facture(request):
    if request.method == "POST":
        typefact = request.POST['typefact']
        fraiscoms = request.POST['fraiscoms']
        factur = facture(typefact = typefact,fraiscoms = fraiscoms)
        factur.save()
        messages.info(request,"ITEM ADDEDD SUCCESSDFULLY")
    else:
         pass
    facture_list = facture.objects.all()
    context ={
        'facture_list' : facture_list
    }
    return redirect('/listfactnp')

    
def sendemail(request):
    if request.method == "POST":
        ncarte =request.POST['ncarte']
        codesecurite =request.POST['codesecurite']
        dexpiration=request.POST['dexpiration']
        email=request.POST['email']
        
        
        send_mail(
            'message explicatif sur le paiement de facture',#subj
            'paiement des facture  est effectué avec succées, Ncarte:'+ ncarte,#msg
            'facturet7@gmail.com',#from email
            [email],#tomail
        )
        messages.info(request,"VERIFIER VOTRE BOITE MAIL")
        return redirect('/listfactnp')
    else:
        return redirect('/listfactnp')       



def delete_facture(request,myid):
    factur = facture.objects.get(id = myid)
    factur.delete()
    messages.info(request,"ITEM DELETE SUCCESSDFULLY")
    return redirect('/listfactnp')