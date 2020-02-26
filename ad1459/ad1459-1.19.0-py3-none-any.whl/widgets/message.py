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

  Messages Themselves.
"""

import logging

from gi.repository import Gtk, GLib, Pango

from .. import formatting as fmt

class Message(Gtk.Label):
    """ A message from IRC.

    This can be a message sent from a user or a status message representing 
    changes from the IRC server (mode changes, joins, parts, etc.). We add these
    to a message row to allow each message to be highlighted individually. It 
    will also allow us to only use one message text per message, reducing 
    memory footprint.

    The text is contained within an Eventbox so that we can catch events and add
    a right-click menu for the message.

    Attributes:
        text (str): The text of the specific message.
        time (str): The timestamp of the message.
    """

    def __init__(self, text, time):
        super().__init__()

        self.log = logging.getLogger('ad1459.message')

        # self = Gtk.Label()
        self.props.xalign = 0
        self.set_line_wrap(True)
        self.set_line_wrap_mode(Pango.WrapMode.WORD_CHAR)
        # self.add(self)

        Gtk.StyleContext.add_class(self.get_style_context(), 'message')

        self.text = text
        self.time = time

        self.show_all()

    ### Data
    @property
    def text(self):
        """str: The text of this message."""
        return self.get_text()
    
    @text.setter
    def text(self, text):
        """ Store the text directly in the label."""
        parser = fmt.get_default_parser()
        escaped_text = GLib.markup_escape_text(text)
        formatted_text = parser.parse_text(escaped_text)
        linked_text = parser.hyperlinks(formatted_text)
        self.set_markup(linked_text)
    
    @property
    def time(self):
        """str: The timestamp at which the message was sent."""
        return self._timestamp
    
    @time.setter
    def time(self, time):
        self._timestamp = time
    
    @property
    def style(self):
        """str: The style class of this message. Dictates how the message looks.
        """
        try:
            return self._style
        except AttributeError:
            return 'message'
        
    @style.setter
    def style(self, style):
        """Apply the style class to the message."""
        self._style = style
        context = self.get_style_context()
        
        for style_class in context.list_classes():
            context.remove_class(style_class)
        context.add_class('message')
        context.add_class(self._style)
