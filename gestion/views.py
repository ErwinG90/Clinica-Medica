from django.shortcuts import render,redirect
from .forms import *
import requests
from django.http import HttpResponse
from requests.exceptions import RequestException

# Create your views here.

def mi_vista(request):
    try:
        api_url = 'https://practice.erwgonzalez.repl.co/'
        response = requests.get(api_url)

        if response.status_code == 200:
            mensaje_hello = response.text
            return HttpResponse(f'Mensaje de la API: {mensaje_hello}')
        else:
            return HttpResponse('Error al obtener el mensaje de la API')
    except RequestException as e:
        return HttpResponse(f'Error en la solicitud a la API: {e}')

def home(request):
    return render(request, 'home.html')

def registro(request):
    data = {
        'form':PacienteForm()
    }
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():


            paciente = form.cleaned_data

            response = requests.post('https://intento1.chpineda.repl.co/api/pacientes/add', json=paciente)
            
            data['mensaje2'] = response

            if response.status_code == 200:
                data['mensaje'] = "Guardado correctamente en la API Flask"
            else:
                data['mensaje'] = "Error al conectar con la API Flask"
                
    else:
        form = PacienteForm()
    
    return render(request, 'registration/registro.html', data)



def registro_medico(request):
    data = {
        'form':MedicoForm()
    }
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():


            medico = form.cleaned_data

            response = requests.post('https://intento1.chpineda.repl.co/api/medicos/adds', json=medico)
            
            data['mensaje2'] = response

            if response.status_code == 200:
                data['mensaje'] = "Guardado correctamente en la API Flask"
            else:
                data['mensaje'] = "Error al conectar con la API Flask"      
    else:
        form = MedicoForm()
    
    return render(request, 'registration/registro_medico.html', data)


def lista_registro(request):
    return render(request, 'lista_registro.html')

def Pacientes(request):

    response = requests.get('https://intento1.chpineda.repl.co/api/pacientes')
    try:
        if response.status_code == 200:
            pacientes = response.json()
            return render(request, 'pacientes.html', {'pacientes': pacientes})
        else:
            return render(request, 'error.html', {'error_msg': 'Error al obtener datos de pacientes'})
    except Exception as ex:
        return render(request, 'error.html', {'error_msg': str(ex)})



def medicos(request):
    response = requests.get('https://intento1.chpineda.repl.co/api/medicos')
    try:
        if response.status_code == 200:
            medicos = response.json()
            return render(request, 'medicos.html', {'medicos': medicos})
        else:
            return render(request, 'medicos.html', {'error_msg': 'Error al obtener datos de medicos'})
    except Exception as ex:
        return render(request, 'medicos.html', {'error_msg': str(ex)})



def citas(request):
    return render(request, 'home.html')
