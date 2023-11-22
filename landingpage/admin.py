from django.contrib import admin
from .models import Donate, Itens


class DonateAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_alimento')


admin.site.register(Donate, DonateAdmin)
admin.site.register(Itens, ItemAdmin)
