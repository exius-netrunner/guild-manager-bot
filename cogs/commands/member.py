import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import config


class MembersCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(guild_ids=[config.GUILD_ID], description="Member hello command")
    async def member_hello(self, interaction: Interaction):
        await interaction.response.send_message('Hello, Member!')

    @nextcord.slash_command(guild_ids=[config.GUILD_ID], description="Ask Zim what he thinks about humans")
    async def ask_zim(self, interaction: Interaction):
        await interaction.response.send_message('SILENCE!!!')


def setup(bot):
    bot.add_cog(MembersCog(bot))
