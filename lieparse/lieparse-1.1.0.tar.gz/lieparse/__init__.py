#!/usr/bin/env python3
""" Liepa Parser: HTML parser ant text retriever using user defined rule set
© 2019-2020 Vidmantas Balčytis

HISTORY
Library was initially written for Vilnius University Liepa-2 project.
Although LIEPA is an abbreviation of project name, in Lithuanian Liepa means "Linden tree".
The tree image is in projects logotype also.

QUICK USAGE
Lets say you have HTML markup text read into string HtmlText.
Then to retrieve all text from division with id="main" you need to:

from lieparse import lieParser
rules = '<div id="main">$Data[]</div> ::$Data[];'
parser = lieParser(rules)
parser.feed(HtmlText)
parser.close()

More sophisticated example can be found after rules syntax definitions.

RULES SYNTAX
Rules consist of statements optionally separated by white space.
White space is considered space, tab, new line and comment.
Comment begins from # sign and lasts to line end.
(Concretely regex match r'(?:\s*(?:#.*?\n)?)*\s*')
Statements can contain incorporated statements and data definitions.

Statements are:
Rep statement - loops matching all incorporated statements:
    #(<<other statements>>)
    #+(<<other statements>>)
    *(<<other statements>>)
    where:
        # is optional numeric value and means repeat count
        + is one-or-more modifier. If standing alone is same as 1+
        * is zero-or-more modifier. Cannot be preceded by number

If ``*`` modifier was specified or when ``+`` modified statement reaches zero count,
statement exits on first match of logical statements following *Rep* construct
(or of course after enclosing *Tag* ends).
In version 1.1.x such *Break* statement has higher priority than internal *Rep*
statements. Earlier if same statement matched as *Rep* or as *Break* it was
considered as a part of *Rep* statement.

If number or '+', '*' modifiers are found before other statements (Tag or Any), repeat block
is generated automatically. So writing '2<div></div>' is automatically converted to
'2(<div></div>)'.

Any statement - matches any of incorporated statements:
    {<<other statements>>}
    Any-match is done by statements definition order until first one matches.
    Statement can contain Any, Tag or Rep statements. Print statement is not allowed here.

Tag statement - main matching statement the html text is checked onto:
    <name attr="string" $aData[<<aData attrs>>] >
        <<filterStr>> $Data[<<Data attrs>>] <<other statements>>
    </name>
    where:
        name is tag name, something like 'div', 'li', 'span'.
        attr is optional and optionally multiple attribute that must be present in html
            tag to be matched. Real tag must contain all, but maybe not only, specified attributes
            to match this rule. If attribute in html tag has no value, in rule it must be
            specified with empty string as a value.
            class="" attribute is split by whitespace into sets while parsing rule as well
            as while parsing html. Rule attribute set must be html attribute subset to match.
            style="" attribute is handled similarly, but splitting on ';' and replacing
                multiple white space to single space and stripping spaces before adding to set.
        $aData is optional and optionally multiple attribute data definition. Can be
            indirect data ($*data[]) also. Definition follows. Data variable name must
            insensitive match regular expression '[a-z]+[a-z0-9_]*'
        filterStr is optional tag data filtering string. If enclosed in '/' marks -
            regular expression match is performed against Tag data. If simple string -
            full match is performed (i.e. "My data" is equivalent to "/^My data$/").
            If tag data is not matched - tag is considered not matching.
        $Data is optional and optionally multiple data collection attribute. Can be
            indirect data ($*data[]) or to-first-tag data ($data[!]) or both.
        Statement can incorporate other statements (Rep, Any, Tag, Print) mixed with
            $Data definitions

Print statement - only facility to output gathered data:
    :<<flags>> <<loopDef>>:<<"string">> $pData[<<pData attrs>>] <<Other print statements>> ;
    where:
        flags is optional print behavior modifiers - string (no quotes) containing one or
        more flag letters. Next flags are defined:
            n - print new line after full print statement
            N - print new line after each individual loop of print statement
            s - separate each print value with space
            U - convert output to UPERCASE
            u - capitalize output words
            l - convert output to lowercase
            A - redirect output to stream A, can be specified, defaults to sys/stdout
            B - redirect output to stream B, can be specified, defaults to sys/stdout
            C - redirect output to stream C, can be specified, defaults to sys/stdout

        stream parameters are spread to child items but child item can have stream redefined

        loopDef is expression defining how much times print body will be performed. If not
            specified it defaults to 1. If defined - it is counted at run time depending
            on real data. Loop counter is from 0 up-to loopDef. On run time current loop counter
            can be accessed in index expressions as $0. Outer loop statements counter is
            accessible as $1 for first surrounding print statement, $2 for second and so on, the
            last being ourselves (so same as $0).
            loopDef can be one of next:
                indexExpr - countable expression (look below) with $# as surrounding
                    loop counters, numbers, parenthesis and arithmetic operations '+', '-', '*'
                    and (form version 1.1.0) C-style ternary operators.
                empty - index is set to 1

        string is optional string that will be printed

        pData is data variable name (can be indirect: $*pData) from which data will be printed
            Full definition is below.

    string, pData and other print statements can be freely mixed inside print statement body.

indexExpr - countable expression, that can be used in print statement loop definition and
    in pData (print statement data) definition.
    indexExpr is countable expression with $# as surrounding loop counters, numbers,
    parenthesis and arithmetic operations '+', '-', '*'

    Valid indexExpr's:
        3
        $2 + 1
        ($1 + 1) * 2
        $Data - 1

Data definitions can be found inside Tag definition (aData), inside Tag body (dData and xData)
    and print statement (pData). Data reference (without []) can be found in print loopDef.

    pData can not be modified - information is only retrieved from named variable.
    Other types of Data is dedicated to collect data from html text.

    All data variables are arrays. After definition (even if it occurs with '+' sign) array
    pointer is 0. Pointer can be incremented by '+' sign in variable attributes. Pointer can
    never be decremented. '-' sign in attributes clears variable data, leaving index unchanged.

    '!' in attributes defines xData instead of dData.

    Variables can be direct:
        $<<name>>[<<attr>>] - defines variable named <<name>>

    and indirect:
        $*<<name>>[<<attr>>] - here name of variable is kept in last element of array $<<name>>[]

    Only one level of indirection is allowed.

    <<attr>> and behavior differs depending on variable scope (aData, dData, xData or pData).
    However in all scopes accessed data is same for same named variable.

For aData, dData and xData:
    <<attr>> consists of optional flag with values '!', +' or '-' and optional space separated
        strings.
    If flag is:
        '!' - xData type variable is defined. Valid only for variables inside Tag body.
        '+' - index value is incremented before other operations. The exception is if variable is
                first time defined - in this case index is left 0.
        '-' - all data accumulated in variable by current index is cleared before other operations.
    When no flag is present, data is appended to variable by current index.
    String can be enclosed in double quotation marks. This allows strings with spaces.
    If no strings are defined - passed data is simply added to variable.

    String can be:
        /<<match>>/         - if passed data not matches regular expression it is ignored. All other
            strings are not processed

        /<<find>>/<<repl>>/ - if <<find>> regular expression matches passed data, it is replaced
            with <<repl>> and got data added to variable. On no match - data is ignored. Other
            strings are processed with all data passed to them.

       +/<<find>>/<<repl>>/ - if <<find>> regular expression matches passed data, it is
            replaced with <<repl>> and got data added to variable. On no match - original
            data is added to variable. Always must be enclosed in quotation marks. New in 1.1.0.
            After replace other processing strings (if any) get replaced, not original data.

        @<<attrName>>       - Value of specified Tag attribute is added to variable.

        <<otherString>>     - specified string is added to variable.

    Data passed to variables is:
        aData - all Tag attributes with names as name="value". If there is some class values
            they are passed as separate class="value" pairs.
        dData - all accumulated data in this and above Tag levels.
        xData - all accumulated data up to first sub-tag match.

For pData:
    <<attr>> can be one of next forms:
        <<indexExpr0>>;<<indexExpr>> <<regexps>>  - for indirect variables only or
        <<indexExpr>> <<regexps>>                - for all variables
    <<indexExpr>> - is optional array index value at which will be printed. If not specified
            defaults to $0
    <<indexExpr0>> - is optional parent array index from which variable name is taken.
            Defaults to $0.
    <<regexps>> is optional regular expressions in form /<<find>>/<<repl>>/
            All expressions are applied to data value before print by order of appearance.

SYSTEM VARIABLES

From version 1.1.0 we have defined some global system variables. If found anywhere in text variable
name is replaced with it's value. You can use command line (or #!flags) option --no-vars-expand
if such behavior is undesirable. Another workaround is shown in example lieparse3_rule.txt
based on extracting data from this chapter.

Defined system variables:

   $URL       -  full URL of site we are examining
   $PROTO     -  protocol of site (http:// or https://)
   $BASEURL   -  base URL of site
   $BASEURLNP -  base URL of site without port number. If no port specified - same as $BASEURL
   $PORT      -  port number. If not specified, empty string
   $DATE      -  date the extracting program is being run (as returned by strftime("%x"))
   $TIME      -  time, program is running (as returned by strftime("%X"))
   $DATETIME  -  date and time, program is running (as returned by strftime("%c"))

Parsing parameters inside rules file

Starting with version 1.1.0 you can define parsing parameters inside rules file.
Older versions treats this as comment.

Syntax is: ``#!<<parameter name>> <<space separated parameter values>>``

Do not define parameters in first file line - Linux shell will treat that as executable file definition.

Next parameters are recognized::

   url      -  location to parse URL
   href     -  same as above. If both specified, first found is used
   winurl   -  URL for Windows systems. Normally used with file:// references
   winhref  -  same as above
   linurl   -  URL for Linux systems. Normally used with file:// references
   linhref  -  same as above
   usragent -  user agent. Can be specified by name or by value
   fromurl  -  set URL we are coming from
   flags    -  specify list of space separated behavior flags. Next are defined:
      ssl-verify, dump-rules, dump-vars, dump-json, dump-json-np, no-vars-expand
   output-file[ABCE]? see LiepaParse -h for definition
   time-locale - specify locale for system time variables $DATE, $DATETIME and $TIME

ADVANCED EXAMPLE
    We will retrieve python library names from https://docs.python.org/3.6/py-modindex.html

    import sys
    from lieparse import lieParser
    from pycurl import Curl, global_init, global_cleanup, GLOBAL_ALL
    usragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"
    url = "https://docs.python.org/3.6/py-modindex.html"
    rules = r'''
    <table class="indextable modindextable">
        *<code class="xref">
            $Data[+]
        </code>
    </table>
    :N $Data:$Data[];     # if flags are ns we will have space separated list
    '''

    global_init(pycurl.GLOBAL_ALL)
    c = Curl()
    c.setopt(c.USERAGENT, usragent)
    c.setopt(c.SSL_VERIFYPEER, 0)      # have problems verifying certificate under Windows
    c.setopt(c.URL, url)
    s = c.perform_rs()
    global_cleanup()

    parser = lieParser(rules)
    parser.feed(s)
    v = parser.close()
    if v != 0:
        print("Unmatched {} items".format(v), file=sys.stderr)

"""

