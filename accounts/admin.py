from django.contrib import admin
from .models import CustomUser, Palestrante, Evento


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')


class PalestranteAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name',)


class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', )


admin.site.register(CustomUser, UserAdmin)

admin.site.register(Palestrante, PalestranteAdmin)
admin.site.register(Evento, EventoAdmin)
