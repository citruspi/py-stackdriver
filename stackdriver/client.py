import os
import ConfigParser
import requests
import json
from instance import Instance

class Client(object):

    authorization = None

    api_location = 'https://api.stackdriver.com'
    api_version = 'v0.2'

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

    def request(self, method='GET', endpoint=None, body=None):
        headers = {}

        headers['x-stackdriver-apikey'] = self.authorization[1]
        headers['Content-Type'] = 'application/json'

        if method in ['POST', 'PUT']:
            if not body:
                body = {}

            body['username'] = self.authorization[0]

            data=json.dumps(body)

        uri = '/'.join([self.api_location, self.api_version, endpoint])

        if method=='GET':
            return requests.get(uri, headers=headers)
        elif method=='POST':
            return requests.post(uri, headers=headers, data=data)
        elif method=='PUT':
            return requests.put(uri, headers=headers, data=data)

    def get_all_instances(self):
        response = self.request(endpoint='instances').json()

        instances = [Instance(source=instance, client=self) for instance in
                                                            response['data']]

        return instances
