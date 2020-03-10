import sys
import os
import re
from py2neo import Graph, Node, Relationship, NodeMatcher, RelationshipMatcher
from tei2neo import parse, GraphUtils


def my_sort(coll):
    def my_coll_sort(val):
        match = re.search(r'\d+_Ms_{}_(?P<page>\d+)'.format(coll), val)
        if match:
            return int(match.groupdict()['page'])
        else:
            return 0
    return my_coll_sort


def my_filter(coll):
    def my_coll_filter(val):
        match = re.search(r'^\d+_Ms_{}.*?xml$'.format(coll), val)
        return match
    return my_coll_filter


def get_graph():
    host = input('hostname (localhost):') or 'localhost'
    port = input('port (7687):') or '7687'
    user = input('port (neo4j):') or 'neo4j'
    import getpass
    password = getpass.getpass('password:') or os.environ.get('SEMPER_NEO4_PASSWORD')

    graph = Graph(
        host = host, 
        port = port,
        user = user,
        password = password,
    )
    return graph


def import_file(filepath, graph=None):
    if graph is None:
        graph = get_graph()
    ut = GraphUtils(graph)

    filepath = os.path.abspath(filepath)
    filename = os.path.basename(filepath)

    ut.delete_graph_for_file(filename)

    # import
    doc, status, soup = parse(filename=filepath)
    tx = graph.begin()
    doc.save(tx)
    tx.commit()

    # create the relationships within the document
    ut.link_inner_relationships(filename)

    # connect the document to existing categories
    ut.connect_to_categories(filename)

    # get all paragraphs in a file
    paras = ut.paragraphs_for_filename(filename)

    # create the unhyphened tokens
    for para in paras:
        tokens = ut.tokens_in_paragraph(para)
        ut.create_unhyphenated(tokens)


def import_files_from_path(path, graph=None):
    """Imports all xml files from a given directory.
    These files must fit the pattern and are ordered by their page number
    before they are imorted.
    """
    if os.path.isfile(path):
        import_file(path)
        return

    if graph is None:
        graph = get_graph()
    ut = GraphUtils(graph)

    # get the last directory name as an indicator for the collection
    collection = os.path.basename(os.path.normpath(path))

    filenames = []
    for root, dirs, files in os.walk(path):
        for filename in sorted(
                filter(my_filter(coll=collection), files),
                key=my_sort(coll=collection)
        ):
            filenames.append(filename)

            filepath = os.path.join(root, filename)
            print(filename)
            import_file(filepath, graph)

            filenames.append(filename)

    ut.connect_teis(*filenames)


if __name__ == '__main__':
    import_files_from_path(sys.argv[1])
