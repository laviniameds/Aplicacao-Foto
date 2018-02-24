from django.shortcuts import render

def inserirDados(request):
    return render(request, "paginas/inserir_dados.html")
