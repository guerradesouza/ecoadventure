
from django import forms 
from .models import InscricaoForm
'''

class InscricaoForm(forms.Form):
    nomeCompleto = forms.CharField(label='Nome Completo', max_length=100)
    rg = forms.CharField(label='RG', max_length=100)
    cpf = forms.CharField(label='CPF')
    dataDeNascimento = forms.DateField(label='Data de Nascimento')
    localOndeTrabalha = forms.CharField(label='Local onde Trabalha', max_length=100)
    profissao = forms.CharField(label='Profissão', max_length=100)
    email = forms.CharField(label='Email', max_length=100)
    telefone = forms.CharField(label='Telefone', max_length=20)
    whatsapp = forms.CharField(label='Whatsapp', max_length=20)
    facebook = forms.CharField(label='Facebook', max_length=100)
    instagram = forms.CharField(label='Instagram', max_length=100)
    cidadeDoCurso = forms.CharField(label='Cidade do Curso', max_length=100)
    endereco = forms.CharField(label='Endereço', max_length=200)
    cursoAph = forms.CheckboxInput()
    cursoSbv = forms.CheckboxInput()
    obs = forms.CharField(label='Observação', widget=forms.Textarea())
'''
   
class InscricaoForm(forms.ModelForm):
    class Meta:
        model = InscricaoForm
        fields = "__all__"







    
