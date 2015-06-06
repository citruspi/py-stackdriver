import datetime


class Maintenance(object):

    __source = None
    __instance = None

    def __init__(self, source, instance):
        self.__source = source
        self.__instance = instance

    @property
    def is_enabled(self):
        return self.__source['maintenance']

    @property
    def reason(self):
        return self.__source.get('reason', None)

    @property
    def user(self):
        return self.__source.get('username', None)

    @property
    def expires(self):
        try:
            timestamp = self.__source['schedule']['expires_epoch']
            return datetime.datetime.fromtimestamp(timestamp)
        except KeyError:
            return None


class Instance(object):

    __source = None
    __client = None

    def __init__(self, source, client):
        self.__source = source
        self.__client = client

    @property
    def id(self):
        return self.__source['id']

    @property
    def instance_id(self):
        return self.__source['instance_id']

    @property
    def name(self):
        return self.__source['name']

    @property
    def provider(self):
        return self.__source['provider']

    @property
    def provider_region(self):
        return self.__source['provider_region']

    @property
    def provider_zone(self):
        return self.__source['provider_zone']

    @property
    def provider_account(self):
        return self.__source['provider_account']

    @property
    def instance_type(self):
        return self.__source['instance_type']

    @property
    def interfaces(self):
        return self.__source['interfaces']

    @property
    def image(self):
        return self.__source['image']

    @property
    def tags(self):
        return {tag['name']: tag['value'] for tag in self.__source['tags']}

    @property
    def launched(self):
        timestamp = self.__source['launch_epoch']

        return datetime.datetime.fromtimestamp(timestamp)

    @property
    def last_monitored(self):
        timestamp = self.__source['monitor_epoch']

        return datetime.datetime.fromtimestamp(timestamp)

    @property
    def state(self):
        return self.__source['state']

    @property
    def agent_version(self):
        return self.__source['agent_version']

    @property
    def extractor_version(self):
        return self.__source['extractor_version']
