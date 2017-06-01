from django import forms

from .models import usuario,apps

class userModelForm(forms.ModelForm):
    class Meta:
        model=usuario
        fields=[
            "nombre",
            "progreso",
            "edad",
            "pcUser",
        ]
        labels={
            "nombre":"Cuale es tu nombre"
        }
        widgets={
            "nombre":forms.TextInput(attrs={'class':'input','placeholder':'Ingresa tu nombre...'}),
            "edad":forms.NumberInput(attrs={'class':'input','placeholder':'Ingresa tu edad...'}),
            "progreso":forms.TextInput(attrs={'class':'input','placeholder':'Ingresa tu progreso...'}),
            "pcUser":forms.TextInput(attrs={'class':'input','placeholder':'Ingresa nombre del pc...'}),
        }