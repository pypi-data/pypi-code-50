#!/usr/bin/env python

# Copyright 2019 Oliver Cope
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import email
import json
import sys
from argparse import ArgumentParser
from getpass import getpass
import asyncio
import logging

from aiohttp import ClientSession
from aiosmtpd.smtp import SMTP
import aiosmtplib

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

argparser = ArgumentParser()
argparser.add_argument('--stdout', help="Log messages to stdout", action='store_true')
argparser.add_argument('--stdout-format', help="Choose format for stdout logging",
                       choices=['text', 'json', 'human'], default='human')
argparser.add_argument('--rewrite-to', '-t', nargs="+",
                       help="Rewrite messages to these addresses")
argparser.add_argument('--bind', '-b', type=str, default="127.0.0.1:2525",
                       help="Bind address, eg '127.0.0.1:2525'")
argparser.add_argument('--relay', '-r', type=str, help="Relay address")
argparser.add_argument('--relay-user', type=str, help="Relay user")
argparser.add_argument('--relay-password', type=str, help="Relay password")
argparser.add_argument('--relay-tls', help="Use TLS", action="store_true",
                       default=False)
argparser.add_argument('--relay-url',
                       help="Relay messages a HTTP POST requests to the given URL.")
argparser.add_argument('--starttls', help="Use STARTTLS", action="store_true",
                       default=False)
argparser.add_argument('--log-envelopes',
                       help="Log all envelopes",
                       action="store_true",
                       default=False)
argparser.add_argument('--log-emails', help="Log all emails", action="store_true",
                       default=False)
argparser.add_argument('--verbose', '-v', action='count', default=0)


class FakeSMTPHandler:

    def __init__(self, relays, rewrite_to, log_envelopes=False, log_emails=False):
        self.relays = relays
        self.rewrite_to = rewrite_to
        self.log_envelopes = log_envelopes
        self.log_emails = log_emails

    async def handle_DATA(self, server, session, envelope):
        peer = session.peer
        mail_from = envelope.mail_from
        rcpt_tos = envelope.rcpt_tos
        data = envelope.content

        logger.info(f"Peer: {peer!r}")
        if self.log_envelopes:
            logger.info(f"New message from <{mail_from}> to <{rcpt_tos}>")

        if self.log_emails:
            logger.info("Message data: \n" + repr(data))

        rcpt_tos = self.rewrite_to or rcpt_tos
        relay_future = asyncio.gather(*(r.send(mail_from, rcpt_tos, data) for r in self.relays))
        await relay_future
        result = relay_future.result()
        for r in result:
            if not r.startswith('2'):
                return r
        return result[0] if result else '250 OK'


class ConfigurableSMTP:

    def __init__(self, host, port, use_tls=False, starttls=False, user=None,
                 password=None):
        self.host = host
        self.port = port
        self.use_tls = use_tls
        self.starttls = starttls
        self.user = user
        self.password = password

    async def connect(self):
        smtp = aiosmtplib.SMTP(self.host, self.port, use_tls=self.use_tls)
        await smtp.connect()
        if self.starttls:
            await smtp.starttls()

        if self.user:
            await smtp.login(self.user, self.password)

        return smtp

    async def send(self, mail_from, rcpt_tos, data):
        smtp = await self.connect()
        await smtp.sendmail(mail_from, rcpt_tos, data)
        return '250 OK'


