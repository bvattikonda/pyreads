import oauth2 as oauth
import urlparse
import urllib
from error import PyReadsError

class AuthHandler(object):
    def apply_auth(self, url, method, headers, parameters):
        raise NotImplementedError

    def get_user(self):
        raise NotImplementedError

class OAuthHandler(AuthHandler):
    OAUTH_HOST = 'www.goodreads.com'
    OAUTH_ROOT = '/oauth/'
    def __init__(self, consumer_key, consumer_secret):
        self._consumer = oauth.Consumer(consumer_key, consumer_secret)
        self.request_token = None
        self.access_token = None
        self.user = None

    def _get_request_token(self):
        try:
            url = self._get_oauth_url('request_token')
            client = oauth.Client(self._consumer)
            response, content = client.request(url)
            request_token = dict(urlparse.parse_qsl(content))
            return oauth.Token(request_token['oauth_token'],
                               request_token['oauth_token_secret'])
        except Exception, e:
            raise PyReadsError(e)

    def _get_oauth_url(self, endpoint):
        prefix = 'http://'
        return prefix + self.OAUTH_HOST + self.OAUTH_ROOT + endpoint

    def set_request_token(self, key, secret):
        self.request_token = oauth.Token(key, secret)
        
    def set_access_token(self, key, secret):
        self.access_token = oauth.Token(key, secret)

    def get_authorization_url(self):
        """ Get the authorization URL to redirect the user """
        try:
            self.request_token = self._get_request_token()
            url = self._get_oauth_url('authorize')
            parameters = {'oauth_token': self.request_token.key}
            url_parts = list(urlparse.urlparse(url))
            url_parts[4] = urllib.urlencode(parameters)
            return urlparse.urlunparse(url_parts)
        except Exception, e:
            raise PyReadsError(e)
    
    def get_access_token(self, request_token):
        """
        After the user has authorized the request token, get the access token
        with user supplied verifier
        """
        try:
            url = self._get_oauth_url('access_token')
            self.request_token = request_token
            client = oauth.Client(self._consumer, self.request_token)
            response, content = client.request(url, 'POST')
            access_token = dict(urlparse.parse_qsl(content))
            token = oauth.Token(access_token['oauth_token'], 
                                access_token['oauth_token_secret'])
            return token
        except Exception, e:
            raise PyReadsError(e)


if __name__ == '__main__':

    """
        This piece of code shows how to and helps generate the first access
        token which can then be used to work with goodreads API.
    """
    CONSUMER_KEY = 'jTvdwlSsuOOgtmQUw5JoXQ'
    CONSUMER_SECRET = 'AwIKsQWPsYeWQFI2c76r2c2K0i7tKj8aqQEC60IqUQ'
    handler = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    url = handler.get_authorization_url()
    print 'Visit and authorize'
    print url
    accepted = 'n'
    while accepted.lower() == 'n':
        accepted = raw_input('Have you authorized? (y/n)')
        
    request_token = handler.request_token
    handler = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    token = handler.get_access_token(request_token)
    print token