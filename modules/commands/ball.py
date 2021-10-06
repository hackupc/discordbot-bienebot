import random

from discord import Embed, Color

from modules.commands.base import BaseCommand

# 8ball command
# Bot randomly decides the answer of your question.
# Functionallity for fun.


class Ball(BaseCommand):
    def __init__(self, channel, author, message, option):
        self.option = option
        self.author = author
        self.message = message
        self.channel = channel
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
        ans = random.choice(answers)
        answer = str(ans[0])
        embcolor = str(ans[1])

        if (self.option == 0):
            embtitle = "Let me guess... **" + answer + "**"
        else:
            f = ""
            if (len(self.question) > 1):
                for w in self.question:
                    f += w + " "
            else:
                f = str(self.question[0])
            embtitle = str(f + " ?.. **" + answer + "**")
        c = Color(int(embcolor))
        embed = Embed(title=embtitle, description="The anwser of your question is " + answer, color=c)
        embed.set_footer(text="BieneBot")
        await self.channel.send(embed=embed)
