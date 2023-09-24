import requests #library needed
from time import sleep #delay to ouput

api_key = '2e1d1ddaedaef757e4645cf039f06d58'

city_input = input("Enter a City: ")
print("If a state code is not applicable, press 'Enter' below.")
state_input = input("Enter a State Code(E.g. TX, AZ, etc...: ")
country_input = input("Enter a Country Code(E.g. USA, GBR, etc...: ")

get_location = requests.get(
    f"http://api.openweathermap.org/geo/1.0/direct?q={city_input},{state_input},{country_input}&limit={1}&appid={api_key}"
    )

if (city_input == 'Houston'):
    print("Fun fact: it's definitely humid")
sleep(.5)
print("Currently obtaining latitude and longitude")

for i in range(3):
    sleep(.5)
    print(".", sep=" ", end="", flush=True) #loading...
print()

print("Printing weather data")
for i in range(3):
    sleep(.5)
    print(".", sep=" ", end="", flush=True)
print()

location_data = get_location.json()[0] #gets latitude and longitude
lat = location_data['lat']
lon = location_data['lon']

get_weather_data = requests.get( #put lat and lon into request to get weather data
    f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=imperial"
)

weather = get_weather_data.json()['list'][0]['weather'][0]['main']
temp = get_weather_data.json()['list'][0]['main']['temp']


def print_weather_and_temp(city, weather, temp):
    if weather == 'Clouds':
        print(f"The weather in {city} is a bit shady with some {weather} in the skies.")
    elif weather == 'Clear':
        print(f"The weather in {city} is  outside with some {weather} skies")

    if temp > 90.00:
        print(f"The temperature in {city} is a high {temp}, is it always this hot?!")
    else: 
        print(f"The temperature in {city} is {temp}")

print_weather_and_temp(city_input, weather, temp)
