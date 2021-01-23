import random

from discord import Embed

from get_enviroment import PARROTS
from modules.commands.base import BaseCommand


class Parrot(BaseCommand):

    async def apply(self):
        parrot = random.choice(PARROTS)
        embed = Embed()
        embed.set_image(url="https://cultofthepartyparrot.com/parrots/hd/%s" % parrot)
        await self.channel.send(embed=embed)
