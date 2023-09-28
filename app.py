from tkinter import *
from tkmacosx import Button
from PIL import ImageTk, Image
import requests #library needed
from time import sleep #delay to ouput
from tkinter.messagebox import _show

root = Tk()
root.title("~The Weather Checker~")
root.geometry("800x600")

    

#background image
bg = ImageTk.PhotoImage(file="images/cloud_bg.png")

my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

#city Input
def city_Click():
    print_city = (f"{city_entry.get('1.0','end')}")
    city['text'] = str(print_city)

city_label = Label(root, text="Enter a city: ", bg="#53B5CE", fg="white")
city_label.pack()                              #cursor color                 when out of focus          in focus
city_entry = Text(root, height=1, width=15, insertbackground="cyan", highlightbackground="white", highlightcolor="yellow", bg="#53B5CE", fg="white")
city_entry.pack()

city_frame = Frame(root, bg="#53B5CE")
city_frame.pack(pady=0)
city_button = Button(city_frame, text="Click after entering your city", borderless=1, command=city_Click)
city_button.pack()

city = Label(root, height=0, bg="#4FB3CA")
city.pack()

#State Input
state_blank = Label(root, text="If a State Code is not applicable, leave blank and click the button.", bg="#4FB3CA")
state_blank.pack()

state_label = Label(root, text="Enter a State Code:\n (E.g. TX, AZ, etc.) ", bg="#52B4CC", fg="white")
state_label.pack()
state_entry = Text(root, height=0, width=15, insertbackground="cyan", highlightbackground="white", highlightcolor="yellow", bg="#53B5CE", fg="white")
state_entry.pack()

def state_Click():
    print_state = (f"{state_entry.get('1.0','end')}")
    state['text'] = str(print_state)

state_frame = Frame(root, bg="#53B5CE")
state_frame.pack(pady=0)
state_button = Button(state_frame, text="Click after entering your State", borderless=1, command=state_Click)
state_button.pack()

state = Label(root, bg="#64BDD4")
state.pack()

#Country Input
country_label = Label(root, text="Enter a Country Code:\n (E.g. USA, CA, etc.)", bg="#6FC4DB", fg="white")
country_label.pack()
country_entry = Text(root, height=1, width=15, insertbackground="cyan", highlightbackground="white", highlightcolor="yellow", bg="#53B5CE", fg="white")
country_entry.pack()

def country_Click():
    print_country = (f"{country_entry.get('1.0','end')}")
    country['text'] = str(print_country)

country_frame = Frame(root, bg="#53B5CE")
country_frame.pack(pady=0)
country_button = Button(country_frame, text="Click after entering your Country", borderless=1, command=country_Click)
country_button.pack()

country = Label(root, bg="#83CFE4")
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
    root.after(3000,lambda : _show("Success!", "Latitude and Longitude Values Have Been Recorded!\nClick the 'Obtain Weather Data' button next"))

lonlat_frame = Frame(root, bg="#53B5CE")
lonlat_frame.pack(pady=0)
lonlat_button = Button(lonlat_frame, text="Click after you are finished entering information", borderless=1, command=continue_Click)
lonlat_button.pack()

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
    root.after(2000,lambda : _show("Success!",  "Obtained Weather Data!\nClick the 'Print Weather Data' to print data"))

gw_frame = Frame(root, bg="#53B5CE")
gw_frame.pack(pady=0)
get_weather_button = Button(gw_frame, text="Click to Obtain Weather Data", borderless=1, command=weather_Click)
get_weather_button.pack()

#put lat and lon into request to get weather data

#new window for this
cityname = city_entry.get('1.0','end')

def print_weather_Click():
    global cityname
    cityname = city_entry.get('1.0','end')
    if weather == 'Clouds':
        root.after(1000,lambda : _show(f"Weather for {cityname}",  f"The skies in {cityname} are a bit shady with some {weather} in the skies.\nThe temperature in {cityname} is {temp} degrees"))
    elif weather == 'Clear':
        root.after(1000,lambda : _show(f"Weather for {cityname}",  f"The weather in {cityname} might get sunny during the day with {weather} skies.\nThe temperature in {cityname} is {temp} degrees"))
    elif weather == 'Rain':
        root.after(1000,lambda : _show(f"Weather for {cityname}",  f"The weather in {cityname} is a bit damp today as it has rained recently.\nThe temperature in {cityname} is {temp} degrees"))
    else:
        root.after(1000,lambda : _show(f"Weather for {cityname}",  f"Weather in {cityname}: {weather}.\nThe temperature in {cityname} is {temp} degrees"))
    root.after(6000, root.destroy)

pw_frame = Frame(root, bg="#53B5CE")
pw_frame.pack(pady=0)
print_weather_button = Button(pw_frame, text="Print Weather Data", borderless=1, command=print_weather_Click)
print_weather_button.pack()

root.mainloop()
