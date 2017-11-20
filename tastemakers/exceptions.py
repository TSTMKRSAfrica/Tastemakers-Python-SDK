__author__ = 'Ebot Tabi'

class BaseTastemakersClientError(Exception):
    """
    Base class for all Tastemakers Client errors.
    """
    def __str__(self):
        # all sub-classes should set self._message in their initializers
        return self._message


class TastemakersApiError(BaseTastemakersClientError):
    def __init__(self, api_error):
        super(TastemakersApiError, self).__init__(api_error)
        self.api_error = api_error
        self._message = "Error from Tastemakers API. Details:\n Message: {}\nCode: "\
                        "{}".format(
            api_error["message"], api_error["error_code"]
        )