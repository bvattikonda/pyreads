import oauth2 as oauth

class AuthHandler(object):
    def apply_auth(self, url, method, headers, parameters):
        raise NotImplementedError

    def get_user(self):
        raise NotImplementedError

class OAuthHandler(AuthHandler):
    OAUTH_HOST = 'www.goodreads.com'
    OAUTH_ROOT = '/'
    def __init__(self, consumer_key, consumer_secret):
        self._consumer = oauth.Consumer(consumer_key, consumer_secret)
        self.request_token = None
        self.access_token = None
        self.user = None

    def _get_oauth_url(self, endpoint):
        prefix = 'http://'
        return prefix + self.OAUTH_HOST + self.OAUTH_ROOT + endpoint

    def set_access_token(self, key, secret):
        self.access_token = oauth.Token(key, secret)

    def apply_auth(self, url, method, headers, parameters):
        request = oauth.Request.from_consumer_and_token(self._consumer, 
                                                        http_url = url,
                                                        http_method = method, 
                                                        token = self.access_token, 
                                                        parameters = parameters)
        request.sign_request(self._sigmethod, self._consumer, self.access_token)
        headers.update(request.to_header())

if __name__ == '__main__':

    """
        This piece of code shows how to and helps generate the first access
        token which can then be used to work with goodreads API.
    """
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    handler = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
