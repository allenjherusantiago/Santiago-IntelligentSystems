from django.shortcuts import render

# Create your views here.

import urllib.request
import json

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=0567a59f0f0593ccb400020478d822bb').read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "feels_like":  str(list_of_data['main']['feels_like']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "main": str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['wetaher'][0]['description']),
            "icon": list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)