import random

from discord import Embed

from modules.commands.base import BaseCommand

# 8ball command
# Bot randomly decides the answer of your question.
# Functionallity for fun.


class Ball(BaseCommand):
    async def apply(self):
        # answer    embed color
        answers = [
            ["YES", 0x44ff00],
            ["NO", 0xa30505],
            ["MAYBE", 0x0559a3]
        ]
        # decide which
        ans = random.randint(0, len(answers))
        answer = str(answers[ans][0])
        embcolor = str(answers[ans][1])
        embtitle = "Let me guess... **" + answer + "**"
        embed = Embed(title=embtitle, description="The anwser of your question is " + answer, color=embcolor)
        embed.set_footer(text="BieneBot")
        await self.channel.send(embed=embed)
