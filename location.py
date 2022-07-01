from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent = "weatherboy")

def getLatLon(locationString, locator = geolocator) -> Nominatim.geocode:
    location = locator.geocode(locationString)
    return location
