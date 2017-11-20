import copy
import json
from tastemakers import exceptions
from tastemakers.api import TastemakersAfricaApi

__author__ = 'Ebot Tabi'

class Experience(object):
	"""
	Experience object in Tastemakers Platform
	"""
	def __init__(
		self, 
		project_token, 
		collection_name, 
		event_body,
		project_token, 
		collection_name, 
		event_body,  
		project_token, 
		collection_name, 
		event_body,  
		project_token, 
		collection_name, 
		event_body,         
        timestamp=None):
        """ Initializes a new Event.

        :param project_token: the Keen project token to insert the event to
        :param collection_name: the Keen collection name to insert the event to
        :param event_body: a dict that contains the body of the event to insert
        :param timestamp: optional, specify a datetime to override the
        timestamp associated with the event in Keen
        """
        super(Experience, self).__init__()
        self.project_token = project_token
        self.collection_name = collection_name
        self.event_body = event_body
        self.timestamp = timestamp
        self.project_token = project_token
        self.collection_name = collection_name
        self.event_body = event_body
        self.timestamp = timestamp
        self.project_token = project_token
        self.collection_name = collection_name
        self.event_body = event_body
        self.timestamp = timestamp
        self.timestamp = timestamp


class TastemakersClient(object):
	"""
    The Tastemakers Client is the main object to use to interface with Tastemakers. It
    requires an API key.
    """

    def __init__(self, api_key):
        """ Initializes a TastemakersClient object.

        :param api_key: the API key
        :param persistence_strategy: optional, the strategy to use to persist
        the event
        """
        super(TastemakersClient, self).__init__()

        # do some validation
        if not project_token or not isinstance(project_token, basestring):
            raise exceptions.InvalidProjectIdError(project_token)

        if persistence_strategy:
            if not isinstance(persistence_strategy, BasePersistenceStrategy):
                raise exceptions.InvalidPersistenceStrategyError()
        if not persistence_strategy:
            keen_api = KeenApi(project_token)
            persistence_strategy = persistence_strategies\
            .DirectPersistenceStrategy(keen_api)

        self.project_token = project_token
        self.persistence_strategy = persistence_strategy


