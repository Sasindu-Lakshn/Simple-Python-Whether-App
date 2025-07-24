# 🌤️ Simple Weather App using OpenWeatherMap API

This is a Python script that fetches and displays the current weather of a given city using the **OpenWeatherMap API**.

## 📌 Features

- Input any city name and get real-time weather details.
- Displays:
  - 🌡️ Temperature (in °C)
  - 🌫️ Weather description
  - 💧 Humidity (%)
  - 🌬️ Wind speed (m/s)
- Handles errors such as invalid city names or network issues.

## 🛠️ Requirements

- Python 3.x
- `requests` library  
  Install using:  
  ```bash
  pip install requests
🚀 How to Use
Clone the repository or download the weather.py file.

Open the script and replace the api_key variable with your OpenWeatherMap API key:

python
Copy
Edit
api_key = "your_api_key_here"
Run the script:

bash
Copy
Edit
python weather.py
Enter the name of the city when prompted.

📦 Sample Output
yaml
Copy
Edit
Enter city name: London
- Weather in London:
- Temperature: 22.4°C
- Description: Clear sky
- Humidity: 48%
- Wind Speed: 3.5 m/s

⚠️ Notes
You must sign up at https://openweathermap.org/api to get your free API key.

Make sure you’re connected to the internet when running the script.
