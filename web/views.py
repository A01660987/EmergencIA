from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render 
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import openai
import os
from dotenv import load_dotenv
from typing import Dict
import json
from decouple import config

load_dotenv()
openai.api_key = config("OPENAI_API_KEY")


def home(request):
    if request.method == 'POST': 
        fullMessage = request.POST.get('fullMessage') 
        response = get_completion(fullMessage) 
        return JsonResponse({'response': response})
    return render(request, "home.html")

def record(request):
    return render(request, "record.html")

@csrf_exempt
def process_audio(request):
    uploaded_file = request.FILES['audio_file']
    # Save the uploaded file temporarily
    with open('temp_audio.wav', 'wb') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
    # Call your Python function to process the audio file (deepgram_test.main())
    processed_results = call_python_function('temp_audio.wav')
    # Delete the temporary file
    os.remove('temp_audio.wav')
    # Return the processed results as JSON
    return JsonResponse(processed_results)

@csrf_exempt
def get_completion(prompt): 
	response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "El próximo mensaje será un ejemplo de una posible llamada a servicios de emergencia. Necesito que me contestes en formato de un json extrayendo la información más pertinente en este caso. La información que debes de extraer será el nombre de la persona que llama, su número telefónico, su ubicación, las razones por las que está teniendo una emergencia, y el o los servicios de emergencia que sea má prudente enviar. Si no tienes uno o más de los datos, el campo deberá ser null. Las opciones de servicio de emergencia serán: \"Ambulancia\", \"Policía\" o \"Bomberos\". El formato del json debe de ser el siguiente: {\"nombre\", \"telefono\", \"ubicacion\", \"razones_de_emergencia\", \"servicios_a_enviar\"}. No imprimas nada adicional al JSON. Si determinas que la llamada no tiene absolutamente ninguna emergencia, entonces incluye esto en el json bajo \"razones_de_emergencia\""},
        {"role": "user", "content": prompt},
        # {"role": "user", "content": "El próximo mensaje será un ejemplo de una posible llamada a servicios de emergencia. Necesito que me provees los índices de las palabras claves que consideres más importantes en este caso, con formato de arreglo."},
        # {"role": "user", "content": prompt},
    ]
)
	response = response.choices[0].message.content  
	return response

@csrf_exempt
def query_view(request): 
	if request.method == 'POST': 
		prompt = request.POST.get('prompt') 
		response = get_completion(prompt) 
		return JsonResponse({'response': response})
	return render(request, 'index.html')

