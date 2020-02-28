"""Pandoc Markdown module."""
from markdgenerator.common import CommonMdGenerator
from markdgenerator.config import NEWLINE

class PandocMdGenerator(CommonMdGenerator):
    """Class to generate Pandoc Markdown text with."""

    def _h1(self, text):
        """Generate markdown h1 title.

        Args:
            text(str):
                string to write
        Returns:
            str
        """
        return NEWLINE + '# {}'.format(text)

    def _h2(self, text):
        """Generate markdown h2 title.

        Args:
            text(str):
                string to write
        Returns:
            str
        """
        return NEWLINE + '## {}'.format(text)

    def _h3(self, text):
        """Generate markdown h3 title.

        Args:
            text(str):
                string to write
        Returns:
            str
        """
        return NEWLINE + '### {}'.format(text)

    def _paragraph(self, text):
        """Generate markdown paragraph text.

        Args:
            text(str):
                string to write
        Returns:
            str
        """
        return NEWLINE + str(text) + NEWLINE

    def _codeblock(self, text):
        """Generate markdown codeparagraph.

        Args:
            text(str):
                string to write
        Returns:
            str
        """
        return NEWLINE.join(('~~~~~~', text, '~~~~~~')) + NEWLINE

    def _render_block(self, block):
        """Finalize text block output.

        Args:
            block(list):
                list of strings corresponding to block elements

        Return:
            str
        """
        return NEWLINE.join(block)+NEWLINE

    def _render_section(self, section):
        """Finalize section output.

        Args:
            section(list):
                list of section components

        Return:
            str
        """
        full_sect_str = ''

        rendfunc = lambda x: self.render_table(x['name']) if x['type'] == "table" else self.render_block(x['name'])
        full_sect_str = NEWLINE.join([rendfunc(el) for el in section])

        return full_sect_str

    def _render_table(self, table):
        """Finalize table output.

        Args:
            table(dict):
                table with all its elements
        Return:
            str
        """
        cols_widths = table['cols_widths']
        table_list = []

        # add first grid line
        table_list.append('+'+'+'.join(['-'*w for w in cols_widths])+'+')

        # add header
        if table['has_header']:
            table_list.append('|'+'|'.join([format(c, '{}'.format(w)) for (c,w) in zip(table['header'],cols_widths)])+'|')
            table_list.append('+'+'+'.join(['='*w for w in cols_widths])+'+')

        # add rows
        for r in table['rows']:
            table_list.append('|'+'|'.join([format(c, '{}'.format(w)) for (c,w) in zip(r,cols_widths)])+'|')
            table_list.append('+'+'+'.join(['-'*w for w in cols_widths])+'+')

        return NEWLINE.join(table_list)+NEWLINE
