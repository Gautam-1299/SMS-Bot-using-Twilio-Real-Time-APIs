import urllib.request
import json 



def get_weather(city):
  url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b5c4f65608ce882fd5cf839e8878a0ad'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  #print(result)
  #C - 273.15
  temp = round(result["main"]["temp"] - 273.15,2)
  return temp