import discord
from discord.utils import get
from get_enviroment import SERVER_NAME, API_URL, headers
import requests


def get_bits_server(client):
    for guild in client.guilds:
        if guild.name == SERVER_NAME:
            return client.get_guild(guild.id)


# Create team rol and channels on discord
async def create_channel_rol(guild, team):
    team_role = await guild.create_role(name=team)
    category = await get_category(guild)

    voice_channel = await category.create_voice_channel(team.replace(" ", "-").lower())
    text_channel = await category.create_text_channel(team.replace(" ", "-").lower())

    overwrite_text = discord.PermissionOverwrite(read_messages=True, send_messages=True,
                                                 add_reactions=True)
    overwrite_voice = discord.PermissionOverwrite(connect=True, speak=True, stream=True, view_channel=True)
    await text_channel.set_permissions(team_role, overwrite=overwrite_text)
    await voice_channel.set_permissions(team_role, overwrite=overwrite_voice)

    return team_role


async def get_category(guild):
    i = sum(map(lambda c: c.name.startswith("Hackers-"), guild.categories))
    organizer = get(guild.roles, name="Organizer")
    mentor = get(guild.roles, name="Mentor")
    sponsor = get(guild.roles, name="Sponsor")

    permissions = discord.PermissionOverwrite(read_messages=True, send_messages=True, connect=True, speak=True,
                                              stream=True, view_channel=True)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False, connect=False),
        organizer: permissions,
        mentor: permissions,
        sponsor: permissions
    }
    if i == 0:
        category = await guild.create_category("Hackers-0")
        await category.edit(overwrites=overwrites)
        return category
    else:
        last = get(guild.categories, name="Hackers-%d" % (i - 1))
        if len(last.channels) >= 48:
            category = await guild.create_category("Hackers-%d" % i)
            await category.edit(overwrites=overwrites)
            return category
        else:
            return last


async def get_all_teams(guild):
    response = requests.get(API_URL, headers=headers)
    all_teams = [e.team_name for e in response if not ""]
    unique_teams = list(set(all_teams))
    for team in unique_teams:
        await create_channel_rol(guild, team)


def get_user_info(userid, param):
    response = requests.get("%s%s/" % (API_URL, str(userid)), headers=headers)
    if param == 'team_name':
        return response.json()['team_name']
    elif param == 'type':
        return response.json()['type']
    elif param == 'all':
        return response.json()
