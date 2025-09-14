from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from datetime import datetime

# Create your views here.

def root(request):
    return render(request, 'index.html')


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


def rozmowa(request: HttpRequest) -> HttpResponse:
    try:
        imie = request.GET['imie']
        powitanie = f'Witaj {imie}'
    except KeyError:
        powitanie = 'Hej, może się przestawisz?'

    return render(request, 'rozmowa.html', context={'message': powitanie})


def oblicz(arg1, arg2, operacja):
    match operacja:
        case '+': return arg1 + arg2
        case '-': return arg1 - arg2
        case '*': return arg1 * arg2
        case '/': return arg1 / arg2
        case '%': return arg1 % arg2
        case '^': return arg1 ** arg2
        case _: raise ValueError(f'Nieznana operacja {operacja}')

def kalkulator(request:HttpRequest) -> HttpResponse:
    wynik = 1313
    try:
        arg1 = int(request.GET['arg1'])
        arg2 = int(request.GET['arg2'])
        operacja = request.GET['operacja']
        wynik = oblicz(arg1, arg2, operacja)
    except Exception:
        pass
    return render(request, 'kalkulator.html',
                  context={'wynik': wynik})

dzialania = {
    'add': ('+', lambda x,y: x + y),
    'sub': ('-', lambda x,y: x - y),
    'mul': ('×', lambda x,y: x * y),
    'div': ('÷', lambda x,y: x // y),
    'mod': ('mod', lambda x,y: x % y),
    'pow': ('^', lambda x,y: x ** y),
}

def kalkulator_post(request: HttpRequest) -> HttpResponse:
    # W obiekcie request zapisane są wszelkie dane, który przyszły w zapytaniu,
    # w tym parametry zapytania. Aby wygodniej nam się z tego korzystało, do nagłówka funkcji dopisujemy type hints.

    # Ten słownik zawiera wszystkie informacje przekazane do szablonu.
    # W tej wersji buduję go stopniowo, w zależności od tego, co dzieje się w funkcji
    kontekst = {}

    # Jeśli zapytanie zawiera dane z formularza, to wyliczamy wynik.
    if 'operacja' in request.POST and 'liczba1' in request.POST and 'liczba2' in request.POST:
        try:
            liczba1 = int(request.POST['liczba1'])
            liczba2 = int(request.POST['liczba2'])
            op = request.POST['operacja']
            znak, funkcja = dzialania[op]
            kontekst['wynik'] = funkcja(liczba1, liczba2)
            kontekst['znak'] = znak
        except KeyError as e:
            kontekst['error'] = 'nieznane działanie'
        except Exception as e:
            kontekst['error'] = str(e)

    return render(request=request,
                  template_name='kalkulator_post.html',
                  context=kontekst)


def formularz(request):
    return render(request, 'formularz.html')

