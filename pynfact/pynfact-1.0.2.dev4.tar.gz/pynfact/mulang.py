# vim: set ft=python fileencoding=utf-8 tw=72 fdm=indent nowrap:
"""
    pynfact.mulang
    ~~~~~~~~~~~~~~

    Markdown translation to HTML and metadata "getter".

    :copyright: (c) 2012-2020, J. A. Corbal
    :license: MIT
"""
import markdown
import textwrap


class Mulang:
    """Generates HTML code from MarkUp LANGuage (mulang) source."""

    def __init__(self, input_data, encoding='utf-8',
            output_format='html5'):
        """
        Initializer

        :param input_data: File from where the data is taken
        :type input_data: str
        :param encoding: Encoding the input file is in
        :type encoding: str
        :param output_format: Output HTML version
        :type output: str
        """
        self.input_data = input_data
        self.encoding = encoding
        self.md = markdown.Markdown(
                extensions=['markdown.extensions.extra',
                            'markdown.extensions.toc',
                            'markdown.extensions.abbr',
                            'markdown.extensions.def_list',
                            'markdown.extensions.footnotes',
                            'markdown.extensions.codehilite',
                            'markdown.extensions.meta'],
                encoding=encoding,
                output_format=output_format)


    def html(self, verbose=True):
        """Generates HTML from Markdown data.

        :param verbose: Tells what this is doing
        :type verbose: bool
        """
        input_file = open(self.input_data, mode="r", \
                          encoding=self.encoding)
        text = input_file.read()
        input_file.close()
        html = self.md.convert(text)

        if verbose:
            print("Parsed", textwrap.shorten(self.input_data, 70))

        return html


    def metadata(self):
        """Gets metadata in the markdown file.

        .. todo: Get the meta without generating HTML again
        """
        input_file = open(self.input_data, mode="r", \
                          encoding=self.encoding)
        text = input_file.read()
        input_file.close()
        html = self.md.convert(text)

        return self.md.Meta

