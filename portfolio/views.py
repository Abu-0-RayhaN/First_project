from django.shortcuts import render
from.models import portfolio
def authportfolio(request):
    port=portfolio.objects.all()
    cin={
        portfolio:port,
    }

    return render(request,'portfolio.html',cin)
