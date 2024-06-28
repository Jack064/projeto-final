from django.shortcuts import render, redirect
from .models import Servico

# Create your views here.
def mysite(request):    
    servicos = Servico.objects.all()
    return render(request, "index.html", {"servicos":servicos})

def cadastro(request):
    return render(request, "cadastro.html")

def logout(request):
    return render(request, "logout.html")

def salvar(request):
    vcodigo = request.POST.get("codigo")
    vdescricao = request.POST.get("descricao")
    vdata = request.POST.get("data")
    vsolicitante = request.POST.get("solicitante")
    vcontato = request.POST.get("contato")
    Servico.objects.create(codigo = vcodigo, descricao = vdescricao, data = vdata, solicitante = vsolicitante, contato = vcontato)
    return redirect(mysite)
    
def editar(request, id):
    servico = Servico.objects.get(id = id)
    return render(request,"update.html",{"servico":servico})

def update(request, id):
    vcodigo = request.POST.get("codigo")
    vdescricao = request.POST.get("descricao")
    vdata = request.POST.get("data")
    vsolicitante = request.POST.get("solicitante")
    vcontato = request.POST.get("contato")
    servico = Servico.objects.get(id = id)
    servico.codigo = vcodigo
    servico.descricao = vdescricao
    servico.data = vdata
    servico.solicitante = vsolicitante
    servico.contato = vcontato
    servico.save()
    return redirect(mysite)

def apagar(request, id):
    servico = Servico.objects.get(id = id)
    servico.delete()
    return redirect(mysite)

