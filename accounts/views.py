from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Evento

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
    return render(request, 'navigation/index.html', {'evento': obj_evetntos})
