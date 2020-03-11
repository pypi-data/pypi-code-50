from pyvxclient.decorators import handle_response, paginate
from pyvxclient.resource import Resource


class ReportObjectConnections(Resource):

    @handle_response
    @paginate
    def get(self, network_operator=None, date=None, limit=30, sort=('created',), q=[], page=1):
        return self.client.report.getReportObjectConnections(network_operator=network_operator,
                                                             date=date,
                                                             page=page, per_page=limit,
                                                             sort=sort, q=q).response()
