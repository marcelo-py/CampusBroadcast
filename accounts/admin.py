from django.contrib import admin
from .models import CustomUser, Palestrante, Evento, DatasParaEvento, Atividade, AtividadeAlunos, Comentario


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


class PalestranteAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name',)


class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', )


class DatasParaEventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'data', )


class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', )


class AtividadeAlunosAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', )


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'comentario', )


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Palestrante, PalestranteAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(DatasParaEvento, DatasParaEventoAdmin)
admin.site.register(Atividade, AtividadeAdmin)
admin.site.register(AtividadeAlunos, AtividadeAlunosAdmin)
admin.site.register(Comentario, ComentarioAdmin)
