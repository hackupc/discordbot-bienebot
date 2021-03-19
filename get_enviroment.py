import json
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND_PREFIX = os.getenv('COMMAND_PREFIX')
SERVER_NAME = os.getenv('SERVER_NAME')
API_TOKEN = os.getenv('API_TOKEN')
DOMAIN = os.getenv('DOMAIN')
headers = {'Authorization': 'Token ' + API_TOKEN}

with open('files/parrots.json', 'r') as fp:
    PARROTS = json.load(fp)
with open('files/memes.json', 'r') as fp:
    MEMES = json.load(fp)
