from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse("Namaste " + name)
    return render(request, 'index.html')


# Create your views here.
