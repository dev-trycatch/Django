from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import CategoryForm, ProductForm

def category_list(request):
    categories = Category.objects.all()
    form = CategoryForm()
    

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')

    return render(request, 'category_list.html', {
        'categories': categories,
        'form': form
    })


def category_update(request, id):
    category = Category.objects.get(id=id)
    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')

    return render(request, 'category_update.html', {'form': form})


def category_delete(request, id):
    Category.objects.get(id=id).delete()
    return redirect('category_list')



# Product crud

def product_list(request):
    products = Product.objects.all()
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    return render(request, 'product_list.html', {
        'products': products,
        'form': form
    })

def product_update(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')

    return render(request, 'product_update.html', {'form': form})


def product_delete(request, id):
    Product.objects.get(id=id).delete()
    return redirect('product_list')
