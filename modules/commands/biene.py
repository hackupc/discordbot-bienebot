import os
import random

from discord import File

from modules.commands.base import BaseCommand


class Biene(BaseCommand):

    async def apply(self):
        path = random.choice(os.listdir("files/bienes/"))
        file = File(path, filename="Biene")
        await self.channel.send('Biene!', file=file)
