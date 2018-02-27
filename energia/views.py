from django.shortcuts import render

def inserirDados(request):
    return render(request, "paginas/inserir_dados.html")

def consumoEnergia(request):
    data = {}
    if request.method == 'POST':
        data['consumo_ponta_qtd'] = request.POST.get('consumo_ponta_qtd', 'consumo_ponta_qtd not found')
        data['consumo_ponta_valor'] = request.POST.get('consumo_ponta_valor', 'consumo_ponta_valor not found')
        data['consumo_fora_qtd'] = request.POST.get('consumo_fora_qtd', 'consumo_fora_qtd not found')
        data['consumo_fora_valor'] = request.POST.get('consumo_fora_valor', 'consumo_fora_valor not found')
        data['tarifa'] = request.POST.get('tarifa', 'tarifa not found')
        data['importe'] = request.POST.get('importe', 'importe not found')
        data['valor_fatura'] = request.POST.get('valor_fatura', 'valor_fatura not found')
    
    return render(request, "paginas/consumo_energia.html", data)

def despesaEnergia(request):
    return render(request, "paginas/despesa_energia.html")

def usina_fotovoltaica(request):
    return render(request, "paginas/usina_fotovoltaica.html")
