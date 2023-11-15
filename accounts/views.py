from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Evento, DatasParaEvento, Atividade, AtividadeAlunos
from django.http import JsonResponse

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
