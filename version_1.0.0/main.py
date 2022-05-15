from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


def getWeather():
    city = input("Enter a city name: ")
    geolocation = Nominatim(user_agent='geoapiExercises')
    location = geolocation.geocode(city)
    tf = TimezoneFinder()
    continent = tf.timezone_at(lng=location.longitude, lat=location.latitude)
    date_time = datetime.now(pytz.timezone(continent))
    current_date = date_time.strftime('%D')
    current_time = date_time.strftime('%I:%M %p')

    api = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=bb09a854cad061813a9288195ec10f9c'
    json_data = requests.get(api).json()
    weather = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    print(continent)
    print('Today is ', current_date)
    print("Time: ", current_time)
    print('Pressure: ', pressure)
    print('Temperature:', temp, '°')
    print('weather: ', weather)
    print('Wind: ', wind)
    print('Humidity: ', humidity)


getWeather()