import  sys
import  os
import  string

import  regex as re

DEBUG = True
NO_TRACE = False

# Attributes that must be separated to dictionary
_split_attrs={"class"}      # Split by space
_split_attrs1={"style"}     # Split by ';' and strip


#*************************************************************************
class CodeError(Exception):
    def __init__(self, value = None):
        self.value = value
        if NO_TRACE:
            sys.tracebacklimit=0
    def __str__(self):
        return "Code ERROR: " + self.value

#*************************************************************************
class SyntaxError(Exception):
    """Indicates syntax error encountered while parsing definitions"""
    def __init__(self, lipo, value = None):
        self.li, self.po, self.estr = lipo
        self.value = value
        if NO_TRACE:
            sys.tracebacklimit=0
    def __str__(self):
        return "Syntax ERROR at line {} pos {}: {}.\n{}".format(self.li, self.po, self.value, self.estr)

#*************************************************************************
class VarUndefError(Exception):
    """Indicates variable undefined error while processing indirect variable"""
    def __init__(self, lipo, value = None):
        self.li, self.po, self.estr = lipo
        self.value = value
        if NO_TRACE:
            sys.tracebacklimit=0
    def __str__(self):
        return "Indirect variable undefined ERROR at line {} pos {}: {}.\n{}".format(self.li, self.po, self.value, self.estr)


#*************************************************************************
class EofError(Exception):
    def __init__(self, value = None):
        self.value = value
        if NO_TRACE:
            sys.tracebacklimit=0
    def __str__(self):
        return "Unexpected end of data ERROR: {}.".format(self.value)

#*************************************************************************
class VarsClass(object):
    """Holds all defined variables"""

    def __init__(self):
        """Initializes new class for holding data objects

        No initialization attributes assumed
        """
        self.vals = {}


    def addVar(self, name, value = None):
        """adds new member to named variable if not exist

            Parameters:
                name  :  name of variable
            Returns: variable value (list)
        """
        if name not in self.vals:
            self.vals[name] = []
        return self.vals[name]

    def setVar(self, name, val):
        """set named variable value

            Parameters:
                name  :  name of variable
                val   :  value to set - normally it is list
        """
        self.vals[name] = val

    def getVar(self, name):
        """get variable from array. Same as addVar but error if not initialized

            Parameters:
                name  :  name of variable
            Returns:  variable value (list)
        """
        return self.vals.get(name)      # Returns None if name is not defined

    def count(self, cb):
        """counts all accumulated data and puts it into VarsClass array
           Function called after filtering is done
        """
        for cid, name, idx, data in cb:      # (cid, name, idx, data) idx == 1 for '+', == 2 for '-'
            if cid == set():
                continue
            v = self.addVar(name)       # add variable if not exists, return it (list)
            if idx == 1:
                v.append("")
            if len(v) == 0:             # autoinit on first use
                v.append("")
            if idx == 2:
                v[len(v) - 1] = ""
            v[len(v) - 1] = (v[len(v) - 1] + " " + data).strip()
            self.setVar(name, v)

    def dump(self, file = None):
        """dump all defined variables"""
        from shutil import get_terminal_size
        cols = get_terminal_size((80, 20)).columns
        outfile = file if file is not None else sys.stderr
        for n in self.vals:
            print("%s:" % n)
            lin = 0
            for v in self.vals[n]:
                sublines = []
                w = cols - 10
                while True:
                    nlpos = v.find('\n')
                    if nlpos > 0 and nlpos <= w:
                        sublines.append(v[:nlpos])
                        v = v[nlpos+1:]
                    elif len(v) > w:
                        sublines.append(v[:w])
                        v = v[w:]
                    elif len(v) > 0:
                        sublines.append(v)
                        v = ""
                    if v == "":
                        break
                first_line = True
                for sl in sublines:
                    if first_line:
                        print("{: >7}:  {}".format("[%s]" % lin, sl), sep = "", file = outfile)
                    else:
                        print(10*" "+ sl, sep = "", file = outfile)
                    first_line = False
                lin += 1
            print(file = outfile)

    def dump_json(self, file = None, pp = False):
        """Dumps variables as JSON

            Parameters:
                file = sys.stderr  :  file to write to
                pp = False         :  use prety-print, default No
        """
        import json
        outfile = file if file is not None else sys.stderr
        if pp:
            print(json.dumps(self.vals, sort_keys=True, indent=4), file = outfile)
        else:
            print(json.dumps(self.vals), file = outfile)

#*************************************************************************
class Base(object):
    """Base class for all other Liepa Parser classes"""

    _sP = r'(?:\s*(?:#.*?\n)?)*\s*'
    _re_skipspc = re.compile(_sP, re.A)
    _re_is_xData = re.compile(r'([a-z]+[a-z0-9_]*)\['+_sP+r'!', re.I | re.A)
    _re_datavar = re.compile(r'([a-z]+[a-z0-9_]*)\['+_sP+r'!?'+_sP+r'([+-]?)'+_sP+r'(?:(".*?"|[^\s"\]]+)'+_sP+r')*\]', re.I | re.A)
    _re_tagname = re.compile(_sP+r'<'+_sP+r'([a-z]+[a-z0-9_.]*)[\s>]', re.I | re.A)
    _re_attrname = re.compile(_sP+r'([a-z]+[a-z0-9_]*)'+_sP+r'='+_sP+r'(".*?"|[^\s>]*)[\s>]', re.I | re.A )
    _re_string = re.compile(_sP+r'(".*?"|/.*?/)(?:'+_sP+r'|[>$])', re.I | re.A)
    _re_tagend = re.compile(r'<'+_sP+r'/'+_sP+r'([a-z]+[a-z0-9_]*)'+_sP+r'>', re.I | re.A)
    _re_repbeg = re.compile(_sP+r'([0-9]*\+?|\*)'+_sP+r'([(<{])', re.I | re.A)
    _re_convspc = re.compile(r'(\s+)', re.A)
    _re_resvar = re.compile(r'(\$[A-Z]+)([^A-Za-z0-9_]|$| )', re.A)

    _incId = 0

    def __init__(self, master = None, data = None):
        self.isCopyOf = None        # contains id() of original object for speculative wait classes
        self.memberList = []        # Pointers to classes Rep, Any, Tag, Data
                                    # if some Data classes goes in line,
                                    # same data is passed to all of them
        if master is None:          # Master class
            if DEBUG and data is None:
                raise   CodeError("data and master cannot be both None in Base class init")
            self.master = self
            self.root = self
            self.data = data.rstrip() + "\n"        # need for comments (#.*?\n) to work in last line
            self.maxpos = len(self.data)
            self.pos = 0
            self.counter = []   # Class variable for data counting. Contains (cid, name, idx, data) from Data classes
                                # id is unique number used to rewind back all counting.
                                # if id == 0 - counting is invalid: was rewound
        else:
            if DEBUG and data is not None:
                raise   CodeError("setting data when master is not None in Base class init has no sense")
            self.master = master
            self.root = self.master.root
        self.rewindId = self.incId
        self._resetScan()

    def _rewindCounterId(self, id):
        """discard all counting that were done with specific id"""
        for idx in range(0, len(self.root.counter)):
            if id in self.root.counter[idx][0]:
                a = [set()]
                a.extend(self.root.counter[idx][1:])
                self.root.counter[idx] = tuple(a)

    def _rewindCounter(self):
        """discard all counting that were done with current id"""
        self._rewindCounterId(self.rewindId)
        self.rewindId = self.incId

    @property
    def incId(self):
        """Each time referenced return unique integer value"""
        Base._incId += 1
        return Base._incId


    def copy(self, cl = None):
        """copy class and return new instance of it"""
        if cl is None:
            cl = Base(master = self.master)
        cl.memberList = [c.copy() for c in self.memberList]
        cl.rewindId = self.rewindId
        return cl

    def close(self):
        """finalize all. Used only in up-level Rep class"""
        pass

    def _resetScan(self):
        """resets scan parameters

            Resets all parameters to initial state, so class can be reused
                on another match: in another Rep loop or after non match detected
        """
        for m in self.memberList:
            m._resetScan()
        self._isMatched = False
        self.inTag = 0

    @property
    def isMatched(self):
        """Getter/setter for isMatched flag"""
        return self._isMatched

    def _set_isMatched(self, matched):
        """real worker for isMatched setter"""
        self._isMatched = matched

    @isMatched.setter
    def isMatched(self, matched):
        self._set_isMatched(matched)


    def __str__(self):
        return "<class {}>".format(self.__class__.__name__)

    def _getErrPos(self, p = None):
        """Recounts error position from absolute to line/pos based

            Returns:  pair with line and position in line and line itself with marked position
        """
        if p is None:
            p = self.root.pos
        li = 1
        po = 0
        estr = ''
        while True:
            ll = self.root.data.find("\n", po)
            estr = self.root.data[po:ll] if ll >= 0 else self.root.data[po:]
            if ll >= 0 and ll < p:
                po = ll + 1
                li += 1
            else:
                po = p - po + 1
                break
        if estr != '':
            s = estr.lstrip()
            n = po - (len(estr) - len(s)) - 1
            estr = s + '\n' + ' '*n + '^'
        return (li, po, estr)

    @staticmethod
    def _isRep(c):
        """Check for repeat block implicit/explicit definition

            Parameters:
                c  :  first character of parser to be matched
            Returns:  True - if rep is implicitly or explicitly defined
        """
        return c.isdigit() or c == '(' or c == '*' or c == '+'


    def _skipSpc(self):
        """Skips to first no-space character

            Returns:  character in current position or None if data over
        """
        m = self._re_skipspc.match(self.root.data[self.root.pos:])
