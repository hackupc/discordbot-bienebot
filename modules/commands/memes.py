from asyncio import sleep

from discord import Embed

from modules.commands.base import BaseCommand
from modules.database.memes import MemesList


class Memes(BaseCommand):

    def __init__(self, channel, author, message):
        super().__init__(channel, author)
        list = message.split(' ')
        self.name = list[0]
        self.is_help = list[0] == 'help'
        if not self.is_help:
            self.is_meme_help = list[1] == 'help'
        else:
            self.is_meme_help = False
        joinable = '_'
        text = joinable.join(list[1:])
        self.message = text.split('|')

    async def apply(self):
        if self.is_help:
            await self.help()
        elif self.is_meme_help:
            await self.meme_help()
        else:
            await self.meme()

    async def help(self):
        list = MemesList().get_info_all()
        list_message = []
        message = "**USE**: uwu meme [command_meme] upper text|lower text"
        for item in list:
            message += "**%s**: %s\n" % (item['name'], item['key'])
            if len(message) > 1900:
                list_message.append(message)
                message = ""
        first = True
        for message in list_message:
            embed = Embed()
            if first:
                first = False
                embed.title = 'List of meme commands'
            embed.description = message
            await self.channel.send(embed=embed)
            await sleep(1)

    async def meme(self):
        embed = Embed()
        url = MemesList().get_url_meme(self.name)
        if len(self.message) > 1:
            embed.set_image(url="%s/%s/%s.png" % (url, self.message[0], self.message[1]))
        else:
            embed.set_image(url="%s/%s.png" % (url, self.message[0]))
        await self.channel.send(embed=embed)

    async def meme_help(self):
        embed = Embed()
        meme = MemesList().get_info(self.name)
        embed.set_image(url=meme['example'])
        embed.title = meme['name']
        embed.description = '**Use**: uwu meme %s upper text|lower text' % meme['key']
        await self.channel.send(embed=embed)
