# 20191219 R.V.
import os
from pathlib import Path

# Local imports
from .qconfigobj import reindent

#------------------------------------------------------------------------------
def makeDoc(configSpecLines):
    """ Return dictionary with sphinx documentation for `configspecLines`

        Args:
            configSpecLines (list): configspec file lines for ConfigObj

        Returns:
            dict: dictionary with sphinx documentation for `configspecLines`
    """
    underlines = '* = - ^ "'.split()
    txt = ''
    sections = {'root': {'attrs': ''}}
    cursection = ['root']
    curlevel = 0

    for line in configSpecLines:
        if not line.strip():
            # Skip blank lines
            continue
        line = line.strip()
        if line.startswith('['):
            # Section
            level = line.count('[')
            name = line.strip('[').strip(']')
            sec = sections
            for key in cursection[:-1]:
                sec = sec[key]
            last = cursection[-1]
            if level > curlevel:
                sec[last]['attrs'] = txt
                #sec[last]['attrs'] += line
                curlevel += 1
            else:
                sec[last]['attrs'] = txt
                del cursection[level:]
                curlevel = level
                sec = sections
                for key in cursection[:-1]:
                    sec = sec[key]
                last = cursection[-1]

            sec[last][name] = {'attrs': ''}
            cursection.append(name)
            txt = ''
            txt += '\n%s\n' % name
            txt += "%s\n\n" % (underlines[level - 1] * len(name))
            if name == '__many__':
                txt += ('| Many sections with *arbitrary names* but with'
                        ' the following structure can be added.\n|\n')
            else:
                txt += ("The **%s** section defines the following"
                        " keywords:\n\n" % name)

        if line.startswith('#'):
            # Comment
            txt += '| %s\n' % line
        else:
            if True:
                # Accepted values
                txt += "\n.. code-block::\n\n"
                line = line.replace('$', '\n')
                if len(line.splitlines()) > 1:
                    line = reindent(line)
                txt += "    %s\n\n" % line
            else:
                line = boldifyKeyword(line)
                line = line.replace('$', '\n')
                if len(line.splitlines()) > 1:
                    line = reindent(line)
                txt += "| %s\n\n" % line

    sec[last][name]['attrs'] = txt
    return sections

#------------------------------------------------------------------------------
def saveSection(section, name, docsource, subpath, header=''):
    """ Recursively save configobject section and subsections
        documentation into separate files, one for each section,
        in a nested folder structure starting at `docsource`.

        Args:
            section (dict): dictionary with the sections documentation
            name (str): .rst file name of the document
            docsource (Path): write .rst file starting from this directory
            subpath (Path): subdirctory to which write the .rst document
            header (str): header for the first level (root) of the document
    """
    txt = header
    txt += section['attrs']
    txt += "\n.. toctree::\n"
    txt += "    :titlesonly:\n\n"
    secnames = list(section.keys())
    secnames.remove('attrs')
    for secname in secnames:
        txt += "    %s <%s/%s>\n" % (secname, secname, secname)
    # Now write the file
    dirpn = docsource.joinpath(subpath)
    try:
        os.makedirs(dirpn)
    except FileExistsError:
        pass
    pn = dirpn.joinpath("%s.rst" % name)
    with open(dirpn.joinpath(pn), "w") as out:
        out.write(txt)

    # And process subsection
    for sn in secnames:
        saveSection(section[sn], sn, docsource, subpath.joinpath(sn))

#------------------------------------------------------------------------------
def makeSphinxDoc(configSpecLines, docsource, header):
    """ Create Sphinx documentation for `configspecLines` at directory
        `docsource`.

        Args:
            configSpecLines (list): configspec file lines for ConfigObj
            docsource (Path): root directory for documentation.
            header (str): header text for the documentation
    """
    sections = makeDoc(configSpecLines)
    saveSection(sections['root'], 'cfg', docsource, Path('.'), header=header)

#------------------------------------------------------------------------------
