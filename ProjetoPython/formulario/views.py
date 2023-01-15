from django.shortcuts import render
from django.http import HttpResponse

def ver_formulario(request):
    return render(request, 'ver_formulario.html')

def ver_formulario2(request):
    return render(request, 'ver_formulario2.html')

