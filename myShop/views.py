from django.shortcuts import render,get_object_or_404
from .models import Product, Category


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'myShop/product_list.html', {
        'products': products,
        'categories': categories
    })

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()

    return render(request, 'myShop/product_list.html', {
        'products': products,
        'categories': categories,
        'current_category': category
    })
