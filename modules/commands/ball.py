import random

from discord import Embed

from modules.commands.base import BaseCommand

#8ball command
class Ball(BaseCommand):

    async def apply(self): 
            # answer    embed color 
        answers = [
            ["YES",     0x44ff00],
            ["NO",      0xa30505],
            ["MAYBE",   0x0559a3]
        ]
        #decide which 
        ans = random.randint(0,len(answers))
        embed = Embed(title="Let me guess..... **"+str(answers[ans][0])+"**", description="The anwser of your question is "+str(answers[ans][0]), color=answers[ans][1])
        embed.set_footer(text="BieneBot")
        await self.channel.send(embed=embed)
