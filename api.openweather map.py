import json
import requests

url = "https://api.openweathermap.org/data/2.5/weather?lat=13.107568&lon=77.5711&appid=fbcebb967a13264f36de8c43dc39e4f9"
r = requests.get(url)
#print("content",r.content)

data = json.loads(r.content)# converting byte to json

print(data)

#print(data.keys())   # To get all the keys

#print(data["main"])   # to get complete temperature

#print(data["main"]["temp"]-273)  # to get in celsius





# output of postman
{
    "coord": {
        "lon": 77.5711,
        "lat": 13.1076
    },
    "weather": [
        {
            "id": 802,
            "main": "Clouds",
            "description": "scattered clouds",
            "icon": "03d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 298.27,
        "feels_like": 298.48,
        "temp_min": 298.15,
        "temp_max": 301.87,
        "pressure": 1011,
        "humidity": 63
    },
    "visibility": 8000,
    "wind": {
        "speed": 4.12,
        "deg": 270
    },
    "clouds": {
        "all": 40
    },
    "dt": 1656830026,
    "sys": {
        "type": 2,
        "id": 2040609,
        "country": "IN",
        "sunrise": 1656808039,
        "sunset": 1656854406
    },
    "timezone": 19800,
    "id": 1252758,
    "name": "Yelahanka",
    "cod": 200
}
