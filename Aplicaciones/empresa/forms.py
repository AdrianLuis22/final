from django import forms
from .models import EmpresaTuristica, GuiaTuristico, ArchivoGuia

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = EmpresaTuristica
        fields = ['nombre', 'direccion', 'telefono', 'email']

class GuiaForm(forms.ModelForm):
    class Meta:
        model = GuiaTuristico
        fields = ['nombres', 'apellidos', 'cedula', 'telefono', 'email', 'empresa']

class ArchivoGuiaForm(forms.ModelForm):
    class Meta:
        model = ArchivoGuia
        fields = ['descripcion', 'foto', 'documento']
