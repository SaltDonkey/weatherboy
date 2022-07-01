from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent = "weatherboy")

def createLocator(locationString, locator = geolocator) -> Nominatim.geocode:
    """
    Creates a location from the Nominatim.geocode() method
    """
    location = locator.geocode(locationString)
    return location