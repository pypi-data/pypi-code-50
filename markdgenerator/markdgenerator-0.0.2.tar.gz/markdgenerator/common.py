"""General API."""
from abc import ABC, abstractmethod
from collections import defaultdict
import pandas as pd
from markdgenerator.config import NEWLINE


class CommonMdGenerator(ABC):
    """Common (abstract) parent class to generate text in markdown languages with."""

    def __init__(self):
        """Init function."""
        self._blocks = defaultdict(list)
        self._tables = defaultdict(list)
        self._sections = defaultdict(list)
        self._last_element = None


    def __str__(self):
        """Get string representation."""
        if(len(self._sections)):
            return NEWLINE.join([self.render_section(s) for s in self._sections])
        elif(len(self._blocks)):
            return NEWLINE.join([self.render_block(b) for b in self._blocks])
        elif(len(self._tables)):
            return NEWLINE.join([self.render_table(t) for t in self._tables])
        else:
            return ''


    def _flush_block(self, block_name=None):
        """Flush a block.

        Args:
            block_name(str):
                block to flush
                (if None) uses the default block
        """
        self._blocks[block_name] = []

    def _flush_table(self, table_name=None):
        """Flush a table.

        Args:
            table_name(str):
                table to flush
                (if None) uses the default table
        """
        self._tables[table_name] = {
            'header': [],
            'rows': [],
            'cols_count': 0,
            'cols_widths': [],
            'rows_count': 0,
            'has_header': False}

    def _flush_section(self, section_name=None):
        """Flush a section.

        Section is a sequence of paragraphs and/or tables and is
        used to bind multiple items together

        Args:
            section_name(str):
                section to flush
                (if None) uses the default section

        """
        self._sections[section_name] = []

    def _add_to_block(self, block_name, text):
        """Add the formatted text to a given block.

        Args:
            block_name(str):
                block to write to
                (if None) uses the default block
            text(str):
                formatted string to write
        """
        # append to the block the formatted text
        self._blocks[block_name].append(text)

        # declare it to be the element used last
        self._last_element = block_name

    def add_table_to_section(self, table_name=None, section_name=None):
        """Add a table to a section.

        Args:
            table_name(str):
                name of the table to add to the section
                (if None) adds the default table, if existing
            section_name(str):
                name of the section,
                (if None) uses the default section
        """
        # determine section
        if table_name not in self._tables:
            if table_name is None:
                err_msg = "Default table not yet used"
            else:
                err_msg = f"Table {table_name} not existing"
            raise ValueError(err_msg)

        self._sections[section_name].append({"type": "table", "name": table_name})

    def add_block_to_section(self, block_name=None, section_name=None):
        """Add a block to a section.

        Args:
            block_name(str):
                name of the block to add to the section
                (if None) adds the default block, if existing
            section_name(str):
                name of the section,
                (if None) uses the default section
        """
        # determine section
        if block_name not in self._blocks:
            if block_name is None:
                err_msg = "Default block not yet used"
            else:
                err_msg = f"Block{block_name} not existing"
            raise ValueError(err_msg)

        self._sections[section_name].append({"type": "block", "name": block_name})

    def h1(self, text, block_name=None):
        """Add a h1 title to a block.

        Args:
            text(str):
                string to write
            block_name(str):
                block to write to
                (if None) uses the default block
        """
        self._add_to_block(
            block_name=block_name,
            text=self._h1(text)
        )

    @abstractmethod
    def _h1(self, text):
        """Generate markdown h1 title.

        Args:
            text(str):
                string to write
        Returns:
            str
        """
        pass

    def h2(self, text, block_name=None):
        """Add a h2 title to a block.

        Args:
            text(str):
                string to write
            block_name(str):
                block to write to
                (if None) uses the default block
        """
        self._add_to_block(
            block_name=block_name,
            text=self._h2(text)
        )

    @abstractmethod
    def _h2(self, text):
        """Generate markdown h2 title.

        Args:
            text(str):
                string to write
        Returns:
            str
        """
        pass

    def h3(self, text, block_name=None):
        """Add a h3 title to a block.

        Args:
            text(str):
                string to write
            block_name(str):
                block to write to
                (if None) uses the default block
        """
        self._add_to_block(
            block_name=block_name,
            text=self._h3(text)
        )

    @abstractmethod
    def _h3(self, text):
        """Generate markdown h3 title.

        Args:
            text(str):
                string to write
        Returns:
            str
        """
        pass

    def paragraph(self, text, block_name=None):
        """Add a paragraph to a block.

        Args:
            text(str):
                string contents of the paragraph
            block_name(str):
                block to write to
                (if None) uses the default block
        """
        self._add_to_block(
            block_name=block_name,
            text=self._paragraph(text)
        )

    @abstractmethod
    def _paragraph(self, text):
        """Generate markdown paragraph text.

        Args:
            text(str):
                string to write
        Returns:
            str
        """
        pass

    def codeparagraph(self, text, block_name=None):
        """Add a codeparagraph to a block.

        Args:
            text(str):
                string contents of the codeparagraph
            block_name(str):
                block to write to
                (if None) uses the default block
        """
        self._add_to_block(
            block_name=block_name,
            text=self._codeblock(text)
        )

    @abstractmethod
    def _codeblock(self, text):
        """Generate markdown codeparagraph.

        Args:
            text(str):
                string to write
        Returns:
            str
        """
        pass

    def render_block(self, block_name=None):
        """Get the markdown string of a block.

        Args:
            block_name(str):
                block to render
                (if None) renders the default block

        Return:
            str
        """
        return self._render_block(self._blocks[block_name])

    @abstractmethod
    def _render_block(self, block):
        """Finalize text block output.

        Args:
            block(list):
                list of strings corresponding to block elements

        Return:
            str
        """
        pass

    def render_section(self, section_name=None):
        """Get the markdown string of a section.

        Args:
            section_name(str):
                section to render
                (if None) renders the default section

        Return:
            str
        """
        return self._render_section(self._sections[section_name])

    @abstractmethod
    def _render_section(self, section):
        """Finalize section output.

        Args:
            section(list):
                list of section components

        Return:
            str
        """
        pass

    def render_table(self, table_name=None):
        """Get the markdown string of a table.

        Args:
            table_name(str):
                table to render
                (if None) renders the default

        Return:
            str
        """
        return self._render_table(self._tables[table_name])

    @abstractmethod
    def _render_table(self, table):
        """Finalize table output.

        Args:
            table(dict):
                table with all its elements
        Return:
            str
        """
        pass

    def add_header(self, header, table_name=None):
        """Add a header to a table.

        Args:
            header(str[]):
                list of strings
            table_name(str):
                table to add header columns to
                (if None) uses the default table
        """
        # convert to strings
        header = [str(c) for c in header]

        # new lines not yet supported
        if any([NEWLINE in c for c in header]):
            raise ValueError('Multi-lines cells not yet supported')

        # if table not yet existing, create it
        if table_name not in self._tables:
            self._flush_table(table_name)

        # check whether the additon is consistent with the table
        if self._tables[table_name]['has_header']:
            raise ValueError('Header already added')

        if self._tables[table_name]['cols_count'] != 0 and self._tables[table_name]['cols_count'] != len(header):
            raise ValueError('Number of cells in the header inconsistent with the number of columns of the table')

        # update the column widths
        if self._tables[table_name]['rows_count'] > 0:
            # some rows are already in the table, update the widths
            self._tables[table_name]['cols_widths'] = [max(a, b) for a, b in \
                zip(self._tables[table_name]['cols_widths'], [len(h) for h in header])]
        else:
            # no rows yet, define the widths from the header
            self._tables[table_name]['cols_widths'] = [len(h) for h in header]

        # all OK, add the header
        self._tables[table_name]['header'] = header
        self._tables[table_name]['has_header'] = True
        self._tables[table_name]['cols_count'] = len(header)

        # declare it to be the element used last
        self._last_element = table_name

    def add_row(self, row, table_name=None):
        """
        Add a row to a table.

        Args:
            row(str[]):
                list of strings
            table_name(str):
                table to add header columns to
                (if None) uses the default table
        """
        # convert to strings
        row = [str(c) for c in row]

        # new lines not yet supported
        if any([NEWLINE in c for c in row]):
            raise ValueError('Multi-lines cells not yet supported')

        # if table not yet existing, create it
        if table_name not in self._tables:
            self._flush_table(table_name)

        # check whether the additon is consistent with the table
        if self._tables[table_name]['cols_count'] != 0 and self._tables[table_name]['cols_count'] != len(row):
            raise ValueError('Number of cells in the row inconsistent with the number of columns of the table')

        # update the column widths
        if  self._tables[table_name]['has_header'] or self._tables[table_name]['rows_count']>0:
            # header or some rows are already in the table, update the widths
            self._tables[table_name]['cols_widths'] = [max(a,b) for a,b in \
                zip(self._tables[table_name]['cols_widths'], [len(c) for c in row])]
        else:
            # no rows/header yet, define the widths from this row
            self._tables[table_name]['cols_widths'] = [len(c) for c in row]

        # all OK, add the row
        self._tables[table_name]['rows'].append(row)
        self._tables[table_name]['cols_count'] = len(row)
        self._tables[table_name]['rows_count'] += 1

        # declare it to be the element used last
        self._last_element = table_name

    def df_to_table(self, df, table_name=None,
                    replace_newlines=False, replace_with='; '):
        """Generate a full table for a given pandas dataframe.

        Args:
            df(pandas.core.frame.DataFrame):
                dataframe
            table_name(str):
                table to generate
                (if None) uses the default table
            replace_newlines(boolean):
                True if newline char should be replaced
            replace_with(str):
                what to replace newline char with
        """
        if table_name in self._tables:
            raise ValueError('Table under {} already existing'.format(table_name))
        if not isinstance(df, pd.core.frame.DataFrame):
            raise TypeError('Not a pandas dataframe')
        if isinstance(df.columns, pd.core.indexes.multi.MultiIndex):
            raise ValueError('Multi-index columns not supported')

        # convert cells to strings
        df_s = df.applymap(str)

        # replace function
        rep = lambda x : x if not replace_newlines else x.replace('\r\n',NEWLINE).replace(NEWLINE,replace_with)

        # add header
        header = [rep(c).strip() for c in list(df_s.columns)]
        self.add_header(header, table_name)

        # iterate over rows and add them
        for i in df.index:
            row = [rep(c).strip() for c in list(df_s.loc[i,:])]
            self.add_row(row, table_name)

        # declare it to be the element used last
        self._last_element = table_name
