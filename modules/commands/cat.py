import random

from discord import Embed

from modules.commands.base import BaseCommand


class Cat(BaseCommand):

    async def apply(self):
        embed = Embed()
        embed.set_image(url="https://cataas.com/cat?width=:%d" % random.uniform(100, 500))
        await self.channel.send(embed=embed)