class HTTPRelay:
    """
    Relay all received emails to an HTTP endpoint.

    On receiving an email, a POST request will be made to the configured URL,
    with the following multipart POST parameters:

    - mail_from the envelope sender address
    - mail_to: the envelope recipient address
    - message: the full email mime encoded body

    A 2xx response from the upstream server causes a "250 OK" response. For
    other HTTP codes, refer to the ``error_status_code_map`` dict.
    """

    error_status_code_map = {
        400: "541 The recipient address rejected your message",
        401: "530 Authentication problem",
        402: "530 Authentication problem",
        404: "550 Non-existent email address",
        410: "550 Non-existent email address",
        413: "523 Size of your mail exceeds the server limits",
        429: "541 Destination system misconfigured (received HTTP XXX)",
        500: "421 Service unavailable",
        502: "421 Service unavailable",
        503: "421 Service unavailable",
        504: "420 Timeout connection problem",
    }

    default_error_response = "441 Recipient's server not responding"

    def __init__(self, url):
        self.url = url

    async def send(self, mail_from, rcpt_tos, data):
        async with ClientSession() as session:
            data = ([('mail_from', mail_from), ('message', data)]
                    + [('rcpt_to', r) for r in rcpt_tos])
            async with session.post(self.url, data=data) as response:
                await response.read()
                if 200 <= response.status < 299:
                    return '250 OK'
                return self.error_status_code_map.get(
                    response.status,
                    self.default_error_response
                )


class StdoutRelay:
    """
    Log messages to stdout.

    :param format: one of json, text or human. If text, the email data is
                   dumped as-is if human, the first text/plain part is decoded
                   and displayed. If json, each email will be dumped as a JSON
                   formatted record.
    """

    def __init__(self, stream=sys.stdout, format='text'):
        self.stream = stream
        self.format = format
        assert format in ('text', 'json', 'human')

    async def send(self, mail_from, rcpt_tos, data):
        if self.format == 'json':
            s = json.dumps({'mail_from': mail_from, 'rcpt_tos': rcpt_tos, 'message': data},
                           indent=4,
                           separators=(',', ': '))
            print(s, file=self.stream)
        else:
            print(f"Envelope-From: {mail_from}", file=self.stream)
            print(f"Envelope-To: {','.join(rcpt_tos)}", file=self.stream)
            if self.format == 'human':
                msg = email.message_from_string(data.decode('ascii'))
                display_headers = {'subject', 'from', 'to', 'date', 'content-type', 'message-id'}
                for key, value in msg.items():
                    if key.lower() in display_headers:
                        print(f"{key}: {value}", file=self.stream)
                print("", file=self.stream)
                for part in msg.walk():
                    if part.get_content_type() == 'text/plain':
                        charset = part.get_content_charset('iso-8859-1')
                        print(part.get_payload(decode=True).decode(charset),
                              file=self.stream)
                        break
                else:
                    print(data, file=self.stream)
                print("\n", file=self.stream)
            else:
                print(data.decode('ascii', 'ignore'), file=self.stream)
        return '250 OK'


def main():
    args = argparser.parse_args()

    bindhost, bindport = args.bind.split(':')
    bindport = int(bindport)

    relays = []

    if args.verbose == 1:
        logging.basicConfig(level=logging.INFO)

    if args.verbose == 2:
        logging.basicConfig(level=logging.DEBUG)

    if args.stdout:
        relays.append(StdoutRelay(format=args.stdout_format))

    if args.relay_url:
        relays.append(HTTPRelay(args.relay_url))

    if args.relay:
        if args.relay_user and not args.relay_password:
            args.relay_password = getpass()
        relayhost, relayport = args.relay.split(':')
        relayport = int(relayport)
        relays.append(
            ConfigurableSMTP(relayhost, relayport, use_tls=args.relay_tls,
                             starttls=args.starttls, user=args.relay_user,
                             password=args.relay_password)
        )

    if relays == []:
        print("No relays specified!", file=sys.stderr)
        argparser.print_help()
        sys.exit(1)

    handler = FakeSMTPHandler(rewrite_to=args.rewrite_to,
                              relays=relays,
                              log_envelopes=args.log_envelopes,
                              log_emails=args.log_emails)

    loop = asyncio.get_event_loop()

    coro = loop.create_server(lambda: SMTP(handler), host=bindhost, port=bindport)
    server = loop.run_until_complete(coro)
    if args.verbose:
        print('Listening on {}'.format(server.sockets[0].getsockname()))

    try:
        loop.run_forever()
    finally:
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()


if __name__ == "__main__":
    main()
