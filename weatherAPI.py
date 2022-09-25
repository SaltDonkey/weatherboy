import requests
import location

# For reference
# baseURL = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"

def _createOpenWeatherURL(lat, lon, apiKey) -> str:
    """
    Takes in a latitude, longitude, and apiKey to fully construct the URL
    for openweathermap.org's API
    """
    return "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}".format(lat = lat, lon = lon, key = apiKey)

def _getResponse(weatherURL : str) -> requests.Response:
    """
    Returns a response from the given weatherURL
    """
    return requests.get(weatherURL)

def _createLocation(locationStr):
    """
    createLocation() takes in a locationStr and returns
    a Location object from geopy's Nominatim Module using
    the .geocode() method
    """
    return location.createLocator(locationStr)

def _getLatLonFromLocation(locationStr : str) -> "tuple(str, str)":
    """
    Given a locationStr, this function will return a tuple containing
    the (latitude, longitude) based on the locationStr

    If the locationStr brings up 0 results, None is returned instead
    """
    location = _createLocation(locationStr)

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
    # First, process the location
    latAndLon = _getLatLonFromLocation(locationStr)

    if not latAndLon:
        return None
    
    lat, lon = latAndLon

    # Second, make a call to OpenWeatherMap's API
    weatherURL = _createOpenWeatherURL(lat, lon, apiKey)

    response = _getResponse(weatherURL)

    # Thirdly, return the corresponding JSON file from the response
    return response.json()