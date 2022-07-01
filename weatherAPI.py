import requests

baseURL = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"

def createOpenWeatherURL(lat, lon, apiKey) -> str:
    return "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}".format(lat = lat, lon = lon, key = apiKey)

def getResponse(weatherURL : str) -> requests.Response:
    return requests.get(weatherURL)

def getJSON(response : requests.Response) -> dict:
    return response.json()
