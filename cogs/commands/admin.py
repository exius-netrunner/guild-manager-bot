import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import config


class AdminCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[config.GUILD_ID], description="Admin hello command")
    async def admin_hello(self, interaction: Interaction):
        await interaction.response.send_message('Hello, Admin!')


def setup(bot):
    bot.add_cog(AdminCog(bot))
