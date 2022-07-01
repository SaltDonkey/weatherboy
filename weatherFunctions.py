import weatherConversions

def getTempInfo(weatherJSON : dict):
    return weatherJSON['main']

def convertTempInfo(tempInfo):
    tempInfo["baseTempF"] = weatherConversions.kelvinsToF(tempInfo["temp"])
    tempInfo["baseTempC"] = weatherConversions.kelvinsToC(tempInfo["temp"])

    tempInfo["feelsLikeF"] = weatherConversions.kelvinsToF(tempInfo["feels_like"])
    tempInfo["feelsLikeC"] = weatherConversions.kelvinsToC(tempInfo["feels_like"])

    tempInfo["highTempF"] = weatherConversions.kelvinsToF(tempInfo["temp_max"])
    tempInfo["highTempC"] = weatherConversions.kelvinsToC(tempInfo["temp_max"])

    tempInfo["lowTempF"] = weatherConversions.kelvinsToF(tempInfo["temp_min"])
    tempInfo["lowTempC"] = weatherConversions.kelvinsToC(tempInfo["temp_min"])

    return tempInfo

def weatherboyTemp(locationSearch, weatherJSON):
    res = "Based on your search for \"{}\"\n\r".format(locationSearch)

    tempInfo = getTempInfo(weatherJSON)
    tempInfo = convertTempInfo(tempInfo)

    tempStr = f"""Current Base Temperature of {tempInfo["baseTempF"]} ˚F, {tempInfo["baseTempC"]} ˚C.
Currently feels like {tempInfo["feelsLikeF"]} ˚F, {tempInfo["feelsLikeC"]} ˚C.
With High of {tempInfo["highTempF"]} ˚F, {tempInfo["highTempC"]} ˚C.
And a Low of {tempInfo["lowTempF"]} ˚F, {tempInfo["lowTempC"]} ˚C.
"""

    return res + tempStr

def weatherboyDesc(locationSearch, weatherJSON):
    res = "Based on your search for \"{}\"\n\r".format(locationSearch)

    tempInfo = getTempInfo(weatherJSON)
    tempInfo = convertTempInfo(tempInfo)
    weatherDesc = weatherJSON["weather"][0]["description"]

    descStr = f"""Current Base Temperature of {tempInfo["baseTempF"]} ˚F, {tempInfo["baseTempC"]} ˚C.
Current Condition(s): {weatherDesc}.
"""

    return res + descStr


def weatherboySummary(locationSearch, weatherJSON):
    res = "Based on your search for \"{}\"\n\r".format(locationSearch)

    coordsStr = "The coordinates for your location are as follows:\n"
    coordsStr += "Longitude: {}, Latitude: {}".format(weatherJSON["coord"]["lat"], weatherJSON["coord"]["lon"])

    tempStr = weatherboyTemp(locationSearch, weatherJSON)
    tempStr = tempStr[tempStr.rindex("\"") + 1:]

    descStr = weatherboyDesc(locationSearch, weatherJSON)
    descStr = descStr[descStr.rindex("Current"):]

    return res + coordsStr + tempStr + "\n" + descStr