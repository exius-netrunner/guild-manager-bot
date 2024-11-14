from nextcord.ext import commands


class EventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    '''
    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore messages sent by the bot itself
        if message.author == self.bot.user:
            return
        print(f'Message from {message.author}: {message.content}')
    '''


def setup(bot):
    bot.add_cog(EventCog(bot))
