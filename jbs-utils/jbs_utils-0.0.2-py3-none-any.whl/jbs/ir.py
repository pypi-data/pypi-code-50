import pandas as pd
from SPARQLWrapper import SPARQLWrapper, CSV
from io import StringIO

_ENDPOINT_URI = 'http://tdk-jbs.cs.technion.ac.il:8890/sparql'
_GRAPH_URI = 'http://jbs.technion.ac.il'
_PREFIXES = {'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
             'owl': 'http://www.w3.org/2002/07/owl#',
             'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
             'jbo': 'http://jbs.technion.ac.il/ontology/',
             'jbr': 'http://jbs.technion.ac.il/resource/',
             'schema': 'https://schema.org/'}

# _SCOPE_TYPE = 'jbo:Text'
# _SCOPE_BOOKS = []
# _SCOPE_SECTIONS = []
# _SCOPE_AUTHORS = []

PROPERTIES_TEXT = ['rdfs:label', 'jbo:text', 'jbo:position']
# _SCOPE_PROPERTIES = []
# _PROPERTIES_ALIASES = {}
# _PROPERTIES_FILTERS = {}


def _escape(value: str):
    return value.replace('"', '\\"')


def set_endpoint(uri='http://tdk-jbs.cs.technion.ac.il:8890/sparql', graph='http://jbs.technion.ac.il'):
    global _ENDPOINT_URI, _GRAPH_URI
    _ENDPOINT_URI, _GRAPH_URI = uri, graph


class Scope:
    def __init__(self):
        self.PROPERTIES = []
        self.PROPERTIES_ALIASES = {}
        self.PROPERTIES_FILTERS = {}
        self.TYPE = 'jbo:Text'
        self.BOOKS = []
        self.SECTIONS = []
        self.AUTHORS = []

    def clear(self):
        self.TYPE = 'jbo:Text'
        self.SECTIONS.clear()
        self.AUTHORS.clear()
        self.BOOKS.clear()
        self.PROPERTIES.clear()
        self.PROPERTIES_ALIASES.clear()
        self.PROPERTIES_FILTERS.clear()

    def add_property(self, prop: str):
        """
        :param prop: e.g., 'jbo:text', 'rdfs:label'. A default column name is generated for each property.
        To change the default (particularly useful for nested propertied) write the name (alias) in
        square brackets, e.g., jbo:interprets#rdfs:label[pasuk]. Note: do not use aliases that collides with
        a property name from the ontology! (e.g., 'book').
        A filter may be defined for the property, e.g.,
        jbo:interprets#jbo:section#rdfs:label(bereshit_in_Hebrew). For nested properties, a filter for the
        last property is currently supported. Note that the filter currently looks for exact string match.
        :return:
        """

        has_alias, has_filter = False, False
        alias, _filter = '', ''

        if '[' in prop:  # we have an alias, e.g., rdfs:label[name]
            alias = prop.split('[')[1][:-1]  # remove the last ']'
            prop = prop.split('[')[0]
            has_alias = True

        if '(' in prop:  # we have a filter, e.g., rdfs:label(פרשת בראשית)
            _filter = prop.split('(')[1][:-1]
            prop = prop.split('(')[0]
            has_filter = True

        if has_alias:
            self.PROPERTIES_ALIASES[prop] = alias
        if has_filter:
            self.PROPERTIES_FILTERS[prop] = _filter

        if prop not in self.PROPERTIES:
            self.PROPERTIES.append(prop)

    def add_properties(self, properties: list):
        for prop in properties:
            self.add_property(prop)

    def add_book(self, book_label: str):
        book_uri = _get_uri('jbo:Book', _escape(book_label))

        if book_uri not in self.BOOKS:
            self.BOOKS.append(book_uri)

    def add_section(self, section_label: str):
        if len(self.BOOKS) != 1:
            raise Exception('A SINGLE book should be added to scope before adding a section.')

        book_uri = self.BOOKS[0]
        section_uri = _get_section_uri(book_uri, _escape(section_label))

        if section_uri not in self.SECTIONS:
            self.SECTIONS.append(section_uri)

    def add_author(self, author_label: str):
        author_uri = _get_uri('jbo:Person', _escape(author_label))

        if author_uri not in self.AUTHORS:
            self.AUTHORS.append(author_uri)

    def set_type(self, class_type: str):
        """
        Within a scope, only ONE type may be set at a time. If not specified, default type is 'jbo:Text'
        :param class_type: e.g., jbo:Book
        :return:
        """
        self.TYPE = class_type


