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
    sucursal = forms.ChoiceField(
        choices=(
            (1, 'Sucursal 1'),
            (1, 'Sucursal 2'),
            (1, 'Sucursal 3'),
        ),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    especialidad = forms.ChoiceField(
        choices=(
            (1, 'Odontología'),
            (2, 'Pediatría'),
            (3, 'Cirugía'),
        ),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    nombre = forms.CharField(max_length=300, required=True)
    apellido = forms.CharField(max_length=300, required=True)
    usuario = forms.CharField(max_length=300, required=True)
    email = forms.EmailField(max_length=300, required=True)
    contraseña = forms.CharField(max_length=300, widget=forms.PasswordInput, required=True)