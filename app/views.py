from django.shortcuts import render
from app.forms import PedidoForm

def fazer_pedido(request):
    msg = ''
    formulario = PedidoForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        formulario = PedidoForm() # para apagar os inputs depois que apertei no submit
        msg = "Pedido realizado com sucesso"
    
    contexto = {
        'form' : formulario,
        'msg' : msg 
    }

    return render(request, 'main.html', contexto)