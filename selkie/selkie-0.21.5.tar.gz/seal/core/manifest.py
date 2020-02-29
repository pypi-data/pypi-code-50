##  @package seal.core.manifest
#   Creates and manages manifests of directory hierarchies.

import os, sys, subprocess, tarfile
from zlib import adler32
from seal.core.io import split_suffix


#--  File Ops  -----------------------------------------------------------------

def _print_trace (fn):
    sys.stderr.write(fn)
    sys.stderr.write('\n')
    sys.stderr.flush()

def _compute_md5_hash (fn, trace):
    s = subprocess.getoutput("openssl md5 < '%s'" % fn)
    if s.startswith('(stdin)= '):
        s = s[9:]
    if trace: print(' ok', file=sys.stderr)
    return s

def _file_size (fn):
    return os.stat(fn).st_size

##  Load a manifest.
#   Returns a dict that maps a relpath to a tuple (relpath, size, chksum/hash).

def load (fn):
    d = {}
    with open(fn) as f:
        for line in f:
            fields = line.rstrip('\r\n').split('\t')
            if len(fields) < 2:
                raise Exception('Bad line in %s' % fn)
            fields[1] = int(fields[1])
            d[fields[0]] = tuple(fields)
    return d

# Returns a pair: (nbytes, checksum)

def _checksum (fn):
    value = 1
    nbytes = 0
    with open(fn, 'rb') as f:
        while True:
            bs = f.read(1024)
            if not bs: break
            nbytes += len(bs)
            value = adler32(bs, value)
    return (nbytes, value)

def _listdir (dir):
    for name in sorted(os.listdir(dir)):
        if name not in ('.', '..'):
            yield (name, os.path.join(dir, name))

def _iter_directories (dir):
    if os.path.isdir(dir):
        yield dir
        for (name, fn) in _listdir(dir):
            for subdir in _iter_directories(fn):
                yield subdir


##  Load a file containing a list of directory names.

def load_dirs_file (fn):
    with open(fn) as f:
        for line in f:
            line = line.rstrip('\r\n')
            if line:
                yield line


#--  Writer  -------------------------------------------------------------------

##  Writer for a manifest.

class Writer (object):

    ##  Constructor.

    def __init__ (self, out, root=None, outputs='', trace=False):

        ##  Filename.
        self.filename = None

        ##  Open stream.
        self.stream = None

        ##  The write method.
        self.write = None

        ##  Last object written.
        self.value = None

        ##  Trace flag.
        self.trace = trace

        # collect in a list
        if isinstance(out, list):
            self.value = out
            self.write = lambda rec: out.append(rec)

        # collect in a dict
        elif isinstance(out, dict):
            self.value = out
            self.write = lambda rec: out.__setitem__(rec[0], rec)
    
        # streaming
        elif out == '-':
            self.trace = False
            self.write = lambda rec: print(*rec, sep='\t')
    
        # write file
        elif isinstance(out, str):
            self.filename = out

        # write default file
        elif out is None:
            if 'h' in outputs:
                self.filename = root + '.hashes'
            elif 's' in outputs:
                self.filename = root + '.chksum'
            elif 'z' in outputs:
                self.filename = root + '.sizes'
            else:
                raise Exception('This cannot happen')
            if os.path.exists(self.filename) and not force:
                raise Exception('File already exists, delete manually or specify -f: %s' % self.filename)

        else:
            raise Exception('Cannot handle this: %s' % repr(out))

    ##  Enter.  Open the file.

    def __enter__ (self):
        if self.filename is not None:
            f = open(self.filename, 'w')
            self.stream = f
            self.trace = True
            self.write = lambda rec: print(*rec, sep='\t', file=f)
        return self

    ##  Exit.  Close the file.

    def __exit__ (self, t, v, tb):
        if self.filename is not None:
            self.stream.close()


#--  Create signature  ---------------------------------------------------------

##  Create a manifest.

def create (ifile=None, otype=None, ofile=None, update=False, trace=False, force=False):
    assert ifile is not None
    known = None
    value = None
    if not otype:
        otype = 'z'

    # update
    if update:
        force = True
        if not os.path.exists(ifile):
            raise Exception('Not found: %s' % ifile)
        if otype is not None:
            raise Exception('Do not specify both -u and -h/-s')
        ofile = ifile
        (ifile, suffix) = split_suffix(ofile)
        if suffix == 'hashes':
            otype = 'h'
        elif suffix == 'chksum':
            otype = 's'
        elif suffix == 'sizes':
            otype = 'z'
        else:
            raise Exception('Can only update .hashes, .chksum, or .sizes files')
        if os.path.exists(ofile):
            known = load(ofile)
        dirs = _iter_directories(ifile)

    # ifile is a directory
    elif os.path.isdir(ifile):
        dirs = _iter_directories(ifile)

    # ifile is a file ending in .dirs
    elif os.path.exists(ifile) and ifile.endswith('.dirs'):
        dirs = load_dirs_file(ifile)

    else:
        raise Exception('Not found: %s' % ifile)

    with Writer(ofile, ifile, otype, trace) as w:
        write_signature(dirs, w.write, otype, known, trace=w.trace)
        return w.value


