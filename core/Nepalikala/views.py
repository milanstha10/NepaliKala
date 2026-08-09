from django.shortcuts import render, get_object_or_404
from .models import Product, HeroBanner


def home(request):
    hero = HeroBanner.objects.filter(
        is_active=True
    ).order_by("-created_at").first()

    context = {
        "hero": hero,
    }

    return render(
        request,
        "index.html",
        context
    )


def contact(request):
    return render(
        request,
        "contact/contact.html"
    )


def shop(request):
    products = Product.objects.filter(
        stock=True
    )

    context = {
        "products": products,
    }

    return render(
        request,
        "products/shop.html",
        context
    )


def collection(request):
    products = Product.objects.all()

    context = {
        "products": products,
    }

    return render(
        request,
        "products/collection.html",
        context
    )


def about(request):
    return render(
        request,
        "about/about.html"
    )


def product_detail(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id
    )

    context = {
        "product": product,
    }

    return render(
        request,
        "products/detail.html",
        context
    )