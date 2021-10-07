![Travis](https://img.shields.io/travis/com/hackupc/discordbot-bienebot)
![Library](https://img.shields.io/badge/Library-Discord.py-blue)
![Size](https://img.shields.io/github/languages/code-size/hackupc/discordbot-bienebot)
![Lines](https://img.shields.io/tokei/lines/github/hackupc/discordbot-bienebot)

![Image](https://hackupc.com/ogimage.png)

🤖 Discord bot for multiple utilities.

## Features

**biene parrot** -> Random parrot

**biene biene** -> Random biene

**biene biene [name]** -> Biene from [name]

**biene cat** -> Random cat

**biene dog** -> Random dog

**biene joke** -> bad joke (pls don't kill me :pleading_face:)

**biene 8ball** -> I guess your future. Ask me anything.

**biene ping** -> Displays info for your internet connection :)

**biene meme [meme_code] text|seperated|by|lines** -> inserts text to meme with code [meme_code]
(more info command: **biene meme help**)

**biene changeteamname [new teamname]** -> Changes the teamname

**biene jointeam [teamname] [mention all the users you want to add to the team]** -> Allows you to join

## Bot prefix

Customizable (environment variable)

# Setup

1. Create a ``.env`` file by copying the ``.env.template`` file. You can do that on linux via :

```sh
cp .env.template .env
```

2. Install ``pip``, ``virtualenv``, and ``python3``.

3. Install requirements by doing

```sh
pip install -r requirements.txt
```

4. Open the ``.env`` file and change your settings. 

5. Finally, run the bot.

```console
python3 bot.py
```

## Developement Setup

It is highly recommended to create a ``virtualenv`` called env (suggestion)

Then activate it and installing all the requirements into the virtual environment. Remember to set python=python3 as a flag.


