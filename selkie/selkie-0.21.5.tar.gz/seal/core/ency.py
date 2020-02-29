##  @package seal.core.ency
#   An encyclopedia of notes.

# The characters are listed in data/seal/entities.txt

import sys, os, re, pipes, seal.core.io
from os.path import expanduser, join, basename
from seal.core import config
from seal.core.misc import shift
from seal.core.io import split_suffix
from seal.app.html import *

##  The Seal data directory.
seal_data = join(seal.core.io.data, 'seal')


#--  DelayedErrorHandler  ------------------------------------------------------

##  A delayed error handler.  Collects error messages and signals them at a
#   later point.

class DelayedErrorHandler (object):

    ##  Constructor.

    def __init__ (self):

        ##  Whether it is active.
        self.armed = False

        ##  Errors that have been collected.
        self.errors = []

    ##  Turn it on.

    def arm (self):
        self.armed = True

    def _check (self):
        if self.armed and self.errors:
            for error in self.errors:
                sys.stderr.write('ERROR: ')
                sys.stderr.write(error)
                sys.stderr.write('\n')
            sys.exit(1)
            
    ##  Add an error.  Signals an error if armed; otherwise just
    #   saves the error.

    def __call__ (self, msg):
        self.errors.append(msg)
        self._check()

    ##  Print out the errors.

    def dump (self):
        for error in self.errors:
            print('ERROR:', error)
    

#-------------------------------------------------------------------------------
#  Config
#
#  In e.g. <cl "foo">foo</cl>, "cl" is the name of a "volume."
#  A volume table maps volume names to pathname prefixes.
#  E.g. "cl" -> "/cl/txt/html"
#

##  Return the filename for a node.  The name may include a "#" portion, which
#   is omitted.

def node_filename (name):
    hash = name.find('#')
    if hash >= 0:
        return name[0:hash] + '.html' + name[hash:]
    else:
        return name + '.html'


#--  Tag  ----------------------------------------------------------------------

##  An HTML-style tag.

class Tag (object):

    ##  Constructor.

    def __init__ (self, file, type, is_start, args, start, end, contents):

        ##  The file that is being parsed.
        self.file = file

        ##  The type of tag (the category).
        self.type = type

        ##  Whether it is a start tag.
        self.is_start = is_start

        ##  The arguments (in place of attributes).
        self.args = args

        ##  The start position in the file.
        self.start = start

        ##  The end position in the file.
        self.end = end

        ##  The complete tag.
        self.contents = contents

    ##  String representation.

    def __repr__ (self):
        return '<Tag %s %s>' % (self.type, ' '.join(repr(arg) for arg in self.args))

    ##  Return the Ency instance from the context.

    def ency (self):
        return self.file.ency()

    ##  Render this tag onto the given page.

    def render (self, page):
        try:
            if self.is_start:
                self.render_start(page, *self.args)
            else:
                self.render_end(page)
        except Exception as e:
            raise HttpException('Unable to render %s\n%s' % (repr(self.contents), str(e)))

    ##  Rendering for a start tag.

    def render_start (self, page, *args):
        page.write(self.contents)

    ##  Rendering for an end tag.

    def render_end (self, page):
        page.write(self.contents)


##  A specialization of Tag for Ency-specific tags.

class EncyTag (Tag):

    ##  Rendering, for a start tag.

    def render_start (self, page, arg):
        page.write('<a href="/%s/%s">' % (self.type, arg))

    ##  Rendering, for an end tag.

    def render_end (self, page):
        page.write('</a>')


##  A tag representing a link.

class LinkTag (EncyTag):

    ##  Rendering, for a start tag.

    def render_start (self, page, name):
        page.write('<a href="%s">' % name)

    ##  Rendering, for an end tag.

    def render_end (self, page):
        page.write('</a>')


##  Write a redirect script onto the page.

def RedirectScript (page, dest):
    page.write('''<script>
window.location.replace("%s");
</script>
''' % dest)


##  A redirect tag.

