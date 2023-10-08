from django.shortcuts import render
from django .http import HttpResponse


# Create your views here.

def kiraz(request):
    return HttpResponse('Iste calisiyor, baksana')
def erik(request):
    return render(request,'Erik.html', {})
def ayva(request):
    return render(request,'Ayva.html', {})
def ayva1(request):
    return render(request,'Ayva1.html', {})
def incir(request):
    return render(request,'incir.html', {})
def kavun(request):
    return render(request,'Kavun.html', {})
def home_page(request):
    return render(request,'Home_page.html', {})
def blog(request):
    return render(request,'Blog.html', {})
def kalori_calculator(request):
    return render(request,'Calori.html', {})
def about_us(request):
    return render(request,'About_us.html', {})
def contact_us(request):
    return render(request,'Contact_us.html', {})