from django.shortcuts import render
from django.conf.urls.static import static
from django.conf import settings
from.models import about,slider,client
aboutdata = about.objects.all()[0]
sliderdata = slider.objects.all()
clientdata = client.objects.all()
contact={
        'about': aboutdata,
        'slider': sliderdata,
        'client': clientdata
    }
def home(request):
   
    return render(request,'index.html',contact)

def services(request):
    return render(request,'services.html')
def aboutus(request):
    return render(request,'about.html',contact)
def clients(request):
    return render(request,'clients.html')

