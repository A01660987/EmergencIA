from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render 
from django.http import JsonResponse 
import openai
import os
from dotenv import load_dotenv
from typing import Dict
import json
from decouple import config

load_dotenv()
# openai.api_key = config("OPENAI_API_KEY")
openai.api_key = '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'


def home(request):
    return render(request, "home.html")

def record(request):
    return render(request, "record.html")

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


def get_completion(prompt): 
	print(prompt) 
	query = openai.Completion.create( 
		engine="text-davinci-003", 
		prompt=prompt, 
		max_tokens=1024, 
		n=1, 
		stop=None, 
		temperature=0.5, 
	)

	response = query.choices[0].text 
	print(response) 
	return response 


def query_view(request): 
	if request.method == 'POST': 
		prompt = request.POST.get('prompt') 
		response = get_completion(prompt) 
		return JsonResponse({'response': response})
	return render(request, 'index.html')

