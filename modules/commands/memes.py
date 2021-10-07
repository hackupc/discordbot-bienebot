from asyncio import sleep

from discord import Embed

from modules.commands.base import BaseCommand
from modules.database.memes import MemesList
from get_enviroment import COMMAND_PREFIX, WANTS_ORIGINAL_MEME_HELP


class Memes(BaseCommand):

    def __init__(self, channel, author, message):
        super().__init__(channel, author)
        list = message.split(' ')
        self.name = list[0]
        # Check if substring is help example: 'prefix meme help'
        self.is_help = list[0] == 'help'
        # check if is help meme ex: 'prefix meme memename help'
        if (len(list) > 1):
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
        message = "**USE: " + COMMAND_PREFIX + " meme [meme_code] help**\n"
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
            await self.user.send(embed=embed)
            await sleep(1)

    async def meme(self):
        # check if meme exists
        if(MemesList().get_url_meme(self.name) == ""):
            await self.channel.send("Meme not found")
        else:
            embed = Embed()
            url = MemesList().get_url_meme(self.name)
            url_format = '/'.join(self.message)
            embed.set_image(url="%s/%s.png?width=500" % (url, url_format))
            await self.channel.send(embed=embed)

    async def meme_help(self):
        embed = Embed()
        meme = MemesList().get_info(self.name)
        embed.title = meme['name']
        if(str(WANTS_ORIGINAL_MEME_HELP).lower() == "true"):
            # use the json example provided by db (not perfect because it doesn't use all the text gaps)
            image = meme['example']
            # once create the image, parse the text to display a proper example of how to use the command properly

            # remove the .png extension 4 = len(".png")
            nonParsedMemeText = meme['example'][:-4]

            # remove the http link, we only want the TEXT.
            # len("https://api.memegen.link/images/") = 32
            nonParsedMemeText = nonParsedMemeText[32:]

            memeexample = ""
            # now we have to replace the first "/" to a " " meme
            # example : rollsafe/can't_get_fired/if_you_don't_have_a_job
            # desired: rollsafe can't_get_fired/if_you_don't_have_a_job
            # because that's the command syntax
            memeexample += nonParsedMemeText[:len(str(meme['key'])) + 1].replace("/", " ")

            # rewrite nonParsedMemeText whithout meme name
            nonParsedMemeText = nonParsedMemeText[len(str(meme['key'])) + 1:]

            # split phrases/gaps/lines
            for phrase in nonParsedMemeText.split("/"):
                if (phrase != "_"):
                    phrase = phrase.replace("_", " ")
                memeexample += phrase + "|"
            memeexample = memeexample[:-1]

        else:
            # use a pre-set system of filling all gaps (for loop)
            format = ""
            for i in range(0, int(meme['lines'])):
                format += "text%d/" % i
            # remove the / at the end
            format = format[:-1]
            # more accurate but less fun.
            image = '%s/%s.png?width=500' % (meme['url'], format)
            memeexample = '%s %s' % (meme['key'], format)
        embed.description = '**Use**: ' + COMMAND_PREFIX + ' meme ' + memeexample
        embed.set_image(url=image)
        await self.channel.send(embed=embed)
