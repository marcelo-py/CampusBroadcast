from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),


    # Para a navegação
    path('', views.feed_view, name='feed_index'),
]
