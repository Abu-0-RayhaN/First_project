from django.shortcuts import render
from .models import contact
from django.contrib import messages


def contactus(request):
    if request.method == 'POST':
        contactdata=contact()
        contactdata.email=request.POST.get('email')
        contactdata.name=request.POST.get('name')
        contactdata.message=request.POST.get('message')
        contactdata.subject=request.POST.get('subject')
        contactdata.save()
        messages.success(request,'Your message has been sent!')
       

    return render(request, 'contact.html')

 #another way to add and save the message.
        #contactdata=contact()
        #contactdata.name=request.POST.get('name')
        #contactdata.email=request.POST.get('email')
        #contactdata.subject=request.POST.get('subject')
        #contactdata.message=request.POST.get('message')
        #contactdata.save()