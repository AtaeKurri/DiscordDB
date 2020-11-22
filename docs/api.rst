.. role:: raw-html(raw)
    :format: html

API Reference
=============

Reference to all of available classes, methods, attributes, etc.


DiscordDB Client
----------------

.. py:class:: discordDBPlus.DiscordDB

    .. py:method:: save(data, channel_id)

        Send a message with the data in it to the data channel.

        :param dict data: The dict data to save
        :type data: :class:`dict`
        :param int channel_id: The channel to send the data in.
        :type channel_id: :class:`int`
        :return: An int containing the message's in which the data was saved.
        :rtype: :class:`int`

        :raw-html:`<br />`

    .. py:method:: saves(data)

        Send multiple messages with multiple data in them.

        :param list data: A `list` of `dict` datas to send messages from
        :type data: :class:`list`
        :return: A list containing ints of the messages in which the data dicts was saved in.
        :rtype: :class:`list[int]`

        .. note::
            The format of the dict must follow this pattern::

            {"channel_id": int, "data": {The normal data you want to send.}}
        
        :raw-html:`<br />`

    .. py:method:: get(message_id, channel_id)

        Get the data from a given message.

        :param int message_id: The id of the message to get the data from
        :type message_id: :class:`int`
        :param int channel_id: The channel to get the data from
        :type channel_id: :class:`int`
        :return: Data
        :rtype: :class:`dict`

        :raw-html:`<br />`

    .. py:method:: getf(message_id, field, channel_id)

        Get only one data field from the given message.

        :param int message_id: The id of the message to get the data from
        :type message_id: :class:`int`
        :param str field: The field name from which the data will be taken.
        :type field: :class:`str`
        :param int channel_id: The channel to get the data from
        :type channel_id: :class:`int`
        :return: The field value
        :rtype: :class:`str`

        :raw-html:`<br />`

    .. py:method:: edit(data, id, channel_id)

        Edit a given message.

        :param dict data: The data which will be used to update the embed message
        :type data: :class:`dict`
        :param int id: The id of the message to update
        :type id: :class:`int`
        :param int channel_id: The channel to edit the data in
        :type channel_id: :class:`int`

        :raw-html:`<br />`

    .. py:method:: search(ids, field, channel_ids)

        Searches a field value in multiple messages and channels and returns all the results.

        :param list ids: Ids in which to search the data in
        :type id: :class:`list[int]`
        :param str field: A field name
        :type field: :class:`str`
        :param int channel_ids: The channel to search the data in
        :type channel_ids: :class:`list[int]`
        :return: A list of dicts with message id and field value
        :rtype: :class:`list[dict]` or :class:`None`
        
        :raw-html:`<br />`

Data Types
----------

.. py:class:: discordDBPlus.models.Data

    A superset class of python dictionaries, which also supports accessing of its keys using . syntax.

Exceptions
----------

.. py:class:: discordDBPlus.models.FieldError

    Raised when a specified Field doesn't exists in a given message data