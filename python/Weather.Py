import requests
import json

# URL for Tokyo's weather forecast (includes Akihabara)
url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"

# Send the request to the API
response = requests.get(url)

# Check if the response is successful
if response.status_code == 200:
    weather_data = response.json()  # Get the data in JSON format
    
    # Extract the temperature from the response
    try:
        # Example: Extracting the forecast for the first area (Tokyo area) from the JSON
        temperature_info = weather_data[0]['timeSeries'][0]['areas'][0]['winds']
        
        # Print the temperature details (maximum and minimum)
        #max_temp = temperature_info['max']['celsius'] if 'max' in temperature_info else 'N/A'
        #min_temp = temperature_info['min']['celsius'] if 'min' in temperature_info else 'N/A'

        #print(f"Max Temperature: {max_temp}°C")
        #print(f"Min Temperature: {min_temp}°C")

        
        print(temperature_info[0])
        print(temperature_info[1])
        print(temperature_info[2])
        
    except (KeyError, IndexError) as e:
        print("Error extracting temperature:", e)

else:
    print("Failed to retrieve data. Status code:", response.status_code)
