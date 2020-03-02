import argparse
import requests
import logging
import lcogt_logging
import datetime

logger = logging.getLogger('sep-service')

SEP_PARAMETER_ARGS = ['threshold', 'deblend', 'deblend_n_threshold', 'min_area', 'noise_model']


def setup_logging(log_level):
    logger.setLevel(log_level)
    handler = logging.StreamHandler()
    handler.setLevel(log_level)
    handler.setFormatter(lcogt_logging.LCOGTFormatter())
    logger.addHandler(handler)


def parse_args():
    parser = argparse.ArgumentParser(description='Perform source extraction via the LCO sep service',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('site', help='3-letter LCO site string, e.g. lsc')
    parser.add_argument('camera', help='4-letter LCO camera string e.g. fa15')
    parser.add_argument('dayobs', help='Dayobs in YYYYmmdd format, e.g 20200214')
    parser.add_argument('auth_token', help='Archive API authentication token')

    # Source extraction service solve parameters:
    parser.add_argument('--sep-mode', dest='sep_mode', help='Source extraction service mode. See sep service docs for details.'
                        , choices=['DEFAULT', 'CUSTOM'], default='DEFAULT', type=str)
    parser.add_argument('--threshold', dest='threshold', help='SExtractor threshold value'
                        , default=10.0, type=float)
    parser.add_argument('--deblend', dest='deblend', help='SExtractor deblend value',
                        default=0.005, type=float)
    parser.add_argument('--deblend-n-threshold', dest='deblend_n_threshold', help='Number of thresholds to be used when deblending objects.',
                        default=32, type=int)
    parser.add_argument('--min-area', dest='min_area', help='SExtractor minarea value',
                        default=9, type=int)
    parser.add_argument('--noise-model', dest='noise_model', help='Noise model to use. See source extraction service docs for details.',
                        choices=['PIXELMODEL', 'GLOBALRMS'], default='PIXELMODEL', type=str)

    # Optional CLI arguments
    parser.add_argument('--log-level', dest='log_level', default='INFO', help='Logging level to be displayed',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
    parser.add_argument('--api-frames-endpoint', dest='api_frames_endpoint', help='Archive API frames endpoint',
                        default='https://archive-api.lco.global/frames/')
    parser.add_argument('--source-extraction-endpoint', dest='source_extraction_endpoint', help='LCO sep service endpoint',
                        default='http://source-extraction.lco.gtn')
    parser.add_argument('--elasticsearch-endpoint', dest='elasticsearch_endpoint', help='LCO elasticsearch endpoint',
                        default='http://elasticsearch.lco.gtn:9200/')
    parser.add_argument('--elasticsearch-index', dest='elasticsearch_index', help='Index to post source extraction output to',
                        default='source-extraction')

    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    setup_logging(args.log_level)

    dayobs = datetime.datetime.strptime(args.dayobs, "%Y%m%d")

    authorization_header = {'Authorization': f'Token {args.auth_token}'}
    frame_search_url = args.api_frames_endpoint + f'?SITEID={args.site}&INSTRUME={args.camera}&DAY_OBS={dayobs.strftime("%Y-%m-%d")}' \
                       + '&RLEVEL=91&OBSTYPE=EXPOSE'

    frames = requests.get(frame_search_url, headers=authorization_header).json().get('results')

    if frames is None:
        logger.error("No frames found in the archive matching the site/camera/dayobs provided! Exiting...")
        exit(1)

    for frame in frames:
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
            logger.error(f"Error in image solve. Status code: {response.status_code} Source extraction service encountered an error. {e}", extra={"tags": payload})
            continue

        # Handle unsuccessful solves
        if not response_json['success']:
            logger.error(f"Source extraction service reported a failure.", extra={"tags": response_json})
            continue

        logger.info("Source extraction complete. Posting result to elasticsearch", extra={"tags": {"basename": basename}})
        # build up elasticsearch record from input data + response
        elasticsearch_data = response_json
        for key in payload.keys():
            elasticsearch_data[key] = payload[key]

        #add DATE-OBS and extraction date
        elasticsearch_data['DATE-OBS'] = frame['DATE_OBS']
        elasticsearch_data['extraction_date'] = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        try:
            response = requests.post(args.elasticsearch_endpoint + args.elasticsearch_index +'/doc/', json=elasticsearch_data)
            response.raise_for_status()
        except requests.HTTPError as e:
            logger.error(f"Error posting result to elasticsearch: {e}", extra={"tags": {"basename": basename}})



