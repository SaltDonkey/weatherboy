import weatherAPI
import weatherFunctions
'''
This is the implmentation of the weatherboy functionality
'''
def runTemp(locationStr, apiKey):
    weatherJSON = weatherAPI.getWeatherJSON(locationStr, apiKey)

    if not weatherJSON:
        return None

    if weatherJSON['cod'] == 200:
        return weatherFunctions.weatherboyTemp(locationStr, weatherJSON)

    else:
        return weatherJSON['cod']

def runDesc(locationStr, apiKey):
    weatherJSON = weatherAPI.getWeatherJSON(locationStr, apiKey)

    if not weatherJSON:
        return None

    if weatherJSON['cod'] == 200:
        return weatherFunctions.weatherboyDesc(locationStr, weatherJSON)

    else:
        return weatherJSON['cod']


def runSummary(locationStr, apiKey):
    weatherJSON = weatherAPI.getWeatherJSON(locationStr, apiKey)

    if not weatherJSON:
        return None

    if weatherJSON['cod'] == 200:
        return weatherFunctions.weatherboySummary(locationStr, weatherJSON)

    else:
        return weatherJSON['cod']