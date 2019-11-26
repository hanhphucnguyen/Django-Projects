from django.shortcuts import render
from .models import image

# Create your views here.
def home(request):
    myimages = image.objects
    return render(request,'home.html', {'myimages' :  myimages})