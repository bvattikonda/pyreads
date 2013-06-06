import oauth2 as oauth
from auth import OAuthHandler

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

    def request(self, uri, method = 'GET'):
        return self.client.request(self.api_url + uri, method, headers = self.headers)

if __name__ == '__main__':
    APP_KEY = 'jTvdwlSsuOOgtmQUw5JoXQ'
    APP_SECRET = 'AwIKsQWPsYeWQFI2c76r2c2K0i7tKj8aqQEC60IqUQ'
    OAUTH_TOKEN = 'RIAfo67nmhulCFS1rjebtA'
    OAUTH_TOKEN_SECRET = 'SugrKz7NlUyifuWYRvd9zSGZzD4fpr5aD1ktTgvjBA'

    pyreads = PyReads(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    print pyreads.request('/api/auth_user')
