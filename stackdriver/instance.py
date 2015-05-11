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
    def launch_epoch(self):
        return self.__source['launch_epoch']

    @property
    def monitor_epoch(self):
        return self.__source['monitor_epoch']

    @property
    def state(self):
        return self.__source['state']

    @property
    def agent_version(self):
        return self.__source['agent_version']

    @property
    def extractor_version(self):
        return self.__source['extractor_version']

