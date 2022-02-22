from django.shortcuts import render

from django.views.generic import ListView

# Create your views here.

# class ModelListView(ListView):
#     model = Model
#     template_name = ".html"

def index(request):
    pass
    return render(request, 'index.html')    


def Checkout(request):
    pass
    return render(request, 'Checkout.html')
    

def Product(request):
    pass
    return render(request, 'Product.html')
        