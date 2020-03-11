from pyvxclient.decorators import handle_response
from pyvxclient.resource import Resource


class Place(Resource):

    @handle_response
    def get(self, customer):
        return self.client.customer.getPlace(customer=customer).response()
