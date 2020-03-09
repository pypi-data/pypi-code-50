# setup.py

from setuptools import setup, find_namespace_packages

setup(
    name='botlib',
    version='76',
    url='https://bitbucket.org/botd/botlib',
    author='Bart Thate',
    author_email='bthate@dds.nl',
    description=""" BOTLIB is a library you can use to program bots. no copyright. no LICENSE. """,
    long_description="""
R E A D M E
###########


BOTLIB is a library you can use to program bots. no copyright. no LICENSE.

as of version 76 the binaries in the tarball are no longer distributed with the egg.
this makes this package a pure library package e.g. no binaries. program your own clientcode with it, see http://pypi.org/project/genoclaim


I N S T A L L


download the tarball from pypi, https://pypi.org/project/botlib/#files

if you want to have BOTLIB started at boot, you need to have the tarball and run:

::

 > sudo bin/install

this will install an botd service in /etc/systemd/system


you can also download with pip3 and install globally.

::

 > sudo pip3 install botlib --upgrade --force-reinstall


U S A G E


::

 > bin/bot localhost \#dunkbots botje
 > bin/botsh
 > bin/botd 
 > bin/botcmd <cmd>
 > bin/botctl <cmd>

logfiles can be found in ~/.bot/logs.


C O N F I G U R A T I O N


use botctl to edit on the system installed botd service:

::

 > bin/botctl cfg krn modules bot.rss,bot.udp
 > bin/botctl cfg irc server localhost
 > bin/botctl cfg irc channel #dunkbots
 > bin/botctl cfg irc nick botje
 > bin/botctl meet ~bart@127.0.0.1
 > bin/botctl rss rss https://news.ycombinator.com/rss

use the -w option if you want to use a different work directory then ~/.bot.


R S S


add an url:

::

 > bin/botctl rss https://news.ycombinator.com/rss
 ok 1

 run the rss command to see what urls are registered:

 > bin/botctl rss
 0 https://news.ycombinator.com/rss

 the fetch command can be used to poll the added feeds:

 > bin/botctl fetch
 fetched 0


U D P


using udp to relay text into a channel, start the bot with -m bot.udp and use
the botudp program to send text via the bot to the channel on the irc server:

::

 > tail -f /var/log/botd/botd.log | bin/botudp 


C O D I N G

if you want to develop on the library clone the source at bitbucket.org:

::

 > git clone https://bitbucket.org/botd/botlib
 > cd botlib
 > sudo python3 setup.py install

if you want to add your own modules to the bot, you can put you .py files in a "mods" directory and use the -m option to point to that directory.

BOTLIB contains the following modules:

::

    bot.dft		- default
    bot.flt		- fleet
    bot.irc		- irc bot
    bot.krn		- core handler
    bot.rss		- rss to channel
    bot.shw		- show runtime
    bot.udp		- udp to channel
    bot.usr		- users

BOTLIB uses the LIBOBJ library which gets included in the tarball.

::

    lo.clk		- clock
    lo.csl		- console 
    lo.hdl		- handler
    lo.shl		- shell
    lo.thr		- threads
    lo.tms		- times
    lo.typ		- types

basic code is a function that gets an event as a argument:

::

 def command(event):
     << your code here >>

to give feedback to the user use the event.reply(txt) method:

::

 def command(event):
     event.reply("yooo %s" % event.origin)


have fun coding ;]


you can contact me on IRC/freenode/#dunkbots.

| Bart Thate (bthate@dds.nl, thatebart@gmail.com)
| botfather on #dunkbots irc.freenode.net


    """,
    long_description_content_type="text/x-rst",
    install_requires=["libobj", "feedparser"],
    license='Public Domain',
    zip_safe=True,
    packages=["bot", "lo"],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
