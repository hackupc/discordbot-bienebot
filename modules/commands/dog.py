import random

from discord import Embed

from modules.commands.base import BaseCommand


class Dog(BaseCommand):

    async def apply(self):
        embed = Embed()
        embed.set_image(url="https://placedog.net/%d" % random.uniform(100, 500))
        await self.channel.send(embed=embed)
