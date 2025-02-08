import requests
import csv
from datetime import datetime

API_KEY = 'cf5170790aefceeddddf59694618d580'  
LATITUDE = 35.682839
LONGITUDE = 139.759455
URL = f'http://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}&units=metric'

response = requests.get(URL)
data = response.json()

# Extraer datos relevantes
weather_data = {
    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'temperature': data['main']['temp'],
    'humidity': data['main']['humidity'],
    'weather': data['weather'][0]['description']
}

# Guardar datos en el archivo CSV
csv_file = "clima-tokio.csv"

with open(csv_file, 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(weather_data.values())

print("Datos del clima en Tokio guardados correctamente.")
