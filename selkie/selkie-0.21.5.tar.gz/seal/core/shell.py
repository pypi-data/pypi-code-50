##  @package seal.core.shell
#   A replacement for seal.core.sh.

try:
    import readline
except ImportError:
    pass

import sys, os, traceback, importlib, re, tarfile
from code import InteractiveConsole
from glob import glob
from seal.core.misc import Shift
from seal.script import manifest
from seal.script.encyd import EncyApp


#--  Commands  -----------------------------------------------------------------

##  Change directory.

def cd (*args):
    fn = None
    with Shift(args) as shift:
        fn = shift.ifable()
    os.chdir(os.path.expanduser(fn))
    

##  Used by encyd.
app = None

##  Start the Ency app, store it in the global variable 'app'.

def encyd (*args):
    global app
    with Shift(args) as shift:
        pass
    app = EncyApp('call', sys.argv[1:], server_port='8004', logfile='-')

##  Create a directory.

def mkdir (*args):
    f = os.makedir
    fn = None
    with Shift(args) as shift:
        if shift.isflag():
            flag = shift()
            if flag == '-p':
                f = os.makedirs
            else:
                raise Exception('Unrecognized flag: %s' % repr(flag))
        fn = shift()
    f(fn)

##  Rename a file.

def mv (*args):
    with Shift(args) as shift:
        fn1 = os.path.expanduser(shift())
        fn2 = os.path.expanduser(shift())
    if os.path.isdir(fn2):
        fn2 = os.path.join(fn2, os.path.basename(fn1))
    os.rename(fn1, fn2)

##  List files or directories.

def ls (*args):
    fn = None
    with Shift(args) as shift:
        fn = shift.ifable()
    if fn is None:
        for name in os.listdir():
            print(name)
    elif '*' in fn:
        for name in glob(fn):
            print(name)
    elif os.path.isdir(fn):
        for name in os.listdir(fn):
            print(name)
    elif os.path.exists(fn):
        print(fn)
    else:
        print('File not found:', fn)
    
##  Pager.

def more (*args):
	with Shift(args) as shift:
		fn = shift()
	if 'PAGESIZE' in os.environ:
		pagesize = int(os.environ['PAGESIZE'])
	else:
		pagesize = 40
	with open(fn) as f:
		try:
			while True:
				for i in range(pagesize):
					print(next(f), end='')
				if input('[More:] ') == 'q':
					break
		except StopIteration:
			pass

##  Print pathname of working directory.

def pwd (*args):
    with Shift(args) as shift:
        pass
    print(os.getcwd())
			
##  Reload the named modules.

def reload (*args):
	with Shift(args) as shift:
		name = shift()
	if name in sys.modules:
		importlib.reload(sys.modules[name])
	else:
		raise Exception('Undefined module: %s' % name)

##  Delete files.

def rm (*args):
    for arg in args:
        if '*' in arg:
            for name in glob(arg):
                os.unlink(name)
        else:
            os.unlink(arg)

##  Set an environment variable.

def set (var, value):
    os.environ[var] = value

##  Manage a tarfile.

def tar (*args):
    specs = {'verbose': False}
    com = None
    with Shift(args) as shift:
        flags = shift()
        for c in flags:
            if c in ('c', 'x', 't'):
                com = c
            elif c == 'f':
                specs['tfile'] = shift()
            elif c == 'z':
                specs['mode'] = c
            elif c == 'v':
                specs['verbose'] = True
            else:
                raise Exception('Unhandled flag: %s' % c)

    if com == 't':
        if 'tfile' not in specs:
            raise Exception('No tarfile supplied')
        with tarfile.open(specs['tfile'], 'r') as tf:
            tf.list(verbose=specs['verbose'])
        
    else:
        raise Exception('Unimplemented')

##  Word count.

def wc (*args):
    with Shift(args) as shift:
        fn = shift()
    nl = 0
    nc = 0
    nsw = 0
    naw = 0
    with open(fn) as f:
        for line in f:
            nl += 1
            nc += len(line)
            wswords = line.split()
            for word in wswords:
                if word:
                    nsw += 1
                    awords = re.split(r'\W+', word)
                    for aword in awords:
                        if aword:
                            naw += 1
    print('Lines:      ', nl)
    print('WS-words:   ', nsw)
    print('Alpha-words:', naw)
    print('Chars:      ', nc)


#--  main  ---------------------------------------------------------------------

def _command (s):
    for i in range(len(s)):
        if s[i].isspace():
            return s[:i]
    return s

##  The main function.

def main (*args):
    echo = False

    with Shift(args) as shift:
        while shift.isflag():
            flag = shift()
            if flag == '-E':
                echo = True
            else:
                shift.error('Bad flag: %s' % flag)

    shell(echo)


##  A shell.

class Shell (object):
	
    ##  Constructor.

    def __init__ (self):
		
        ##  The builtin commands.
        self.coms = {
            'cd': cd,
            'echo': print,
            'encyd': encyd,
            'ls': ls,
            'manifest': manifest.main,
            'mkdir': mkdir,
            'more': more,
            'mv': mv,
            'pwd': pwd,
            'reload': reload,
            'rm': rm,
            'set': set,
            'tar': tar,
            'wc': wc
            }

        ##  The local variables.
        self.locals = {
            '__name__': '__console__',
            '__doc__': None
            }

        ##  An InteractiveConsole.
        self.console = InteractiveConsole(self.locals)
		
    ##  Run the shell.

    def __call__ (self, echo=False):
        while True:
            try:
                line = input('$$> ')
                if echo: print(line)
                
                expanded = self.expand_vars(line)
                com = _command(expanded)
	            
                if com == 'exit':
                    break
	
                elif com in self.coms:
                    f = self.coms[com]
                    argv = expanded.split()
                    value = f(*argv[1:])
	
                else:
                    needmore = True
                    while needmore:
                        needmore = self.console.push(line)
	
            except EOFError:
                break
	
            except:
	            traceback.print_exc()
	            
    ##  Get the value of a local variable.

    def getvar (self, name):
        if name in self.locals:
            return str(self.locals[name])
        else:
            return os.getenv(name)
            
    ##  Expand $VAR references in s.

    def expand_vars (self, s):
        out = []
        i = 0
        while True:
            j = s.find('$', i)
            if j < 0:
                if i < len(s):
                    out.append(s[i:])
                break
            # s[j] is a $
            if j > i: out.append(s[i:j])
            i = j + 1
            if s[i] == '$':
                out.append('$')
                i += 1
            elif s[i] in '({':
                if s[i] == '(': end = ')'
                else: end = '}'
                i += 1
                j = s.find(end, i)
                name = s[i:j].strip()
                if not name: raise Exception('Empty env var name')
                v = self.getvar(name)
                if v: out.append(v)
                i = j + 1
            elif s[i].isalpha() or s[i] == '_':
                j = i + 1
                while j < len(s) and (s[j].isalnum() or s[j] == '_'):
                    j += 1
                name = s[i:j].strip()
                if not name: raise Exception('Empty env var name')
                v = self.getvar(name)
                if v: out.append(v)
                i = j
            else:
                raise Exception('Illegal character after $')
        return ''.join(out)
    
##  An instance of Shell.
shell = Shell()


if __name__ == '__main__':
    main(*sys.argv[1:])
