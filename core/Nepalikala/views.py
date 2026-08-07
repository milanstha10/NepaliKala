from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html") 

def shop(request):
    return render(request, "products/shop.html")

def collection(request):
    return render(request, "products/collection.html")

def about(request):
    return render(request, "about/about.html")