#        if m:               # FIXME: never can be none - empty string matches
        self.root.pos += m.end()
        if self.root.pos < self.root.maxpos:
            return self.root.data[self.root.pos]
        raise EofError("_skipSpc")

    def _skipNSpc(self):
        """advances one character up and then skips spaces

            Returns:  character in current position or None if data over
        """
        if self.root.pos < self.root.maxpos - 1:
            self.root.pos += 1
            return self._skipSpc()
        raise EofError("_skipNSpc")

    @staticmethod
    def _stripspc(data):
        """Local function used to accumulate data

            Parameters:
                data  :  entry string
            Returns:  string with all white spaces replaced to one space
        """
        return Base._re_convspc.sub(" ", data).strip()


    def _parse(self):
        self._skipSpc()

    def printTree(self, n = 0):
        """Print syntax definitions tree"""
        for m in self.memberList:
            print("  "*n, m, sep = '')
            m.printTree(n+1)

    def _findById(self, i):
        """find element by id()

            Parameters:
                i  :  id() of element
            Returns:  pair (self, idx) where idx is index in memberList[]
                None if not found in this class list
        """
        for idx in range(0, len(self.memberList)):
            m = self.memberList[idx]
            if id(m) == i:
                return(self, idx)
            v = m._findById(i)
            if v is not None:
                return v
        return None

    def _getNextToMatch(self, idx):
        """get next class to match if current is *() class (Rep with repCount == -1)

            Parameters:
                idx  :  index of current class we are trying to match in memberList[]
                class is of *() type
            Returns:  list of classes that on match should break *() block

            Our classes can be:
                - next non Data class in our list
                    - if next is *() - consider one more next also
                - if search for classes hit end of list
                    - ... and we are in () class, but repCount != -1
                        - consider classes from list beginning while it is not us
                    - ... and we are in *() class
        """
        waitfor = []
        begneeded = isinstance(self, Rep)
        if not isinstance(self, Any):                       # Need class from same level for Rep and Tag
            for i in range(idx + 1, len(self.memberList)):  # Get first non Data class in our list
                m = self.memberList[i]
                if isinstance(m, (Data, Print)):
                    continue
                # Have next class. Tag and Any - fit needs.
                if m.isCopyOf == 0:         # mangled class
                    m = m.memberList[-1]
                waitfor.append(m)
                if not isinstance(m, Rep) or m.repCount != -1:
                    begneeded = False
                    break
            if begneeded:           # we are Rep class and need block from beginning of us
                if self.repCount != 1:     # we are in *()
                    for i in range(0, idx):
                        m = self.memberList[i]
                        if isinstance(m, (Data, Print)):
                            continue
                        # Have next class. Tag and Any - fit needs.
                        if m.isCopyOf == 0:         # mangled class
                            m = m.memberList[-1]
                        waitfor.append(m)
                        if not isinstance(m, Rep) or m.repCount != -1:
                            break
                # Get from master if at end of tag
                if id(self) != id(self.master) and \
                    (isinstance(self, Rep) and \
                        (self.repCount == -1 or self.repCount == 1)): # can leave rep
                    for i in range(0, len(self.master.memberList)):
                        if id(self.master.memberList[i]) == id(self):
                            waitfor.extend(self.master._getNextToMatch(i))
                            break
        return waitfor

    def _mangle(self):
        """mangle memberList[] chain and change *() blocks
        to Any blocks containing () and blocks that will
        break *() matching if matched
        """
        for idx in range(0, len(self.memberList)):
            m = self.memberList[idx]
            m._mangle()
            if isinstance(m, Rep) and not m.isMatched and m.repCount == -1:
                l = self._getNextToMatch(idx)       # List with matches that breaks *()
                if len(l) > 0:
                    a = Any(self)
                    m.master = a
                    a.memberList.append(m)
                    for n in l:
                        k = n.copy()
                        k.isCopyOf = id(n)
                        k.master = a
                        a.memberList.insert(0, k)      # For priority put before m
                    a.isCopyOf = 0
                    self.memberList[idx] = a
                    for i in range(1, len(a.memberList)):
                        a.memberList[i]._mangle()

    def _unmangle(self):
        """undo mangle operation

        Called after some block inside mangled {} block has matched or
        some () block has matched and it's repCount has changed to -1
        """
        for idx in range(0, len(self.memberList)):
            m = self.memberList[idx]
            if m.isCopyOf == 0:          # Mangle group
                n = m.memberList[-1]
                n.master = self
                self.memberList[idx] = n
            self.memberList[idx]._unmangle()

    def _starttag(self, tag, atd, notForTags = False):
        """entered when HTMLParser has encountered start tag

            Parameters:
                tag  :  name of tag found
                atd  :  dictionary of attributes
        """
        print("Start tag:", tag)
        print("     attr:", atd)

    def _endtag(self, tag):
        """entered when HTMLParser has encountered end tag

            Parameters:
                tag  :  name of end tag found
            Default behavior is to print tag
        """
        print("End tag  :", tag)

    def _gotdata(self, data):
        """entered when HTMLParser has encountered data tag

            Parameters:
                data  :  string data
            Default behavior is to print data
        """
        print("Data     :", data)

    def _tagMatched(self, data):
        """called on tag match for each class in list upto
                matched Tag class itself

            Purpose is to inform xData classes to finish accumulate data
        """
        pass

