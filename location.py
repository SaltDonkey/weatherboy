from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent = "weatherboy")

def createLocator(locationString : str, locator = geolocator) -> Nominatim.geocode:
    """
    Creates a location from the Nominatim.geocode() method
    """
    return locator.geocode(locationString)