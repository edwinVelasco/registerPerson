from django import forms
from app.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['identification', 'celphone', 'phone', 'name', 'last_name',
                  'leader', 'birthdate', 'rh', 'neighborhood', 'addres',
                  'state', 'date_meeting']

        widgets = {
            'identification': forms.TextInput(),
            'celphone': forms.TextInput(),
            'phone': forms.TextInput(),
            'name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'rh': forms.TextInput(),
            'addres': forms.TextInput(),
            'state': forms.CheckboxInput(),
            'leader': forms.Select(),
            'neighborhood': forms.Select()
        }

        error_messages = {
            'unique_together': 'Persona registrada anteriormente',
            'name': {
                'required': 'Nombre requerido'
            },
            'last_name': {
                'required': 'Apellidos requerido'
            },
            'celphone': {
                'required': 'Número telefonico requerido'
            },
            'leader': {
                'required': 'El lider es requerido'
            }
        }

