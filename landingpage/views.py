from django.shortcuts import render, redirect
from accounts.models import Palestrante
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import DonateForm
from .models import Donate
from django.core.serializers import serialize


def landing_page(request):
    if request.user.is_authenticated:
        return redirect('accounts:feed_index')

    objects_palestrantes = Palestrante.objects.all()
    return render(request, 'landingpage/index.html', {'palestrantes': objects_palestrantes})


@csrf_exempt
def donate_view(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        local = request.POST.get('local')
        itens = request.POST.get('itens')


        form = DonateForm(request.POST)
        if form.is_valid():
            donate_instance = form.save()
            return JsonResponse({'status': 'success', 'id': donate_instance.id})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    donate_objects = Donate.objects.all()

    data_list = []
    for donate_object in donate_objects:
        # Acesse os campos do objeto 'Donate' e adicione-os à lista de dados
        data_list.append({
            'nome': donate_object.nome,
            'email': donate_object.email,
            'telefone': donate_object.telefone,
            'local': donate_object.local,
            'itens': [item.nome_alimento for item in donate_object.itens.all()],
            'data': donate_object.data.strftime('%Y-%m-%d'),  # Formate a data conforme necessário
        })

    # Crie um JSON manualmente
    data_json = {'data': data_list}

    return JsonResponse(data_json, safe=False)
