from urllib2 import urlopen
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
        self.user = None

    def _get_oauth_url(self, endpoint):
        prefix = 'http://'
        return prefix + self.OAUTH_HOST + self.OAUTH_ROOT + endpoint

    def apply_auth(self, url, method, headers, parameters):
        request = oau
