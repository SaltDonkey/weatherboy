from weatherConversions import kelvinsToC, kelvinsToF

"""
These functions are the ones that will convert all the pieces together into a string
in which Weatherboy will output in Discord
"""

def _getTempInfo(weatherJSON : dict[dict]) -> dict:
    """
    Returns the value of the "main" key in the OpenWeatherMap's API JSON
    output. weatherJSON["main"] will have all the vital components, including
    the temperature and conditions.
    """
    return weatherJSON['main']

def _convertTempInfo(tempInfo: dict) -> dict:
    """
    Modifies the tempInfo dictionary to include the base temperature,
    the currently feels-like temperature, the high temperature, and the low.

    Both Fahrenheit and Celsius are stored.
    """

    tempInfo["baseTempF"] = kelvinsToF(tempInfo["temp"])
    tempInfo["baseTempC"] = kelvinsToC(tempInfo["temp"])

    tempInfo["feelsLikeF"] = kelvinsToF(tempInfo["feels_like"])
    tempInfo["feelsLikeC"] = kelvinsToC(tempInfo["feels_like"])

    tempInfo["highTempF"] = kelvinsToF(tempInfo["temp_max"])
    tempInfo["highTempC"] = kelvinsToC(tempInfo["temp_max"])

    tempInfo["lowTempF"] = kelvinsToF(tempInfo["temp_min"])
    tempInfo["lowTempC"] = kelvinsToC(tempInfo["temp_min"])

    return tempInfo

def weatherboyTemp(locationSearch : str, weatherJSON : dict) -> str:
    res = "Based on your search for \"{}\"\r\n".format(locationSearch)

    tempInfo = _getTempInfo(weatherJSON)
    tempInfo = _convertTempInfo(tempInfo)

    tempStr = f"""Current Base Temperature of {tempInfo["baseTempF"]} ˚F, {tempInfo["baseTempC"]} ˚C.
Currently feels like {tempInfo["feelsLikeF"]} ˚F, {tempInfo["feelsLikeC"]} ˚C.
With High of {tempInfo["highTempF"]} ˚F, {tempInfo["highTempC"]} ˚C.
And a Low of {tempInfo["lowTempF"]} ˚F, {tempInfo["lowTempC"]} ˚C.
"""

    return res + tempStr

def weatherboyDesc(locationSearch : str, weatherJSON : dict) -> str: 
    res = "Based on your search for \"{}\"\r\n".format(locationSearch)

    tempInfo = _getTempInfo(weatherJSON)
    tempInfo = _convertTempInfo(tempInfo)
    weatherDesc = weatherJSON["weather"][0]["description"]

    descStr = f"""Current Base Temperature of {tempInfo["baseTempF"]} ˚F, {tempInfo["baseTempC"]} ˚C.
Current Condition(s): {weatherDesc}.
"""

    return res + descStr


def weatherboySummary(locationSearch : str, weatherJSON : dict) -> str:
    res = "Based on your search for \"{}\"\r\n".format(locationSearch)

    coordsStr = "The coordinates for your location are as follows:\n"
    coordsStr += "Longitude: {}, Latitude: {}".format(weatherJSON["coord"]["lat"], weatherJSON["coord"]["lon"])

    tempStr = weatherboyTemp(locationSearch, weatherJSON)
    # Remove the "Based on your search" part of the tempStr
    tempStr = tempStr[tempStr.rindex("\"") + 1:]

    descStr = weatherboyDesc(locationSearch, weatherJSON)
    # Remove everything up to but not inluding "Current Condition(s)" part of the descStr
    descStr = descStr[descStr.rindex("Current"):]

    return res + coordsStr + tempStr + "\n" + descStr