from discord import Embed
from discord.utils import get
from modules.commands.base import BaseCommand


class Help(BaseCommand):

    async def apply(self):
        description = """
        biene parrot -> Random parrot
        biene biene -> Random biene
        biene biene [name] -> Biene from [name]
        biene cat -> Random cat
        biene dog -> Random dog
        biene joke -> bad joke (pls don't kill me :pleading_face:)
        biene ping -> Displays info for your internet connection :)
        biene meme [meme_code] text|seperated|by|lines -> inserts text to meme with code [meme_code]
        (more info pinned in #random)
        biene changeteamname [new teamname] -> Changes the teamname
        biene jointeam [teamname] [mention all the users you want to add to the team]
        """

        if get(self.author.roles, name='Organizer') is not None:
            description += """biene createteam [teamname] [mention 1 member of new team]
            biene userinfo [mention the user you want to stalk :smirk:]  
            biene reactions -> display a list of reactions by username and emoji from a message
            biene addsticker [sticker name] [mention the username that receives the sticker]
            """
        embed = Embed(title="Biene commands", description=description, color=0x00fbff)
        await self.user.send(embed=embed)