#*************************************************************************
class Rep(Base):
    """Repeat block.
        used to define all outer program as well as repeat blocks
        Has next main fields:
            count: if positive - repeat count, if negative - '*'
                    decrements after each pass. If == 0 - finished
        Class memberList can contain only Tag, Any or other Rep classes
    """

    def __init__(self, master = None, data = None, url = None, locale = None):
        self.count = 1
        self.mangled = False
        self.url = url
        self.noExpand = False
        super().__init__(master = master, data = data)
        if data is not None:
            self.outfile = [sys.stdout for i in range(0,4)]
            self.outfile.append(sys.stderr)
            self.staticDict = {}        # for staticaly expanded URLs
            self.setURL(url, locale)    # set URL related and run time
            self._parse1(2)

    def __str__(self):
        return "<class {}: count = {}>".format(self.__class__.__name__, self.count)

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
        self.repCount = value

    def _set_isMatched(self, matched):
        """real worker for isMatched setter"""
        self._isMatched = matched
        if matched:
            if self.master.isCopyOf is None:          # we are not in mangled block
                root = self.root
                root._unmangle()
                for m in self.memberList:
                    if isinstance(m, Print):
                        m.isMatched = True
                if self.repCount > 0:
                    self.repCount -= 1
                elif self.repCount < -1:
                    self.repCount += 1
                rc = self.repCount
                self._resetScan()               # Sets repCount to count, what is not we need
                self.repCount = rc              # Restore repCount
                if self.repCount == 0:
                    self._isMatched = True
                self.rewindId = self.incId
                root._mangle()
        else:
            for m in self.memberList:
                m.isMatched = False
            self._rewindCounter()
            self._resetScan()

    def copy(self, cl = None):
        """copy class and return new instance of it"""
        if cl is None:
            cl = Rep(master = self.master)
        cl.count = self.count
        cl.repCount = self.repCount
        return super().copy(cl)

    def _resetScan(self):
        """resets scan parameters"""
        super()._resetScan()
        self.repCount = self.count          # restore passed count

    def _parse1(self, expdef):
        """used for top level block definition

            Parameters:
                expdef = 0  :   Class explicitly started with '('
                expdef = 1  :   Class for one Tag or Any
                expdef = 2  :   First class - ends on file end
            Returns:  position for parsing
        """
        # Finished with count and group definition. Get member(s)
        while True:
            try:
                c = self._skipSpc()
            except EofError:
                if expdef == 2:
                    break
                raise
            if c == '<':                        # Tag
                dt = Tag(self)
            elif c == '{':                      # Any group
                dt = Any(self)
            elif self._isRep(c):                # Rep
                dt = Rep(self)
            elif c == ')':
                if expdef == 0:
                    self.root.pos += 1
                    break
                raise SyntaxError(self._getErrPos(), "unexpected ')'")
            elif c == ':':                      # Print
                dt = Print(self)
            else:
                raise SyntaxError(self._getErrPos(), "unknown symbol {}".format(c))
            dt._parse()
            self.memberList.append(dt)
            if expdef == 1:
                break

    def _parse(self):
        """Parses one full Rep entry

            Returns:  position in line after _parse is done
            Entry to parser is done after number or '(' is detected
            Parse pointer shows to first symbol of interest
            Rep can contain classes: Rep, Tag, Any
        """
        m = self._re_repbeg.match(self.root.data[self.root.pos:])
        if not m:
            raise SyntaxError(self._getErrPos(), "invalid Rep definition")
        rep = m.group(1)
        if rep != "":                   # default is 1
            if rep == "*":
                self.count = -1
            else:
                if rep[-1] == '+':
                    if len(rep) == 1:
                        self.count = -2     # only "=" same as "1+"
                    else:
                        self.count = - (1 + int(rep[0:-1]))
                else:
                    self.count = int(rep)
        expdef = 0                      # assume '(' specified
        self.root.pos += m.end()
        if m.group(2) != '(':           # explicit definition
            expdef = 1
            self.root.pos -= 1
        ### From here is dropped to subroutine _parse1 - needed for top class init
        self._parse1(expdef)

    def _starttag(self, tag, atd, notForTags = False):
        """entered when HTMLParser has encountered start tag

            Parameters:
                tag  :  name of tag found
                atd  :  dictionary of attributes
        """
        if self.isMatched:
            return
        if id(self.master) == id(self) and not self.mangled:
            self.root._mangle()
            self.mangled = True
        for m in self.memberList:
            if not m.isMatched:         # Ready
                m._starttag(tag, atd)
                break

    def _endtag(self, tag):
        """entered when HTMLParser has encountered end tag

            Parameters:
                tag  :  name of end tag found
        """
        if self.isMatched:
            return
        for m in self.memberList:
            if not m.isMatched:         # Ready
                m._endtag(tag)
                break
        # check all matched
        for m in self.memberList:
            if not m.isMatched:         # Ready
                return
        # All tags are matched - mark all as matched
        self.isMatched = True

    def _gotdata(self, data):
        """entered when HTMLParser has encountered data tag

            Parameters:
                data  :  string data
        """
        if self.isMatched:
            return
        for m in self.memberList:
            if not m.isMatched:         # Ready
                m._gotdata(data)
                break

    def close(self):
        """finalize all. Used only in up-level Rep class"""
        unmatched = 0
        u = False
        if id(self.master) == id(self) and not self.isMatched:
            for m in self.memberList:
                if not m.isMatched:
                    u = True
                    m.isMatched = False
                    if isinstance(m, Rep) and m.repCount == -1 or m.isCopyOf == 0:
                        continue
                    unmatched += 1
                elif u and isinstance(m, Print):
                    m.isMatched = True
        return unmatched

    def setURL(self, url, loc = None):
        """set static parameters from passed url

            Parameters:
                url  :  url we will go to
            Returns:  none
            Counts and sets next ststic parameters:
            $URL - this url
            $BASEURL - protocol and site only
            $PROTO - protocol (eg. https://"")
        """
        m = re.match(r'([A-Za-z]+://)', url)
        n = re.match(r'([A-Za-z]+://[^/?#:]*)(:[0-9]*)?', url)
        if not m or not n:
            raise  CodeError("invalid URL")
        self.staticDict["$PROTO"] = m.group(1).lower()
        self.staticDict["$BASEURLNP"] = n.group(1).lower()
        self.staticDict["$BASEURL"] = n.group(1).lower() + (n.group(2) if n.group(2) is not None else "")
        self.staticDict["$PORT"] = n.group(2)[1:] if n.group(2) is not None else ""
        self.staticDict["$URL"] = n.group(1).lower() + url[n.end(1):]
        from datetime import datetime
        if loc is not None:
            from locale import setlocale, LC_TIME
            try:
                setlocale(LC_TIME, loc)
            except:
                pass
        n = datetime.now()
        self.staticDict["$DATE"] = n.strftime("%x")
        self.staticDict["$TIME"] = n.strftime("%X")
        self.staticDict["$DATETIME"] = n.strftime("%c")


#*************************************************************************
class Any(Base):
    """Any of selections block
        Main attributes:
            memberList - inherited from Base
            memberList can contain next classes: Tag, Rep
                No Any or Data allowed
            It is treated differently - on waitFor returns list of all tags
    """
    def __init__(self, master):
        super().__init__(master = master)

    def __str__(self):
        return "<class {}>".format(self.__class__.__name__)

    def _set_isMatched(self, matched):
        """real worker for isMatched setter"""
        self._isMatched = matched
        if matched:
            machfound = False
            for m in self.memberList:
                if not machfound and m.isMatched:
                    machfound = True
                else:
                    m.isMatched = False
            if self.isCopyOf == 0:          # matched in mangled block
                rep = self.memberList[-1]
                root = self.root
                if rep.isMatched:
                    root._unmangle()
                    rep.isMatched = True    # Another processing if Rep is not in mangled block !!!
                    root._mangle()
                else:                       # match break block
                    rep._isMatched = True   # Set attribute only, skipping all processing
                    for i in range(0, len(self.memberList) - 1):
                        k = self.memberList[i]
                        if k.isMatched:                 # speculatively matched - find origin and replace
                            cl, j = root._findById(k.isCopyOf)     # class and index in memberList
                            k.isCopOf = None
                            k.master = cl
                            cl.memberList[j] = k
                            break
                    root._unmangle()
                    root._mangle()
            else:
                self.rewindId = self.incId
        else:
            for m in self.memberList:
                m.isMatched = False
            self._rewindCounter()
            self._resetScan()

    def copy(self, cl = None):
        """copy class and return new instance of it"""
        if cl is None:
            cl = Any(master = self.master)
        return super().copy(cl)

    def _parse(self):
        """Parses one full Any entry
            Returns:  position in line after _parse is done
            Entry to parser is done after '{' is detected.
            Parse pointer shows to '{' sign.
        """
        self.root.pos += 1                       # skip '{'
        while True:
            c = self._skipSpc()              # find next val
            if c == '<':                    # Tag
                dt = Tag(self)
            elif self._isRep(c):      # Rep
                dt = Rep(self)
            elif c == '}':
                self.root.pos += 1
                return
            else:
                raise SyntaxError(self._getErrPos(), "expected '}'")
            dt._parse()
            self.memberList.append(dt)

    def _starttag(self, tag, atd, notForTags = False):
        """entered when HTMLParser has encountered start tag

            Parameters:
                tag  :  name of tag found
                atd  :  dictionary of attributes
        """
        for m in self.memberList:
            if not m.isMatched:         # Ready
                m._starttag(tag, atd)

    def _endtag(self, tag):
        """entered when HTMLParser has encountered end tag

            Parameters:
                tag  :  name of end tag found
        """
        matched = False
        for m in self.memberList:
            if m.isMatched:             # Have matched
                raise CodeError("a priory matched in Any class")
            m._endtag(tag)
            if m.isMatched:
                matched = True
                break           # Matched
        # One (first) matched - means we have a match
        if matched:
            self.isMatched = True

    def _gotdata(self, data):
        """entered when HTMLParser has encountered data tag

            Parameters:
                data  :  string data
        """
        for m in self.memberList:
            if not m.isMatched:         # Ready
                m._gotdata(data)


#*************************************************************************
class Tag(Base):
    """Tag itself
        Main attributes:
            name        :   tag name
            attrDict    :   dictionary for matching attributes
            attrData    :   list of aData classes to get filtered attributes
            memberList  - inherited from Base
            memberList can contain next classes: dData, Tag, Rep, Any
    """

    _multiTags = ['any', 'none']

    def __init__(self, master):
        self.attrDict = {}
        self.attrData = []
        self.filter = None
        self.name = None
        self.taglist = set()
        super().__init__(master = master)

    def __str__(self):
        return "<class {}: {}, dict = {}, data = {}>".format(self.__class__.__name__,
                self.name,
                self.attrDict,
                [repr(d) for d in self.attrData])

    def __str__(self):
        return "<class {}: {}, dict = {}, attr = {}>".format(self.__class__.__name__,
                self.name,
                self.attrDict,
                [repr(d) for d in self.attrData])

    def __repr__(self):
        return "<name = {}, dict = {}, attr = {}>".format(
                self.name,
                self.attrDict,
                [repr(d) for d in self.attrData])

    def _resetScan(self):
        """resets scan parameters"""
        super()._resetScan()
        self.outData = ""
        self.atd = {}                       # Remembered attributes passed
        for m in self.attrData:
            m._resetScan()

    def _set_isMatched(self, matched):
        """real worker for isMatched setter

        set matched state
        For True - populate to all children that have no attribute set
        For False - populate to all, not depending on attribute
        """
        if matched:
            for m in self.master.memberList:    # Applied to xData classes before us only
                if id(m) == id(self):
                    break
                m._tagMatched(self.outData)

            for m in self.memberList:       # self.attrData is matched when start tag encountered
                if not m.isMatched or isinstance(m, Print):
                    m.isMatched = True

            for m in self.attrData:         # aData does not increment rewindId
                m.rewindId = self.incId

            self.rewindId = self.incId
        else:
            for m in self.memberList + self.attrData:
                m.isMatched = False
            self._rewindCounter()
        self._resetScan()
        self._isMatched = matched

    def copy(self, cl = None):
        """copy class and return new instance of it"""
        if cl is None:
            cl = Tag(master = self.master)
        cl.attrDict = self.attrDict.copy()
        cl.attrData = [c.copy() for c in self.attrData]
        cl.name = self.name
        cl.filter = self.filter
        cl.atd = self.atd.copy()
        cl.taglist = self.taglist.copy()
        return super().copy(cl)

    def _getAttrVal(self, aname):
        """gett attribute value by name"""
        if aname in self.atd:
            return " ".join(list(self.atd[aname]))
        return ""

    def _parse(self):
        """Parses one full TAG entry

            Returns:  position in line after _parse is done
            Entry to parser is done after '<' is detected.
            Parse pointer shows to '<' sign.
        """
        m = self._re_tagname.match(self.root.data[self.root.pos:])
        if not m:
            raise SyntaxError(self._getErrPos(), "expected tag name")
        self.name = m.group(1)
        if '.' in self.name:
            tg = self.name.split('.')
            if tg[0] not in self._multiTags:
                raise SyntaxError(self._getErrPos(), "Invalid multitag. Expected {}".format(self._multiTags))
            self.name = tg[0]
            self.taglist = set(tg[1:])
        elif self.name in self._multiTags:
                raise SyntaxError(self._getErrPos(), "Multi-tag must have at least one member")
        self.root.pos += m.end() - 1

        while True:
            m = self._re_attrname.match(self.root.data[self.root.pos:])
            if not m:
                break
            aname = m.group(1)
            aval = m.group(2)
            if aval[0] == '"':
                aval = aval.strip('"')
            if aname in _split_attrs:
                avar = aval.split()      # got array of attributes
            elif aname in _split_attrs1:
                avar = [self._stripspc(a) for a in aval.split(';')]
            else:
                avar = [aval]
            va = self.attrDict.get(aname, set())
            for av in avar:
                va.add(av)
            self.attrDict[aname] = va
            self.root.pos += m.end() - 1
