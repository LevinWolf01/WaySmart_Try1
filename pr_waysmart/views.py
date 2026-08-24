from django.shortcuts import render
from django.http import HttpResponse

def fn_inicio(request):
    return render(request, 'pr_waysmart/bienvenido.html')