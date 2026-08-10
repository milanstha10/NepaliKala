from django.shortcuts import get_object_or_404, render
from .models import HeroBanner, Product

def home(request):
    hero = HeroBanner.objects.filter(is_active=True).order_by("-created_at").first()
    return render(request, "index.html", {"hero": hero})

def contact(request):
    return render(request, "contact/contact.html")

def shop(request):
    products = Product.objects.filter(stock=True)
    return render(request, "products/shop.html", {"products": products})

def collection(request):
    products = Product.objects.all()
    return render(request, "products/collection.html", {"products": products})

def about(request):
    return render(request, "about/about.html")

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "products/detail.html", {"product": product})

