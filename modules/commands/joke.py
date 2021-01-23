import random

from modules.commands.base import BaseCommand
from modules.database.jokes_text_en import PRO_JOKES_EN, JOKES_EN


class Joke(BaseCommand):

    def __init__(self, channel, author, option):
        super().__init__(channel, author)
        self.option = option

    async def apply(self):
        if self.option == 0:
            text = random.choice(PRO_JOKES_EN)
        elif self.option == 1:
            text = random.choice(JOKES_EN)
        else:
            text = random.choice(JOKES_EN + PRO_JOKES_EN)
        await self.channel.send(text)
