from hikari import UnauthorizedError
import lightbulb
import weather

"""
This is the main module that includes all the commands and the
high level implementation for Weatherboy
"""
    
def createWeatherboy(token):
    """
    Creates a new instance of the Weatherboy bot by using the given
    Discord bot token
    """
    return lightbulb.BotApp (
        token = token
        )

if __name__ == "__main__":
    # Take and store Discord bot token and the openweathermap.org API key
    discordToken = input("Input in the Discord Token for weatherboy: ")
    openweatherAPIkey = input("Input in the API Key for openweathermap.org: ")

    try:
        bot = createWeatherboy(discordToken)
    except UnauthorizedError:
        print("Put in the wrong Discord bot token or some other error has occurred, please Try Again")

    """
    /checktemp
    params = location
    """
    @bot.command
    @lightbulb.option("location", "Enter in a location to check the weather!", type = str, default = "Elk Grove, CA")
    @lightbulb.command("checktemp", "Checks the weather for the given location")
    @lightbulb.implements(lightbulb.SlashCommand)
    async def checkweather(context):
        weatherResult = weather.runTemp(context.options.location, openweatherAPIkey)

        if weatherResult is None:
            await context.respond("No results found for given location of \"{}\"".format(context.options.location))
        elif type(weatherResult) is int:
            await context.respond("An error of code {} has occurred from openweathermap.org".format(weatherResult))
        else:
            await context.respond(weatherResult)

    """
    /checkdesc
    params = location
    """
    @bot.command
    @lightbulb.option("location", "Enter in a location to check the description of the weather!", type = str, default = "Elk Grove, CA")
    @lightbulb.command("checkdesc", "Displays the conditions of the weather of a given location")
    @lightbulb.implements(lightbulb.SlashCommand)
    async def checkweather(context):
        weatherResult = weather.runDesc(context.options.location, openweatherAPIkey)

        if weatherResult is None:
            await context.respond("No results found for given location of \"{}\"".format(context.options.location))
        elif type(weatherResult) is int:
            await context.respond("An error of code {} has occurred from openweathermap.org".format(weatherResult))
        else:
            await context.respond(weatherResult)

    """
    /checksummary
    params = location
    """
    @bot.command
    @lightbulb.option("location", "Enter in a location to check the whole summary of the weather!", type = str, default = "Elk Grove, CA")
    @lightbulb.command("checksummary", "Checks the both the weather temperature and condition for the given location")
    @lightbulb.implements(lightbulb.SlashCommand)
    async def checkweather(context):
        weatherResult = weather.runSummary(context.options.location, openweatherAPIkey)

        if weatherResult is None:
            await context.respond("No results found for given location of \"{}\"".format(context.options.location))
        elif type(weatherResult) is int:
            await context.respond("An error of code {} has occurred from openweathermap.org".format(weatherResult))
        else:
            await context.respond(weatherResult)

    bot.run()


# NOTES

# Create Event Handler
## This one simply echos/repeats what anyone says in a Discord chat
# @bot.listen(hikari.GuildMessageCreateEvent)
# async def printMessage(event):
#     print(event.content)

# @bot.listen(hikari.StartedEvent)
## This one makes the bot output "Bot started successfully!" whenever
# it first boots up
# async def onStartup(event):
#     print("Bot started successfully!")

# Creating Singular Slash Command
# @bot.command 
## @lightbulb.command(commandName, descriptionOfCommand)
# @lightbulb.command("ping", "Says pong!")
# @lightbulb.implements(lightbulb.SlashCommand)
# async def ping(context):
#     await context.respond("Pong!")

# Create Group Commands and Sub Commands
# @bot.command
## Not too sure what Group and Sub Commands are
# @lightbulb.command("group", "This is a group")
# @lightbulb.implements(lightbulb.SlashCommandGroup)
# async def testGroup(context):
#     pass

# @testGroup.child
# @lightbulb.command("subcommand", "This is a subcommand")
# @lightbulb.implements(lightbulb.SlashSubCommand)
# async def subCommand(context):
#     await context.respond("I am a subcommand!")

# Create Slash Commands w/ OPTIONS
# @bot.command
## This is if you want paramaters to be added to your commands
## The parameters are from @lightbulb.option
## @lightbulb.option(paramName, descriptionOfParam, type = typeOfParam)
# @lightbulb.option("num2", "The second number", type = int)
# @lightbulb.option("num1", "The first number", type = int)
# @lightbulb.command("add", "Add two numbers together")
# @lightbulb.implements(lightbulb.SlashCommand)
# async def add(context):
#     await context.respond(context.options.num1 + context.options.num2)