# Finished with attributes. Next can be only data '$' or '>'
        while True:
            c = self._skipSpc()
            if c == '$':
                self.root.pos += 1           # skip '$'
                c = self._skipSpc()         # Check for indirect or exclusive data
                indirect = False
                if c == '*':
                    indirect = True
                    self.root.pos += 1
                    c = self._skipSpc()     # Check for exclusive data
                dt = aData(self)
                if indirect:
                    dt.Indirect = True
            elif c == '/':
                if self._skipNSpc() == '>':
                    self.root.pos += 1
                    return
                else:
                    raise SyntaxError(self._getErrPos(), "expected '>'")
            elif c == '>':
                self.root.pos += 1
                break
            else:
                raise SyntaxError(self._getErrPos(), "expected '>'")
            dt._parse()
            self.attrData.append(dt)

# inside tag body
        while True:
            if self.filter is None:
                m = self._re_string.match(self.root.data[self.root.pos:])     # Search for string
                if m:
                    self.filter = m.group(1).strip('"')
                    self.root.pos += m.end()
            c = self._skipSpc()             # expecting '$'' for data or '<' for open/close
            if c == '$':
                self.root.pos += 1               # skip '$'
                c = self._skipSpc()         # Check for indirect or exclusive data
                indirect = False
                if c == '*':
                    indirect = True
                    self.root.pos += 1
                    c = self._skipSpc()     # Check for exclusive data
                m = self._re_is_xData.match(self.root.data[self.root.pos:])
                if m:
                    dt = xData(self)
                else:
                    dt = dData(self)
                if indirect:
                    dt.Indirect = True
            elif c == '<':
                m = self._re_tagend.match(self.root.data[self.root.pos:])
                if m:                       # Tag end
                    name = m.group(1)
                    if name != "" and name != self.name:
                        raise SyntaxError(self._getErrPos(), "unmatched end tag: expected {}".format(self.name))
                    self.root.pos += m.end()
                    return
                # previous if do not pass here, no else needed
                # must be another Tag
                dt = Tag(self)
            elif c == '{':                  # Any group
                dt = Any(self)
            elif self._isRep(c):            # Rep
                dt = Rep(self)
            elif c == ':':                      # Print
                dt = Print(self)
            else:
                raise SyntaxError(self._getErrPos(), "unknown symbol {}".format(c))
            dt._parse()
            self.memberList.append(dt)

    def _tagMatch(self, tag):
        """Return TRUE if tag is ok for us and FALSE IF NOT"""
        if self.name == 'any' and tag in self.taglist:
            return True
        if self.name == 'none' and tag in self.taglist:
            return False
        return tag == self.name


    def _starttag(self, tag, atd, notForTags = False):
        """entered when HTMLParser has encountered start tag

            Parameters:
                tag  :  name of tag found
                atd  :  dictionary of attributes
                notForTags : if TRUE message is not for TAG CLASS
        """
        if notForTags:
            return
        justmatch = False
        if self.inTag == 0:         # Check open match
            if not self._tagMatch(tag):
                return
            for an in self.attrDict:
                if not an in atd:       # Have no attribute name in tag
                    return
                td = atd[an]
                for av in self.attrDict[an]:
                    if not av in td:
                        return
            self.atd = atd              # save for _getAttrVal
            for ad in self.attrData:    # Count embedded attribute data now
                ad._starttag(tag, atd)
                ad.isMatched = True
            justmatch = True
        if justmatch or self.inTag > 0:
            self.inTag += 1                 # Increment our tag level
            for m in self.memberList:
                if not m.isMatched:         # Ready
                    m._starttag(tag, atd, justmatch)
                    if isinstance(m, Data):
                        continue
                    break

    def _endtag(self, tag):
        """entered when HTMLParser has encountered end tag

            Parameters:
                tag  :  name of end tag found
        """
        if self.inTag == 0:
            return
        self.inTag -= 1

        for m in self.memberList:
            if not m.isMatched:         # Ready
                m._endtag(tag)

        if self.inTag == 0:         # Check and mark are we matched
            if self.filter != None:
                if self.filter[0] == '/' and self.filter[-1] == '/':
                    s = re.search(self.filter.strip('/'), self.outData)
                    if s is None:
                        self.isMatched = False
                        return
                else:
                    if self.filter != self.outData:
                        self.isMatched = False
                        return
            matched = True
            for m in self.memberList:
                if m.isMatched or (isinstance(m, Rep) and m.repCount == -1):
                    continue
                matched = False
                break
            self.isMatched = matched


    def _gotdata(self, data):
        """entered when HTMLParser has encountered data tag

            Parameters:
                data  :  string data
        """
        if self.inTag > 0:
            for m in self.memberList:
                if not m.isMatched:         # Ready
                    m._gotdata(data)
        self.outData = self._stripspc(self.outData + data)


#*************************************************************************
class Data(Base):
    """Data consuming class
        It's base for 2 real-used classes:
            aData   :   for attributes data
            dData   :   for text data
            xData   :   for one-level text data
        Parser enters here when '$' sign is detected, pointing directly after it
        Main attributes:
        name    :   data variable name
        idx     :   index policy:   0 - leave same (no mark) - data is appended to existing,
                                    1 - increment (+) - data will be stored,
                                    2 - clear (-) - clear previous data not incrementing index.
        find    :   regex for find, if repl is None - filter only
        repl    :   replace part for regex
    """

    def __init__(self, master):
        self.Indirect = False
        super().__init__(master = master)
        self.idx = 0
        self.name = None
        self.namePos = 0
        self.frepl = []         # will contain pairs of (find, repl)
                                # if find is None - add string repl
                                # if find is not none and repl is None - filer contents
                                # if both not none - do find/replace in contents

    def __str__(self):
        return "<class {}: {}, idx = {}, frepl = {}>".format(
            self.__class__.__name__,
            self.name,
            self.idx,
            self.frepl)

    def __repr__(self):
        return "name = {}, idx = {}, frepl = {}".format(
            self.name,
            self.idx,
            self.frepl)

    def _resetScan(self):
        """reset scan parameters.

            If matched is False rewind back counter
        """
        super()._resetScan()
        self.outData = ""
        self.accData = ""

    def _set_isMatched(self, matched):
        """real worker for isMatched setter
        when set to True, counts all data
            when set to False - resets all internal data
        """
        if matched:
            rids = set([self.rewindId])
            m = self.master
            while id(m.master) != id(m):
                rids.add(m.rewindId)
                m = m.master
            name = self.name
            if self.Indirect:           # Indirect name
                va = VarsClass()
                va.count(self.root.counter)
                v = va.getVar(self.name)
                if v is None:
                    raise VarUndefError(self._getErrPos(self.namePos), self.name)
                name = v[-1]
            self.root.counter.append((rids, name, self.idx, self.outData))
        else:
            self._rewindCounter()
            self._resetScan()
        self._isMatched = matched

    def copy(self, cl = None):
        """copy class and return new instance of it"""
        if cl is None:
            cl = Data(master = self.master)
        cl.frepl = self.frepl.copy()
        cl.idx = self.idx
        cl.name = self.name
        cl.namePos = self.namePos
        cl.outData = self.outData
        cl.accData = self.accData
        return super().copy(cl)

    def _parse(self):
        """Parses one full data entity

            Returns:  position in line after _parse is done
            Entry to parser is done after '$' is detected.
            Parse pointer shows directly after '$' sign or after "$*" in case of indirect
        """
        m = self._re_datavar.match(self.root.data[self.root.pos:])
        if not m:
            raise SyntaxError(self._getErrPos(), "variable definition expected")
        self.name = m.group(1)
        self.namePos = self.root.pos + m.start(1)
        sig = m.group(2)                # Modification sign
        if '+' in sig:
            self.idx |= 1
        if  '-' in sig:
            self.idx |= 2
        for avval in m.captures(3):
            if avval == '':                         # For empty string we must have it enclosed in double quotes!
                continue
            if avval.startswith('@'):               # Attribute def
                self.frepl.append( (None, None, avval[1:]) )
            else:
                avval = avval.strip('"')
                replinclusive = None
                if avval.startswith("+/") and avval.endswith('/'):
                    replinclusive = '+'
                    avval = avval[1:]
                if avval.startswith('/') and avval.endswith('/'):
                    avar = avval.split('/')
                    if 3 <= len(avar) <= 4:
                        avar = avar[1:-1]
                        avar.append(None)       # Mark only filter needed
                        self.frepl.append( (avar[0], avar[1], replinclusive) )
                    else:
                        raise SyntaxError(self._getErrPos(), "Expected regular expression")
                else:
                    self.frepl.append( (None, avval, None) )
        self.root.pos += m.end()

    def _gotAccData(self):
        """Deal with accumulated data"""
        odata = ""
        if len(self.frepl) == 0:
            odata = self.accData
        else:
            for find, repl, attr in self.frepl:
                if find is None:            # Set text required
                    if repl is None:        # attribute value
                        odata += self.master._getAttrVal(attr)   # must be Tag class
                    elif repl != "":
                        odata += repl
                elif repl is None:          # Filter only
                    if re.match(find, self.accData) is None:
                        return
                else:                       # make find/replace
                    if re.search(find, self.accData):
                        odata1 = re.sub(find, repl, self.accData)
                        odata += odata1
                        if attr == '+':
                            self.accData = odata1
                    elif attr == '+':       # "+/find/repl/" form
                        odata += self.accData
        odata = self.replConsts(odata)      # Check for $CONSTANTS
        m = self.master
        if isinstance(m, Tag) and m.name == "pre":
            self.outData += odata
        else:
            self.outData = self._stripspc(self.outData + odata)

    def replConsts(self, odata):
        """Function replConsts

            Parameters:
                odata  :  string to be added to output
            Returns:  converted string
            Searches for constants in string and replaces to known data
            Constants are $URL, $BASEURL, $PROTO
        """
        if not self.root.noExpand:
            mark = 0
            while True:
                m = self._re_resvar.search(odata[mark:])
                if not m:
                    break
                if m.group(1) in self.root.staticDict:
                    start = m.start()+mark
                    end = m.end(1)
                    try:
                        if odata[end] == ' ':
                            end += 1
                    except:
                        pass
                    odata = odata[:start] + self.root.staticDict[m.group(1)] + odata[m.end()+mark:]
                mark += m.end()
        return odata


