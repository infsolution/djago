from django.shortcuts import render, redirect
from perfil.models import *

def index(request):
    perfil = get_perfil_logado(request)
    return render(request, 'perfil/index.html',{'perfis':Perfil.objects.all(),'perfil_logado':perfil})

def exibir_perfil(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    return render(request, 'perfil/perfil.html', {'perfil_logado':perfil})

def convidar(request, perfil_id):
        perfil_a_convidar = Perfil.objects.get(id=perfil_id)
        perfil_logado = get_perfil_logado(request)
        perfil_logado.convidar(perfil_a_convidar)
        return redirect('index')

'''def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')'''

def get_perfil_logado(request):
        return Perfil.objects.get(id=1)
