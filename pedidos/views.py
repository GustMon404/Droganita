from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import connection

from .forms import LoginForms, PedidosForm
from .models import *


def home(request):
    if request.user.is_authenticated:
        if Diretor.objects.filter(user=request.user):
            return render(request, 'pedidos/gerar_relatorio.html')
        else:
            form_pedido = PedidosForm()
            if request.method == 'GET':
                return render(request, 'pedidos/pedido.html', {'form_pedido': form_pedido})

            elif request.method == 'POST':
                pedido = Pedido()
                funcionario = Funcionario.objects.get(user=request.user)

                pedido.produto = request.POST['produto']
                pedido.descricao = request.POST['descricao']
                pedido.marca = request.POST['marca']
                pedido.tipo = request.POST['tipo']

                pedido.encomenda = request.POST.get('encomenda', False)
                pedido.falta = request.POST.get('falta', False)

                pedido.funcionario = funcionario
                pedido.save()
                messages.info(request, 'Solicitacao de pedido feita com sucesso!')
                return redirect(reverse('home'))


def login_user(request):
    form_login = LoginForms()
    if request.method == "GET":
        return render(request, 'pedidos/login.html', {'form_login': form_login})
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        else:
            messages.info(request, 'Usuário não autorizado')
            return redirect('login')


def logout_user(request):
    logout(request)
    return redirect(reverse('login'))


# usar regex
def teste(request):
    tipos = {
        'etico': "'ET'",
        'generico': "'GN'",
        'similar': "'SM'",
        'perfumaria': "'PF'",
        'todos_med': "'ET','GN','SM'",
        'gensim': "'GN','SM'",
        'todos':"'ET','GN','SM','PF'"
    }
    tipo = tipos.get(request.GET.get('tipo'))

    falta = "falta='false'"
    encomenda = "encomenda=false"

    if request.GET.get('falta'):
        falta = "falta=true"
    if request.GET.get('encomenda'):
        encomenda = "encomenda=true"

    consulta = "select * from pedidos_pedido where tipo in ({}) and {} and {}".format(tipo, falta, encomenda)

    cursor = connection.cursor()
    cursor.execute(consulta)
    return HttpResponse(cursor.fetchall())
# Create your views here.
