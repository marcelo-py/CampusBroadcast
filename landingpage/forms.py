from django import forms
from .models import Donate

class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = ['nome', 'email', 'telefone', 'local', 'itens']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona classes CSS ou outros atributos, se necessário
        self.fields['itens'].widget.attrs.update({'class': 'seletor-itens-multiplo', 'multiple': 'multiple'})