class RedirectTag (EncyTag):

    ##  Rendering, for a start tag.

    def render_start (self, page, dest):
        RedirectScript(page, dest)

    ##  Rendering, for an end tag.

    def render_end (self, page):
        pass


##  A compound redirect.

class CompoundRedirectTag (EncyTag):

    ##  Rendering, for a start tag.

    def render_start (self, page, name):
        type = self.type[:-8]
        RedirectScript(page, '/%s/%s' % (type, name))


#--  TagCatalog  ---------------------------------------------------------------

##  An address tag.

class AddrTag (EncyTag):
    ##  Rendering a start tag.
    def render_start (self, page, name):
        page.write('<a href="/my/addresses#%s">' % re.sub(' ', '%20', name))

##  An archive-file link.

class ArchTag (LinkTag):
    ##  Rendering a start tag.
    def render_start (self, page, pathname):
        page.write('<a href="/arch/%s">' % pathname)
    ##  Rendering an end tag.
    def render_end (self, page):
        page.write('</a>&nbsp;<img src="/.lib/archive.gif"></img>')

##  An external-page link.

class ExtTag (LinkTag):
    ##  Rendering an end tag.
    def render_end (self, page):
        page.write('</a>&nbsp;<img src="/.lib/external.gif"></img>')

##  A latex tag.

class LatexTag (EncyTag):
    ##  Rendering a start tag.
    def render_start (self, page):
        pass

##  A library-reference tag.

class LibTag (EncyTag):
    ##  Rendering a start tag.
    def render_start (self, page, id):
        page.write('<a href="/lib/%s">' % id)

##  A math tag.

class MathTag (EncyTag):
    ##  Rendering a start tag.
    def render_start (self, page):
        pass

##  A citation tag.

class CiteTag (EncyTag):
    ##  Rendering a start tag.
    def render_start (self, page, id):
        page.write('<a href="/cl/lib#%s">' % id)

##  A tabular-file tag.

class TabularTag (EncyTag):
    ##  Rendering a start tag.
    def render_start (self, page, name):
        dir = self.file.dir
        file = EncyFile(dir, name, 'tab')
        print('file=', repr(file), 'contents=', repr(file.contents))
        file.render(page)
    ##  Rendering an end tag.
    def render_end (self):
        pass

_tag_catalog = {
    'addr': AddrTag,
    'arch': ArchTag,
    'archredirect': CompoundRedirectTag,
    'cite': CiteTag,
    'citeredirect': CompoundRedirectTag,
    'cl': EncyTag,
    'clredirect': CompoundRedirectTag,
    'crs': EncyTag,
    'crsredirect': CompoundRedirectTag,
    'doc': EncyTag,
    'docredirect': CompoundRedirectTag,
    'ext': ExtTag,
    'extredirect': RedirectTag,
    'home': EncyTag,
    'homeredirect': CompoundRedirectTag,
    'java': EncyTag,
    'javadoc': EncyTag,
    'latex': LatexTag,
    'lib': LibTag,
    'math': MathTag,
    'my': EncyTag,
    'myredirect': CompoundRedirectTag,
    'node': LinkTag,
    'per': EncyTag,
    'perredirect': CompoundRedirectTag,
    'redirect': RedirectTag,
    'tabular': TabularTag
}


