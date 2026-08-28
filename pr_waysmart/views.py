from django.shortcuts import render

def fn_inicio(request):
    return render(request, 'bienvenido.html')  # 👈 sin "pr_waysmart/"
