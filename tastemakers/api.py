import requests
from tastemakers import exceptions
import json

__author__ = 'Ebot Tabi'

class TastemakersAfricaApi(object):
    """
    Responsible for communicating with the Tastemakers Africa API. Used by multiple
    persistence strategies or async processing.
    """

    # the default base URL of the Tastemakers Africa API
    base_url = "http://platform.tastemakersafrica.com/api"
    # the default version of the Tastemakers Africa API
    api_version = "v1"

    def __init__(self, api_key, base_url=None,
                 api_version=None):
        """ Initializes a TastemakersAfricaApi object

        :param api_key: the Tastemakers Africa project token
        :param base_url: optional, set this to override where API requests
        are sent
        :param api_version: string, optional, set this to override what API
        version is used
        """
        super(TastemakersAfricaApi, self).__init__()
        self.api_key = api_key
        if base_url:
            self.base_url = base_url
        if api_version:
            self.api_version = api_version

    def get(self, resource):
    	url = "{0}/{1}/{2}".format(self.base_url, self.api_version, resource)
    	headers = {"Content-Type": "application/json", "X-Tastemakers-Key": self.api_key}
    	response = requests.post(url, data=payload, headers=headers)
    	return response.json



    def post(self, resource, data):
        """ Posts a payload to the Tastemakers Africa Platform API.

        :param data: a payload to upload
        """
        url = "{}/{}/{}/events/".format(self.base_url, self.api_version,
                                            event.collection_name)
        headers = {"Content-Type": "application/json", "X-Tastemakers-Key": self.api_key}
        payload = json.dumps(data)
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code != 201:
            error = response.json
            raise exceptions.TastemakersApiError(error)

