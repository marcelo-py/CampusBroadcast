from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Evento, DatasParaEvento, Atividade, AtividadeAlunos
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
import json


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('landingpage:landing_page')  # Redireciona para a página inicial
        
    else:
        form = RegistrationForm()
        
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        login(request, user)
        return redirect('accounts:feed_index')
    

def logout_view(request):
    logout(request)

    return redirect('landingpage:landing_page')

#  para a navegação Logado
def feed_view(request):
    obj_evetntos = Evento.objects.filter(is_fixed=True).first()
    date_events_objects = DatasParaEvento.objects.filter(evento=obj_evetntos).order_by('data')

    get_req_obj_id = request.GET.get('data_atividades_id', None)
    print('>>>>>>>>>>>>>>>>>>>',get_req_obj_id)


    if get_req_obj_id:
        date_get = DatasParaEvento.objects.get(id=get_req_obj_id)
        date_atividades = Atividade.objects.filter(data_rel=date_get).order_by('horario_inicio')
        list_atividades_dates = [
                    {
                        'nome': date.nome,
                        'descricao': date.description,
                        'palestrantes': [f"{palestrante.first_name} {palestrante.last_name}" for palestrante in date.palestrantes.all()],
                        'hora_inicio': date.horario_inicio.strftime('%H'),
                        'hora_fim': date.horario_fim.strftime('%H'),
                        'local': date.local
                } for date in date_atividades
            ]

        
        resposta = {'list_atividades': list_atividades_dates}
        return JsonResponse(resposta)

    date_atividades = Atividade.objects.filter(data_rel=date_events_objects.first())
    atividade_alunos = AtividadeAlunos.objects.all()
    return render(request, 'navigation/index.html', {
                                                        'evento': obj_evetntos,
                                                        'days_events': date_events_objects,
                                                        'atividades_first_day': date_atividades,
                                                        'atividades_alunos': atividade_alunos 
                                                    })


def curtir(request):
    if request.method == "PUT":
        user_request = request.user
        data_dict = json.loads(request.body)
        objct_id = data_dict.get('pub_id')
        pub_objct = get_object_or_404(AtividadeAlunos, pk=objct_id)
        
        if user_request not in pub_objct.curtidas.all():
            pub_objct.curtidas.add(user_request)
        else:
            pub_objct.curtidas.remove(user_request)

        return JsonResponse({'mensagem': 'curtido com sucesso'}, status=200)
    
    return HttpResponse('Esse metodo aqui não!', status=405)


def interesse(request):
    if request.method == "PUT":
        user_request = request.user
        data_dict = json.loads(request.body)
        objct_id = data_dict.get('pub_id')
        pub_objct = get_object_or_404(AtividadeAlunos, pk=objct_id)
        
        if user_request not in pub_objct.interests.all():
            pub_objct.interests.add(user_request)
        else:
            pub_objct.interests.remove(user_request)

        return JsonResponse({'mensagem': 'Interessado com sucesso!'}, status=200)
    
    return HttpResponse('Esse metodo aqui não!', status=405)


def create_publication(request):
    if request.method == "POST":
        type_publication = request.POST.get('type_publication')
        if type_publication == 'search':
            AtividadeAlunos.objects.create(
                titulo=None,
                descricao=None,
                link=None,
                data_expira=None,
            )

        elif type_publication == 'presentation':
            AtividadeAlunos.objects.create(
                titulo=None,
                descricao=None,
                data_apresentacao=None,
                local=None
            )

        elif type_publication == 'project':
            AtividadeAlunos.objects.create(
                titulo=None,
                descricao=None,
                nome_projeto=None,
                project_options=None
            )

        else:
            return JsonResponse({'mensagem': 'Algo invalido'}, status=502)
        
        return JsonResponse({'mensagem': 'Publicado com sucesso!'}, status=200)
    
    return JsonResponse({'mensagem': 'Publicado com sucesso!'}, status=200)

