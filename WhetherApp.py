import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if data.get("cod") != 200:
            print(f"Error from API: {data.get('message', 'Unknown error')}")
            return None
        
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather
    
    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None

def main():
    # Replace below string with your actual OpenWeatherMap API key:
    api_key = "812c651e2f05b06eb53449857788c7a2"
    
    city = input("Enter city name: ")
    weather = get_weather(city, api_key)
    
    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description'].capitalize()}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Could not retrieve weather data. Please try again.")

if __name__ == "__main__":
    main()
