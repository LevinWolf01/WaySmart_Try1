from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TipoDePago, PagosEntrega

def pagos_index(request):
    if request.method == 'POST':
        # Guardar 1: Registrar Tipo de Pago
        if 'btn_tipo_pago' in request.POST:
            efectivo = request.POST.get('efectivo') or None
            transferencia = request.POST.get('transferencia') or None

            TipoDePago.objects.create(
                efectivo=efectivo,
                transferencia=transferencia
            )
            return redirect('pagos_index')

        # Guardar 2: Registrar Pago de Entrega
        elif 'btn_pago_entrega' in request.POST:
            id_tipo = request.POST.get('tipo_de_pago')
            valor_total = request.POST.get('valor_total')
            metodo_pago = request.POST.get('metodo_pago')
            evidencia_url = request.POST.get('evidencia_url')
            fecha_de_pago = request.POST.get('fecha_de_pago')
            estado = request.POST.get('estado')

            tipo_instancia = TipoDePago.objects.get(pk=id_tipo)

            PagosEntrega.objects.create(
                tipo_de_pago=tipo_instancia,
                valor_total=valor_total,
                metodo_pago=metodo_pago,
                evidencia_url=evidencia_url,
                fecha_de_pago=fecha_de_pago,
                estado=estado
            )
            return redirect('pagos_index')

    # Consulta para llenar los select e interfaces
    tipos_pago = TipoDePago.objects.all()
    pagos = PagosEntrega.objects.all()

    return render(request, 'app_PagosEntrega_TipoPago/pagos_index.html', {
        'tipos_pago': tipos_pago,
        'pagos': pagos,
    })