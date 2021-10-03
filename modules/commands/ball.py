import random

from requests.api import options

from discord import Embed

from modules.commands.base import BaseCommand

# 8ball command
# Bot randomly decides the answer of your question.
# Functionallity for fun.


class Ball(BaseCommand):
    def __init__(self, channel, message, option):
        self.option = option
        self.question = message

    async def apply(self):
        # answer    embed color
        answers = [
            ["YES", 0x44ff00],
            ["DEFINETLY YES", 0x44ff00],
            ["SURE 99,9%", 0x44ff00],
            ["NO", 0xa30505],
            ["DEFINETLY NO", 0xa30505],
            ["MAYBE", 0x0559a3],
            ["NOT SURE 100%", 0x0559a3],
            ["I'M NOT SURE", 0x0559a3]
        ]
        # decide which
        ans = random.randint(0, len(answers))
        answer = str(answers[ans][0])
        embcolor = str(answers[ans][1])

        if (self.option == 0):
            embtitle = "Let me guess... **" + answer + "**"
        else:
            embtitle = self.question, "?.. **" + answer + "**"
        embed = Embed(title=embtitle, description="The anwser of your question is " + answer, color=embcolor)
        embed.set_footer(text="BieneBot")
        await self.channel.send(embed=embed)
