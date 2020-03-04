from typing import List

from strongdoc import client
from strongdoc import constants
from strongdoc.proto import search_pb2, strongdoc_pb2_grpc


def search(token, query):
    """
    Search for document that contains a specific word.
    A gRPC connection timeout will be implemented.
    
    :param token:
        The user JWT token.
    :type token:
        `string`
    :param query:
        The query string.
    :type query:
        `string`
    :raises grpc.RpcError:
        Raised by the gRPC library to indicate non-OK-status RPC termination.

    returns:
        The hit list of the search.
    :rtype:
        `Array` of :class:`DocumentResult`
    """
    with client.connect_to_server_with_auth(token) as auth_conn:
        client_stub = strongdoc_pb2_grpc.StrongDocServiceStub(auth_conn)

        request = search_pb2.SearchRequest(query=query)

        response = client_stub.Search(request, timeout=constants.GRPC_TIMEOUT)

        hits: List[DocumentResult] = []
        for hit_result in response.hits:
            hits.append(DocumentResult(hit_result.docID, hit_result.score))

        return hits


class DocumentResult:
    """
    A class that will hold a single document that matches the search result from the Search query.
    """

    def __init__(self, docid, score):
        """
        Constructs a document that matches the search result

        :param docid:
            The matching document ID
        :type docid:
            `string`
        :param score:
            The score of the matching document
        :type score:
            `float`
        """
        self._docid = docid
        self._score = score

    @property
    def docid(self):
        """
        Get the matching document ID

        returns:
            The matching document ID
        :rtype:
            `string`
        """
        return self._docid

    @docid.setter
    def docid(self, docid):
        """
        Set the matching document ID

        :param docid:
            The matching document ID
        :type docid:
            `string`
        """
        self._docid = docid

    @property
    def score(self):
        """
        Get the score of the matching document

        returns:
            The score of the matching document
        :rtype:
            `float`
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Set the score of the matching document

        :param score:
            The score of the matching document
        :type score:
            `float`
        """
        self._score = score
