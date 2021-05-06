from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 
                'categories': categories, 
                'products':products}
    return render(request, 'shop/product/list.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, avaiable=True)
    context = {'product': product}
    return render(request, 'shop/product/detail.html', context)
