from django.shortcuts import render
from utils.criptos.cripto_analise import analise
# Create your views here.
def home_page(requests):
    return render(request=requests,template_name='index.html')
def cripto_view(requests):
    cripto_name = requests.GET.get('cripto', '')
    if cripto_name:
        return render(request=requests,template_name='cripto.html',context={'coin':analise(cripto_name)})
    else:
        return render(request=requests,template_name='cripto.html',context={'ct':"Nenhum nome de cripto foi enviado."})