# 
#         # start doc
#         prefix = 'file://'
#         dir = self.doc_dir
#         link = '<a href="%s%s/%s">' % (prefix, dir, arg)
#         file.write(link)
# 
#         # start ext
#         link = '<a href="%s">' % arg 
#         file.write(link) 
# 
#         # start home
#         prefix = 'file://'
#         link = '<a href="%s%s/%s">' % (prefix, self.myroot, arg)
#         file.write(link)
# 
#         # start java
#         arg = re.sub('[.]', '/', arg)
#         prefix = 'file://'
#         dir = self.sys_javadoc_dir
#         link = '<a href="%s%s/%s.html"><tt>' % (prefix, dir, arg)
#         file.write(link)
# 
#         # start lib
#         prefix = 'file://'
#         link = '<a href="%s%s/%s">' % (prefix, self.lib_dir, arg)
#         file.write(link)
# 
#         # start my
#         fn = node_filename(arg)
#         prefix = 'file://'
#         link = '<a href="%s%s/%s">' % (prefix, self.my_html_dir, fn)
#         file.write(link)
# 
#         # start per
#         fn = node_filename(arg)
#         prefix = 'file://'
#         link = '<a href="%s%s/%s">' % (prefix, self.per_html_dir, fn)
#         file.write(link)
# 
#         # start javadoc
#         arg = re.sub('[.]', '/', arg)
#         i = arg.rfind('/')
#         if i >= 0: classname = arg[i+1:]
#         else: classname = arg
#         if not classname: error('<javadoc> arg is empty or ends in period or slash')
#         if classname[0].islower():
#             arg += '/package-summary'
#         link = '<a href="file://%s/%s.html"><tt>' % (self.cl_javadoc_dir, arg)
#         file.write(link)
# 
#         # start math
#         endmath = contents.find('</math>', tag_end)
#         if endmath < 0: error('Missing </math> tag')
#         expression = contents[tag_end:endmath]
#         tag_end = endmath + 7
#         imgname = self.name + '.math' + str(math_count) + '.png'
#         math_count += 1
#         t = pipes.Template()
#         t.append('mathtopng $OUT', '-f')
#         pipe = t.open(self.outdir + '/' + imgname, 'w')
#         pipe.write(expression)
#         pipe.close()
#         link = '<img src="%s"></img>' % imgname
#         file.write(link)
# 
#         # start latex
#         endlatex = contents.find('</latex>', tag_end)
#         if endlatex < 0: error('Missing </latex> tag')
#         expression = contents[tag_end:endlatex]
#         tag_end = endlatex + 8
#         imgname = self.name + '.latex' + str(latex_count) + '.png'
#         latex_count += 1
#         t = pipes.Template()
#         t.append('latextopng $OUT', '-f')
#         pipe = t.open(self.outdir + '/' + imgname, 'w')
#         pipe.write(expression)
#         pipe.close()
#         link = '<img src="%s"></img>' % imgname
#         file.write(link)
# 
# 
#         
#         # start archredirect
#         self.redirect(self.archive_dir + '/' + arg, file)
# 
#         # start citeredirect
#         self.redirect(self.cl_html_dir + '/lib.html#' + arg, file)
# 
#         # start clredirect
#         self.redirect(self.cl_html_dir + '/' + node_filename(arg), file)
# 
#         # start crsredirect
#         self.redirect(self.crs_dir + '/' + arg, file)
# 
#         # start docredirect
#         self.redirect(self.doc_dir + '/' + arg, file)
# 
#         # start extredirect
#         self.redirect(arg, file)
# 
#         # start homeredirect
#         self.redirect(self.myroot + '/' + arg, file)
# 
#         # start myredirect
#         self.redirect(self.my_html_dir + '/' + node_filename(arg), file)
# 
#         # start redirect
#         self.redirect(node_filename(arg), file)
# 
#         # start perredirect
#         self.redirect(self.per_html_dir + '/' + node_filename(arg), file)
# 
# 
# 
#         # end addr
#         file.write('</a>')
# 
#         # end arch
#         file.write('</a>&nbsp;<img src="' + self.images_path + '/archive.gif"></img>')
# 
#         # end cite
#         file.write('</a>')
# 
#         # end cl
#         file.write('</a>')
# 
#         # end crs
#         file.write('</a>')
# 
#         # end doc
#         file.write('</a>')
# 
#         # end ext
#         file.write('</a>&nbsp;<img src="' + self.images_path + '/external.gif"></img>')
# 
#         # end home
#         file.write('</a>')
# 
#         # end java
#         file.write('</tt></a>')
# 
#         # end javadoc
#         file.write('</tt></a>')
# 
#         # end lib
#         file.write('</a>')
# 
#         # end my
#         file.write('</a>')
# 
#         # end node
#         file.write('</a>')
# 
#         # end per
#         file.write('</a>')


#--  Tokens  -------------------------------------------------------------------

