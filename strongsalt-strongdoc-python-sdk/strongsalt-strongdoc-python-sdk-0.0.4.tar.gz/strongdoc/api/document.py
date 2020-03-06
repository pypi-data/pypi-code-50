from strongdoc import client
from strongdoc.proto import document_pb2, documentNoStore_pb2, strongdoc_pb2_grpc

BLOCK_SIZE = 10000


def _stream_upload_request_generator(doc_name, plaintext, block_size=BLOCK_SIZE):
    request = document_pb2.UploadDocStreamReq(docName=doc_name)

    yield request

    for i in range(0, len(plaintext), block_size):
        block = plaintext[i: i + block_size]
        request = document_pb2.UploadDocStreamReq(plaintext=block)

        yield request


def _stream_encrypt_request_generator(doc_name, plaintext, block_size=BLOCK_SIZE):
    request = documentNoStore_pb2.EncryptDocStreamReq(docName=doc_name)

    yield request

    for i in range(0, len(plaintext), block_size):
        block = plaintext[i: i + block_size]
        request = documentNoStore_pb2.EncryptDocStreamReq(plaintext=block)

        yield request


def _stream_decrypt_request_generator(docid, ciphertext, block_size=BLOCK_SIZE):
    request = documentNoStore_pb2.DecryptDocStreamReq(docID=docid)

    yield request

    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i: i + block_size]
        request = documentNoStore_pb2.DecryptDocStreamReq(ciphertext=block)

        yield request


# upload_document uploads a document to be stored by strongdoc
def upload_document(token, doc_name, plaintext):
    """
    Uploads a document to the service for storage.

    :param token:
        The user JWT token.
    :type token:
        `string`
    :param doc_name:
        The name of the document.
    :type doc_name:
        `string`
    :param plaintext:
        The text of the document.
    :type plaintext:
        `byte array`
    :returns:
        The uploaded document ID.
    :rtype:
        `string`
    """
    with client.connect_to_server_with_auth(token) as auth_conn:
        client_stub = strongdoc_pb2_grpc.StrongDocServiceStub(auth_conn)

        request_iterator = _stream_upload_request_generator(doc_name, plaintext)

        response = client_stub.UploadDocumentStream(request_iterator)

        return response.docID


# download_document downloads a document stored in strongdoc
def download_document(token, docid):
    """
    Download a document from the service.

    :param token:
        The user JWT token.
    :type token:
        `string`
    :param docid:
        The ID of the document.
    :type docid:
        `string`
    :returns:
        The downloaded document.
    :rtype:
        `byte array`
    """
    with client.connect_to_server_with_auth(token) as auth_conn:
        client_stub = strongdoc_pb2_grpc.StrongDocServiceStub(auth_conn)

        request = document_pb2.DownloadDocStreamReq(docID=docid)

        plaintext = b""
        response_iterator = client_stub.DownloadDocumentStream(request)

        for res in response_iterator:
            plaintext += res.plaintext

        return plaintext


# encrypt_document encrypts a document with strongdoc, but does not store the actual document
def encrypt_document(token, doc_name, plaintext):
    """
    Encrypts a document using the service, but do not store it.
    Instead return the encrypted ciphertext.

    :param token:
        The user JWT token.
    :type token:
        `string`
    :param doc_name:
        The name of the document.
    :type doc_name:
        `string`
    :param plaintext:
        The text of the document.
    :type plaintext:
        `byte array`

    Returns
    -------
    docID: string
        The document ID for the uploaded document.
        This ID is needed to decrypt the document.
    ciphertext: byte array
        The encrypted ciphertext of the document.
    """
    with client.connect_to_server_with_auth(token) as auth_conn:
        client_stub = strongdoc_pb2_grpc.StrongDocServiceStub(auth_conn)

        request_iterator = _stream_encrypt_request_generator(doc_name, plaintext)

        docid = None
        ciphertext = b""
        response_iterator = client_stub.EncryptDocumentStream(request_iterator)

        for res in response_iterator:
            docid = res.docID
            ciphertext += res.ciphertext

        return docid, ciphertext


# decrypt_document encrypts a document with strongdoc. It requires original ciphertext, since the document is not stored
def decrypt_document(token, docid, ciphertext):
    """
    Decrypt a document using the service.
    The user must provide the ciphertext returned during the encryptDocument API call.

    :param token:
        The user JWT token.
    :type token:
        `string`
    :param docid:
        The ID of the document.
    :type docid:
        `string`
    :param ciphertext:
        The document ciphertext to be decrypted.
    :type ciphertext:
        `bye array`
    :returns:
        The decrypted plaintext content of the document.
    :rtype:
        `byte array`
    """
    with client.connect_to_server_with_auth(token) as auth_conn:
        client_stub = strongdoc_pb2_grpc.StrongDocServiceStub(auth_conn)

        request_iterator = _stream_decrypt_request_generator(docid, ciphertext)

        plaintext = b""
        response_iterator = client_stub.DecryptDocumentStream(request_iterator)

        for res in response_iterator:
            plaintext += res.plaintext

        return plaintext


# remove_document deletes the document from strongdoc storage
def remove_document(token, docid):
    """
    Remove a document from the service.

    :param token:
        The user JWT token.
    :type token:
        `string`
    :param docid:
        The ID of the document.
    :type docid:
        `string`
    :returns:
        Whether the removal was a success.
    :rtype:
        `bool`
    """
    with client.connect_to_server_with_auth(token) as auth_conn:
        client_stub = strongdoc_pb2_grpc.StrongDocServiceStub(auth_conn)

        request = document_pb2.RemoveDocumentRequest(docID=docid)

        client_stub.RemoveDocument(request)
