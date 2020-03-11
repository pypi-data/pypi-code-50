#
# Copyright (C) 2018-2020  Leo P. Singer <leo.singer@ligo.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
import asyncio
import getpass
import logging
import netrc
import uuid

import pkg_resources
from safe_netrc import netrc as _netrc
from safe_netrc import NetrcParseError
import slixmpp

from ._version import get_versions

__all__ = ('LVAlertClient',)
__version__ = get_versions()['version']
del get_versions

log = logging.getLogger(__name__)

DEFAULT_SERVER = 'lvalert.cgca.uwm.edu'


def _get_default_login(netrcfile, server):
    try:
        netrcfile = _netrc(netrcfile)
    except (OSError, NetrcParseError):
        log.exception('Cannot load netrc file: %s', netrc)
        return None, None

    auth = netrcfile.authenticators(server)
    if auth is None:
        log.warn('No netrc entry found for server: %s', server)
        return None, None

    default_username, _, default_password = auth
    return default_username, default_password


def _get_login(username, password, netrc, interactive, server):
    default_username, default_password = _get_default_login(netrc, server)
    prompt = 'password for {}@{}: '.format(username, server)

    if username is not None and password is not None:
        return username, password
    elif username is None and default_username is None:
        raise RuntimeError('Username not specified')
    elif username is None or username == default_username:
        return default_username, default_password
    elif interactive:
        return username, getpass.getpass(prompt)
    else:
        raise RuntimeError('Password not specified')