##  A token list.

class HTMLTokens (object):
    
    # does not permit '>' even inside of quoted string
    _tag_pattern = re.compile(r'<(/?)([a-z]+)(\s+([^>]+))?>')
    _string_pattern = re.compile(r'(?:"((?:\\.|[^"])*)")')

    ##  Constructor.

    def __init__ (self, file, string):

        ##  The file being tokenized.
        self.file = file

        ##  The contents of the file as a string.
        self.contents = string

        ##  Current offset in the file.
        self.offset = 0

        ##  Current tag.
        self.tag = None

    ##  Returns self.

    def __iter__ (self): return self
        
    ##  Iterator method.

    def __next__ (self):

        if self.tag is not None:
            tag = self.tag
            self.tag = None
            self.offset = tag.end
            return tag

        if self.offset >= len(self.contents):
            raise StopIteration()

        tag = self._find_tag()

        if tag is None:
            text = self.contents[self.offset:]
            self.offset = len(self.contents)
            return text

        elif tag.start > self.offset:
            text = self.contents[self.offset:tag.start]
            self.tag = tag
            self.offset = tag.start
            return text

        else:
            self.offset = tag.end
            return tag

    def _find_tag (self):
        match = self._tag_pattern.search(self.contents, self.offset)
        if match:
            contents = match.group(0)
            is_start = (match.end(1) == match.start(1))
            type = match.group(2)
    
            # <foo "bar"/> = <foo "bar">
            tagbody = match.group(4) or ''
            if tagbody.endswith('/'):
                tagbody = tagbody[:-1]
    
            args = tuple(re.findall(self._string_pattern, tagbody))
            start = match.start(0)
            end = match.end(0)
    
            if type in _tag_catalog:
                cls = _tag_catalog[type]
            else:
                cls = Tag
    
            return cls(self.file, type, is_start, args, start, end, contents)


#--  Translator  ---------------------------------------------------------------

##  Translates Ency-specific tags and entities to regular HTML.

class Translator (object):

    ##  Pattern for entities.
    entity_pattern = re.compile('&([A-Za-z.-]+);')

    ##  Constructor.

    def __init__ (self, ency):

        ##  The Ency object.
        self.ency = ency

        ##  The error method, which is actually a delayed error handler.
        self.error = DelayedErrorHandler()

        ##  How many math tags have been encountered.
        self.math_count = 0

        ##  How many latex tags have been encountered.
        self.latex_count = 0

    ##  Read from tokens; write to page.

    def __call__ (self, page, tokens):
        self.error.arm()
        for token in tokens:
            if isinstance(token, str):
                self.write_expanding_entities(token, page)
            else:
                token.render(page)

    ##  Write the given string to the file, but expand character
    #   entities as you go.

    def write_expanding_entities (self, string, file):
        entmap = self.ency.entmap
        offset = 0
        while offset < len(string):
            match = self.entity_pattern.search(string, offset)
            if match:
                i = match.start(0)
                j = match.end(0)
                if i > offset:
                    file.write(string[offset:i])
                key = match.group(1)
                if key in entmap:
                    file.write(entmap[key])
                else:
                    file.write(string[i:j])
                offset = j
            else:
                if offset < len(string):
                    file.write(string[offset:])
                    offset = len(string)


#--  EncyFile  -----------------------------------------------------------------

# Iteration over texts (strings) and tags

##  Reader for an Ency file (.xml).

