import oauth2

class PyReads(object):
    def __init__(self, app_key = None, app_secret = None,
                 oauth_token = None, oauth_secret = None,
                 headers = None):
    """
        Instantiates the instance of PyReads. Takes optional arguments.

        :param app_key: (optional) Your developer key
        :param app_secret: (optional) Your developer secret
        :param oauth_token: (optional) Used to make authenticated calls on behalf of users
        :param oauth_secret: (optional) Used to make authenticated calls on behalf of users
        :param headers: HTTP headers to be sent along with every request.
    """
    

    self.headers = headers