def run_query(query: str, pretty=[], set_limit: int = 0, set_offset: int = 0, debug=False) -> pd.DataFrame:
    """
    Was taken from project elinda.py
    :param query:
    :param pretty: columns to make their URI pretty
    :param set_limit: limit the number of results. In case of '0' the is not limit
    :param set_offset: results offset. In case of '0' the is no offset
    :return:
    """

    if debug:
        print(query)

    sparql_wrapper = SPARQLWrapper(_ENDPOINT_URI)
    sparql_wrapper.addDefaultGraph(_GRAPH_URI)

    merged_results = pd.DataFrame()
    df = pd.DataFrame()
    sparql_wrapper.setReturnFormat(CSV)
    current_offset = set_offset
    if set_limit == 0:
        set_limit = 9999999999999999999999999
    # else:
    #     set_limit += set_offset
    limit_part = '\nLIMIT ' + str(set_limit)

    while ((len(df.index) != 0) or (current_offset == set_offset)) and (set_limit > 0 and current_offset < set_limit):
        offset_part = '\nOFFSET ' + str(current_offset)
        sparql_wrapper.setQuery(_prefixes_to_string() + "\n" + query + limit_part + offset_part)
        sparql_wrapper.setReturnFormat(CSV)
        results = sparql_wrapper.query().convert()
        results = results.decode("utf-8")
        results.split('\\n')
        df = pd.read_csv(StringIO(results))
        merged_results = merged_results.append(df, ignore_index=True)
        current_offset += 10000
        if (set_limit > 0) and (set_limit - current_offset < 10000):
            limit_part = '\nLIMIT ' + str(set_limit - current_offset + set_offset)

    for col in pretty:
        merged_results[col] = merged_results[col].apply(_show_uri_with_prefix)
    return merged_results


def fetch(scope: Scope, debug=False) -> pd.DataFrame:
    """
    Returns the subjects and property data specified in the scope. The default type of the subjects is jbo:Text
    and may be overriden by scope.set_type().
    :return:
    """

    if not scope.PROPERTIES:  # is empty
        print("Warning: no properties in scope.")

    book_values = _get_as_values('book', scope.BOOKS)
    author_values = _get_as_values('author', scope.AUTHORS)
    section_values = _get_as_values('section', scope.SECTIONS)

    # should be refactored...
    props = ''
    columns = []
    for prop in scope.PROPERTIES:
        alias = None if prop not in scope.PROPERTIES_ALIASES else scope.PROPERTIES_ALIASES[prop]
        _filter = None if prop not in scope.PROPERTIES_FILTERS else scope.PROPERTIES_FILTERS[prop]

        if '#' not in prop:  # not a nested property
            prop_var = prop.split(':')[1] if alias is None else alias
            props += '?uri %s ?%s.' % (prop, prop_var)
            props += _get_filter(prop_var, _filter)
            columns.append(prop_var)
        elif prop.count('#') == 1:  # a nested 2 property
            prop_split = _split_nested_property_string(prop)
            prop_var = prop_split[1][1] if alias is None else alias
            props += '?uri %s ?%s.' % (prop_split[0][0], prop_split[0][1])
            props += '?%s %s ?%s.' % (prop_split[0][1], prop_split[1][0], prop_var)
            props += _get_filter(prop_var, _filter)
            columns.append(prop_var)
        elif prop.count('#') == 2:  # a nested 3 property
            prop_split = _split_nested_property_string(prop)
            prop_var = prop_split[2][1] if alias is None else alias
            props += '?uri %s ?%s.' % (prop_split[0][0], prop_split[0][1])
            props += '?%s %s ?%s.' % (prop_split[0][1], prop_split[1][0], prop_split[1][1])
            props += '?%s %s ?%s.' % (prop_split[1][1], prop_split[2][0], prop_var)
            props += _get_filter(prop_var, _filter)
            columns.append(prop_var)
        elif prop.count('#') == 3:  # a nested 4 property
            prop_split = _split_nested_property_string(prop)
            prop_var = prop_split[3][1] if alias is None else alias
            props += '?uri %s ?%s.' % (prop_split[0][0], prop_split[0][1])
            props += '?%s %s ?%s.' % (prop_split[0][1], prop_split[1][0], prop_split[1][1])
            props += '?%s %s ?%s.' % (prop_split[1][1], prop_split[2][0], prop_split[2][1])
            props += '?%s %s ?%s.' % (prop_split[2][1], prop_split[3][0], prop_var)
            props += _get_filter(prop_var, _filter)
            columns.append(prop_var)
        elif prop.count('#') > 3:
            raise Exception('not supported yet...')

    columns_header = '?' + ' ?'.join(columns) if columns else ''
    query = """SELECT ?uri %s WHERE {
        %s
        %s
        %s
        ?uri a %s.
        %s
        %s
        %s
        %s
        }""" % (columns_header, book_values if scope.BOOKS else '', author_values if scope.AUTHORS else '',
                section_values if scope.SECTIONS else '', scope.TYPE, '?uri jbo:book ?book.' if scope.BOOKS else '',
                '?book jbo:author ?author.' if scope.AUTHORS else '',
                '?uri jbo:within ?section.' if scope.SECTIONS else '', props)

    pretty = ['uri']
    for col in columns:
        pretty.append(col)

    # print(query)
    return run_query(query, pretty=pretty, debug=debug)


