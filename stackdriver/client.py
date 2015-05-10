import os

class Client(object):

    authorization = None

    def __init__(self, username=None, api_key=None):
        if username is None:
            username = os.environ.get('STACKDRIVER_USERNAME', None)

        if api_key is None:
            api_key = os.environ.get('STACKDRIVER_API_KEY', None)

        self.authorization = (username, api_key)

