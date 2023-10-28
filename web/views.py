from django.shortcuts import render
from django.http import JsonResponse
import os

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
