class Data(dict):
    """Actually a superset class of python dictionaries, which also supports accessing of its keys using . syntax.

    Extra Attributes
    ----------------
    created_at : datetime.datetime
        The time this data was created in UTC.

    """

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, item):
        data = self[str(item)]
