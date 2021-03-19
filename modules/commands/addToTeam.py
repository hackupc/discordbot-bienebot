from discord.utils import get
from modules.services.api import Api


class AddToTeam:

    def __init__(self, channel, author, message, users):
        self.channel = channel
        self.author = author
        self.users = users
        self.team_name = message
        self.api = Api()

    async def apply(self):
        role = get(self.author.roles, name=self.team_name)
        if role is None:
            await self.channel.send("You are not in this team")
            return
        for user in self.users:
            try:
                user_info = self.api.get_user_info(user.id, 'team_name')
                if user_info == "":
                    self.api.add_member_to_team(user.id, self.team_name)
                    await user.add_roles(role)
                    await self.channel.send("%s has joined the team!" % user.name)
                    await self.user.send("You have joined the team %s!" % self.team_name)
                else:
                    await self.channel.send("The user %s has a team already" % user.name)

            except (self.api.USER_NOT_FOUND, self.api.BAD_REQUEST, self.api.SERVER_ERROR) as e:
                await self.channel.send(e.message)
