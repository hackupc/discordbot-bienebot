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
        else:
            if self.message.upper() in list:
                file = File('%s%s.png' % (path, self.message.upper()), filename="Biene.png")
                await self.channel.send('Biene!', file=file)
            else:
                await self.channel.send('Not found! Try again bitch')
