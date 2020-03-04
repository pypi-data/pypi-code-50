import logging
import requests
import datetime

logger = logging.getLogger('sep-service')


class SourceExtractionException(Exception):
    pass


def perform_source_extraction(frame, args):
    basename = frame['basename']
    logger.info(f"Performing source extraction on {basename}.")
    payload = {'basename': basename,
               'mode': args.sep_mode,
               'threshold': args.threshold,
               'deblend': args.deblend,
               'deblend_n_threshold': args.deblend_n_threshold,
               'min_area': args.min_area,
               'noise_model': args.noise_model}
    try:
        response = requests.post('http://source-extraction.lco.gtn/image/', json=payload)
        response.raise_for_status()
        response_json = response.json()
    except requests.HTTPError as e:
        logger.error(
            f"Error in image solve. Status code: {response.status_code} Source extraction service encountered an error. {e}",
            extra={"tags": payload})
        raise SourceExtractionException

    # Handle unsuccessful solves
    if not response_json['success']:
        logger.error(f"Source extraction service reported a failure.", extra={"tags": response_json})
        raise SourceExtractionException

    logger.info("Source extraction complete. Posting result to elasticsearch", extra={"tags": {"basename": basename}})
    # build up elasticsearch record from input data + response
    elasticsearch_data = response_json
    for key in payload.keys():
        elasticsearch_data[key] = payload[key]

    # add DATE-OBS and extraction date
    elasticsearch_data['extraction_date'] = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    elasticsearch_data['num_sources'] = len(elasticsearch_data.get('FLUX'))

    try:
        response = requests.post(args.elasticsearch_endpoint + args.elasticsearch_index + '/doc/',
                                 json=elasticsearch_data)
        response.raise_for_status()
    except requests.HTTPError as e:
        logger.error(f"Error posting result to elasticsearch: {e}", extra={"tags": {"basename": basename}})
        raise SourceExtractionException


def get_dayobs_between_dates(start_datetime, end_datetime):
    """
    Given start and end dates, generate a list of dayobs (inclusive)
    e.g for start='2019-05-07' and end='2019-05-10',
    return ['20190507', '20190508', ..., '20190510']
    """
    return [(start_datetime + datetime.timedelta(days=offset)).strftime('%Y-%m-%d') for offset in
            range(0, (end_datetime - start_datetime).days + 1)]
