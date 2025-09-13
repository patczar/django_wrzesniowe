from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def say_hello(request):
    return HttpResponse('Hello Django')


# bieżący czas można odczytać pisząc datetime.now() (potrzebny import)
# zadanko: dodaj tutaj funkcję, która odczytuje bieżący czas
# i spraw, żeby była dostępna pod adresem /czas
def ktora_godzina(request):
    return HttpResponse(datetime.now())

def czas_html(request):
    godzina = datetime.now().strftime('%H:%M:%S')
    html = f'''<html><head>
    <title>Która godzina</title>
    </head>
    <body style="background-color: #FFFFDD">
    <p>Teraz jest późna godzina <strong style="color:purple">{godzina}</strong></p>
    </body>
    </html>
    '''
    return HttpResponse(html, content_type='text/html;charset=UTF-8')

def czas_szablon(request):
    data_czas = datetime.now()
    data = data_czas.strftime('%Y-%m-%d')
    czas = data_czas.strftime('%H:%M:%S')
    fmt = data_czas.strftime('%d.%m.%Y %H:%M')

    return render(request, 'wyswietl_czas.html',
                  context={'dt': data_czas,
                           'data': data,
                           'czas': czas,
                           'fmt': fmt,
                           })
