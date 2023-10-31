from django.shortcuts import render, redirect

def landing_page(request):
    if request.user.is_authenticated:
        redirect('accounts:feed_index')

    return render(request, 'landingpage/index.html')
