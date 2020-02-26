#!/usr/bin/env python3

""" AD1459, an IRC Client

  Copyright ©2019-2020 by Gaven Royer

  Permission to use, copy, modify, and/or distribute this software for any
  purpose with or without fee is hereby granted, provided that the above
  copyright notice and this permission notice appear in all copies.

  THE SOFTWARE IS PROVIDED "AS IS" AND ISC DISCLAIMS ALL WARRANTIES WITH REGARD
  TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
  FITNESS. IN NO EVENT SHALL ISC BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR
  CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
  DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
  ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
  SOFTWARE.

  ListBoxRows for messages.
"""

import logging

import gi
gi.require_versions(
    {
        'Gtk': '3.0',
        'Pango': '1.0'
    }
)
from gi.repository import Gtk, GLib, Pango

from .. import formatting as fmt

class MessageRow(Gtk.ListBoxRow):
    """ A ListBoxRow representing a message.

    The attributes for this class are stored directly in the Gtk.Label widgets
    drawn within these rows, as this obviates the need to store extra variables
    in memory.

    We use two copies of the message text, timestamp, and sender. This is to
    display the message differently depending on if this was a server message or
    a normal message. Server messages are combined into one long message, and 
    be collapsed to save space.

    Attributes:
        time (str): The time the message was sent.
        sender (str): The user/network who sent the message. "*" by default.
        text (str): The text of the message.
    """

    def __init__(self, server_msg=False):
        self.server = server_msg
        super().__init__()
        self.log = logging.getLogger('ad1459.message-row')

        # We don't want these to be selectable in the list
        self.props.selectable = False
        Gtk.StyleContext.add_class(self.get_style_context(), "message-row")
        self.props.margin = 1
        self.set_margin_start(6)
        self.set_margin_end(6)
        self.set_focus_on_click(False)

        layout = Gtk.Grid()
        self.add(layout)

        self.sender_label = Gtk.Label()
        self.sender_label.set_halign(Gtk.Align.START)
        self.sender_label.set_margin_start(6)
        self.sender_label.set_margin_end(12)
        layout.attach(self.sender_label, 0, 0, 1, 1)

        self.revealer = Gtk.Revealer()
        self.revealer.set_margin_start(18)
        self.revealer.set_margin_end(12)
        layout.attach(self.revealer, 0, 1, 3, 1)

        self.messages_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 0)
        self.revealer.add(self.messages_box)

        self.time_label = Gtk.Label()
        self.time_label.set_hexpand(True)
        self.time_label.set_margin_end(6)
        self.time_label.set_halign(Gtk.Align.END)
        layout.attach(self.time_label, 2, 0, 1, 1)
        self.show_all()

        self.expander = Gtk.Expander()
        self.expander.set_halign(Gtk.Align.START)
        self.expander.connect('notify::expanded', self.show_hide)
        self.expander.set_expanded(True)
        layout.attach(self.expander, 1, 0, 1, 1)

        if not self.server:
            self.log.debug('Expanding non-server message')
            self.expander.set_expanded(True)
            self.expander.props.opacity = 0.5

        # Keep track of whether the user toggles the expander
        self.toggled = False
    
    def add_message(self, message):
        """Adds a message to this row.

        Arguments:
            message(:obj:`Message`): The message object to add.
        """
        self.expander.set_expanded(False)
        self.messages_box.add(message)
        self.expander.set_expanded(True)

        if self.server:
            self.expander.set_label(f'{self.count} server messages')
            if self.count > 10 and not self.toggled:
                self.expander.set_expanded(False)
    
    # Internal Handlers
    def show_hide(self, expander, data=None):
        """ handler for the expander-revealer above. 
        
        When the expander is toggled, we set the revealer property to the same
        as the expander's property.
        """
        state = self.expander.get_expanded()
        self.revealer.props.reveal_child = state
        if not state and not self.server:
            self.expander.set_label(f'{self.count} collapsed messages')
        elif state and not self.server:
            self.expander.set_label('')
        # User toggled manually, remember that.
        self.toggled = True
    
    @property
    def kind(self):
        """str: The type of message this is, based on who sent it and 
        its contents.
        """
        return self._kind
    
    @kind.setter
    def kind(self, kind):
        self._kind = kind
        Gtk.StyleContext.add_class(self.get_style_context(), kind)

    @property
    def count(self):
        """int: the number of message in this message row."""
        messages = self.messages_box.get_children()
        return len(messages)

    @property
    def time(self):
        """str: The time the message was sent."""
        return self.time_label.get_text()
    
    @time.setter
    def time(self, time):
        time = GLib.markup_escape_text(time)
        self.time_label.set_markup(f'<small><i>{time}</i></small>')
    
    @property
    def sender(self):
        """ The sender of the message, or * for none/network. """
        return self.sender_label.get_text()
    
    @sender.setter
    def sender(self, sender):
        self.sender_label.set_markup(f'<small><b>{sender}</b></small>')
    
    @property
    def text(self):
        """ The message text."""
        for message in self.messages_box.get_children():
            yield message.text
    
    def show_all_contents(self):
        self.show_all()
