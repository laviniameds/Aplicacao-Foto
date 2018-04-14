from django.shortcuts import render

def inserirDados(request):
    return render(request, "paginas/view_inserir_dados.html")

def consumoEnergia(request):
    data = {}
    valores = {}
    if request.method == 'POST':
        data['consumo_ponta_qtd'] = request.POST.get('consumo_ponta_qtd', 'consumo_ponta_qtd not found')
        data['consumo_ponta_valor'] = request.POST.get('consumo_ponta_valor', 'consumo_ponta_valor not found')
        data['consumo_fora_qtd'] = request.POST.get('consumo_fora_qtd', 'consumo_fora_qtd not found')
        data['consumo_fora_valor'] = request.POST.get('consumo_fora_valor', 'consumo_fora_valor not found')
        data['consumo_fora_preco'] = request.POST.get('consumo_fora_preco', 'consumo_fora_preco not found')
        data['tarifa'] = request.POST.get('tarifa', 'tarifa not found')
        data['injetado_fv'] = request.POST.get('injetado_fv', 'injetado_fv not found')
        data['importe'] = request.POST.get('importe', 'importe not found')
        data['tributo_federal'] = request.POST.get('tributo_federal', 'tributo_federal not found')       
        data['valor_fatura'] = request.POST.get('valor_fatura', 'valor_fatura not found')
    
    """ FORMULAS DE CADA CAMPO8:

    GERACAO_DA_USINA = SUNNY PORTAL

    TABELA DE CONSUMO DE ENERGIA ATIVA

    valores['cosern'] = int(data['consumo_ponta_qtd']) + int(data['consumo_fora_qtd'])
    valores['injetado_fv'] = int(data['injetado_fv'])
    valores['consumido_fv'] = (GERACAO_DA_USINA * int(data['tarifa']) / int(data['tarifa'])
    valores['total_EA'] = valores['cosern'] + valores['consumido_fv'] + valores['injetado_fv']

    TABELA DE DESPESA DE ENERGIA ATIVA

    valores['tarifa'] = int(data['tarifa'])
    valores['com_fv'] = int(data['consumo_ponta_valor']) + int(data['consumo_fora_valor']) + int(data['importe'])
    valores['sem_fv'] = (int(data['consumo_ponta_valor']) + int(data['consumo_fora_valor']) + int(data['injetado_fv']) +
                        valores['consumido_fv']) * int(data['consumo_fora_preco'])  
    valores['valor_bruto'] = int(data['valor_fatura']) - int(data['tributo_federal'])
    valores['economia'] = valores['sem_fv'] - valores['sem_fv']

    TABELA DA USINA FOTOVOLTAICA

    valores['geracao'] = GERACAO_DA_USINA
    valores['total_UF'] = GERACAO_DA_USINA * int(data['tarifa']
    valores['injetado_UF'] = int(data['tarifa'] * valores['injetado_fv']
    valores['consumido_UF'] = valores['total_UF'] - GERACAO_DA_USINA
    
    """

    return render(request, "paginas/view_tabelas.html", valores)
