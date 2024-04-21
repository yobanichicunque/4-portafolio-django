from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("<h1>Mi portafolio personal</h1><h3>Pagina principal</h3>")


def about(request):
    return HttpResponse("<h1>Mi portafolio personal</h1><h3>Acerca de...</h3><p>Soy Yobani Chicunque y soy programador</p>")


def portfolio(request):
    return HttpResponse("<h1>Mi portafolio personal</h1><h3>Binevenido a mi portafolio...</h3><p>Este es mi portafolio</p>")


def contact(request):
    return HttpResponse("<h1>Mi portafolio personal</h1><h3>Contacto</h3><p>Este es mi contacto</p>")
