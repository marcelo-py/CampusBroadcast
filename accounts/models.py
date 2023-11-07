from django.db import models
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O endereço de e-mail é obrigatório')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)  # O objeto é criado
        user.set_password(password)  # Isso garante que a senha seja armazenada de forma segura no banco de dados
        user.save(using=self._db)  #  Objeto é salvo no bd
        return user

    #  Metodo para superusuario
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    training = models.CharField(max_length=20, verbose_name='formação', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # Adicione is_superuser como um campo
    is_palestrante = models.BooleanField(default=False)

    #  Para evitar os conflitos

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Palestrante(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    training = models.CharField(max_length=20, verbose_name='formação')
    is_visitant = models.BooleanField(default=False)
    photo = models.ImageField('foto', upload_to='', blank=True, null=True)
    date_add = models.DateTimeField(default=timezone.now)


class Evento(models.Model):
    titulo = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    local = models.CharField(max_length=20)
    data_inicio = models.DateField(verbose_name='Data inicio do evento', blank=True, null=True)
    data_fim = models.DateField(verbose_name='da final do evento')
    organizadores =models.ManyToManyField(CustomUser, related_name='organizadores_evento')
    anunciado_por = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField('foto', upload_to='eventos', blank=True, null=True)

    is_fixed = models.BooleanField(default=False)
    data_post = models.DateTimeField(default=timezone.now)
    

class DatasParaEvento(models.Model):
    data = models.DateField(verbose_name='Dia para evento')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    atividades = models.ManyToManyField('Atividade', related_name='atividades_para_data')  # é preciso adicionar antes uma atividade

    data_adicionado = models.DateTimeField(default=timezone.now)


class Atividade(models.Model):
    nome = models.CharField(max_length=120)  # nome da atividade
    membros = models.ManyToManyField(CustomUser, related_name='membros_evento')  # O orgaizador precisa ter uma conta para ser adicionado 
    # Para evento
    palestrantes = models.ManyToManyField(Palestrante, related_name='atividade_palestrante')  # é preciso adicionar o palestrante antes 
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, blank=True, null=True)  # não se trata apenas de atividades para evento 

    horario_inicio = models.TimeField(blank=True, null=True)
    horario_fim = models.TimeField(blank=True, null=True)

    is_event = models.BooleanField(default=False)
    
    data_adicionado = models.DateTimeField(default=timezone.now)
