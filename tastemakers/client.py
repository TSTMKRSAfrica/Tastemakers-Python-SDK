import copy
import json
from tastemakers import exceptions
from tastemakers.api import TastemakersAfricaApi

__author__ = 'Ebot Tabi'


class Experience(object):
    """
    Experience object in Tastemakers Platform
    """

    def __init__(self):
        """ Initializes a new Experience.
        """
        pass


class TastemakersClient(object):
    """
    The Tastemakers Client is the main object to use to interface with Tastemakers. It
    requires an API key.
    """

    def __init__(self, api_key):
        """ Initializes a TastemakersClient object.

        :param api_key: the API key
        """
        self.api_key = api_key
        self.tastemakers_africa_api = TastemakersAfricaApi(self.api_key)

        # do some validation
        if not self.api_key or not isinstance(self.api_key, basestring):
            raise exceptions.InvalidApiKeyError(self.api_key)

    def get_experiences(self):
        return self.tastemakers_africa_api.get("experiences")
