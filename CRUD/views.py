from django.shortcuts import render, redirect
from .models import ProductList
from .forms import ProductListForm

def create_product(request):
    if request.method == 'POST':
        form = ProductListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductListForm()
    return render(request, 'addProduct.html', {'form': form, 'action': 'add'})

def product_list(request):
    products = ProductList.objects.all()
    return render(request, 'productList.html', {'products': products})

def update_product(request, pk):
    product = ProductList.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductListForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductListForm(instance=product)
    return render(request, 'addProduct.html', {'form': form, 'product': product, 'action': 'update'})

def delete_product(request, pk):
    try:
        product = ProductList.objects.get(pk=pk)
        product.delete()
        return redirect('product_list')
    except ProductList.DoesNotExist:
        return redirect('product_list')