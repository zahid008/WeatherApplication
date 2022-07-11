import pytz
from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
import json
from django.shortcuts import render
from datetime import datetime
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim


# Create your views here.
def home(request):
    try:
        if request.method == 'POST':
            city = request.POST['city']

            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                            city + '&units=metric&appid=bb09a854cad061813a9288195ec10f9c').read()
            list_of_data = json.loads(source)

            geolocation = Nominatim(user_agent='geoapiExercises')
            location = geolocation.geocode(city)
            tf = TimezoneFinder()
            continent = tf.timezone_at(lng=location.longitude, lat=location.latitude)
            date_time = datetime.now(pytz.timezone(continent))
            current_date = date_time.strftime('%D')
            current_time = date_time.strftime('%I:%M %p')

            data = {
                "date": str(current_date),
                "current_time": str(current_time),
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ', '
                              + str(list_of_data['coord']['lat']),
                "location": str(continent),

                "temp": str(list_of_data['main']['temp']) + ' °C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                "wind": str(list_of_data['wind']['speed']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': list_of_data['weather'][0]['icon'],
            }
            print(data)
        else:
            data = {}
    except:
        message = 'Error found in home function'

    return render(request, "HTMLS/home.html", data)
