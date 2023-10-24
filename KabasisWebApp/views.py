from django.shortcuts import render, HttpResponse



# Create your views here.

def home(request):

    return render(request, "KabasisWebApp/home.html")



def tienda(request):

    return render(request, "KabasisWebApp/tienda.html")

def blog(request):

    return render(request, "KabasisWebApp/blog.html")

def contacto(request):

    return render(request, "KabasisWebApp/contacto.html")