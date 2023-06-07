from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def home(request):
    return render(request,'loginRegistration.html')
def about(request):
    products=Product.objects.all()
    return render(request,'about.html',{'products':products})
def contact(request):
    return render(request,'contact.html')