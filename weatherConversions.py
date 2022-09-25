"""
Simple conversion functions that converts Kelvin to 
Degrees Fahrenheit or Celsius. Both conversions are rounded
to 3 decimal places
"""

def kelvinsToF(kelvin):
    "K to Deg F"
    return round((kelvin - 273.15) * (9/5) + 32, 3)

def kelvinsToC(kelvin):
    "K to Deg C"
    return round(kelvin - 273.15, 3)