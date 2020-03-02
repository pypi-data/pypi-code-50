from aws import paginate
from aws.connection_manager import get_client


class Resource:
    def __init__(self, profiles, regions):
        self.profiles = profiles
        self.regions = regions

    @property
    def clients(self):
        return [
            get_client(profile=profile,
                       region=region,
                       service='cloudformation') for profile in self.profiles
            for region in self.regions
        ]

    def scrape(self):
        for client in self.clients:
            paginator = paginate.Paginator(client, 'describe_stacks')
            return paginator.scrape()
