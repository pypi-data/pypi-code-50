import argparse
import requests
import logging
import lcogt_logging
import datetime

from sep_service_caller import utils, settings

logger = logging.getLogger('sep-service')

SEP_PARAMETER_ARGS = ['threshold', 'deblend', 'deblend_n_threshold', 'min_area', 'noise_model']


def setup_logging(log_level):
    logger.setLevel(log_level)
    handler = logging.StreamHandler()
    handler.setLevel(log_level)
    handler.setFormatter(lcogt_logging.LCOGTFormatter())
    logger.addHandler(handler)


def parse_args():
    parser = argparse.ArgumentParser(description='Perform source extraction via the LCO source extraction service',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    subparsers = parser.add_subparsers(help='sep-service sub-commands', dest='command')
    # basename subparser
    basename_parser = subparsers.add_parser('file', help='Specify a basename to perform source extraction on')
    basename_parser.add_argument('basename', help='Basename of image to perform source extraction on.')
    basename_parser.add_argument('auth_token', help='Archive API authentication token')


    # dayobs subparser
    dayobs_parser = subparsers.add_parser('dates', help='Specify a site/camera/date range to perform source extractions on.')
    dayobs_parser.add_argument('site', help='3-letter LCO site string, e.g. lsc')
    dayobs_parser.add_argument('camera', help='4-letter LCO camera string e.g. fa15')
    dayobs_parser.add_argument('dayobs_start', help='Dayobs start in YYYYmmdd format, e.g 20200214')
    dayobs_parser.add_argument('dayobs_end', help='Dayobs end in YYYYmmdd format, e.g 20200215')
    dayobs_parser.add_argument('auth_token', help='Archive API authentication token')

    # Add all optional parameters to each parser - they are the same for both
    defined_subparsers = [basename_parser, dayobs_parser]
    for subparser in defined_subparsers:
        # Source extraction service solve parameters:
        subparser.add_argument('--sep-mode', dest='sep_mode',
                               help='Source extraction service mode. See sep service docs for details.'
                               , choices=['DEFAULT', 'CUSTOM'], default='DEFAULT', type=str)
        subparser.add_argument('--threshold', dest='threshold', help='SExtractor threshold value'
                               , default=10.0, type=float)
        subparser.add_argument('--deblend', dest='deblend', help='SExtractor deblend value',
                               default=0.005, type=float)
        subparser.add_argument('--deblend-n-threshold', dest='deblend_n_threshold',
                               help='Number of thresholds to be used when deblending objects.',
                               default=32, type=int)
        subparser.add_argument('--min-area', dest='min_area', help='SExtractor minarea value',
                               default=9, type=int)
        subparser.add_argument('--noise-model', dest='noise_model',
                               help='Noise model to use. See source extraction service docs for details.',
                               choices=['PIXELMODEL', 'GLOBALRMS'], default='PIXELMODEL', type=str)

        # Optional CLI arguments
        subparser.add_argument('--log-level', dest='log_level', default='INFO', help='Logging level to be displayed',
                               choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
        subparser.add_argument('--api-frames-endpoint', dest='api_frames_endpoint', help='Archive API frames endpoint',
                               default='https://archive-api.lco.global/frames/')
        subparser.add_argument('--source-extraction-endpoint', dest='source_extraction_endpoint',
                               help='LCO sep service endpoint',
                               default='http://source-extraction.lco.gtn')
        subparser.add_argument('--elasticsearch-endpoint', dest='elasticsearch_endpoint',
                               help='LCO elasticsearch endpoint',
                               default='http://elasticsearch.lco.gtn:9200/')
        subparser.add_argument('--elasticsearch-index', dest='elasticsearch_index',
                               help='Index to post source extraction output to',
                               default='source-extraction')

    args = parser.parse_args()

    return args


def main():
    args = parse_args()
    setup_logging(args.log_level)

    authorization_header = {'Authorization': f'Token {args.auth_token}'}

    # if we are using the file subcommand
    if args.command == 'file':
        basename_search_url = args.api_frames_endpoint + settings.BASENAME_SEARCH.format(args.basename)
        logger.info("Gathering frame metadata from archive.", extra={"tags": {"basename":args.basename}})
        frame = requests.get(basename_search_url, headers=authorization_header).json().get('results')[0]
        if frame is None:
            logger.error("No frames found in the archive matching the basename provided! Exiting...")
            exit(1)
        try:
            utils.perform_source_extraction(frame, args)
        except utils.SourceExtractionException:
            logger.error(f"Source extraction failed on file {args.basename}")
    # else, user has specified the date range sub-command
    else:
        dayobs_start = datetime.datetime.strptime(args.dayobs_start, "%Y%m%d")
        dayobs_end = datetime.datetime.strptime(args.dayobs_end, "%Y%m%d")

        if dayobs_start > dayobs_end:
            logger.error("Dayobs range invalid. Please try again.")
            exit(1)

        dates = utils.get_dayobs_between_dates(dayobs_start, dayobs_end)
        frames = []

        logger.info(f"Gathering frames from {args.site}, {args.camera}, between {args.dayobs_start} and {args.dayobs_end}")
        for dayobs in dates:
            # loop through each date and gather a set of frames from the archive API
            frame_search_url = args.api_frames_endpoint + settings.FRAME_SEARCH.format(args.site, args.camera, dayobs)
            results = requests.get(frame_search_url, headers=authorization_header).json().get('results')

            if results is None:
                logger.warning(f"No frames found in the archive matching {args.site}, {args.camera}, {dayobs}. Check that the supplied API token is correct.")
            else:
                frames.extend(results)

        if len(frames) != 0:
            logger.info(f"Beginning source extraction on {len(frames)} frames.")
            for frame in frames:
                try:
                    utils.perform_source_extraction(frame, args)
                except utils.SourceExtractionException:
                    logger.error(f"Source extraction failed on file {frame['basename']}. Continuing...")




