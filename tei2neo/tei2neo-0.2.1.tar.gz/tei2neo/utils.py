from py2neo import Graph, Node, Relationship, NodeMatcher, ClientError
from collections import defaultdict
from .semper_mapping import classes_for_token


class GraphUtils():

    def __init__(self, graph):
        self.graph = graph

    def delete_graph_for_file(self, filename):
        cursor = self.graph.run(
            'MATCH(n) WHERE n.filename=$filename DETACH DELETE n', 
            parameters = {
                "filename": filename
            }
        )

    def delete_graph(self):
        cursor = self.graph.run( 'MATCH(n) DETACH DELETE n' )


    def get_teis_for_categories(self, categories=None, operator="AND"):
        """For given categories, this method searches database and returns TEI nodes
        that are of these categories.
        """
        if categories == None:
            categories = []
        elif not isinstance(categories, list):
            categories=[categories]

        wheres = ['"{}" IN tei.categories'.format(category) for category in categories]
        where = (" "+operator+" ").join(wheres)
        if not where:
            # if no categories are provided, make sure that at least only return
            # TEI documents that contain the categories attribute
            where = "EXISTS( tei['categories'])"

        cypher = """
            MATCH (tei :TEI)
            WHERE {}
            RETURN tei
        """
        cursor = self.graph.run(cypher.format(where))

        teis = []
        while cursor.forward():
            for tei in cursor.current:
                teis.append(tei)
        return teis


    def paragraphs_for_filename(self, filename, only_with_matching_zone=True):
        kwargs = { "filename": filename }

        cypher = ""
        if only_with_matching_zone:
            cypher = """
                MATCH(paragraph :p {filename:$filename})-[:facs]->(zone :zone)
                RETURN paragraph, zone
            """
        else:
            cypher = """
                MATCH(paragraph :p {filename:$filename})
                OPTIONAL MATCH (p)-[:facs]->(zone :zone)
                RETURN paragraph, zone
            """
        cursor = self.graph.run(
            cypher,
            parameters = {
                "filename": filename
            }
        )

        paragraphs = []
        while cursor.forward():
            paragraph, zone = cursor.current
            paragraph.zone = zone
            paragraphs.append(paragraph)

        return paragraphs


    def nodes_with_link_for_filename(self, filename):
        """for a given filename, this query returns all nodes
        that contain any of the link_attributes (see below)
        The goal is to create relationships from these nodes to their targets
        """

        kwargs = { "filename": filename }
        link_attributes = ["facs", "next", "prev", "target", "ref"]
        where = " OR ".join("EXISTS(n.{})".format(attr) for attr in link_attributes)
        cypher = """
            MATCH (n)
            WHERE 
        """
        cypher += where
        cypher += " RETURN n"

        nodes = []
        while cursor.forward():
            for nodes in cursor.current:
                nodes.append(nodes)

        return nodes


    def concatenation_exists(self, node):
        cypher = """
        MATCH (node1)-[r :CONCATENATED]->(node2)
        WHERE ID(node1) = $node_id
        RETURN r
        """
        cursor = self.graph.run(cypher, parameters={"node_id": node.identity})

        # return 1 if there exists a relation
        return cursor.forward()

    def get_categories(self):
        cypher = """
        MATCH (cat :category)
        RETURN cat.`xml:id` as id, cat.description
        """
        cats = []
        while cursor.forward():
            for cat in cursor.current:
                cats.append(cat)

        return cats


    def paras2dict(self, paras, words_concatenated=0, follow_metamarks=True):
        """Takes an array of paragraph tokens
        returns a dictionary:
        {
            "zones": {}
            "paragraphs": []
        }
        
        """
        # translate True/False values to 0 and 1
        if words_concatenated:
            words_concatenated = 1
        else:
            words_concatenated = 0

        paras_dict = {}
        zones = {}
        paras_dict["zones"] = zones
        paras_dict["paragraphs"] = []
        delspan_to = ""

        for para in paras:
            zones["#"+para.zone.get('xml:id')]= {
                "points": para.zone.get('points'),
                "rendition": para.zone.get('rendition'),
                "subtype": para.zone.get('subtype'),
            }
            is_add = False
            metamark_start = False
 
            current_classes = set()
            create_new_token_group = False
 
            current_para = para
 
            current_token_group = None
            elements = []
 
            paragraph_dict = {
                "facs": para.get('facs'),
                "xml:id": para.get('xml:id'),
                "_elements": elements
            }
            paras_dict["paragraphs"].append(paragraph_dict)
 
            string = ""
            for token in self.tokens_in_paragraph(
                para,
                concatenated=words_concatenated,
                follow_metamarks=follow_metamarks
            ):
                    
                new_facs = ""

                # handle end of an add element
                if is_add and not 'add' in token.labels:
                    # mark end of the addition: ⟩
                    elements.append({
                        "string": "⟩",
                        "classes": list(current_classes)
                    })
                    is_add = False

                # handle end of a delSpan element
                if 'anchor' in token.labels and delspan_to and token.get('anchor','') in delspan_to:
                    elements.append({
                        "string": "◀",
                        "classes": list(current_classes),
                    })
                    delspan_to=""

                # handle metamarks: the token has a different paragraph_id
                # create a new token group when this happens
                if not current_para.get('xml:id') == token.get('paragraph_id'):
                    current_para = self.get_paragraph(
                        filename=token.get('filename'),
                        xml_id = token.get('paragraph_id')
                    )
                    create_new_token_group = True
                    new_facs = current_para.get('facs')

                # check if anything changed
                new_classes = classes_for_token(token)
                if not new_classes == current_classes:
                    create_new_token_group = True
 
                # handle <add> elements: add ⟨here is added string⟩
                # prepend another element
                if 'add' in token.labels and not is_add:
                    # mark addition-start: ⟨
                    # put it in front of current strings
                    elements.append({
                        "string": "⟨",
                        "classes": list(current_classes)
                    })
                    is_add = True
 
                # handle beginning of a delSpan: prepend another element
                if 'delSpan' in token.labels and not delspan_to:
                    elements.append({
                        "string": "▶",
                        "classes": list(current_classes),
                    })
                    delspan_to = token.get('spanTo')


                # create a new token group: all strings will be appended
                # as long they have the same style
                if create_new_token_group or current_token_group is None:
                    current_classes = new_classes
                    current_token_group = {
                        "string": "",
                        "classes": list(current_classes),
                    }
                    if new_facs:
                        current_token_group["facs"] = new_facs
                        new_facs = None
                    create_new_token_group = False

                    # append the token group to our elements
                    elements.append(current_token_group)
 
                # handle linebreaks
                if 'lb' in token.labels:
                    current_token_group['string'] += " | "
                    continue

                # append the string, including whitespace
                current_token_group['string'] += token.get('string', '') + token.get('whitespace','')


            # is still in add: close it when paragraph ends
            if is_add:
                elements.append({
                    "string": "⟩",
                    "classes": list(current_classes)
                })
                is_add = False

        # still in delSpan: close it when all paragraphs are done:
        if delspan_to:
            elements.append({
                "string": "◀",
                "classes": list(current_classes),
            })
            delspan_to=""


        return paras_dict


    def tokens_in_paragraph(self, paragraph:Node, concatenated=0, follow_metamarks=False):
        """For a given paragraph, this method returns all nodes
        connected via a NEXT relationship. 
        If concatenated=1, it will return a concatenated version of the textpath.
        Returns all nodes in the found textpath.
        """

        cypher="""
        MATCH (para)-[:NEXT]->(t),
        textpath = shortestPath((t)-[:NEXT*]->(lt))
        WHERE ID(para)=$paragraph_id
        AND (para)-[:LAST]->(lt)
        AND ALL (
            rel IN relationships(textpath)
            WHERE (rel.concatenated IS NULL OR rel.concatenated = $concatenated)
        )
        RETURN nodes(textpath)
        """
        # NOTE: it is assumed that a path containing a concatenated (non-hyphened)
        # word will be always shorter than a path containing a hyphened word.
        # The non-concatenated textpath actually never has the relation-attribute 
        # rel.concatenated=0 (it is always NULL)

        cursor = self.graph.run(
            cypher, 
            parameters={
                "paragraph_id": paragraph.identity,
                "concatenated": concatenated
            }
        ) 

        tokens = []
        while cursor.forward():
            for entry in cursor.current:
                for token in entry:
                    if follow_metamarks \
                    and 'metamark' in token.labels \
                    and token.get('function', '') == 'Einfügung' \
                    and token.get('target', ''):
                        tei_file, anchor = token.get('target').split('#')
                        if not tei_file:
                            tei_file = paragraph.get('filename')
                            target_paragraph = self.get_paragraph(
                                filename = tei_file,
                                xml_id = anchor
                            )
                            if target_paragraph:
                                metamark_tokens = self.tokens_in_paragraph(
                                    paragraph = target_paragraph,
                                    concatenated = concatenated,
                                    follow_metamarks = follow_metamarks
                                )
                                tokens += metamark_tokens
                    else:
                        tokens.append(token)
        return tokens


    def get_paragraph(self, filename, xml_id):
        """Returns a paragraph node for filename and xml_id
        """

        parameters = { 
            "filename": filename,
            "xml_id": xml_id,
        }

        cypher = """
            MATCH (paragraph :p {filename:$filename, `xml:id`: $xml_id})
            OPTIONAL MATCH (p)-[:facs]->(zone :zone)
            RETURN paragraph, zone
        """
        cursor = self.graph.run(cypher, parameters = parameters)

        while cursor.forward(amount=2):
            paragraph, zone = cursor.current
            paragraph.zone = zone

        return paragraph
                


    def tokens_in_paragraphs(self,
        paragraphs,
        concatenate_words=0,
        concatenate_paragraphs=0,
        follow_metamarks=0
    ):
        """For a given list of paragraphs (nodes) this method tries to:
        - return concatenated words,
        - concatenate paragraphs, when they are connected via next and prev attributes
        - follow metamarks, when linked via target attribute
        - remove duplicate paragraphs i.e. paragraphs that have already been
          visited should not appear again.
        - this method is not recursive, i.e. search-depth is 1, which should be fine in 99% of the cases.
        """
        paragraph_visited = {}
        paragraph_dict = {}
        for paragraph in paragraphs:
            paragraph_dict[paragraph.identity] = paragraph 

        nodes = []

        for paragraph in paragraphs:
            if paragraph.identity in paragraph_visited:
                continue
            nodes.append(paragraph)
            tokens = self.tokens_in_paragraph(paragraph, concatenated=concatenate_words)
            for token in tokens:
                nodes.append(token)
                if 'metamark' in token.labels\
                and token.get('target', False):
                    tei_file, anchor = token.get('target').split('#')
                    if anchor in paragraph_dict:
                        metamark_tokens = self.tokens_in_paragraph(
                            paragraph_dict[anchor], 
                            concatenated=concatenate_words
                        )
                        nodes += metamark_nodes
                        paragraph_visited[anchor] = True 

        return


    def create_unhyphenated(self, tokens):
        """tokens=Array of all tokens in a paragraph, as returned
        by GraphUtils.tokens_in_paragraph(para). This procedures looks for linebreaks with type=hyph
        If found, it looks forward and backwards to find the hyphened wordparts
        It then concatenates the wordparts, creates a new Node and new Releations.
        """
        tx = self.graph.begin()

        for i, token in enumerate(tokens):
            j=0
            k=0
            if token.has_label('lb'):
                wordstart = None
                wordend = None
                if token.get('type') == 'hyph':
                    
                    # walk back and find a token which is a wordpart
                    # and not any punctuation or similar
                    j=i-1
                    while j>0:
                        #print("j = {}".format(j))
                        if tokens[j].has_label('token') \
                        and tokens[j]["string"] \
                        and not tokens[j]["is_punct"]: 
                            #print("TRY: "+str(tokens[j]))
                            wordstart = tokens[j]
                            break
                        else:
                            j = j-1

                    # walk forward and find a token
                    k=i+1
                    while k>0 and tokens[k]:
                        #print("k = {}".format(k))
                        if tokens[k].has_label('token'):
                            #print("TRY END: "+str(tokens[k]))
                            wordend = tokens[k]
                            break
                        else:
                            k = k+1
                          
                    concat_word = ''
                    if wordstart and wordend and not self.concatenation_exists(wordstart):
                        #print("---START: "+str(wordstart))
                        #print("---  END: "+str(wordend))
                        if any(
                            wordstart["string"].endswith(s) for s\
                            in ['-', '\N{NOT SIGN}', '\N{NON-BREAKING HYPHEN}']
                        ):
                            concat_word = wordstart["string"][:-1]
                        else:
                            concat_word = wordstart["string"]
                            
                        concat_word += wordend["string"]
                        
                        # create new concatenated token
                        # with blank as whitespace
                        labels = list(
                            set(
                                ['token', 'concatenated'] + list(wordstart.labels) + list(wordend.labels)
                            )
                        )
                        attrs = { 
                            "string"    : concat_word,
                            "whitespace": wordend["whitespace"],
                            "filename"  : wordstart["filename"],
                            "idno"      : wordstart["idno"],
                        }
                        concat_node = Node(
                            *labels,
                            **attrs
                        )
                        #print("+ {}".format(concat_word))
                        tx.create(concat_node)
                        
                        # create relations from hyphened wordpards to concatenated word
                        rs = Relationship(
                            wordstart,
                            "CONCATENATED",
                            concat_node
                        )
                        rs2 = Relationship(
                            wordend,
                            "CONCATENATED",
                            concat_node
                        )
                        tx.create(rs)                
                        tx.create(rs2)
                        
                        # create direct connection for non-hyphened version
                        # of the thext
                        if j >0:
                            before_wordstart = tokens[j-1]
                            rs3 = Relationship(
                                before_wordstart,
                                "NEXT",
                                concat_node,
                                concatenated=1
                            )
                            tx.create(rs3)
                            
                        if len(tokens) > k+1:
                            after_wordend = tokens[k+1]
                            rs4 = Relationship(
                                concat_node,
                                "NEXT",
                                after_wordend,
                                concatenated=1
                            )
                            tx.create(rs4)
        tx.commit()

    def connect_teis(self, *filenames):
        """Connects the TEI nodes with NEXT and PREV, given the filenames
        This allows to quickly show the previous and next pages of a document
        """
        if len(filenames)<2:
            raise ValueError("Please provide at least two filenames")

        for i in range(len(filenames)-1):
            cypher = """
            MATCH (tei1 :TEI)
            WHERE tei1.filename = $filename1
            MATCH (tei2 :TEI)
            WHERE tei2.filename = $filename2
            MERGE (tei1)-[:NEXT]->(tei2)
            MERGE (tei2)-[:PREV]->(tei1)
            """ 
            parameters = {
                "filename1": filenames[i],
                "filename2": filenames[i+1]
            }
            cursor = self.graph.run(cypher, parameters=parameters)


    def connect_to_categories(self, filename):
        """Connects the categories in the catRef element
        with the existing categories in the graph database.
        Returns the category nodes for the given document.
        """
        cypher = """
        // match the catRef element and extract its category-targets
        MATCH (cat :catRef)
        WHERE cat.filename = $filename
        AND cat['target'] IS NOT NULL
        WITH SPLIT(cat['target'], " ") as pointers
        UNWIND pointers as pointer
        WITH SPLIT(pointer, "#") AS target

        // match the corresponding category targets
        MATCH (c :category)
        WHERE c.`xml:id` = target[1]

        // create relationships between the categories and the TEI node
        MATCH (tei :TEI)
        WHERE tei.filename = $filename
        MERGE (tei)-[:HAS_CATEGORY]->(c)
        RETURN c
        """

        parameters = { "filename": filename }
        cursor = self.graph.run(cypher, parameters = parameters)
        categories = []
        while cursor.forward():
            for category in cursor.current:
                categories.append(category)
        return categories

    def connect_references(self, filename):
        """Connects reference strings elements <rs> to its register nodes
        """

        cypher = """
        // match the rs element and extract its ref
        MATCH (rs :rs)
        WHERE rs.filename = $filename
        AND rs['ref'] IS NOT NULL
        AND rs['type'] IS NOT NULL
        WITH SPLIT(rs['ref'], " ") as pointers,
        rs['type'] as rs_type
        UNWIND pointers as pointer
        WITH rs_type, SPLIT(pointer, "#") AS target
        MATCH (ref)
        WHERE rs_type in labels(ref)
        AND ref.filename = target[0]
        AND ref.`xml:id` = target[1]

        // match the corresponding references
        MATCH (c :)
        WHERE c.`xml:id` = target[1]

        """

    def link_inner_relationships(self, filename):
        """creates new relationships between nodes of a given filename,
        that contain one of the link attributes below which point to
        a node inside the same xml file. Ignores all :join nodes, because
        they are handled by the handle_join_elements method.

        Within a link attribute, pointers can be separated by whitespace
        https://www.tei-c.org/release/doc/tei-p5-doc/en/html/ref-att.global.linking.html

        This method should be only run once after a TEI document has
        been parsed.
        Does not return anything.
        """
        
        link_attributes = ["facs", "next", "prev", "target", "ref"]

        cypher = """
        MATCH (from_node)
        WHERE from_node.filename = $filename
        AND NOT from_node:join
        AND from_node[$link_attribute] IS NOT NULL
        WITH from_node, SPLIT(from_node[$link_attribute], " ") AS pointers
        UNWIND pointers as pointer
        WITH from_node, SPLIT(pointer, "#") AS target
        WITH from_node, target,
        CASE WHEN target[0] = "" 
            THEN $filename 
            ELSE target[0] 
            END 
        AS filename
        MERGE (to_node {filename: filename, `xml:id`:target[1]} )
        """

        for link_attribute in link_attributes:
            parameters = {
                "filename"      : filename,
                "link_attribute": link_attribute,
            }
            create_rel = " CREATE (from_node)-[r:{}]->(to_node)".format(
                link_attribute.lower()
            )
            cursor = self.graph.run(cypher+create_rel, parameters = parameters)


    def tei_for_categories(self, *categories):
        exists_categories = []
        for category in categories:
            exists_categories.append(
                'EXISTS ((tei)-[:HAS_CATEGORY]->(:category {`xml:id`: "{}"}))'.format(category)
            )

        cypher = "MATCH (tei :TEI) WHERE"
        cypher += " AND ".join(exists_categories)
        cypher += " RETURN tei"
        cursor = self.graph.run(cypher)

        teis = []
        while cursor.forward():
            for tei in cursor.current:
                teis.append(category)
        return teis


    def handle_join_elements(self, filename):
        """Searches for all <join> elements for a given filename.
        Creates relationships between the mentioned elements of the «target» attribute
        Does not return anything.
        TODO: modify this method to establish a connection between two tokens
        on separate pages:
        (ta :token {`xml:id`:"p.page1"})-[:NEXT]->(tb :token {``xml:id`:"p.page2"})
        And update all tokens so they contain the identfiers of both joined paragraphs
        """
        
        cypher = """
            MATCH (join_node :join)
            WHERE join_node.filename = $filename
            AND join_node['target'] IS NOT NULL
            WITH join_node, SPLIT(join_node['target'], " ") AS endpoints
            WITH join_node, SPLIT(endpoints[0], "#") AS source, SPLIT(endpoints[1], "#") AS target
            WITH join_node, source, target,
            CASE WHEN source[0] = "" THEN $filename ELSE source[0] END AS source_filename,
            CASE WHEN target[0] = "" THEN $filename ELSE target[0] END AS target_filename
            MERGE (from_node {filename: source_filename, `xml:id`:source[1]})
            MERGE (to_node {filename: target_filename, `xml:id`:target[1]})
            MERGE (from_node)-[r :JOIN]->(to_node)
        """

        parameters = { "filename": filename }
        cursor = self.graph.run(cypher, parameters = parameters)


    def search_for_terms(self, terms, scope="page", categories=None):

        def get_search_mode_term(term):
            mode = ""
            import re
            if term.startswith("*") and term.endswith("*"):
                term = re.sub(r'\*', '', term)
                mode = "CONTAINS"
            elif term.startswith("*"):
                term = re.sub(r'\*', '', term)
                mode = "ENDS WITH"
            elif term.endswith("*"):
                term = re.sub(r'\*', '', term)
                mode = "STARTS WITH"
            else:
                mode = "="
            return (mode, term)


        if not isinstance(terms, list):
            terms = [terms]

        cypher = """
            MATCH (n0:token)
            WHERE n0.string {} "{}"
        """.format(*get_search_mode_term(terms[0]) )

        where_categories = ""
        if categories is not None:
            if not isinstance(categories, list):
                categories = [categories]
            where_categories = [
                '"{}" IN tei.categories'.format(category) for category in categories
            ]

        if where_categories:
            where_categories_str = (" AND ").join(where_categories)
            cypher += """
                MATCH (tei :TEI)
                WHERE {}
                AND tei.filename = n0.filename
            """.format(where_categories_str)


        if len(terms) > 1:
            for i, term in enumerate(terms):
                # a second or third term must be found within the same scope
                # (e.g. paragraph, filename, document)
                if i == 0: continue

                cypher +="""
                MATCH (n{}:token)
                WHERE n{}.string {} "{}"
                """.format(i, i, *get_search_mode_term(term))

                if scope == "paragraph":
                    # within the same document-collection (idno)
                    cypher += " AND n{}.idno = n0.idno ".format(i)
                    cypher += " AND n{}.paragraph_id = n0.paragraph_id ".format(i)
                # within the same TEI documents
                elif scope == "page":
                    cypher += " AND n{}.filename = n0.filename ".format(i)
                # within the same collection
                else:
                    cypher += " AND n{}.idno = n0.idno ".format(i)

        cypher +="""
            MATCH(para:p)
            WHERE para.idno=n0.idno
        """

        if scope == "paragraph":
            cypher += " AND para.`xml:id`= n0.paragraph_id"

        elif scope == "page":
            cypher += " AND para.filename= n0.filename"

        cypher += " return DISTINCT para"
        print(cypher)

        cursor = self.graph.run(cypher)

        paras = [] 
        while cursor.forward():
            for para in cursor.current:
                tokens = self.tokens_in_paragraph(para, concatenated=1)
                paras.append({
                    "para": para,
                    "tokens": tokens
                })

        return paras

        
    def create_indexes(self):
        labels = "del add rendition zone p pb anchor biblStruct category facsimile handNote item person place quote scriptNote".split() 
        for label in labels:
            cypher = "CREATE INDEX {}_idx FOR (n:{}) ON (n.filename, n.`xml:id`)".format(
                label, label
            )
            try:
                cursor = self.graph.run(cypher)
                print("{}_idx index created".format(label))
            except ClientError:
                print("{}_idx index already created".format(label))


    def get_indexes(self):
        cypher = "CALL db.indexes()"
        cursor = self.graph.run(cypher)
        indexes = []
        while cursor.forward():
            indexes.append(cursor.current)

        return indexes

