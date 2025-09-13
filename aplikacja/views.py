from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def say_hello(request):
    return HttpResponse('Hello Django')


# bieżący czas można odczytać pisząc datetime.now() (potrzebny import)
# zadanko: dodaj tutaj funkcję, która odczytuje bieżący czas
# i spraw, żeby była dostępna pod adresem /czas
def ktora_godzina(request):
    return HttpResponse(datetime.now())

