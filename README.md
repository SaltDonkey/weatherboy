# weatherboy
A super rudimentary Discord bot that outputs weather info based on a given location.

# How to Use
Every command has one optional input only, "Location". Whatever is put into "Location" will be used to produce a set
of latitude and longitude coordinates. Subsequently, these geographical coordinates will be used to output the weather
results for those coordinates.

If no "Location" is passed in, "Elk Grove, CA" will be used by default.

# Commands
/checksummary - Displays the coordinates for the given location, the base temperature, the perceived temperature (what it feels like),
the high and low temperatures, and the current conditions

/checkdesc - Displays only the base temperature and the current conditions of the given location

/checktemp - Displays everything about the temperature of the given location only. Includes base temperature, perceived temperature, and 
the high and low temperatures