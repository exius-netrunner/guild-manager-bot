import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import config


class OwnerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[config.GUILD_ID], description="Owner hello command")
    async def owner_hello(self, interaction: Interaction):
        await interaction.response.send_message('Hello, Owner!')


def setup(bot):
    bot.add_cog(OwnerCog(bot))
