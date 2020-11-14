API Reference
=============

Reference to all of available classes, methods, attributes, etc.


DiscordDB Client
----------------

.. py:class:: discordDBPlus.DiscordDB

    .. py:method:: set_channel(channel_id)

        Change the channel id to send data to.

        :param int channel_id: The id of the new channel
        :type channel_id: :class:`int`

    .. py:method:: save(data)

        Send a message with the data in it to the data channel.

        :param dict data: The dict data to save
        :type data: :class:`dict`
        :return: An int containing the message's in which the data was saved.
        :rtype: :class:`int`

    .. py:method:: saves(data)

        Send multiple messages with multiple data in them.

        :param list data: A `list` of `dict` datas to send messages from
        :type data: :class:`list`
        :return: A list containing ints of the messages in which the data dicts was saved in.
        :rtype: :class:`list[int]`

    .. py:method:: get(message_id)

        Get the data from a given message.

        :param int message_id: The id of the message to get the data from
        :type message_id: :class:`int`
        :return: Data
        :rtype: :class:`dict`

    .. py:method:: getf(message_id, field)

        Get only one data field from the given message.

        :param int message_id: The id of the message to get the data from
        :type message_id: :class:`int`
        :param str field: The field name from which the data will be taken.
        :type field: :class:`str`
        :return: The field value
        :rtype: :class:`str`

    .. py:method:: edit(data, id)

        Edit a given message.

        :param dict data: The data which will be used to update the embed message
        :type data: :class:`dict`
        :param int id: The id of the message to update
        :type id: :class:`int`


Data Types
----------

.. py:class:: discordDBPlus.models.Data
..
    Not currently used.
