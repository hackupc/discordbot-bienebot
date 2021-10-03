from discord import Embed
from discord.utils import get
from modules.commands.base import BaseCommand
from get_enviroment import COMMAND_PREFIX


class Help(BaseCommand):

    async def apply(self):
        description = """
        **""" + COMMAND_PREFIX + """ parrot** -> Random parrot
        **""" + COMMAND_PREFIX + """ biene** -> Random biene
        **""" + COMMAND_PREFIX + """ biene [name]** -> Biene from [name]
        **""" + COMMAND_PREFIX + """ cat** -> Random cat
        **""" + COMMAND_PREFIX + """ dog** -> Random dog
        **""" + COMMAND_PREFIX + """ joke** -> bad joke (pls don't kill me :pleading_face:)
        **""" + COMMAND_PREFIX + """ 8ball** -> I guess your future. Ask me anything.
        **""" + COMMAND_PREFIX + """ ping** -> Displays info for your internet connection :)
        **""" + COMMAND_PREFIX + """ meme [meme_code] text|seperated|by|lines **-> inserts text to meme with code [meme_code]
        (more info command: **""" + COMMAND_PREFIX + """ meme help**)
        **""" + COMMAND_PREFIX + """ changeteamname [new teamname]** -> Changes the teamname
        **""" + COMMAND_PREFIX + """ jointeam [teamname] [mention all the users you want to add to the team]**
        """

        if get(self.author.roles, name='Organizer') is None:
            pass
        else:
            description += "**" + COMMAND_PREFIX + """ createteam [teamname] [mention 1 member of new team]** -> Creates new team
            **""" + COMMAND_PREFIX + """ userinfo [mention the user you want to stalk :smirk:]** -> Get information of a user
            **""" + COMMAND_PREFIX + """ reactions** -> display a list of reactions by username and emoji from a message
            **""" + COMMAND_PREFIX + """ addsticker [sticker name] [mention the username that receives the sticker]** -> Give sticker
            """
        embed = Embed(title="Biene commands", description=description, color=0x00fbff)
        await self.user.send(embed=embed)
