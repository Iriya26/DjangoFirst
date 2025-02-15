from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def home(request):
    return HttpResponse("Hello, World!")


def weather_view(request):

   # URL for Tokyo's weather forecast (includes Akihabara)
    url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
    
    # Make a request to the weather API
    response = requests.get(url)
    
    # If the request is successful
    if response.status_code == 200:
        weather_data = response.json()
        
        # Extract relevant weather data (temperature in this case)
        try:
            temperature_info = weather_data[0]['timeSeries'][0]['areas'][0]['winds']
            max_temp = temperature_info[0]
            min_temp = temperature_info[1]
            
            # Prepare data to send to the template
            context = {
                'max_temp': max_temp,
                'min_temp': min_temp,
            }
        except (KeyError, IndexError) as e:
            context = {
                'error': "Failed to retrieve weather data."
            }
    else:
        context = {
            'error': "Failed to retrieve weather data. Status code: " + str(response.status_code)
        }
    
    return render(request, 'weather.html', context)
