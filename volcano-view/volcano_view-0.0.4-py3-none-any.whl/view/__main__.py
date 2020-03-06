import argparse
import sys
import logging
import socketserver
import zipfile

from .web_exc import WebException
from .base_web_handler import BaseWebHandler
from .web_handler import WebHandler

_LOG_LEVELS = {
    'all': logging.NOTSET,
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warn': logging.WARNING,
    'error': logging.ERROR,
}


def configure_logger(env):
    assert env.log, env

    msg_fmt = '%(levelname)s %(asctime)s [%(name)s] %(message)s'

    if env.log == 'none':
        logging.disable(logging.CRITICAL)
    else:
        lev = _LOG_LEVELS.get(env.log, None)
        if lev is None:
            raise SystemExit('Invalid value for logging level: "{}". Use all,debug,info,warn,error.'.format(env.log))
        logging.basicConfig(level=lev, format=msg_fmt)

    logging.addLevelName(logging.CRITICAL, '!!!')
    logging.addLevelName(logging.ERROR, '!! ')
    logging.addLevelName(logging.WARNING, '!  ')
    logging.addLevelName(logging.INFO, '   ')
    logging.addLevelName(logging.DEBUG, '   ')


def configure_my_args(parser):
    parser.add_argument('-l', '--log', help='Log level', default='info', choices=list(_LOG_LEVELS.keys()))
    parser.add_argument('-i', '--iface', help='Listen interface', default='')
    parser.add_argument('-w', '--wd', help='Working directory', default='')
    parser.add_argument('-p', '--port', help='Listen port', default=8080, type=int)
    parser.add_argument('-s', '--sim', help='Enable simulation', action='store_true')
    parser.add_argument('--nozip', help='Disable zipped resources', action='store_true')


class LoadException(Exception):
    pass


def main() -> int:
    zip_arch = None
    try:
        # Args
        arg_parser = argparse.ArgumentParser()
        configure_my_args(arg_parser)
        env = arg_parser.parse_args()

        # Logging
        configure_logger(env)
        log = logging.getLogger('web')

        if env.sim:
            log.warning('Data will be simulated')
            from .reader_sim import SimulationReader            # pylint: disable=import-outside-toplevel
            WebHandler.Reader = SimulationReader(env, log)
        else:
            log.info('Data connection to MySQL will be used')
            from .reader_ecosui_db import EcoSUIReader          # pylint: disable=import-outside-toplevel
            WebHandler.Reader = EcoSUIReader(env, log)

        if env.nozip:
            log.info('Zipped web resources disabled, using source folder')
        else:
            try:
                zip_arch = zipfile.ZipFile('www.zip')
                with zip_arch.open('{}/index.html'.format(BaseWebHandler.StaticPath), 'r'):
                    log.info('Zip file with web resources tested ok')    # test open
            except Exception as ex:
                log.error(ex)
                return 1
                
            BaseWebHandler.WebPackage = zip_arch

        # reload вызывается также в runtime, поэтому он wx. 
        # попытка загрузки при старте нужна для проверки конфигурации
        try:
            WebHandler.Reader.reload_wx()
        except WebException as ex:
            log.error(ex)
            return 1

        try:
            log.info('Listen on %s:%s', env.iface, env.port)

            with socketserver.TCPServer((env.iface, env.port), WebHandler) as httpd:    # pylint: disable=not-context-manager
                httpd.serve_forever()

            return 0

        except (Warning, LoadException) as ex:
            log.error(ex)
            return 1
            
    finally:
        logging.shutdown()
        
        if zip_arch:
            try:
                zip_arch.close()
            except:             # pylint: disable=bare-except
                pass


if __name__ == '__main__':
    sys.exit(main())
