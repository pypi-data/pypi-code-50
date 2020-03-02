# -*- coding: utf-8 -*-

# Druwez - A GUI printing tool
# https://www.florian-diesch.de/software/druwez/
#
# Copyright (C) 2019 Florian Diesch devel@florian-diesch.de
#
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from gi.repository import Gtk, Gio
from gettext import gettext as _
import textwrap
import urllib.parse

from . import settings, license

def add_help_menu(submenu):
    menu_item = Gtk.ImageMenuItem(_('Go to Web Page'))
    menu_item.set_image(Gtk.Image.new_from_stock(Gtk.STOCK_JUMP_TO, 
                                                 Gtk.IconSize.MENU))
    menu_item.connect('activate', on_menuitem_goto_webpage)
    submenu.append(menu_item)

    menu_item = Gtk.SeparatorMenuItem()
    submenu.append(menu_item)
            
    menu_item = Gtk.ImageMenuItem(_('Report a Bug'))
    menu_item.set_image(Gtk.Image.new_from_stock(Gtk.STOCK_JUMP_TO, 
                                                 Gtk.IconSize.MENU))
    menu_item.connect('activate', on_menuitem_bug)
    submenu.append(menu_item)

    menu_item = Gtk.ImageMenuItem(_('Help with Translations'))
    menu_item.set_image(Gtk.Image.new_from_stock(Gtk.STOCK_JUMP_TO, 
                                                 Gtk.IconSize.MENU))
    menu_item.connect('activate', on_menuitem_translations)
    submenu.append(menu_item)
    
    menu_item = Gtk.ImageMenuItem(_('Access source code repository'))
    menu_item.set_image(Gtk.Image.new_from_stock(Gtk.STOCK_JUMP_TO, 
                                                 Gtk.IconSize.MENU))
    menu_item.connect('activate', on_menuitem_sourcecode)
    submenu.append(menu_item)
    
    menu_item = Gtk.ImageMenuItem(_('Donate via PayPal'))
    menu_item.set_image(Gtk.Image.new_from_stock(Gtk.STOCK_JUMP_TO, 
                                                 Gtk.IconSize.MENU))
    menu_item.connect('activate', on_menuitem_donate)
    submenu.append(menu_item)
    
    submenu.show_all()

def open_url(url):
    u = urllib.parse.urlparse(url)
    appinfo=Gio.app_info_get_default_for_uri_scheme(u.scheme)
    appinfo.launch_uris([url], None)

def on_menuitem_about_activate(menuitem):
    about.show_about_dialog()

def on_menuitem_docs(menuitem):
    open_url(settings.LOCAL_DOCS_URL)

def on_menuitem_goto_webpage(menuitem):
    open_url(settings.WEB_URL)

def on_menuitem_donate(menuitem):
    open_url(settings.PAYPAL_URL)

def on_menuitem_sourcecode(menuitem):
    open_url(settings.SOURCE_URL)

def on_menuitem_translations(menuitem):
    open_url(settings.TRANSLATIONS_URL)

def on_menuitem_bug(menuitem):
    open_url(settings.BUGREPORT_URL)
   

def show_about_dialog():
    dlg = Gtk.AboutDialog()
    dlg.set_program_name(settings.APP_TITLE)
    dlg.set_version('%s (%s)' % (settings.APP_VERSION, settings.APP_TIMESTAMP))
    dlg.set_website(settings.WEB_URL)
    dlg.set_authors(['%s <%s>' % (settings.APP_AUTHOR, 
                                  settings.APP_AUTHOR_EMAIL)])
    dlg.set_wrap_license(True)
    dlg.set_copyright('Copyright (c) %s %s' % (settings.APP_YEAR, 
                                               settings.APP_AUTHOR))
    dlg.set_translator_credits(_("translator-credits"));
    dlg.set_license(license.license_txt)

    dlg.run()
    dlg.destroy()

