from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .forms import ProductForm
from .models import Producto

# Create your views here.

def hello_world(request):
    producto = Producto.objects.order_by('id')
    template = loader.get_template('index.html')
    context = {
        'producto' : producto
    }

    return HttpResponse(template.render(context, request))

def product_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    template = loader.get_template('product_detail.html')
    context = {
        'producto' : producto
    }

    return HttpResponse(template.render(context, request))

def new_product(request):
    if request.method=='POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm()
    template = loader.get_template('new_product.html')
    context = {
        'form' : form
    }

    return HttpResponse(template.render(context, request))
