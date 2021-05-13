import os
import random

from discord import File

from modules.commands.base import BaseCommand


class Biene(BaseCommand):

    def __init__(self, channel, author, message=None):
        super().__init__(channel, author)
        self.message = message

    async def apply(self):
        file = None
        path = 'files/bienes/'
        list = os.listdir(path)
        if self.message is None:
            name = random.choice(list)
            file = File(path + name, filename="Biene.png")
            await self.channel.send('Biene!', file=file)
        else:
            self.message = self.message.upper() + '.png'
            if self.message in list:
                file = File(path + self.message, filename="Biene.png")
                await self.channel.send('Biene!', file=file)
            else:
                await self.channel.send('Not found! Try again')
