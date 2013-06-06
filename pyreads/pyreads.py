import oauth2 as oauth
from auth import OAuthHandler
from endpoints import api_table
import re
import urllib
import urlparse

class PyReads(object):
    def __init__(self, app_key = None, app_secret = None,
                 oauth_token = None, oauth_token_secret = None,
                 headers = None, proxies = None):
        self.api_url = 'http://www.goodreads.com'
        self.auth_handler = OAuthHandler(app_key, app_secret, oauth_token, oauth_token_secret)
                            
        self.client = oauth.Client(self.auth_handler.consumer,
                                   self.auth_handler.access_token,
                                   proxy_info = proxies)
        self.headers = headers

        def setFunction(key):
            return lambda **kwargs: self._constructFunction(key, **kwargs)
        
        for key in api_table.keys():
            self.__dict__[key] = setFunction(key)

    def _update_query(self, query_string):
        queries = [query.split('=', 1) if '=' in query else [query, ''] for query in query_string.split('&') if query]
        params = {}
        for key, value in queries:
            if value == 'None':
                continue
            params[key] = value

        return urllib.urlencode(params)

    def _constructFunction(self, api_call, **kwargs):
        fn = api_table[api_call]
        url = re.sub(
            '\{\{(?P<m>[a-zA-Z_]+)\}\}',
            lambda m: "%s" % kwargs.get(m.group(1)),
            self.api_url + fn['url']
        )

        parseResult = list(urlparse.urlparse(url))
        parseResult[4] = self._update_query(parseResult[4])
        url = urlparse.urlunparse(parseResult)
        
        content = self._request(url, method=fn['method'], params=kwargs)

        return content

    def _request(self, url, method = 'GET', params = None):
        print url
        body = urllib.urlencode(params)
        return self.client.request(url, method, body = body, headers = self.headers)

if __name__ == '__main__':
    APP_KEY = ''
    APP_SECRET = ''
    OAUTH_TOKEN = ''
    OAUTH_TOKEN_SECRET = ''

    pyreads = PyReads(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    print pyreads.shelf_list(key = APP_KEY, user_id = '6462529')
