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

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


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
    
    def __str__(self):
        return self.titulo
    

class DatasParaEvento(models.Model):
    data = models.DateField(verbose_name='Dia para evento')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    atividades = models.ManyToManyField('Atividade', related_name='atividades_para_data')  # é preciso adicionar antes uma atividade

    data_adicionado = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.data}"

class Atividade(models.Model):
    nome = models.CharField(max_length=120)  # nome da atividade
    description = models.TextField(max_length=125, blank=True, null=True)
    membros = models.ManyToManyField(CustomUser, related_name='membros_evento')  # O orgaizador precisa ter uma conta para ser adicionado 
    # Para evento
    palestrantes = models.ManyToManyField(Palestrante, related_name='atividade_palestrante')  # é preciso adicionar o palestrante antes 
    local = models.CharField(max_length=20, null=True, blank=True)
    data_rel = models.ForeignKey(DatasParaEvento, on_delete=models.CASCADE,
                                 blank=True, null=True, verbose_name='Data da atividade')  # é preciso tem uma data criada
    horario_inicio = models.TimeField(blank=True, null=True)
    horario_fim = models.TimeField(blank=True, null=True)

    is_event = models.BooleanField(default=False)
    
    data_adicionado = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.nome
    

class AtividadeAlunos(models.Model):
    titulo = models.CharField(max_length=110)
    descricao = models.TextField()
    local = models.CharField(max_length=25, null=True, blank=True)
    membros = models.ManyToManyField(CustomUser, related_name='membros_atividades', blank=True)
    data_expira = models.DateField()
    data_apresentacao = models.DateTimeField(null=True, blank=True)
    link = models.URLField(max_length=210, null=True, blank=True)

    add_for = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    data_adicionado = models.DateTimeField(default=timezone.now)

    TYPE_PUBLICATION_OPTIONS = (
        ('search', 'pesquisa'),
        ('presentation', 'apresentação'),
        ('project', 'projeto')
    )
    PROJECT_OPTIONS = (
        ('init', 'inicio'),
        ('end', 'fim')
    )
    type_publication = models.CharField(max_length=13, choices=TYPE_PUBLICATION_OPTIONS, null=True, blank=True)
    project_options = models.CharField(max_length=7, choices=PROJECT_OPTIONS, null=True, blank=True)

    curtidas = models.ManyToManyField(CustomUser, related_name='cutidas_atividades', blank=True)
    interests = models.ManyToManyField(CustomUser, related_name='interesses_atividades', blank=True)

    def __str__(self):
        return self.titulo
    

class Comentario(models.Model):
    comentario = models.TextField()
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    atividade = models.ForeignKey(AtividadeAlunos, on_delete=models.CASCADE)

    def __str__(self):
        return self.comentario