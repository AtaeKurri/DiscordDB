# DiscordDB
[![Documentation Status](https://readthedocs.org/projects/discorddb/badge/?version=latest)](https://discorddb.readthedocs.io/en/latest/?badge=latest)

A simple database which uses a Discord channel to store data.
This is a fork from thec0sm0s's DiscordDB.
This version aims to be more flexible.

### Features
* Sending multiple data packs at the same time (Just started to program it)
* Edit a data entry from a message id.

### Installation
Not currently available


### Basic Example
```python
from discordDB import DiscordDB
from discord.ext import commands


LOGS = []
DATABASE_CHANNEL_ID = The id of a channel (int)


class MyBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix="!")
        self.discordDB = DiscordDB(self, DATABASE_CHANNEL_ID)

    @commands.command()
    async def log(self, ctx, *, text):
        data = {
            "name": ctx.author.name,
            "text": text
        }
        _id = await self.discordDB.set(data)
        LOGS.append(_id)

    @commands.command()
    async def show_logs(self, ctx):
        for _id in LOGS:
            data = await self.discordDB.get(_id)
            await ctx.send(f"Name: {data.name}, Text: {data.text}")


bot = MyBot()
bot.run("TOKEN")
```

If you wish to save the LOGS to be able to recover them after the bot closed,
you can consider put it in a file using json or some file managment system.


### Requirements
* discord.py


### Documentation
Head over to [documentation] for full API reference. 


[documentation]: https://discorddb.readthedocs.io/en/latest/
