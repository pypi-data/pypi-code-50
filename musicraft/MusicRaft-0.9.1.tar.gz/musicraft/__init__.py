version = '0.9.1'

import sys, os, tempfile, platform

# from .abcraft import external

debugging = int(os.getenv('MUSICRAFT_DBG', 0))
qt_module_name = os.getenv('MUSICRAFT_QT', 'PySide2')
using_shared_executables = False

print(f"using version {version} of package 'musicraft'  from {os.path.split(__file__)[0]}")

dbg_print = (debugging & 1) and print or (lambda *pp, **kw: None)

# locate the directory in which this file, thus package musicraft, resides
head_dir = os.path.normpath(os.path.split(__file__)[0]+ '/../')

# Depending on the install method, this may or may not also be the parent or our 'share' directory.
# There's got to be a better way, but this should work:

if head_dir.endswith('-packages'):
    head_dir = os.path.normpath(head_dir + ((platform.system()=='Windows') and '/../../' or '/../../../'))

print("head_dir....", head_dir)
temp_dir = tempfile.gettempdir()

USE_EXECS_FROM_SHARE_ARGS = ('-S', '--share')
GIVE_DEBUG_INFO_ARGS = ('-D', '--debug')
DO_NOT_GIVE_DEBUG_INFO_ARGS = ('-ND', '--no-debug')
DEBUG_INFO_ARGS = GIVE_DEBUG_INFO_ARGS + DO_NOT_GIVE_DEBUG_INFO_ARGS
USE_QT_PACKAGE_ARGS = ('--PyQt4', '--PySide', '--PyQt5', '--PySide2', )

for arg in sys.argv[1:]:
    if not arg.startswith('-'):
        continue  # presumably a filename top be looked at later,
    if arg in DEBUG_INFO_ARGS:
        debugging = arg in GIVE_DEBUG_INFO_ARGS
    elif arg in USE_QT_PACKAGE_ARGS:
        qt_module_name = arg[2:]
    elif arg in USE_EXECS_FROM_SHARE_ARGS:
        # keyword --share or -S means:
        # "use executables (abcm2ps etc.) from the bundled 'share' directory"
        using_shared_executables = True
        # If this is absent, these are usually assumed to be present on the system path.... but see further below!
        print("bundled shared executables will be used...")
    else:
        print(f"Musicraft does not understand keyword argument '{arg}' so will just ignore it.")
    sys.argv.remove(arg)  # clean out keyword argument to ultimately just leave filenames if any.

dbg_print = (debugging & 1) and print or (lambda *pp, **kw: None)

if qt_module_name == 'PySide':
    from PySide import (QtCore, QtGui, QtSvg, QtWebKit)
    Signal = QtCore.Signal
    print ("using PySide!")
    name_from_dialog = lambda x:x[0]
    QtPrintSupport = QtGui
    QtWidgets = QtGui
    QtWebEngine = QtWebKit
    QtWebEngineWidgets = QtWebKit
    WebView = QtWebKit.QWebView
elif qt_module_name == 'PyQt4':
    from PyQt4 import (QtCore, QtGui, QtSvg, QtWebKit)

    Signal = QtCore.pyqtSignal
    print("using Pyqt4!")
    name_from_dialog = lambda x: x
    QtPrintSupport = QtGui
    QtWidgets = QtGui
    QtWebEngine = QtWebKit
    QtWebEngineWidgets = QtWebKit
    WebView = QtWebKit.QWebView
elif qt_module_name == 'PySide2':
    from PySide2 import (QtCore, QtGui, QtWidgets, QtPrintSupport, QtSvg, QtWebEngine, QtWebEngineWidgets)
    Signal = QtCore.Signal
    print("using PySide2!")
    name_from_dialog = lambda x: x[0]
    WebView = QtWebEngineWidgets.QWebEngineView
elif qt_module_name == 'PyQt5':
    from PyQt5 import (QtCore, QtGui, QtWidgets, QtSvg, QtPrintSupport, QtWebEngine, QtWebEngineWidgets)
    Signal = QtCore.pyqtSignal
    print("using Pyqt5!")
    name_from_dialog = lambda x:x
    WebView = QtWebEngineWidgets.QWebEngineView
else:
    raise NameError("bad value: MUSICRAFT_QT = " + qt_module_name)

from .shared import *
#from .raft import *
from .abcraft import external

whereAmI = platform.system()

if using_shared_executables:
    print("bundled shared executables will be used...")
    # code below is perhaps unnecssarily long-winded... but it's at least easily tweakable for special requirements!
    if whereAmI == 'Linux':
        external.Abcm2svg.exec_dir = 'share/Linux/bin/'
        external.Abc2midi.exec_dir = 'share/Linux/bin/'
        external.Abc2abc.exec_dir = 'share/Linux/bin/'
    elif whereAmI == 'Darwin':
        external.Abcm2svg.exec_dir = 'share/OSX/bin/'
        external.Abc2midi.exec_dir = 'share/OSX/bin/'
        external.Abc2abc.exec_dir = 'share/OSX/bin/'
    elif whereAmI == 'Windows':
        external.Abcm2svg.exec_dir = 'share/windows/abcm2ps-8.14.4/'
        external.Abc2midi.exec_dir = 'share/windows/abcmidi_win32/'
        external.Abc2abc.exec_dir = 'share/windows/abcmidi_win32/'
    else:
        print(f"sorry, Musicraft does not come with shared abc... apps for platform '{whereAmI}'")
        print("Please install these by other means and start musicraft without '-S'/'--share'.")

