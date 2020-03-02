import boto3


class Paginator:
    def __init__(self, client, operation):
        self.client = client
        self.operation = operation

    def scrape(self):
        paginator = self.client.get_paginator(self.operation)
        response_iterator = paginator.paginate()
        return [response for response in response_iterator]
