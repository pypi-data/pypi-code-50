import json
import logging
from time import sleep
try:
    import thread
except ImportError:
    import _thread as thread
import websocket

logger = logging.root

seqno = 0
MAX_RETRIES = 5

STATUS = ['DONE', 'IN_PROGRESS']


class LoreException(Exception):
    pass


class Spyglass:
    _url = None
    _ws = None
    _username = None
    _password = None

    dataset_id = None
    seqno = 0

    results = {}

    def __init__(self, url, username, password, dataset_id=None):
        self._url = url
        websocket.enableTrace(False)
        self._ws = websocket.WebSocketApp(url,
                                          on_message=self.on_message,
                                          on_error=self.on_error,
                                          on_close=self.on_close)
        self._ws.on_open = self._on_open
        self._username = username
        self._password = password
        self.dataset_id = dataset_id
        self._connecting = True
        thread.start_new_thread(self._ws.run_forever, ())
        # wait for conection and auth
        while self._connecting:
            sleep(0.1)

        if not self.connected:
            raise Exception("Could not connect")

        # todo handle dataset

    def _on_open(self):
        def _auth(*args):
            self._ws.send(
                '{} auth {} {}'.format(self.seqno, self._username,
                                       self._password))
            while True:
                sleep(0.1)
                if self.seqno in self.results:
                    if self.results[self.seqno]['message'] == 'Success':
                        self.connected = True
                    else:
                        self.connected = False
                    self._connecting = False
                    break

        thread.start_new_thread(_auth, ())

    def on_message(self, message_string):
        message = json.loads(message_string)
        if "message" in message and message["message"] == 'Stream Start':
            self.results[message['seqno']] = [message]
        elif message['seqno'] in self.results:
            self.results[message['seqno']].append(message)
        else:
            self.results[message['seqno']] = message

    def on_error(self, error):
        raise Exception(error)

    def on_close(self):
        pass

    @staticmethod
    def _build_command(command, positional_args=None, keyword_args=None):
        build_command = "{}".format(command)
        if positional_args:
            build_command += " {}".format(' '.join(positional_args))
        if keyword_args:
            build_command += " {}".format(' '.join(
                ['--{} {}'.format(k, v) for k, v
                 in keyword_args.items() if v is not None]))
            build_command += " {}".format(' '.join(
                ['--{}'.format(k, v) for k, v
                 in keyword_args.items() if v is None]))
        return build_command

    def sync_cmd(self, command, positional_args=None, keyword_args=None,
                 retry=0):
        self.seqno += 1
        seqno = self.seqno
        final_command = self._build_command(command,
                                            positional_args,
                                            keyword_args)
        if retry > MAX_RETRIES:
            raise Exception('Could not run command {}'.format(final_command))

        logging.info(
            'sending sync command: {} {}'.format(seqno, final_command))
        # if lost connection try to reconnect then re-execute command
        result = {'seqno': None}
        try:
            self._ws.send("{} {}".format(seqno, final_command))
            while self.seqno not in self.results:
                sleep(0.1)
            result = self.results[self.seqno]
        except Exception as e:
            logger.warn(e)
            return self.sync_cmd(command, positional_args, keyword_args,
                                 retry + 1)

        # if no session, init session first
        if 'message' in result and result['message'].startswith(
                'ERROR: Without a session') and self.dataset_id:
            self.get_session()
            return self.sync_cmd(command, positional_args, keyword_args,
                                 retry + 1)
        logger.info("got results for seqno: {}".format(self.seqno))
        logger.info(result)
        if hasattr(result, 'message') and 'ERROR:' in result['message']:
            raise LoreException(result['message'])

        return (STATUS[0], seqno, result)

    def streaming_cmd(self, command, positional_args=None, keyword_args=None):
        """ return an iterator for streaming data"""
        self.seqno += 1
        seqno = self.seqno
        final_command = self._build_command(command,
                                            positional_args,
                                            keyword_args)
        self._ws.send("{} {}".format(seqno, final_command))
        while True:
            if self.seqno in self.results and len(
                    self.results[self.seqno]) != 0:
                result = self.results[self.seqno].pop(0)
                if result['message'] == 'Stream Start':
                    logger.info('stream starting')
                elif self.seqno == result['seqno'] and result[
                    'message'].startswith('ERROR'):
                    raise Exception(result['message'])
                elif result['message'] == 'Stream Stop':
                    break
                elif self.seqno == result['seqno'] and result['message']:
                    yield (STATUS[0], seqno, result)
                else:
                    raise Exception(result)

    def async_cmd(self, command, positional_args=None, keyword_args=None):
        self.seqno += 1
        seqno = self.seqno
        final_command = self._build_command(command,
                                            positional_args,
                                            keyword_args)
        logging.info(
            'sending async command: {} {}'.format(seqno, final_command))
        self._ws.send("{} {}".format(self.seqno, final_command))
        return (STATUS[1], seqno, {})

    def get_session(self):
        if not self.dataset_id:
            raise Exception('Need a dataset_id to get a session')
        self.sync_cmd('session', [self.dataset_id])
