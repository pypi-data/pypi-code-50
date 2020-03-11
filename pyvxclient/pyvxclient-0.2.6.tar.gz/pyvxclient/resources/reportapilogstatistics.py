from pyvxclient.decorators import handle_response, paginate
from pyvxclient.resource import Resource


class ReportApiLogStatistics(Resource):

    @handle_response
    @paginate
    def get(self, start, stop, limit=30, sort=('client_ip', 'name', 'resource', 'method'), q=[], page=1):
        return self.client.report.getReportApiLogStatistics(start=start,
                                                            stop=stop,
                                                            page=page, per_page=limit,
                                                            sort=sort, q=q).response()
