import requests
from tastemakers import exceptions

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

    def __init__(self, project_token, base_url=None,
                 api_version=None):
        """ Initializes a TastemakersAfricaApi object

        :param project_token: the Tastemakers Africa project token
        :param base_url: optional, set this to override where API requests
        are sent
        :param api_version: string, optional, set this to override what API
        version is used
        """
        super(TastemakersAfricaApi, self).__init__()
        self.project_token = project_token
        if base_url:
            self.base_url = base_url
        if api_version:
            self.api_version = api_version

    def post_event(self, event):
        """ Posts a single event to the Tastemakers Africa API.

        :param event: an Event to upload
        """
        url = "{}/{}/projects/{}/events/{}".format(self.base_url, self.api_version,
                                            self.project_token,
                                            event.collection_name)
        headers = {"Content-Type": "application/json"}
        payload = event.to_json()
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code != 201:
            error = response.json
            raise exceptions.TastemakersAfricaApiError(error)

