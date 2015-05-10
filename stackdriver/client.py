import os
import ConfigParser

class Client(object):

    authorization = None

    def __init__(self, username=None, api_key=None):
        if username is None:
            username = os.environ.get('STACKDRIVER_USERNAME', None)

        if api_key is None:
            api_key = os.environ.get('STACKDRIVER_API_KEY', None)

        if username is None or api_key is None:
            config = ConfigParser.RawConfigParser()
            config.read(os.path.expanduser('~/.stackdriver'))

            if username is None:
                username = config.get('Credentials', 'username')

            if api_key is None:
                api_key = config.get('Credentials', 'api_key')

        self.authorization = (username, api_key)

