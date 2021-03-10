import requests
from discord.utils import get
from get_enviroment import API_URL, headers


class AddSticker:

    def __init__(self, channel, author, message, user):
        self.channel = channel
        self.author = author
        self.user = user
        self.sticker_name = message

    async def apply(self):
        if get(self.author.roles, name='Organizer') is None:
            await self.channel.send("You have no permissions to add stickers")
            return
        data = {
            "stickers": self.sticker_name
        }
        response = requests.put("%s%s/" % (API_URL, str(self.user.id)), headers=headers, data=data)
        if 'stickers' in response.json():
            await self.channel.send('Sticker %s added!' % self.sticker_name)
        elif 'detail' in response.json():
            await self.channel.send('User not found in database')
        else:
            await self.channel.send(response.json()[0])
