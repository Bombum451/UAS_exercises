import requests
from dotenv import dotenv_values
env = dotenv_values('.env')

keyword = input("Please state the location: ")

request = "https://api.openweathermap.org/data/2.5/weather?q=" + str(keyword) + "&APPID=" + str(env['API_KEY'])

response = requests.get(request).json()

print("")
print(response["weather"][0]["description"])

temp = response["main"]["temp"]
temp = round(temp - 273)

print(str(temp) + "°C")