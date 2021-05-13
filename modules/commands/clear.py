from asyncio import sleep

from modules.commands.base import BaseCommand


class Clear(BaseCommand):

    async def apply(self):
        if not self.author.top_role.permissions.administrator:
            await self.channel.send("You have no permissions. Contact an organizer")
            return
        deleted = await self.channel.purge(limit=10000)
        msg = await self.channel.send('purged %d messages' % len(deleted))
        await sleep(2)
        await msg.delete()
