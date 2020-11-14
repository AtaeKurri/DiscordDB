.. _intro:


Introduction
============

DiscordDBPlus acts like a simple database which uses a discord channel to store data which
are generally not much important and you do not care about in an unlimited manner.
This is a fork of DiscordDB that aims to be more complete and have more features.


Requirements
------------

**discord.py**
    It requires ``discord.py`` as a main wrapper to post or get data from discord channel.


Installing
----------

You can install DiscordDBPlus directly from PyPI using PIP and following command
in shell or command prompt: ::

    python3 -m pip install -U DiscordDBPlus


Basic Usage
-----------

.. code-block:: python3

  from discordDBPlus import DiscordDB
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
          _id = await self.discordDB.save(data)
          LOGS.append(_id)

      @commands.command()
      async def show_logs(self, ctx):
          for _id in LOGS:
              data = await self.discordDB.get(_id)
              await ctx.send(f"Name: {data.name}, Text: {data.text}")

      @commands.command()
      async def log(self, ctx, id):
          _id = int(id)
          data = await DB.get(_id)
          data["name"] = "example modification"
          data["text3"] = "Edited text"
          await DB.edit(data, _id)


  bot = MyBot()
  bot.run("TOKEN")
