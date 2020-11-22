import discord

from .models import Data, FieldError


class DiscordDB(object):
    """The Discord database client.

    Parameters
    ----------
    bot : discord.ext.commands.Bot
        An instance of discord.py Client or Bot representing your discord application.

    """

    def __init__(self, bot):
        self.__bot = bot

    def channel(self, _channel_id):
        """A method which returns an instance of ``discord.TextChannel`` which is being used as database."""
        return self.__bot.get_channel(_channel_id)

    async def save(self, data: dict, channel_id: int) -> int:
        """A method to post and save data to your database channel.

        Parameters
        ----------
        data : dict
            Dictionary representing your raw data.

        channel_id : int
            The id of the channel to send the data to.

        Returns
        -------
        int
            An special integer which should be saved by the client to get this same data later.

        """
        embed = discord.Embed.from_dict({
            "inline?": True,
            "fields": [{
                "name": name, "value": value
            } for name, value in data.items()]
        })
        message = await self.channel(channel_id).send(embed=embed)
        return message.id

    async def saves(self, data: list) -> list:
        """A method used to post and save multiple data dict to a single channel.

        Parameters
        ----------
        data : list[dict]
            List of data dictionaries

        Returns
        -------
        list
            A list of ids
        """
        _data_list = []
        for _data in data:
            _channel_id = _data["channel_id"]
            embed = discord.Embed.from_dict({
                "inline?": True,
                "fields": [{
                    "name": name, "value": value
                } for name, value in _data["data"].items()]
            })
            message = await self.channel(_channel_id).send(embed=embed)
            _data_list.append(message.id)
        return _data_list

    async def get(self, _id: int, channel_id: int) -> Data:
        """A method used to get your saved data from the database channel.

        Parameters
        ----------
        _id : int
            An special integer which was received from the :py:meth:`discordDBPlus.DiscordDB.save` method.

        channel_id : int
            The id of the channel to get the data from.

        Returns
        -------
        Data
            A instance of :class:`discordDBPlus.models.Data`. Supports . syntax
            A dict containing the data recovered from the message.

        """
        message = await self.channel(channel_id).fetch_message(_id)
        _data = message.embeds[0].to_dict()["fields"]
        data = Data({_["name"]: _["value"] for _ in _data})
        data.created_at = message.created_at
        return data

    async def getf(self, _id: int, _field:str, channel_id: int) -> Data:
        """A method used to get the data of only one field of a given message.

        Parameters
        ----------
        _id : int
            The id of the message your want to get the data from.

        _field : str
            The field name to get the data from.

        channel_id : int
            The id of the channel to get the data from.

        Returns
        -------
        Data
            Data object containing the message date of creating, the field name and the field content.
        """
        message = await self.channel(channel_id).fetch_message(_id)
        _data_msg = message.embeds[0].to_dict()["fields"]
        _data = {_["name"]: _["value"] for _ in _data_msg}
        if _field in _data:
            data = Data({"field": _field, "content": _data[_field]})
            data.created_at = message.created_at
            return data
        else:
            raise FieldError("The specified field doesn't exists in the data message")

    async def edit(self, _data: dict, _id: int, channel_id: int):
        """A method used to edit a data message.
        You can use the get method to edit the Data dict then use this method to edit the embed.

        Parameters
        ----------
        _data : dict
            A dict containing the changes you want to make to the original message.

        _id : int
            The id of the message to edit.

        channel_id : int
            The id of the channel to edit the data from
        """
        message = await self.channel(channel_id).fetch_message(_id)
        embed = discord.Embed.from_dict({
            "fields": [{
                "name": name, "value": value
            } for name, value in _data.items()]
        })
        await message.edit(embed=embed)

    async def search(self, _ids: list, _field: str, channel_ids: list) -> list:
        """A method used to search a value inside one message from a list of messages ids
        
        Parameters
        ----------
        _ids : list
            A list containing all the messages to search the data from.

        _field : str
            The value index you need to search.

        channel_ids : list[int]
            A list of id of the channel to search datas from

        Returns
        -------
        list[Data]
            A list of :class:`discordDBPlus.modelsData` containing the messages ids the data field was in,
            the channels ids and the fields contents.

        None
            The field doesn't exists anywhere in the given messages.
        """
        _dictlist = []
        _found = False
        for channel_id in channel_ids:
            for _id in _ids:
                try:
                    message = await self.channel(channel_id).fetch_message(_id)
                    _data = message.embeds[0].to_dict()["fields"]
                    data = {_["name"]: _["value"] for _ in _data}
                    for key, value in data.items():
                        if key == _field:
                            d = Data({"channel_id": channel_id, "message_id": message.id, "value": data[key]})
                            d.created_at = message.created_at
                            _dictlist.append(d)
                            _found = True
                except:
                    pass
        
        if _found:
            return _dictlist
        elif not _found:
            return None