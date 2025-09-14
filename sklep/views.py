from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def lista_produktow(request: HttpRequest) -> HttpResponse:
    produkty = Product.objects.all()
    return HttpResponse(str(produkty), content_type='text/plain')


def lista_produktow_txt(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()
    wynik = 'Produkty naszego sklepu:'
    for product in products:
        wynik += f'\n - {product.name} za {product.price} zł'
        if product.valid_to is not None:
            wynik += f', termin ważności: {product.valid_to}'
    return HttpResponse(wynik, content_type='text/plain;charset=utf-8')


def lista_produktow_html(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()
    return render(request, 'towary.html', context={'products': products})