class EncyFile (object):

    ##  Constructor.

    def __init__ (self, dir, name, suffix=None):

        ##  The directory.
        self.dir = dir

        ##  The file name.
        self.name = None

        ##  The suffix.
        self.suffix = None

        ##  The complete filename.
        self.filename = None

        ##  The title.
        self.title = None

        ##  The contents.  It is:
        #    - an XMLFile if the suffix is '.xml'
        #    - a TabularFile if the suffix is '.tab'
        #    - a DiskDirectory if the file is a directory
        #    - a RawFile otherwise.
        self.contents = None

        self._set_filename(name, suffix)
        # Contents initializer needs title to exist
        self._set_title()
        self._set_contents()
        
    ##  String representation.

    def __repr__ (self):
        return '<EncyFile %s %s %s>' % (repr(self.name), repr(self.suffix), repr(self.filename))

    def _set_filename (self, name, suffix):
        if suffix is None:
            (self.name, self.suffix) = self.dir.split_suffix(name)
        else:
            self.name = name
            self.suffix = suffix

        if self.suffix:
            tail = self.name + '.' + self.suffix
        else:
            tail = self.name

        self.filename = self.dir.join(tail)

    def _set_title (self):
        if self.name == 'index':
            self.title = self.dir.name
        else:
            self.title = self.name
        self.title = re.sub('_', ' ', self.title)

    def _set_contents (self):
        if self.suffix == 'xml':
            self.contents = XMLFile(self)
        elif self.suffix == 'tab':
            self.contents = TabularFile(self)
        elif os.path.isdir(self.filename):
            self.contents = DiskDirectory(self.dir.ency, self.name, self.filename)
        elif os.path.exists(self.filename):
            self.contents = RawFile(self.filename, self.suffix)
        else:
            raise PageNotFound('File not found: %s' % self.filename)

    ##  If the contents is a directory, returns a file by name.

    def __getitem__ (self, key):
        if isinstance(self.contents, Directory):
            return self.contents[key]
        else:
            raise Exception('EncyFile does not contain items')

    ##  Returns the Ency object from context.

    def ency (self):
        return self.dir.ency

    ##  Renders the contents onto the page.

    def render (self, page):
        self.contents.render(page)

    ##  Dispatches to the to_page() method of the contents.

    def to_page (self):
        return self.contents.to_page()


##  An XML file.

class XMLFile (object):

    ##  Constructor.

    def __init__ (self, file):

        ##  An EncyFile.
        self.file = file

        ##  The file title.
        self.title = self.file.title

        ##  An HTMLTokens object.
        self.tokens = None

        with open(file.filename, 'r', errors='backslashreplace') as f:
            contents = f.read()

        match = re.match(r'\s*<h1>([^<>]*)</h1>(\s*\n)?', contents)
        if match:
            self.title = match.group(1)
            contents = contents[match.end(0):]
        
        self.tokens = HTMLTokens(self.file, contents)

    ##  Convert to a page.  Creates a Translator and calls it.

    def to_page (self):
        page = HtmlPage(None, title=self.file.title)
        H1(page, self.file.title)
        trans = Translator(self.file.ency())
        trans(page, self.tokens)
        return page


##  A tabular file.

