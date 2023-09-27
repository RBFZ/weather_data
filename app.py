from tkinter import *
import requests #library needed
from time import sleep #delay to ouput
from tkinter.messagebox import _show

root = Tk()
root.title("~The Weather Checker~")
root.geometry("1000x800")

#city Input
def city_Click():
    print_city = (f"You entered: {city_entry.get('1.0','end')}")
    city['text'] = str(print_city)

city_label = Label(root, text="Enter a city: ")
city_label.pack()
city_entry = Text(root, height=1, width=15, bg="grey", fg="black", borderwidth=5)
city_entry.pack()

city_button = Button(root, width=20, text="Click after entering your city", command=city_Click)
city_button.pack()

city = Label(root)
city.pack()

#State Input
state_blank = Label(root, text="If a state code is not applicable, leave blank and click the button.")
state_blank.pack()

state_label = Label(root, text="Enter a State Code: (E.g. TX, AZ, etc.) ")
state_label.pack()
state_entry = Text(root, height=1, width=15, bg="grey", fg="black", borderwidth=5)
state_entry.pack()

def state_Click():
    print_state = (f"You entered: {state_entry.get('1.0','end')}")
    state['text'] = str(print_state)

state_button = Button(root, width=20, text="Click after entering your State", command=state_Click)
state_button.pack()

state = Label(root)
state.pack()

#Country Input
country_label = Label(root, text="Enter a Country Code: (E.g. USA, CA, etc.)")
country_label.pack()
country_entry = Text(root, height=1, width=15, bg="grey", fg="black", borderwidth=5)
country_entry.pack()

def country_Click():
    print_country = (f"You entered: {country_entry.get('1.0','end')}")
    country['text'] = str(print_country)

country_button = Button(root, width=20, text="Click after entering your Country", command=country_Click)
country_button.pack()

country = Label(root)
country.pack()

#input ends
#API requests start
api_key = '2e1d1ddaedaef757e4645cf039f06d58'

city_input = city_entry.get('1.0','end').lower()
state_input = state_entry.get('1.0','end').lower()
country_input = country_entry.get('1.0','end').lower()

get_location = requests.get(
    f"http://api.openweathermap.org/geo/1.0/direct?q={city_input},{state_input},{country_input}&limit={1}&appid={api_key}"
    )
#obtaining latitude and longitude

def continue_Click():
    city_input = city_entry.get('1.0','end').strip().lower()
    state_input = state_entry.get('1.0','end').strip().lower()
    country_input = country_entry.get('1.0','end').strip().lower()
    get_location = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={city_input},{state_input},{country_input}&limit={1}&appid={api_key}"
    )
    if city_entry.get('1.0','end').strip() in ("Houston", "houston"):
        hou_label = Label(root, text="Fun fact: It's Probably Humid...")
        hou_label.pack()
    latlon_label = Label(root, text="Currently obtaining latitude and longitude...")
    sleep(1)
    latlon_label.pack()
    global lat
    global lon
    location_data = get_location.json()[0] #gets latitude and longitude
    lat = location_data['lat']
    lon = location_data['lon']
    root.after(3000,lambda : _show("Success!", "Latitude and Longitude Values Have Been Recorded!\nPlease click the 'Obtain Weather Data' button next"))

done_button = Button(root, width=30, text="Click after you are finished entering information", command=continue_Click)
done_button.pack()

#obtaining weather values from lat/lon location data

def weather_Click():
    get_weather_data = requests.get( #put lat and lon into request to get weather data
    f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=imperial"
    )
    global weather
    global temp
    weather = get_weather_data.json()['list'][0]['weather'][0]['main']
    temp = get_weather_data.json()['list'][0]['main']['temp']
    print_weather_data = Label(root, text="Obtaining Weather Data...")
    print_weather_data.pack()
    root.after(2000,lambda : _show("Success!",  "Obtained Weather Data!\nPlease click the 'Print Weather Data' button next"))

get_weather_button = Button(root, width=30, text="Click to Obtain Weather Data", command=weather_Click)
get_weather_button.pack()

#put lat and lon into request to get weather data

#new window for this
cityname = city_entry.get('1.0','end')

def print_weather_Click():
    global cityname
    cityname = city_entry.get('1.0','end')
    if weather == 'Clouds':
        root.after(1000,lambda : _show(f"Weather for {cityname}",  f"The skies in {cityname} are a bit shady with some {weather} in the skies.\nThe temperature in {cityname} is {temp} degrees"))
        #print(f"The weather in {city} is a bit shady with some {weather} in the skies.")
    elif weather == 'Clear':
        root.after(1000,lambda : _show(f"Weather for {cityname}",  f"The weather in {cityname} might get sunny during the day with {weather} skies.\nThe temperature in {cityname} is {temp} degrees"))
        #print(f"The weather in {city} is  outside with some {weather} skies")
    elif weather == 'Rain':
        root.after(1000,lambda : _show(f"Weather for {cityname}",  f"The weather in {cityname} is a bit damp today as it has been raining.\nThe temperature in {cityname} is {temp} degrees"))
    else:
        root.after(1000,lambda : _show(f"Weather for {cityname}",  f"Weather in {cityname}: {weather}.\nThe temperature in {cityname} is {temp} degrees"))
    root.after(6000, root.destroy)

print_weather_button = Button(root, width=30, text="Print Weather Data", command=print_weather_Click)
print_weather_button.pack()

root.mainloop()
