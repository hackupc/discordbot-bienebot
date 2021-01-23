import os
import random

from discord import File

from modules.commands.base import BaseCommand


class Biene(BaseCommand):

    async def apply(self):
        path = 'files/bienes/'
        name = random.choice(os.listdir(path))
        file = File(path + name, filename="Biene.png")
        await self.channel.send('Biene!', file=file)