class TabularFile (object):

    ##  Constructor.

    def __init__ (self, file):

        ##  An EncyFile.
        self.file = file

        ##  The types of the columns.
        self.types = []

        ##  The number of visible columns.  ('html_class' columns are not visible.)
        self.nvisible = 0

        ##  The current line number.
        self.line_number = 0

        ##  Collected errors.
        self.errors = []

    ##  Append an error.

    def error (self, msg):
        self.errors.append('%s line %s: %s' % (repr(self.file), self.line_number, msg))

    ##  The number of columns; requires types to be set.

    def ncols (self):
        if self.types:
            return len(self.types)
        else:
            return 0

    ##  Set the number of columns.  If types has alread been set, n must be at
    #   least the number of types already listed.  'ascii' types will be added
    #   until the number of types equals n.

    def set_ncols (self, n):
        if self.types and len(self.types) != n:
            self.error('Inconsistent number of columns')
        if len(self.types) < n:
            for _ in range(n - len(self.types)):
                self.types.append('ascii')
                self.nvisible += 1

    ##  Render the table onto the given page.

    def render (self, page):
        with open(self.file.filename) as f:
            table = Table(page)
            for line in f:
                self.line_number += 1
                fields = line.rstrip('\r\n').split('\t')
                rectype = fields[0]
                print('READ', rectype)
                if rectype == 'T':
                    if len(fields) < 2:
                        self.error('T takes at least 1 field')
                    else:
                        self._set_types(fields[1:])
                elif rectype == 'H':
                    print('render header', repr(table), fields[1:])
                    self._render_header(table, fields[1:])
                elif rectype == 'S':
                    if len(fields) != 2:
                        self.error('S takes one field')
                    else:
                        self._render_section(table, fields[1])
                elif rectype == 'D':
                    self._render_record(table, fields[1:])
                elif rectype == 'W':
                    if len(fields) != 2:
                        self.error('W takes one field')
                    else:
                        table.set_attribute('width', fields[1])
                else:
                    self.error('Bad record type: %s' % repr(rectype))
        if self.errors:
            for err in self.errors:
                String(P(page), err)

    def _set_types (self, types):
        if self.types:
            self.error('Types specified multiple times')
        else:
            self.types = types
            self.nvisible = sum(1 for t in types if t != 'html_class')

    def _render_header (self, table, fields):
        n = len(fields)
        self.set_ncols(n)
        print('make row')
        row = Header(table)
        print('row=', repr(row))
        for i in range(n):
            if self.types[i] != 'html_class':
                String(Cell(row), fields[i])

    def _render_section (self, table, name):
        n = self.nvisible
        if n is None:
            self.error('Need to know number of columns before using S')
        row = Header(table)
        String(Cell(row, colspan=n), name)

    def _render_record (self, table, fields):
        n = len(fields)
        self.set_ncols(n)
        htmlclass = None
        for i in range(n):
            if self.types[i] == 'html_class' and fields[i]:
                htmlclass = fields[i]
        if htmlclass:
            row = Row(table, htmlclass=htmlclass)
        else:
            row = Row(table)
        for i in range(n):
            field = fields[i]
            type = self.types[i]
            if type == 'link':
                Link(Cell(row), field, field)
            elif type == 'node_if_exists':
                if field in self.file.dir:
                    Link(Cell(row), field, field)
                else:
                    String(Cell(row), field)
            elif type == 'ascii':
                String(Cell(row), field)
            elif type == 'html_class':
                pass
            else:
                self.error('Bad type: %s' % repr(type))


#--  Directory  ----------------------------------------------------------------
#
#  EncyFile uses Directory.split_suffix() and Directory.join() to determine its
#  filename.
#
#  It uses Directory.name to set its title.
#

##  The base class for directories.

class Directory (object):

    ##  Constructor.

    def __init__ (self, ency, name):

        ##  The Ency object.
        self.ency = ency

        ##  The name of the directory.
        self.name = name

    ##  Must be overridden by specializations.

    def join (self, tail):
        raise Exception('Specializations must override')

    ##  Just calls split_suffix() from seal.core.io.

    def split_suffix (self, tail):
        return split_suffix(tail)

    ##  Fetch a child file by name.

    def __getitem__ (self, name):
        page = EncyFile(self, name)
        if page is None:
            raise Exception('EncyFile %s/%s returned no page' % (self.name, name))
        return page

    ##  String representation.

    def __repr__ (self):
        return '<%s %s>' % (self.__class__.__name__, self.name)


##  A physical directory.

class DiskDirectory (Directory):

    ##  Constructor.

    def __init__ (self, ency, name, filename):
        Directory.__init__(self, ency, name)

        ##  The filename of the directory.
        self.filename = filename

    ##  Returns the filename of a descendant.

    def join (self, tail):
        return join(self.filename, tail)

    ##  If adding '.xml' yields an existing file, uses '.xml' as the suffix.
    #   Otherwise, splits the suffix off the filename.

    def split_suffix (self, tail):
        if os.path.exists(self.join(tail + '.xml')):
            return (tail, 'xml')
        else:
            return split_suffix(tail)

    ##  True if the filename names an existing file, or if adding '.xml' yields
    #   an existing file.

    def __contains__ (self, tail):
        if os.path.exists(self.join(tail + '.xml')):
            return True
        else:
            return os.path.exists(self.join(tail))

    ##  Returns a redirect to the page named 'index'.

    def to_page (self):
        return Redirect(join(self.filename, '/index'))


##  A virtual directory containing library files.