##  Write the manifest contents.

def write_signature (dirs, write, otype, known=None, trace=False):
    total = 0
    for dir in dirs:
        if not (os.path.exists(dir) and os.path.isdir(dir)):
            raise Exception('Not an existing directory: %s' % dir)
        for (name, fn) in _listdir(dir):
            fn = os.path.join(dir, name)
            if not (os.path.isdir(fn) or os.path.islink(fn)):
                if known and fn in known:
                    rec = known[fn]
                elif otype == 'h':
                    if trace: _print_trace(fn)
                    rec = (fn, _file_size(fn), _compute_md5_hash(fn, trace))
                elif otype == 's':
                    if trace: _print_trace(fn)
                    rec = (fn, _checksum(fn))
                else:
                    rec = (fn, _file_size(fn))
                total += rec[1]
                write(rec)
    write(('TOTAL:', total))


#--  List directories  ---------------------------------------------------------

##  List all directories in the hierarchy.

def list_directories (ifile):
    for dir in _iter_directories(ifile):
        print(dir)


#--  Extract sizes  ------------------------------------------------------------

##  Print out the file sizes from a manifest file.

def extract_sizes (fn):
    with open(fn) as f:
        for line in f:
            fields = line.rstrip('\r\n').split('\t')
            print(fields[0], fields[1], sep='\t')


#--  Diff  ---------------------------------------------------------------------

# no * in interior
# applies to pathname components

##  Returns True if the filename is a "temporary" file.  Specifically, if the
#   filename is '.git', '.DS_Store', '__pycache__', or ends in '~' or '.safe'.

def istemp (fn):
    cpts = fn.split('/')
    for cpt in cpts:
        if cpt in ('TOTAL:', '.git', '.DS_Store', '__pycache__'):
            return True
        else:
            for suffix in ('~', '.safe'):
                if cpt.endswith(suffix):
                    return True
    return False

def _diffs (src, tgt):
    for rec1 in src.values():
        key = rec1[0]
        val1 = rec1[1]
        if key in tgt:
            val2 = tgt[key][1]
            if val1 != val2:
                yield ('replace', key, val1, val2)
        else:
            yield ('add', key, val1, None)
    for rec2 in tgt.values():
        key = rec2[0]
        val2 = rec2[1]
        if key not in src:
            yield ('delete', key, None, val2)

##  Write out a list of differences.

def difference (diff_spec, ofile='-', full=False):
    (local_fn, diff_from) = diff_spec
    direction = 'export'

    if os.path.isdir(local_fn):
        local_tab = create(ifile=local_fn, ofile={})
    else:
        local_tab = load(local_fn)
    remote_tab = load(diff_from)

    if direction == 'import':
        tgt = local_tab
        src = remote_tab
    elif direction == 'export':
        tgt = remote_tab
        src = local_tab
    else:
        raise Exception('Bad direction: %s' % repr(direction))

    with Writer(ofile) as w:
        if full:
            for (action, key, val1, val2) in _diffs(src, tgt):
                if val1 is None: val1 = '-'
                if val2 is None: val2 = '-'
                rec = ('%-60s %12s %12s' % (key, val1, val2),)
                w.write(rec)
        else:
            for (action, key, val1, val2) in _diffs(src, tgt):
                if not istemp(key):
                    w.write((action, key))
        return w.value


#--  Import/export  ------------------------------------------------------------

##  Save a list of differences to file.

def save_diffs (diffs, fn):
    with open(fn, 'w') as f:
        for rec in diffs:
            print(*rec, sep='\t', file=f)

##  Read in a list of differences.

def read_diffs (f):
    diffs = []
    for line in f:
        rec = line.rstrip('\r\n').split('\t')
        diffs.append(rec)
    return diffs

##  Load a list of differences from a file.

def load_diffs (fn):
    with open(fn) as f:
        return read_diffs(f)

##  Produces a delta tarfile.

def export_delta (diff_spec, ofile=None, diff=None):
    (src, tgt) = diff_spec
    diffs = difference(diff_spec, ofile=[])
    if diffs:
        if ofile is None:
            ofile = src + '-delta.tgz'
        print('Writing', ofile)
        save_diffs(diffs, 'manifest.diffs')
        with tarfile.open(ofile, 'w:gz') as tf:
            tf.add('manifest.diffs')
            for (action, relpath) in diffs:
                if action in ('add', 'replace'):
                    tf.add(relpath)
        os.unlink('manifest.diffs')

def _binary_to_ascii (f):
    for line in f:
        yield line.decode('ascii')

##  Read a delta tarfile and install the files in the local directory.

def import_delta (ifile=None):
    with tarfile.open(ifile, 'r:gz') as tf:
        mf = tf.extractfile('manifest.diffs')
        diffs = read_diffs(_binary_to_ascii(mf))
        mf.close()
        for (action, relpath) in diffs:
            if action == 'add':
                print('Adding', relpath)
                tf.extract(relpath)
            elif action == 'replace':
                print('Replacing', relpath)
                tf.extract(relpath)
            elif action == 'delete':
                print('Deleting', relpath)
                os.unlink(relpath)
