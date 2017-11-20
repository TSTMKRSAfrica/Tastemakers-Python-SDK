__author__ = 'Ebot Tabi'

class BaseStore(object):
    """
    A store strategy is responsible for persisting a given data
    somewhere (i.e. directly to Tastemakers, a local cache etc.)
    """

    def persist(self, data):
        """Store the given data somewhere.

        :param data: the data to persist
        """
        raise NotImplementedError()


class DirectStore(BaseStore):
    """
    A Store strategy that saves directly to Tastemakers and bypasses any local
    cache.
    """

    def __init__(self, api):
        """ Initializer for DirectPersistenceStrategy.

        :param api: the Tastemakers Api object used to communicate with the Tastemakers API
        """
        super(DirectPersistenceStrategy, self).__init__()
        self.api = api

    def persist(self, data):
        """ Posts the given data directly to the Tastemakers API.

        :param data: an Event to persist
        """
        self.api.post(data)


class RedisStore(BaseStore):
    """
    A Store strategy that persists events to Redis for later processing.

    Not yet implemented.
    """
    pass


class FileStore(BaseStore):
    """
    A Store strategy that persists events to the local file system for
    later processing.

    Not yet implemented.
    """
    pass
