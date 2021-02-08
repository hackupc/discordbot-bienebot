from discord import Embed

from modules.commands.base import BaseCommand


class Help(BaseCommand):

    async def apply(self):
        description = """
        uwu parrot -> Random parrot
        uwu biene -> Random biene
        uwu biene [name] -> Biene from [name]
        uwu cat -> Random cat
        uwu dog -> Random dog
        uwu joke -> bad joke (pls don't kill me :pleading_face:)
        uwu ping -> Displays info for your internet connection :)
        uwu meme [meme_code] text|seperated|by|lines -> inserts text to meme with code [meme_code] 
        (more info pinned in #random)
        """
        embed = Embed(title="UwU commands", description=description, color=0x00fbff)
        await self.user.send(embed=embed)