#*************************************************************************
class aData(Data):
    """Data subclass for attributes
        Behavior: Text values are appended to variable with leading space,
                    if variable had some data
                See _gotdata function for example
    """

    def copy(self, cl = None):
        """copy class and return new instance of it"""
        if cl is None:
            cl = aData(master = self.master)
        return super().copy(cl)

    def _starttag(self, tag, atd, notForTags = False):
        """entered when HTMLParser has encountered start tag

            Parameters:
                tag  :  name of tag found
                atd  :  dictionary of attributes
            Function is passed from inside start tag, so simply count data here
        """
        astr = ""
        for an in atd:
            ad = atd[an]
            if len(ad) == 0:        # empty set
                astr += " " + an
            else:
                for av in ad:
                    astr += ' {}="{}"'.format(an, av)
        self._gotdata(astr + " ")            # on empty attribute set " " is sent

    def _gotdata(self, data):
        """entered when HTMLParser has encountered data tag

            Parameters:
                data  :  string data
            Internal attribute dictionary is converted to
                string and passed here. Note that attributes order can not match
                For instance next tag can produce any of data values:
                <div class="abc def" left alt="Some text">:
                ' alt="Some text" class="abc" class="def" left ' -- or --
                ' left class="def" class="abc" alt="Some text"' -- or --
                ' class="dwf" class="abc" alt="Some text" left '
            In any case attributes with same name will go inline one after other
            Notice that string is passed with leading and trailing spaces.
            Only attribues in _split_attrs and _split_attrs1 are split into parts.
        """
        self.accData += data
        self._gotAccData()

#*************************************************************************
class dData(Data):
    """Data subclass for in-line text data
        Behavior: Text values are appended to variable with leading space,
                    if variable had some data
            Class accepts data variables with $Id[] definition - i. e. those
            which accumulate all data in all tags inside this one
    """

    def copy(self, cl = None):
        """copy class and return new instance of it"""
        if cl is None:
            cl = dData(master = self.master)
        return super().copy(cl)

    def _set_isMatched(self, matched):
        super()._set_isMatched(matched)
        if matched:
            self.rewindId = self.incId

    def _starttag(self, tag, atd, notForTags = False):
        """entered when HTMLParser has encountered start tag

            Parameters:
                tag  :  name of tag found
                atd  :  dictionary of attributes
        """
        self.inTag += 1                 # Increment our tag level

    def _endtag(self, tag):
        """entered when HTMLParser has encountered end tag

            Parameters:
                tag  :  name of end tag found
        """
        if self.inTag == 0:
            return
        self.inTag -= 1
        if self.inTag == 0:
            self._gotAccData()
            self.isMatched = True          # Mark done

    def _gotdata(self, data):
        """entered when HTMLParser has encountered data tag

            Parameters:
                data  :  string data
        """
        self.accData += data

#*************************************************************************
class xData(dData):
    """Data subclass for in-line text data
        Behavior: Text values are appended to variable with leading space,
                    if variable had some data
            Class accepts data variables with $!Id[] definition - i. e. those
            which accumulate only same level data up to first tag open/close
    """

    def copy(self, cl = None):
        """copy class and return new instance of it"""
        if cl is None:
            cl = xData(master = self.master)
        return super().copy(cl)

    def _resetScan(self):
        """reset scan parameters"""
        super()._resetScan()
        self.noNextMatch = True

    def _gotdata(self, data):
        """entered when HTMLParser has encountered data tag

            Parameters:
                data  :  string data
        """
        if self.noNextMatch:
            self.accData += data

    def _tagMatched(self, data):
        """some tag below our definition has matched"""
        if self.noNextMatch and self.accData.endswith(data):
            self.accData = self.accData[:-len(data)]
        self.noNextMatch = False

#*************************************************************************
class Count(object):
    """Contains expression counting routines

    You need to define _getErrPos function and self.indexPos variable in derived
    class to use this base class
    """
    _sP = Base._sP
    _re_var = re.compile(r'\$(\*?)([a-z]+[a-z0-9_]*)', re.I | re.A)
    _eX = _sP + r'(?:(\$[0-9]+|&[0-9]+|\$\*?[a-z]+[a-z0-9_]*|[*+)(-]|[0-9]+)'+_sP+r')*' + _sP
    _re_eX = re.compile(_eX, re.I | re.A)
    _qB = r'\('+ _eX + r'(>|<|>=|<=|==|!=)'+ _eX + r'\?' + _eX + r':'+ _eX + r'\)'
    _re_qB = re.compile(_qB, re.I | re.A)


    def getExprLen(self, dchar):
        """Get indexExpr length up to first ':' or ']'

            Parameters:
                dchar  :  delimiting symbols depending on context. ':', ';"/]', '"/]'
            Returns:  expression length not including serarating character
                self.root.pos is updated to point to separating character
            On entry pointer points after first char of indexExpr
        """
        inpar = 0
        beg = self.root.pos
        self.root.pos -= 2      # one more back for NSpc
        while True:
            c = self._skipNSpc()             # find next val
            if c == '(':
                inpar += 1
            elif c == ')':
                inpar -= 1
                if inpar < 0:
                    raise SyntaxError(self._getErrPos(), "invalid parenthesis")
            elif c in dchar:
                if inpar == 0:
                    return self.root.pos - beg + 1

    def getval(self, str):
        """Get value - array length - by specified string

            Parameters:
                str  :  string in form $data or $*data
            Returns:  counter or 0 on error
        """
        m = self._re_var.match(str)
        if not m:
            raise SyntaxError(self._getErrPos(), "unknown symbol")
        Indirect = True if m.group(1) == '*' else False
        name = m.group(2)
        va = VarsClass()
        va.count(self.root.counter)
        try:
            if Indirect:           # Indirect name
                v = va.getVar(name)
                name = v[li[-1]]
            v = va.getVar(name)
            return len(v)
        except:
            return 0
