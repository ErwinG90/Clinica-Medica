from django import forms

class PacienteForm(forms.Form):
    rut = forms.IntegerField(required=True)
    nombre = forms.CharField(max_length=300, required=True)
    apellido = forms.CharField(max_length=300, required=True)
    usuario = forms.CharField(max_length=300, required=True)
    email = forms.EmailField(max_length=300, required=True)
    contraseña = forms.CharField(max_length=300, widget=forms.PasswordInput, required=True)
    direccion = forms.CharField(max_length=300, required=True)
    telefono = forms.IntegerField(required=True)

class MedicoForm(forms.Form):
    rut = forms.IntegerField(required=True)

    
    sucursal_id = forms.ChoiceField(
        choices=(
            (1, 'San Maria'),
            (2, 'Salvacion'),
            (3, 'Ultimo Respiro'),
        ),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    especialidad_id = forms.ChoiceField(
        choices=(
            (1, 'Odontología'),
            (2, 'Cardiología'),
            (3, 'Anestesiología'),
        ),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    nombre = forms.CharField(max_length=300, required=True)
    apellido = forms.CharField(max_length=300, required=True)
    usuario = forms.CharField(max_length=300, required=True)
    email = forms.EmailField(max_length=300, required=True)
    contraseña = forms.CharField(max_length=300, widget=forms.PasswordInput, required=True)



class LoginPacienteForm(forms.Form):
    email = forms.EmailField(max_length=300, required=True)
    contraseña = forms.CharField(max_length=300, widget=forms.PasswordInput, required=True)