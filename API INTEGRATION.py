import requests    #HTTP requests
import datetime    #Handling date and tim
import matplotlib.pyplot as plt    #Plotting graphs

# Define city and API key
get_city = "Mumbai,IN"
API_KEY = "26e65b70d2c5c813473389c6c45cdad9"
API_url = f'https://api.openweathermap.org/data/2.5/forecast?q={get_city}&appid={API_KEY}&units=metric'
#request weather forecast in metric units (Celsius)


# Request weather forecast data
responses = requests.get(API_url)
if responses.status_code == 200:
    weather_data = responses.json()
    
    # Initialize empty lists to store forecast data
    forecast_dates = []
    temps = []
    humiditiy_level = []

    print(f"\n5-Day Weather Forecasts (Midday) for {get_city}:\n")   #Heading
    for entry in weather_data['list']:
        time = entry['dt_txt']

        # Filter for 12:00 PM readings only
        if "12:00:00" in time:
            date_time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
            temp = entry['main']['temp']
            humid_lev = entry['main']['humidity']
            descrip = entry['weather'][0]['description']

            # Append data to the lists
            forecast_dates.append(date_time)
            temps.append(temp)
            humiditiy_level.append(humid_lev)

            print(f"{date_time.strftime('%a, %d %b')}: {descrip}, Temp: {temps}°C, Humidity: {humid_lev}%")


    #  Visualize temperature and humidity trends
    plt.figure(figsize=(10, 5))
    plt.plot(forecast_dates, temps, marker='o', linestyle='-', color='orange', label='Temperature (°C)')
    plt.plot(forecast_dates, humiditiy_level, marker='x', linestyle='--', color='blue', label='Humidity (%)')

    plt.title(f" 5-Days of Midday Forecast: {get_city}")
    plt.xlabel("Date")
    plt.ylabel("Values")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

else:
    # Print error if the API call was unsuccessful
    print(f"Data retrieval failed ! Status code: {responses.status_code}")
