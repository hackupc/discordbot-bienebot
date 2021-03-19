from discord.utils import get
from modules.services.api import Api


class AddSticker:

    def __init__(self, channel, author, message, user):
        self.channel = channel
        self.author = author
        self.user = user
        self.sticker_name = message
        self.api = Api()

    async def apply(self):
        if get(self.author.roles, name='Organizer') is None:
            await self.channel.send("You have no permissions to add stickers")
            return

        try:
            self.api.add_sticker(self.user.id, self.sticker_name)
            await self.channel.send('Sticker %s added!' % self.sticker_name)

        except (self.api.USER_NOT_FOUND, self.api.BAD_REQUEST, self.api.SERVER_ERROR) as e:
            await self.channel.send(e.message)