# General purpose queries

def get_all_books() -> list:
    """
    Returns all the books in the JBS dataset.
    :return:
    """
    query = """SELECT ?uri ?label  WHERE {
        ?uri a jbo:Book; rdfs:label ?label.
        }"""

    return run_query(query)['label'].tolist()


def get_info_tanach_mefarshim_by_book(torah_only=False) -> pd.DataFrame:
    """
    Returns a dataframe with information about Tanach mefarshim (by books),
    where each row describes a pair (mefaresh, book).
    Dataframe columns: mefaresh, book, words_total, words_avg, coverage, year
    """
    rows = []
    perushim = get_tanach_perushim(torah_only=torah_only)
    book_info = get_info_tanach_books()

    grouped = perushim.groupby(['mefaresh', 'tanach_book'])

    for (mefaresh, book) in grouped.groups.keys():
        this_row = {'mefaresh': mefaresh, 'book': book}

        # set words_total, words_avg
        group = grouped.get_group((mefaresh, book))
        this_row['words_total'] = group.size_words.sum()
        this_row['words_avg'] = group.size_words.mean()

        # set year
        this_row['year'] = group.year.iloc[0]

        # set coverage
        book_pasuk_total = book_info.loc[book_info['book_name'] == book]['pasuk_total'].values[0]
        this_row['coverage'] = round((len(group) / book_pasuk_total) * 100, 1)

        rows.append(this_row)

    return pd.DataFrame(rows)


def get_info_tanach_books() -> pd.DataFrame:
    """
    Returns a dataframe with information about Tanach books, where each row describes a single book.
    Dataframe columns: book_name, position, pasuk_total
    """
    query = """
            SELECT ?book_name ?position COUNT(?pasuk) AS ?pasuk_total WHERE {
                ?pasuk a jbo:Pasuk; jbo:book ?book.
                ?book rdfs:label ?book_name; jbo:position ?position.
                } GROUP BY ?book_name ?position
            """
    return run_query(query)


def get_tanach_perushim(torah_only=False, section_heb=None) -> pd.DataFrame:
    """
    Returns a dataframe with all the perushim on the Tanach.

    :param torah_only: True to retrieve only Torah perushim
    :param section_heb: name of a parasha (e.g., parashat bereshit) or perek (e.g., bereshit a)
    where perushim should relate to.
    :return:
    """

    scope = Scope()

    perush_type = 'jbo:PerushTorah' if torah_only or section_heb is not None else 'jbo:PerushTanach'
    scope.set_type(perush_type)
    properties = ['rdfs:label[perush]', 'jbo:book#jbo:year[year]', 'jbo:numOfWords[size_words]',
                  'jbo:book#rdfs:label[mefaresh]',
                  'jbo:interprets#rdfs:label[pasuk]',
                  'jbo:interprets#jbo:book#rdfs:label[tanach_book]',
                  'jbo:interprets#jbo:book#jbo:position[tanach_book_position]',
                  'jbo:interprets#jbo:text[pasuk_text]',
                  'jbo:interprets#jbo:position[pasuk_position]']
    if section_heb is not None:
        properties.append('jbo:interprets#jbo:within#rdfs:label(%s)[section]' % section_heb)

    scope.add_properties(properties)

    return fetch(scope)


