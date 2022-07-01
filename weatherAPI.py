import requests
import location

# For reference
# baseURL = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"

def createOpenWeatherURL(lat, lon, apiKey) -> str:
    """
    Takes in a latitude, longitude, and apiKey to fully construct the URL
    for openweathermap.org's API
    """
    return "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}".format(lat = lat, lon = lon, key = apiKey)

def getResponse(weatherURL : str) -> requests.Response:
    """
    Returns a response from the given weatherURL
    """
    return requests.get(weatherURL)

def createLocation(locationStr):
    """
    createLocation() takes in a locationStr and returns
    a Location object from geopy's Nominatim Module using
    the .geocode() method
    """
    locationObj = location.createLocator(locationStr)
    return locationObj

def getLatLonFromLocation(locationStr):
    """
    Given a locationStr, this function will return a tuple containing
    the (latitude, longitude) based on the locationStr

    If the locationStr brings up 0 results, None is returned instead
    """
    location = createLocation(locationStr)

    if not location:
        return

    return (location.latitude, location.longitude)

def getWeatherJSON(locationStr, apiKey):
    """
    getWeatherJSON() takes in a locationStr and the openweathermap.org API key
    and returns the corresponding JSON string.

    If the given locationStr brings up 0 results or the created location item is invalid, 
    None is returned
    """
    latAndLon = getLatLonFromLocation(locationStr)

    if not latAndLon:
        return None
    
    lat = latAndLon[0]
    lon = latAndLon[1]

    weatherURL = createOpenWeatherURL(lat, lon, apiKey)

    response = getResponse(weatherURL)
    return response.json()