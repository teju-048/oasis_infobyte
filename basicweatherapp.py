import requests

city_name = input("Enter the name of your city: ")
API_Key = '375c6f8493b328d52a2f0c6b10494821'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_Key}&units=metric'


response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data['weather'][0]['description'])
    print('Current Temperature is',data['main']['temp'])
    print('Current Temperature Feels like is',data['main']['feels_like'])
    print('Current Humidity Feels like is',data['main']['humidity'])

