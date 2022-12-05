from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hola mundo") # Create your views here.
