import requests

def get_weather(api_key, location):
    # URL for OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        'q': location,   # You can also use 'zip' for ZIP code
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    # Make the request to the OpenWeatherMap API
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract relevant information
        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']

        # Display the weather information
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {weather_description.capitalize()}")
    else:
        print("Error:", response.json().get('message', 'City not found'))

def main():
    api_key = 'f61ba5700d41f1911530b1de084b103e'  # Replace with your actual API key
    location = input("Enter city name or ZIP code: ")
    get_weather(api_key, location)

if __name__ == '__main__':
    main()
