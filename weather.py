import weatherAPI
import weathStrFabricators

"""
This is the implmentation of the weatherboy functionality
"""

def runTemp(locationStr : str, apiKey : str) -> None or str or int:
    """
    Given a location and the API key, this function will return
    the descriptive string detailing the temperature of the given location.

    If the location could not be found via OpenWeatherMap API, then it will
    return None.

    If a status code other than 200 is found, then this function will instead
    return that status code for output.
    """
    weatherJSON = weatherAPI.getWeatherJSON(locationStr, apiKey)

    if not weatherJSON:
        return None

    if weatherJSON['cod'] == 200:
        return weathStrFabricators.weatherboyTemp(locationStr, weatherJSON)

    else:
        return weatherJSON['cod']

def runDesc(locationStr : str, apiKey : str) -> None or str or int:
    """
    Given a location and the API key, this function will return
    the descriptive string detailing the description of the weather 
    of the given location.

    If the location could not be found via OpenWeatherMap API, then it will
    return None.

    If a status code other than 200 is found, then this function will instead
    return that status code for output.
    """
    weatherJSON = weatherAPI.getWeatherJSON(locationStr, apiKey)

    if not weatherJSON:
        return None

    if weatherJSON['cod'] == 200:
        return weathStrFabricators.weatherboyDesc(locationStr, weatherJSON)

    else:
        return weatherJSON['cod']


def runSummary(locationStr : str, apiKey : str) -> None or str or int:
    """
    Given a location and the API key, this function will return
    the descriptive string detailing a total summary of the weather of 
    the location. This includes both the temperature and the description
    of the weather.

    If the location could not be found via OpenWeatherMap API, then it will
    return None.

    If a status code other than 200 is found, then this function will instead
    return that status code for output.
    """
    weatherJSON = weatherAPI.getWeatherJSON(locationStr, apiKey)

    if not weatherJSON:
        return None

    if weatherJSON['cod'] == 200:
        return weathStrFabricators.weatherboySummary(locationStr, weatherJSON)

    else:
        return weatherJSON['cod']