#           raise VarUndefError(self._getErrPos(self.namePos), name)

    def listCount(self, li):
        """count simple list, Used by more general function countExpr

            Parameters:
                li  :  list to count eg. [1, '+', '-', 2, '*', 3]
            Returns:  integer result value
            On entry we have list of integer values separated by string values from set
            {'-', '+', '*'}. '-' can be used as minus operation as well as unary minus.
            Parentheses are removed already.
        """
        try:
            # Deal with 'unary' minuses
            b = 0
            while True:
                try:
                    n = li.index('-', b)
                    while len(li) > n+1 and li[n+1] == '-':
                        n += 1
                    if n == 0:
                        li[1] = -li[1]
                        li = li[1:]
                    elif isinstance(li[n-1], str):
                        li[n+1] = -li[n+1]
                        li = li[0:n] + li[n+1:]
                    b = n + 1               # Year, even after move start pos is n+1
                except ValueError:          # '-' not found
                    break
            # Deal with multiplications
            b = 0
            while True:
                try:
                    n = li.index('*', b)            # find multiplication
                    if n == 0 or len(li) < n+2:
                        raise IndexError
                    if n == 1:
                        li = [li[0]*li[2]] + li[3:]
                    else:
                        li = li[0:n-1] + [li[n-1]*li[n+1]] + li[n+2:]
                    b = n
                except ValueError:          # '*' not found
                    break
            # left is to sum all
            if len(li) & 1 != 1:
                raise IndexError
            res = li[0]
            for n in range(1, len(li), 2):
                if li[n] == '+':
                    res += li[n+1]
                else:                   # can be only '-'
                    res -= li[n+1]
            return res
        except IndexError:
            raise SyntaxError(self._getErrPos(self.indexPos), "invalid index syntax")


    def countExpr(self, expr, pars, tcnt):
        """count list

            Parameters:
                expr  : expression to count, eg.
                    ['$1', '*', '(', '2', '+', $0', ')', '+', '&0', '+', '$Data']
                pars  : list of indexes [$1, $2,...$0]
                tcnt  : list of already calculated expressions for &#
            Returns:  integer index value

        """
        if len(expr) == 0:
            return pars[-1]
        c = [int(n) if n.isnumeric() else tcnt[int(n[1:])] if n[0] == '&' else n if n[0] != '$' else self.getval(n) if not n[1].isnumeric() else pars[-1] if int(n[1:]) == 0 else pars[int(n[1:]) - 1] for n in expr]
        while True:
            try:
                n = c.index(')')
                for m in range(n - 1, -1, -1):
                    if c[m] == '(':
                        c = c[0:m] + [self.listCount(c[m+1:n])] + c[n+1:]
                        break
                    elif m == 0:
                        raise SyntaxError(self._getErrPos(self.indexPos), "unmatched parenthesis in index")
            except ValueError:          # '-' not found
                break
        return self.listCount(c)

    def precountTernary(self, ex):
        """Function precountTernary

            Parameters:
                ex  :  some expression possible with ternary operators
                    For eg '$0 + 1 + ($data + 1 < 4 ? $*data - 1 : $1 + ($href <= 4 ? $href + 1 : 4))'
            Returns:  pair containing of
                list with countExpr compatible expression
                    in our case ['$0', '+', '1', '+','&1']
                list with ternary expression lists. In our case
                [[['$href'], ['<='], ['4'], ['$href','+','1'], ['4']],
                 [['$data','+','1'], ['<'], ['4'], ['$*data','-','1'], ['$1','+','&0']]]
        """
        tern = []       # For results
        te = ex
        while True:
            m = self._re_qB.search(te)
            if not m:
                break
            tex = [m.captures(i) for i in range(1,6)]
            # We have list of lists
            # [['$href'], ['<='], ['4'], ['$href', '+', '1'], ['4', ')']]
            # Now we can have additional flowting ')' in last positions of tex[4]
            inpar = 0
            lgpos = m.ends(5)       # get positions of last group captures
            beg = m.start()         # position of match start in te
            end = m.end()           # position of match end - to be updated
            for c in tex[4]:
                if c == '(':
                    inpar += 1
                elif c == ')':
                    inpar -= 1
            l = len(tex[4]) - 1
            for i in range(l, l+inpar, -1):
                if tex[4][i] != ')':
                    # TODO: fix error position
                    raise SyntaxError(self._getErrPos(), "invalid parenthesis")
                tex[4].pop()
                end = lgpos[i]
            p = len(tern)
            tern.append(tex)
            te = te[:beg] + "&{}".format(p) + te[end:]
        # Have formated lists in tern and left string without ternary in te
        m = self._re_eX.match(te)
        if not m:
            # TODO: fix error position
            raise SyntaxError(self._getErrPos(), "invalid index expression")
        return (m.captures(1), tern)

    def countTern(self, ex, li, tcnt):
        """count ternary expression

            Parameters:
                ex  :  ternary expression is list of 5 list items
                for ex [['$data','+','1'], ['<'], ['4'], ['$*data','-','1'], ['$1','+','&0']]
                item [1] is comparison operation string
                other items are index expressions in countExpr style
            Returns:  counted number
        """
        r = []
        for i in range(0, 5):
            if i == 1:
                continue
            r.append(self.countExpr(ex[i], li, tcnt))
        op = ex[1][0]
        if op == "<":
            log = r[0] < r[1]
        elif op == ">":
            log = r[0] > r[1]
        elif op == "<=":
            log = r[0] <= r[1]
        elif op == ">=":
            log = r[0] >= r[1]
        elif op == "!=":
            log = r[0] != r[1]
        elif op == "==":
            log = r[0] == r[1]
        else:       # must never hapen: regex will not allow
            raise CodeError("Something wrong with ternary expression parameters parsing: operator '{}'".format(op))
        return r[2] if log else r[3]


#*************************************************************************
class Print(Base, Count):
    """Print class defines general print settings

    Parser is entered after ':' sign is detected
    Print statement syntax approximately matches next case insensitive regexp:
    r':([nNsUulABC]?) (?:(\$[0-9]+|\$\*?[a-z]+[a-z0-9_]*|[*+)(-]|[0-9]+))*:(".*"|\$\*?[a-z][a-z0-9]*\[[+-]?(".*")*\]|PS)*;'
        - PS here stands for another print statement
        - separating white space and comments are skipped
    In other words:
        - print statement begins from ':' sign and has modifiers that occupies up to next ':' sign
            - flags can contain optional repeat count consisting countable expression with parenthesis,
             plus minus and multiplication signs. Numbers after $ represent index of surrounding
             print statements, $1 pointing to outermost $2 to next and so on up to us.
             Additionally $0 also points to our statement.
            - flags can contain optional direct or indirect variable definition. Indirect
                definitions are processed exactly before print statement. Length of variable
                (variable will be auto-init if is not defined) is assumed as print repeat count.
            For instance next print defines executes print statement 1 time:
                "::", ":1:", ":$Suv", ":$*Nrv:" if $Suv is undefined at print time or $Nrv
                is undefined at print time or value of $Nrv[-1] cannot be resolved as variable
                name at print time.
    """
    _sP = Base._sP
    _re_printflag = re.compile(_sP + r'(?-i:([nNsUulABC]*))' + _sP + r'([\]($&0-9:a-z-])', re.I | re.A)
    _re_printbody = re.compile(_sP+r'(?:("[^"]*?")'+_sP+r')*(?:(\$)?(\*?))'+_sP+r'([(:;]?)', re.I | re.A)

    def __init__(self, master):
#        self.namePos = []
        self.etern = []
        self.eidx = ['1']
        self.flags = ''
        super().__init__(master = master)

    def __str__(self):
        return "<class {}: {}>".format(self.__class__.__name__, self.eidx, self.etern)

    def __repr__(self):
        return "eidx = {}, etern = {}, frepl = {}".format(self.eidx, self.etern, self.frepl)

    def _resetScan(self):
        """resets scan parameters"""
        super()._resetScan()
        self._isMatched = True

    def _print_us(self, li = [], file = None):
        """Print all accumulated data"""

        outfile = self.root.outfile[0] if file is None else file
        useflags = self.flags
        if 'A' in useflags:
            outfile = self.root.outfile[1]
        elif 'B' in useflags:
            outfile = self.root.outfile[2]
        elif 'C' in useflags:
            outfile = self.root.outfile[3]

        tcnt = []
        for ex in self.etern:
            tcnt.append(self.countTern(ex, li, tcnt))
        idx = self.countExpr(self.eidx, li, tcnt)

        for i in range(0, idx):
            for m in self.memberList:
                m._print_us(li + [i], file = outfile)
            if 'N' in useflags:
                print(file = outfile)       # NL after each
        if 'n' in useflags:
            print(file = outfile)           # NL after all


    def _set_isMatched(self, matched):
        """real worker for isMatched setter

        set matched state
        For True - populate to all children that have no attribute set
        For False - populate to all, not depending on attribute
        """
        if matched:
            self._print_us()
        self._resetScan()

    def copy(self, cl = None):
        """copy class and return new instance of it"""
        if cl is None:
            cl = Print(master = self.master)
#        cl.namePos = self.namePos.copy()
        cl.count = self.count
        cl.repCount = self.repCount
        return super().copy(cl)

    def _parse(self):
        """Parses one full Print entry

            Returns:  position in line after _parse is done
            Entry to parser is done after ':' is detected.
            Parse pointer shows to ':'
        """
        self.root.pos += 1
        m = self._re_printflag.match(self.root.data[self.root.pos:])
        if not m:
            raise SyntaxError(self._getErrPos(), "expected print attribute data")
# group(1) - flags, group(2) - 1 symbol separator. If ':' - indexExpr not present
        self.flags = m.group(1)
        self.root.pos += m.end()
        if m.group(2) != ':':           # eidx = [1] by default. Processing "present" chain
            el = self.getExprLen(':')      # get expression length
            ex = self.root.data[self.root.pos - el:self.root.pos]
            self.eidx, self.etern = self.precountTernary(ex)
            self.root.pos += 1

        while True:
            m = self._re_printbody.match(self.root.data[self.root.pos:])
# we have 4 groups match:
# m.captures(1) list with specified strings - [] if none (in this case group(1) is None)
# m.group(2) '$' if variable present
# m.group(3) '*' (only if above correct) for Indirect
# m.group(4) ';' - end of print statement (if group(2) is empty string)
#            ':' - another print statement beginning
#            '(' - indexExpresiion beginning

            self.root.pos += m.end()
            for s in m.captures(1):
                dt = stData(self)
                dt._gotdata(s.strip('"'))
                self.memberList.append(dt)
            if m.group(2) == '$':
                dt = pData(self)
                if m.group(3) == '*':
                    dt.Indirect = True
            elif m.group(4) == '(':             # embedded indexExpr
                dt = idxExpr(self)
            elif m.group(4) == ':':             # embedded print statement
                dt = Print(self)
                self.root.pos -= 1
            elif m.group(4) == ';':             # end of print statement
                break
            else:
                raise SyntaxError(self._getErrPos(), "unknown symbol")
            dt._parse()
            self.memberList.append(dt)


#*************************************************************************
class pData(Data, Count):
    """Data subclass for print data"""

    _sP = Base._sP
    _re_pdatahead = re.compile(r'([a-z]+[a-z0-9_]*)\['+ _sP + r'([\]";$&0-9-])', re.I | re.A)
    _re_pdatavar = re.compile(r'(?:(".*?"|[^\s"\]]+)'+_sP+r')*\]', re.I | re.A)