def get_properties_for_type(class_type: str) -> list:
    """
    Returns the properties for the given type. Note that we sample
    one subject for knowing that so the result may not be correct if the
    subjects so not share the same properties.

    :param class_type:
    :return:
    """

    # first we sample one subject:
    query = """SELECT ?uri  WHERE {
            ?uri a %s.
            }""" % class_type

    df = run_query(query, set_limit=1)
    uri = df.uri[0]

    properties = _get_properties(uri)

    return [p for p in properties.property]


#####################
# Utility functions #
#####################
def _get_uri(class_type: str, label: str):
    """
    Returns a URI with that type and label
    :param class_type: e.g., 'jbo:Book'
    :param label: e.g., 'tanach' (in Hebrew)
    :return:
    """
    query = 'SELECT ?uri WHERE {?uri a %s. ?uri rdfs:label "%s"}' % (class_type, label)
    df = run_query(query)
    if len(df) == 0:
        raise Exception('No uri found for %s' % label)
    elif len(df) > 1:
        raise Exception('Many URIs found for %s' % label)
    else:
        return df['uri'].iloc[0]


def _get_section_uri(book_uri: str, section_label: str):
    query = 'SELECT ?uri WHERE {?uri a jbo:Section; jbo:book <%s>; rdfs:label "%s".}' % (book_uri, section_label)
    df = run_query(query)
    if len(df) == 0:
        raise Exception('No section found for %s' % section_label)
    elif len(df) > 1:
        raise Exception('Many sections found for %s' % section_label)
    else:
        return df['uri'].iloc[0]


def _prefixes_to_string():
    prefixes_str = ""
    for prefix, value in _PREFIXES.items():
        prefixes_str += 'PREFIX ' + prefix + ': <' + value + '>\n'
    return prefixes_str


def _get_properties(uri: str) -> pd.DataFrame:
    """Returns the properties this uri, e.g., jbr:text-tanach-rashi-1-1-1, has"""
    query = """SELECT DISTINCT(?property)  WHERE {
        <%s> ?property [].
        }""" % uri

    df = run_query(query, pretty=['property'])
    # df['property'] = df['property'].apply(_show_uri_with_prefix)
    return df


def _get_as_values(var_name: str, uri_list: list, brackets=True):
    values = 'VALUES ?%s {' % var_name
    for uri in uri_list:
        values += '%s%s%s ' % ('<' if brackets else '', uri, '>' if brackets else '')

    values += '}\n'
    return values


def _get_filter(prop_name: str, _filter: str):
    return 'FILTER (str(?%s) = "%s")' % (prop_name, _filter) if _filter is not None else ''


def _split_nested_property_string(nested_string: str):
    """
    E.g., given jbo:interprets#jbo:within#rdfs:label, return a list of tuples:
    [('jbo:interprets', 'interprets'), ('jbo:within', 'interprets_within'), ('rdfs:label', 'interprets_within_label')]

    :param nested_string:
    :return:
    """

    result = []
    prop_var = ''

    for prop in nested_string.split('#'):
        prop_var += '_' + prop.split(':')[1]
        if prop_var.startswith('_'):
            prop_var = prop_var[1:]  # remove leading underscore
        result.append((prop, prop_var))

    return result


def _get_prefix_for_uri(url):
    for prefix, address in _PREFIXES.items():
        if address == url:
            return prefix
    return ''


def _show_uri_with_prefix(uri):
    # is it a URL?
    if not isinstance(uri, str) or not (uri.startswith('http://') or uri.startswith('https://')):
        return uri  # do nothing, it is not a URI

    if '#' in uri:
        tag = uri.split('#')[-1]
        uri = uri.rsplit('#', 1)[0] + '#'
    else:
        tag = uri.split('/')[-1]
        uri = uri.rsplit('/', 1)[0] + '/'
    prefix = _get_prefix_for_uri(uri)
    return prefix + ':' + tag


if __name__ == "__main__":
    print(get_properties_for_type('jbo:Book'))
