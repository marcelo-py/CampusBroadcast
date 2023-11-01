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
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # Adicione is_superuser como um campo

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
    training = models.CharField(max_length=20)

    date_add = models.DateTimeField(default=timezone.now)


class Evento(models.Model):
    titulo = models.CharField(max_length=120)
    decription = models.TextField(blank=True, null=True)
    local = models.CharField(max_length=20)
    data_evento = models.DateTimeField(verbose_name='Dia e horário do evento')

    palestrantes = models.ManyToManyField(Palestrante, related_name='palestrantes_principais')
    anunciado_por = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    data_post = models.DateTimeField(default=timezone.now)