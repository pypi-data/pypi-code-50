# setup.py

from setuptools import setup, find_namespace_packages

setup(
    name='botlib',
    version='72',
    url='https://bitbucket.org/botd/botlib',
    author='Bart Thate',
    author_email='bthate@dds.nl',
    description=""" botlib is a library you can use to program bots, is placed in the Public Domain and contains no copyright or LICENSE. """,
    long_description="""
R E A D M E
###########


BOTLIB is a library you can use to program bots. no copyright. no LICENSE.


I N S T A L L


download the tarball from pypi, https://pypi.org/project/botlib/#files


you can also download with pip3 and install globally.

::

 > sudo pip3 install botlib --upgrade

if you want to develop on the library clone the source at bitbucket.org:

::

 > git clone https://bitbucket.org/botd/botlib
 > cd botlib
 > sudo python3 setup.py install

if you want to have BOTLIB started at boot, run:

::

 > sudo bin/install

this will install an botd service in /etc/systemd/system


U S A G E


::

 > bot -m bot.rss localhost \#dunkbots botje
 > bot -y
 > botd 
 > botcmd <cmd>
 > botctl <cmd>

logfiles can be found in ~/.bot/logs.


C O N F I G U R A T I O N


use botcmd to edit localy and botctl to edit on the system installed botd service:

::

 > botcmd cfg krn modules bot.rss,bot.udp
 > botcmd cfg irc server localhost
 > botcmd cfg irc channel #dunkbots
 > botcmd cfg irc nick botje
 > botcmd meet ~bart@127.0.0.1
 > botcmd rss rss https://news.ycombinator.com/rss

use the -w option if you want to use a different work directory then ~/.bot.


R S S


start the rss module by adding rss to the modules option at start:

::

 > bot -m bot.rss 

add an url:

::

 > botcmd rss https://news.ycombinator.com/rss
 ok 1

 run the rss command to see what urls are registered:

 > botcmd rss
 0 https://news.ycombinator.com/rss

 the fetch command can be used to poll the added feeds:

 > botcmd fetch
 fetched 0


U D P


using udp to relay text into a channel, start the bot with -m bot.udp and use
the botudp program to send text via the bot to the channel on the irc server:

::

 > tail -f ~/.bot/logs/botd.log | botudp 


M O D U L E S


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


C O D I N G


if you want to add your own modules to the bot, you can put you .py files in a "mods" directory and use the -m option to point to that directory.

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
    license='Public Domain',
    zip_safe=True,
    install_requires=["feedparser", "libobj"],
    packages=["bot"],
    scripts=["bin/bot", "bin/botcmd", "bin/botctl", "bin/botd", "bin/botudp"],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