class LibDirectory (Directory):

    ##  Return the filename for the given citation number.

    def join (self, id):
        return self.ency.find_lib_file(id)


#--  Ency  ---------------------------------------------------------------------

##  A table containing Ency-specific character entities.

class EntityMap (object):

    ##  Constructor.

    def __init__ (self, ency):

        ##  The contents, a dict.
        self.table = tab = {}

        with open(join(seal_data, 'entities.txt')) as f:
            for line in f:
                (key, value) = line.split()
                # Expand out U+ values
                if value.startswith('U+'):
                    value = '#%d' % int(value[2:], 16)
                tab[key] = '&%s;' % value

        # Add directory names
        for (name, fn) in ency.directories.items():
            tab[name] = fn

    ##  Fetch a definition.

    def __getitem__ (self, key):
        return self.table[key]

    ##  Whether the given name is defined.

    def __contains__ (self, key):
        return key in self.table


##  The main Ency object.

class Ency (object):

    ##  Maps directory names to directory objects.
    #   Initially just 'file' and 'lib', but more are taken from the
    #   configuration file.  In particular, each item in the 'ency.dirs'
    #   list provides a directory.

    directories = {'file': (DiskDirectory, '/'),
                   'lib': (LibDirectory,)}

    ##  Constructor.

    def __init__ (self, _):

        ##  The entity map.
        self.entmap = None

        ##  The library path, obtaining by splitting the 'ency.libpath'
        #   configuration setting at colons.
        self.libpath = []

        ##  The CSS file, from the 'ency.css' configuration setting.
        self.css = None

        if 'ency' in config.environ:
            ency = config.environ['ency']
            if 'dirs' in ency:
                for (name, fn) in ency['dirs'].items():
                    self.directories[name] = (DiskDirectory, expanduser(fn))
            if 'libpath' in ency:
                self.libpath = ency['libpath'].split(':')
            if 'css' in ency:
                self.css = ency['css']

        self.entmap = EntityMap(self)

    ##  Get an item.

    def __getitem__ (self, name):
        if name == '': return Redirect('my/index2')
        else:
            ent = self.directories[name]
            cls = ent[0]
            args = ent[1:]
            return cls(self, name, *args)

    ##  Get a filename.

    def get_filename (self, type, specs, name, default=None):
        fn = specs.get(name)
        if fn is None:
            if default is None:
                self.error('No spec, no default for %s' % name)
            else:
                fn = default
        if fn is not None:
            fn = os.path.abspath(os.path.expanduser(fn))
            if len(fn) > 1 and fn[-1] == '/': fn = fn[:-1]
            if not os.path.exists(fn):
                self.error('Not found: %s' % fn)
            if os.path.isdir(fn): actual_type = 'dir'
            else: actual_type = 'file'
            if type != actual_type:
                self.error('Expected a %s: %s' % (type, fn))
        return fn
             
    ##  Find a library file.  Signals an error on failure.

    def find_lib_file (self, name):
        for dir in self.libpath:
            dir = expanduser(dir)
            fn = join(dir, name)
            if os.path.exists(fn):
                return fn
        raise Exception('Lib file not found: %s\nPath: %s' % (name, ', '.join(self.libpath)))




#         my = expanduser('~/git/spa/html')
# 
#         self.logical_dirs = {
#             'my' = my,
#             'cl': expanduser('~/git/cl/html'),
#             'per': expanduser('~/git/per/html'),
#             'arch': expanduser('~/archive'),
#             'addr': my,
#             'cite': 
# 
#         # <cl <clredirect <cite <citeredirect
#         self.cl_html = self.cl + '/txt/html'
# 
#         # <crs <crsredirect
#         self.crs = self.cl + '/txt/crs'
# 
#         # <doc <docredirect
#         self.doc_dir = self.clroot + '/txt/doc'
#         # <java
#         self.sys_javadoc_dir = self.clroot + '/txt/doc/java-docs-1.5.0/api'
#         # <javadoc
#         self.cl_javadoc_dir = self.clroot + '/txt/doc/cl'
#         # <lib
#         self.lib_dir = self.clroot + '/txt/lib'
# 
#         self.entity_map = None
# 
#         self.arch_path = arch
#         self.images_path = specs.get('images_path') or '.'
#         self.css_path = specs.get('css_path') or 'spa.css'
        