#    _re_pdatavar = re.compile(r'([a-z]+[a-z0-9_]*)\['+ _sP + r'(?:' + _eX +r'(;))?'+ _eX + r'(?:(".*?"|[^\s"\]]+)'+_sP+r')*\]', re.I | re.A)


    def __init__(self, master):
        super().__init__(master = master)
        self.eidx = []
        self.iidx = []
        self.etern = []
        self.itern = []
        self.indexPos = 0
        self.iindexPos = 0
        self.namePos = 0

    def __repr__(self):
        if self.Indirect:
            return "name = {}, eidx = {}, etern = {}, iidx = {}, itern = {}, frepl = {}".format(
                self.name,
                self.eidx,
                self.etern,
                self.iidx,
                self.itern,
                self.frepl)
        else:
            return "name = {}, eidx = {}, tern = {} frepl = {}".format(
                self.name,
                self.eidx,
                self.etern,
                self.frepl)

    def __str__(self):
        if self.Indirect:
            return "<class {}: {}, eidx = {}, etern = {}, iidx = {}, itern = {}, frepl = {}>".format(
                self.__class__.__name__,
                self.name,
                self.eidx,
                self.etern,
                self.iidx,
                self.itern,
                self.frepl)
        else:
            return "<class {}: {}, eidx = {}, tern = {} frepl = {}>".format(
                self.__class__.__name__,
                self.name,
                self.eidx,
                self.etern,
                self.frepl)


    def copy(self, cl = None):
        """copy class and return new instance of it"""
        if cl is None:
            cl = pData(master = self.master)
        cl.eidx = self.eidx.copy()
        cl.iidx = self.iidx.copy()
        cl.etern = self.etern.copy()
        cl.itern = self.itern.copy()
        cl.indexPos = self.indexPos
        cl.iindexPos = self.iindexPos
        return super().copy(cl)

    def _parse(self):
        """Parses one full PRINT data entity

            Returns:  position in line after _parse is done
            Entry to parser is done after '$' is detected.
            Parse pointer shows directly after '$' sign or after "$*" in case of indirect
        """
        m = self._re_pdatahead.match(self.root.data[self.root.pos:])
        if not m:
            raise SyntaxError(self._getErrPos(), "variable definition expected")
# group(1) -name, group(2) - 1 symbol separator.
# If in ']";' - indexExpr not present. However if ';' an self.Indirect next index epr must be checked
        self.name = m.group(1)
        self.namePos = self.root.pos + m.start(1)
        if m.group(2) not in ']"':                  # index present
            if m.group(2) != ';':                   # realy some index
                self.root.pos += m.end(2)           # point to separating index
                el = self.getExprLen(';"/]')        # get expression length
                ex = self.root.data[self.root.pos - el:self.root.pos]
                idx, tern = self.precountTernary(ex)
                c = self._skipSpc()
                if c == ';':      # it was iidx
                    if not self.Indirect:
                        raise SyntaxError(self._getErrPos(), "double index can have only indirect variables")
                    self.iidx = idx
                    self.itern = tern
                    self.iindexPos = self.root.pos - el
                    # In this case we can have another index
                    self.root.pos += 2              # getExprLen will roll back
                    el = self.getExprLen('"/]')        # get expression length
                    ex = self.root.data[self.root.pos - el:self.root.pos]
                    if len(ex) > 0:
                        self.eidx, self.etern = self.precountTernary(ex)
                        self.indexPos = self.root.pos - el
                else:
                    self.eidx = idx
                    self.etern = tern
                    self.indexPos = self.root.pos - el
        else:
            self.root.pos += m.start(2)

        m = self._re_pdatavar.match(self.root.data[self.root.pos:])
        if m:
            for avval in m.captures(1):
                avval = avval.strip('"')
                avar = avval.split('/')
                if len(avar) != 4 or avar[0] != '' or avar[3] != '':
                    raise SyntaxError(self._getErrPos(), "Expected regular expression")
                self.frepl.append( (avar[1], avar[2], None) )
            self.root.pos += m.end()


    def _print_us(self, li, file):
        """Print all accumulated data

            Parameters:
                li  :  list of indexes [$1, $2,...$0]
            Last index can be accessed as $n, where n is len(li) or $0
            Real data index is counted using predefined index expression
            self.eidx and passed index values list li
            If self.eidx is empty, $0 is assumed
        """
        tcnt = []
        for ex in self.etern:
            tcnt.append(self.countTern(ex, li, tcnt))
        idx = self.countExpr(self.eidx, li, tcnt)

        name = self.name
        va = VarsClass()
        va.count(self.root.counter)
        if self.Indirect:           # Indirect name
            v = va.getVar(name)
            if v is None:
                raise VarUndefError(self._getErrPos(self.namePos), name)
            tcnt = []
            for ex in self.itern:
                tcnt.append(self.countTern(ex, li, tcnt))
            name = v[self.countExpr(self.iidx, li, tcnt)]
        v = va.getVar(name)
        if v is None:
            raise VarUndefError(self._getErrPos(self.namePos), name)
# Apply find/replace if defined
        s = v[idx]
        s = self.replConsts(s)
        for find, repl, attr in self.frepl:
            s = re.sub(find, repl, s)
        e = ''
        if 's' in self.master.flags:
            e = ' '
        if 'U' in self.master.flags:
            s = s.upper()
        if 'l' in self.master.flags:
            s = s.lower()
        if 'u' in self.master.flags:
            s = s.capitalize()
        print(s, end = e, file = file)

#*************************************************************************
class idxExpr(Data, Count):
    """Data subclass for index expression countin and printing"""

    def __init__(self, master):
        super().__init__(master = master)
        self.eidx = ['1']
        self.etern = []
        self.indexPos = 0

    def __repr__(self):
        return "eidx = {}, tern = {}".format(
            self.eidx,
            self.etern)


    def copy(self, cl = None):
        """copy class and return new instance of it"""
        if cl is None:
            cl = idxExpr(master = self.master)
        cl.eidx = self.eidx
        cl.etern = self.etern.copy()
        cl.indexPos = self.indexPos
        return super().copy(cl)

    def _parse(self):
        """Parses one full idxExpr entity

            Returns:  string with full expression
                position in line after _parse is done is updated to point after closing ')'
            Entry to parser is done after '(' is detected in print body
            Parse pointer shows to '('
        """
        inpar = 0
        beg = self.root.pos - 1
        self.root.pos -= 2      # one more back for NSpc
        while True:
            c = self._skipNSpc()             # find next val
            if c == '(':
                inpar += 1
            elif c == ')':
                inpar -= 1
                if inpar < 0:
                    raise SyntaxError(self._getErrPos(), "invalid parenthesis")
                elif inpar == 0:
                    self.root.pos += 1          # skip ending ')'
                    ex = self.root.data[beg:self.root.pos]
                    break
        # have possible ternary expression in ex
        self.eidx, self.etern = self.precountTernary(ex)

    def _print_us(self, li, file):
        """Print all accumulated data"""
        tcnt = []
        for ex in self.etern:
            tcnt.append(self.countTern(ex, li, tcnt))
        idx = self.countExpr(self.eidx, li, tcnt)
        e = ''
        if 's' in self.master.flags:
            e = ' '
        print(idx, end = e, file = file)

#*************************************************************************
class stData(Data):
    """Data subclass for static string print data"""

    def copy(self, cl = None):
        """copy class and return new instance of it"""
        if cl is None:
            cl = stData(master = self.master)
        return super().copy(cl)

    def __repr__(self):
        return "data = {}".format(
            self.outData)

    def _print_us(self, li, file):
        """Print all accumulated data"""
        e = ''
        s = self.outData
        if 's' in self.master.flags:
            e = ' '
        if 'U' in self.master.flags:
            s = s.upper()
        if 'l' in self.master.flags:
            s = s.lower()
        if 'u' in self.master.flags:
            s = s.capitalize()
        print(s, end = e, file = file)

    def _gotdata(self, data):
        """Differently from other classes is called only once, at data init"""
        self.outData = self.replConsts(data)

#*************************************************************************
# Data parser section
from html.parser import HTMLParser

class lieParser(HTMLParser):
    """Main working class for Liepa Parser"""

    def __init__(self, syn, url = "https://pypi.org/project/lieparse/", locale = None):
        """Initializer for lieParser class

            Parameters:
                syn  :  parse definitions. String or class Rep instance are accepted

            For everyday use you should use string of parsing definitions here.
            The exception is when you want to debug definitions syntax, where you can pass initialized
            Rep instance here and then use printTree function (or pass string and use .synparser.printTree())
            NOTE: url parameter was not present in versions 1.0.x. So it is added as optional
        """
        super().__init__()
        if isinstance(syn, str):
            self.synparser = Rep(data = syn, url = url, locale = locale)
        elif isinstance(syn, Rep):
            syn.setURL(syn.url, locale)
            self.synparser = syn
        else:
            raise CodeError("Initializer must be string or Rep class")

    def close(self):
        """Finalize all tasks

            Returns:  Number of unmatched items in upper level
                    0 - all matched
        """
        super().close()
        return self.synparser.close()

    def handle_starttag(self, tag, attrs):
        atd = {}
        for attr in attrs:
            idx = attr[0]
            if attr[1] is None:
                val = []
            else:
                if idx in _split_attrs:
                    val = attr[1].split()
                elif idx in _split_attrs1:
                    val = [Base._stripspc(a) for a in attr[1].split(';')]
                else:
                    val = [attr[1]]
            v = atd.get(idx, set())
            for a in val:
                v.add(a)
            atd[idx] = v
        self.synparser._starttag(tag, atd)

    def handle_endtag(self, tag):
        self.synparser._endtag(tag)

    def handle_data(self, str):
        self.synparser._gotdata(str)

    def setOutfile(self, handle, numb = 0):
        """Set output file stream. Defaults to sys.stdout"""
        self.synparser.outfile[numb] = handle

    def noExpand(self, val):
        """Set Do-not expand system variables flag"""
        self.synprser.noExpand = val

