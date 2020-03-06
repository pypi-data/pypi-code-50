def generate_row_data(results):
    """Yield headers and data from a Google Analytics report.

    Args:
        results (dict): Google Analytics statistics results.

    Yields:
        list: CSV-style headers and data from the report.
    """
    report = results.get("reports")[0]
    column_header = report.get('columnHeader', {})

    metric_headers = column_header.get(
        'metricHeader', {}
    ).get('metricHeaderEntries', [])

    headers = column_header.get('dimensions', []).copy()
    headers.extend(header.get("name") for header in metric_headers)
    yield headers

    for row in report.get('data', {}).get('rows', []):
        yield row['dimensions'] + row['metrics'][0]['values']


def build_ga_request(
        view_id,
        start_date,
        end_date,
        metrics,
        dimensions,
        filters=None
):
    """Build a request body for querying Google Analytics.

    Args:
        view_id (str): View ID associated with GA account.
        start_date (str): in format YYYY-mm-dd.
        end_date (str): in format YYYY-mm-dd.
        metrics (list): Specific metrics to report.
        dimensions (list): How to break down metrics.
        filters (str): Path to filter dimensions by.

    Returns:
        dict: Request body used to query Google Analytics.
    """
    request_dict = {
        'viewId': view_id,
        'dateRanges': [{'startDate': start_date, 'endDate': end_date}],
        'metrics': [{'expression': metric} for metric in metrics],
        'dimensions': [{'name': dimension} for dimension in dimensions],
    }

    if filters:
        filter_set = [{'dimension_name': 'ga:pagePath', 'expressions': filters}]
        request_dict.update(dimensionFilterClauses=[{'filters': filter_set}])

    return {'reportRequests': [request_dict]}


def get_statistics(service, request):
    return service.reports().batchGet(body=request).execute()
