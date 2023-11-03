from django.shortcuts import render, redirect
from accounts.models import Palestrante


def landing_page(request):
    if request.user.is_authenticated:
        return redirect('accounts:feed_index')

    objects_palestrantes = Palestrante.objects.all()
    return render(request, 'landingpage/index.html', {'palestrantes': objects_palestrantes})