class LVAlertClient(slixmpp.ClientXMPP):
    """An XMPP client configured for LVAlert.

    Parameters
    ----------
    username : str, optional
        The XMPP username, or :obj:`None` to look up from the netrc_ file.
    password : str, optional
        The XMPP password, or :obj:`None` to look up from the netrc_ file.
    resource : str, optional
        The XMPP resource ID, or :obj:`None` to generate a random one.
    netrc : str, optional
        The netrc_ file. The default is to consult the ``NETRC`` environment
        variable or use the default path of ``~/.netrc``.
    interactive : bool, optional
        If :obj:`True`, then fall back to asking for the password on the
        command line if necessary.
    server : str, optional
        The LVAlert server hostname.

    Example
    -------

    Usage of the :class:`LVAlertClient` class typically has three phases:

    1.  Create a client instance. Pass any desired connection options (server,
        username, password) to the constructor.

    2.  Configure a pubsub listener by calling the :meth:`listen` method and
        one or more event handlers by calling the
        :meth:`~slixmpp.xmlstream.xmlstream.XMLStream.add_event_handler`
        method.

    3.  Start the client run loop by calling the :meth:`start` method. The
        client run loop continues processing until it is interrupted by a
        :exc:`KeyboardInterrupt` or a call to the :meth:`stop` method either
        from one of the event handlers or from another thread.

    The simplest use case is a client that runs a callback for each LVAlert
    message that is received:

    .. code-block:: python

        def process_alert(node, payload):
            if node == 'cbc_gstlal':
                alert = json.loads(payload)
                print(alert)

        client = LVAlertClient()
        client.listen(process_alert)
        client.start()  # Runs until interrupted with Ctrl-C

    Typically, if you want to call one of the administrative methods
    (:meth:`get_nodes`, :meth:`get_subscriptions`, :meth:`subscribe`, or
    :meth:`unsubscribe`), you will add them to a callback for the
    ``session_start`` event. Since these four methods are :term:`coroutines
    <coroutine>`, the callback should be defined using the ``async``/``await``
    syntax:

    .. code-block:: python

        client = LVAlertClient()

        async def callback(*args):
            subscriptions = await client.get_subscriptions()
            print('Subscribed to:', subscriptions)

        client.add_event_handler('session_start', callback)
        client.start()  # Runs until interrupted with Ctrl-C

    To register a *single-shot* callback, pass ``disposable=True`` to
    :meth:`~slixmpp.xmlstream.xmlstream.XMLStream.add_event_handler`. This is
    most useful if you want to perform some action once, then immediately
    disconnect and stop:

    .. code-block:: python

        client = LVAlertClient()

        async def callback(*args):
            await client.subscribe('cbc_gstlal', 'cbc_pycbc')
            client.stop()

        client.add_event_handler('session_start', callback, disposable=True)
        client.start()  # Stops after callback reaches client.stop()

    """

    def __init__(self, username=None, password=None, resource=None, netrc=None,
                 interactive=False, server=DEFAULT_SERVER):
        username, password = _get_login(
            username, password, netrc, interactive, server)
        if resource is None:
            resource = uuid.uuid4().hex
        jid = '{}@{}/{}'.format(username, server, resource)

        super().__init__(jid, password)

        self.register_plugin('xep_0060')  # Activate PubSub plugin
        self.add_event_handler("session_start", self._session_start)
        self.ca_certs = pkg_resources.resource_filename(__name__, 'certs.pem')
        self._stopped = None

    async def _session_start(self, event):
        self.send_presence()
        await self.get_roster()

    def listen(self, callback):
        """Set a callback to be executed for each pubsub item received.

        Parameters
        ----------
        callback : callable
            A function of two arguments: the node and the alert payload.
        """
        self._callback = callback
        self.add_event_handler('pubsub_publish', self._pubsub_publish)

    def start(self):
        """Run the client until :meth:`stop` is called.

        Establish a connection, process all events, and run all event handlers,
        until :meth:`stop` is called or the current thread is interrupted
        (e.g., by a :exc:`KeyboardInterrupt`).

        If the connection is ever dropped, it is re-established automatically.

        Once processing stops, the connection is closed cleanly before this
        method returns.
        """
        self._stopped = self.loop.create_future()
        self.init_plugins()
        self.connect()
        try:
            self.loop.run_until_complete(self._stopped)
        finally:
            self.disconnect()
            self.loop.run_until_complete(self.disconnected)

    def _stop(self):
        if self._stopped is not None:
            self._stopped.set_result(True)
            self._stopped = None

    def stop(self):
        """Stop the client.

        If the client has been started by calling :meth:`start`, then
        :meth:`start` will return and the connection will be closed.

        Notes
        -----
        This method is thread safe, so you can use it to stop the client from
        another thread. For example:

        .. code-block:: python

            from threading import Thread
            from time import sleep

            client = LVAlertClient()

            def wait_then_stop():
                sleep(5)
                client.stop()
            Thread(target=wait_then_stop).start()

            client.start()

        """
        self.loop.call_soon_threadsafe(self._stop)

    def _pubsub_publish(self, msg):
        node = msg['pubsub_event']['items']['node']
        text = msg['pubsub_event']['items']['item']['payload'].text
        try:
            self._callback(node, text)
        except:  # noqa: E722
            log.exception('Exception occurred in callback')

    @property
    def _pubsub_server(self):
        return 'pubsub.{}'.format(self.boundjid.server)

    async def get_nodes(self):
        """Get a list of all available pubsub nodes.

        Returns
        -------
        list
            A list of strings naming the available pubsub nodes

        """
        result = await self['xep_0060'].get_nodes(self._pubsub_server)
        return [item for _, item, _ in result['disco_items']['items']]

    async def get_subscriptions(self):
        """Get a list of your subscriptions.

        Returns
        -------
        list
            A list of strings naming the subscribed pubsub nodes

        """
        result = await self['xep_0060'].get_subscriptions(self._pubsub_server)
        return sorted({stanza['node'] for stanza in
                       result['pubsub']['subscriptions']['substanzas']})

    async def _subscribe(self, node):
        await self['xep_0060'].subscribe(self._pubsub_server, node)

    async def subscribe(self, *nodes):
        """Subscribe to one or more pubsub nodes.

        Parameters
        ----------
        *args : list
            A list of strings naming the pubsub nodes to which to subscribe

        """
        await asyncio.gather(*(self._subscribe(node) for node in nodes))

    async def _unsubscribe(self, node):
        subs = await self['xep_0060'].get_subscriptions(
            self._pubsub_server, node)
        subs = subs['pubsub']['subscriptions']['substanzas']
        subids = [sub['subid'] for sub in subs]
        await asyncio.gather(*(
            self['xep_0060'].unsubscribe(self._pubsub_server, node, subid)
            for subid in subids))

    async def unsubscribe(self, *nodes):
        """Unsubscribe from one or more pubsub nodes.

        Parameters
        ----------
        *args : list
            A list of strings naming the pubsub nodes from which to unsubscribe

        """
        await asyncio.gather(*(self._unsubscribe(node) for node in nodes))
