import requests
import matplotlib.pyplot as plt
from datetime import datetime
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def get_weather(api_key, location,dates,avg_temps):
    try:
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        forecast_url = "http://api.openweathermap.org/data/2.5/forecast"

        params = {
            "q": location,
            "appid": api_key,
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if data.get("cod") == 200:
            weather_desc = data["weather"][0]["description"] if "weather" in data else "Unknown"
            temp_k = data["main"]["temp"] if "main" in data else "Unknown"

            choice = input("\nChoose temperature scale ( Enter 1 for Celsius and 2 for  Fahrenheit):\n").strip().lower()
            if choice == '1':
                temp_c = kelvin_to_celsius(temp_k)
                print(f"\nWeather in {location}-->{weather_desc} and the Temperature is {temp_c:.2f}°C\n")
            elif choice == '2':
                temp_f = kelvin_to_fahrenheit(temp_k)
                print(f"\nWeather in {location}--> {weather_desc} and the Temperature is  {temp_f:.2f}°F\n")
            else:
                print("Invalid choice")

            wind_speed = data["wind"]["speed"] if "wind" in data else "Unknown"
            print(f"\nWind Speed: \n{wind_speed} m/s\n")
            
            forecast_params = {
                "q": location,
                "appid": api_key,
                "cnt": 40  # Number of forecast intervals (8 days * 5 intervals per day)
            }
            forecast_response = requests.get(forecast_url, params=forecast_params)
            forecast_data = forecast_response.json()

            print("\n_____6-Day Forecast:_____\n")
            daily_temps = {}  # To store daily average temperatures

            for forecast in forecast_data.get("list", []):
                forecast_time = datetime.utcfromtimestamp(forecast["dt"])
                date_key = forecast_time.date()

                if date_key not in daily_temps:
                    daily_temps[date_key] = []

                forecast_temp_k = forecast["main"]["temp"]
                forecast_temp_c = kelvin_to_celsius(forecast_temp_k)
                daily_temps[date_key].append(forecast_temp_c)

            dates_1 = []
            temp = []
            for date, temps in daily_temps.items():
                avg_temp = sum(temps) / len(temps)
                print(f"{date.strftime('%Y-%m-%d')} - Average Temperature: {avg_temp:.2f}°C")
                dates_1.append(date.strftime('%Y-%m-%d'))
                
                temp.append(avg_temp)

            return dates_1,temp

           

        else:
            print(f"Error: Unable to fetch weather data for {location}")


    except requests.exceptions.RequestException:
        print("Error: NO INTERNET, Kindly check your internet connection")



def plot_temperature_graph(dates,avg_temps):
    
    formatted_dates = [date for date in dates]
    plt.figure(figsize=(10, 6))
    plt.plot(formatted_dates, avg_temps, marker='o')
    plt.title(f"6-Day Temperature Forecast of {user_location}")
    plt.xlabel("Date")
    plt.ylabel("Average Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
def show_weather():
    user_location = location_entry.get()
    dates = []
    avg_temps = []
    a, b = get_weather(api_key, user_location, dates, avg_temps)
    
    plot_temperature_graph(a, b)
    
    weather_info.config(text=f"Weather data for {user_location} displayed below:")

root = Tk()
root.title("Weather Forecast")

api_key = "d6473b61f30e673d8da312056a6d00d6"

frame = Frame(root)
frame.pack(padx=10, pady=10)

location_label = Label(frame, text="Enter city name or ZIP code:")
location_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

location_entry = Entry(frame)
location_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

get_weather_button = Button(frame, text="Get Weather", command=show_weather)
get_weather_button.grid(row=1, columnspan=2, pady=10)

weather_info = Label(root, text="", font=("Helvetica", 12, "bold"))
weather_info.pack(pady=10)

canvas_frame = Frame(root)
canvas_frame.pack()

fig, ax = plt.subplots(figsize=(8, 5))
canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
canvas.get_tk_widget().pack()

root.mainloop()
