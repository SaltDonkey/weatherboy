import weatherAPI
import weatherJSONParsing
import location

'''
This is the implmentation of weatherAPI uses the free version of openweathermap.org
'''

def createLocation(locationStr):
    locationObj = location.getLatLon(locationStr)

    return locationObj


def runAll(locationStr, apiKey):
    location = createLocation(locationStr)

    if not location:
        return

    lat, lon = location.latitude, location.longitude


    weatherURL = weatherAPI.createOpenWeatherURL(lat, lon, apiKey)

    response = weatherAPI.getResponse(weatherURL)
    weatherJSON = response.json()

    if weatherJSON['cod'] == 200:
        return weatherJSONParsing.constructWeatherboyInfoStr(locationStr, weatherJSON)

    else:
        return weatherJSON['cod']
