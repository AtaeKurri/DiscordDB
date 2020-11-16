# DiscordDBPlus

[![Documentation Status](https://readthedocs.org/projects/discorddbplus/badge/?version=latest)](https://discorddbplus.readthedocs.io/en/latest/?badge=latest)

A simple database which uses a Discord channel to store data.
This is a fork from thec0sm0s's DiscordDB.
This version aims to be more flexible.

### Features
* Sending multiple data packs at the same time
* Edit a data entry from a message id.
* searches data fields into multiple channels and multiple messages

### Installation

To install current latest release you can use following command:
```sh
python3 -m pip install DiscordDBPlus
```


### Basic Example
```python
from discordDBPlus import DiscordDB
from discord.ext import commands


LOGS = []


class MyBot(commands.Bot):

    def __init__(self):
        super().__init__(command_prefix="!")
        self.discordDB = DiscordDB(self) # You need to give the bot object to the DiscordDB instance

    @commands.command()
    async def log(self, ctx, *, text):
        data = {
            "name": ctx.author.name,
            "text": text
        }
        _id = await self.discordDB.save(data, id of a channel:int)
        LOGS.append(_id)

    @commands.command()
    async def show_logs(self, ctx):
        for _id in LOGS:
            data = await self.discordDB.get(_id, id of a channel:int)
            await ctx.send(f"Name: {data[name]}, Text: {data[text]}")

    @commands.command()
    async def edit_data(self, ctx, id):
        _id = int(id)
        data = await DB.get(_id, id of a channel:int)
        data["name"] = "example modification"
        data["text3"] = "Edited text"
        await DB.edit(data, _id, id of a channel:int)

    @commands.command()
    async def get_one_field(self, ctx):
        for _id in LOGS:
          data = await self.discordDB.getf(_id, "A field", id of a channel:int)
          await ctx.send(f"Text: {data}")


bot = MyBot()
bot.run("TOKEN")
```

If you wish to save the LOGS to be able to recover them after the bot closed,
you can consider put it in a file using json or some file managment system.

Since the 0.0.8 version, the initial declaration of the instance of DiscordDB
don't take a channel id argument anymore.
Instead, to have more flexibility, you need to give the channel id inside the
arguments of the command you want to use.


### Requirements
* discord.py


### Documentation
Head over to [documentation] for full API reference.

[documentation]: https://discorddbplus.readthedocs.io/en/latest/
