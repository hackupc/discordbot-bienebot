from abc import ABC, abstractmethod

from discord.utils import get


class BaseCommand(ABC):

    def __init__(self, channel, author):
        self.channel = channel
        self.author = get(channel.guild.members, id=author.id)
        self.user = author

    @abstractmethod
    async def apply(self):
        pass