#     def dump (self):
#         print('outdir =', self.outdir)
#         print('myroot =', self.myroot)
#         print('archive_dir =', self.archive_dir)
#         print('my_html_dir =', self.my_html_dir)
#         print('per_html_dir =', self.per_html_dir)
#         print('cl_html_dir =', self.cl_html_dir)
#         print('crs_dir =', self.crs_dir)
#         print('doc_dir =', self.doc_dir)
#         print('sys_javadoc_dir =', self.sys_javadoc_dir)
#         print('cl_javadoc_dir =', self.cl_javadoc_dir)
#         print('lib_dir =', self.lib_dir)
#         print('arch_path =', self.arch_path)
#         print('images_path =', self.images_path)
#         print('css_path =', self.css_path)
#         print()
#         print('name =', self.name)
#         print('outfn =', self.outfn)
#         print('title =', self.title)
#         print()
#         self.error.dump()


#---------------------------------------------------------------------
#  Main
#

##  Converts a relative pathname to absolute.
#   os.path.abspath expands away symbolic links; this one doesn't.

def abspath (path):
    if os.path.isabs(path): return path
    else: return os.path.normpath(os.getenv('PWD') + '/' + path)


# def main ():
# 
#     flags = {'I': 'images_path',
#              'S': 'css_path'}
# 
#     specs = {}
#     action = 'translate'
# 
#     while shift.isflag():
#         flag = shift()
#         if len(flag) > 2: shift.error('Bad flag: %s' % flag)
#         flag = flag[1]
#         if flag in flags:
#             key = flags[flag]
#             value = shift()
#             specs[key] = value
#         elif flag == 'g':
#             action = 'dump'
#         else:
#             shift.error('Unrecognized flag: %s' % flag)
# 
#     specs['infn'] = shift()
#     if not shift.isdone():
#         specs['outdir'] = shift()
#     shift.done()
# 
#     ency = Ency(specs)
#     getattr(ency, action)()
#                           
# 
# if __name__ == '__main__':
#     main()



#-------------------------------------------------------------------------------
# entity_map = {
# 
#     'all':      '#8704',
#     'bottom':   '#8869',
#     'cap':      '#8745',
#     'cdot':     '#8729',
#     'circ':     '#8728',
#     'complex':  '#8484',
#     'cong':     '#8773',
#     'cup':      '#8746',
#     'dlarrow':  '#8656',
#     'drarrow':  '#8658',
#     'endash':   '#8211',
#     'emdash':   '#8212',
#     'emptyset': '#8709',
#     'equiv':    '#8801',
#     'exists':   '#8707',
#     'geq':      '#8805',
#     'grad':     '#8711',
#     'in':       '#8712',
#     'infty':    '#8734',
#     'int':      '#8747',
#     'invprod':  '#8720',
#     'invunif':  '#8852',
#     'larrow':   '#8592',
#     'leftarrow': '#8592',
#     'leftrightarrow':  '#8596',
#     'leq':      '#8804',
#     'lrarrow':  '#8596',
#     'minus':    '#8722',
#     'natural':  '#8469',
#     'neg':      '#0172',
#     'neq':      '#8800',
#     'nequiv':   '#8802',
#     'nexists':  '#8708',
#     'notin':    '#8713',
#     'partial':  '#8706',
#     'prod':     '#8719',
#     'propto':   '#8733',
#     'rarrow':   '#8594',
#     'sim':      '#8764',
#     'subd':     '#8847',
#     'subs':     '#8848',
#     'subdeq':   '#8849',
#     'subseq':   '#8850',
#     'sum':      '#8721',
#     'surd':     '#8730',
#     'top':      '#8868',
#     'ucdelta':  '#8710',
#     'unif':     '#8851',
#     'vee':      '#8744',
#     'wedge':    '#8743'
# 
# }
