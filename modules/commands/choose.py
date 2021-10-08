import random
from discord import Embed
from modules.commands.base import BaseCommand
from get_enviroment import COMMAND_PREFIX


class Choose(BaseCommand):

    def __init__(self, channel, author, message):
        self.channel = channel
        self.author = author
        self.message = message

    async def apply(self):
        options = self.message.split(",")
        selected = random.choice(options)

        desc = "My random choice is **" + selected + "**"
        embed = Embed(title="Random choice", description=desc, color=0x0559a3)
        embed.set_footer(text="BieneBot | " + COMMAND_PREFIX + " choose")
        await self.channel.send(embed=embed)
