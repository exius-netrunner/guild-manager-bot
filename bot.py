import config
import nextcord
from nextcord.ext import commands

# Set up the bot initializers
intents = nextcord.Intents.all()
activity = nextcord.Activity(type=nextcord.ActivityType.competing, name="domination!!!")

# Create a bot instance with no command prefix
bot = commands.Bot(intents=intents,
                   activity=activity)


@bot.event
async def on_ready():
    print(f'Bot Ready')
    # Synchronize slash commands to the specific guild
    guild = nextcord.Object(id=config.GUILD_ID)
    await bot.sync_application_commands(guild_id=guild.id)


# Load cogs
initial_extensions = [
    'cogs.commands.owner',
    'cogs.commands.admin',
    'cogs.commands.member',
    'cogs.events.events'
]

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

# Run the bot
bot.run(config.TOKEN)
