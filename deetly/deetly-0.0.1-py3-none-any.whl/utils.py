"""Deetly utils.

Utility functions
"""
import datetime
import hashlib
import re
from typing import Dict
import uuid

import pandas as pd
import pyarrow
import requests
import urllib3

api_url = "https://us-central1-mesiqi-238408.cloudfunctions.net/deetlyAPI"


def getMediaType(fmt: str) -> str:
    """Guess media type from file type.

    Args:
        fmt: file type

    Returns:
        String
    """
    if fmt == "csv":
        return "text/csv"
    elif fmt == "json":
        return "application/json"
    else:
        return "text/csv"


def getIdFromMetadata(metadata: Dict) -> str:
    """Get id from metadata dict if availble.

    If id not available then a new id is inserted.
    The id is calculated as a hash to metadata dict.

    Args:
        metadata: metadata dict

    Returns:
        String
    """

    author = metadata.get("author", None)
    name = metadata.get("title", None)
    theme = metadata.get("theme", None)
    created = metadata.get("created", datetime.datetime.today().isoformat())

    id_string = "-".join(filter(None, (author, name, theme)))
    if id_string:
        # pylint: disable=S303
        hash_object = hashlib.md5(id_string.encode())
        dp_id = hash_object.hexdigest()
        return re.sub("[^0-9a-z]+", "-", dp_id.lower())
    else:
        return str(uuid.uuid4())


def get_name_from_url(resource_url: str) -> str:
    """Extract resourcename from url.

    Args:
        resource_url: resource URL

    Returns:
        String

    Raises:
        ValueError: If the input string is not a valid url format.
    """
    parsed_url = urllib3.util.parse_url(resource_url)

    if not parsed_url.scheme == "https" and not parsed_url.scheme == "http":
        raise ValueError(
            f"Remote resource needs to be a web address, scheme is {parsed_url.scheme}"
        )

    resource = parsed_url.path.split("/")[-1]
    name = resource.split(".", 1)[0]

    if len(name) == 0:
        raise ValueError(f"Url does not contain a filename")

    return name


def serialize_table(df: pd.DataFrame, compress: bool = False) -> bytearray:
    """Serialize pandas dataframe to arrow buffer.

    Args:
        df: pandas dataframe

    Returns:
        Bytearray
    """
    ser = pyarrow.serialize(df).to_buffer()
    return ser


def upload_file(
    space: str,
    token: str,
    package_id: str,
    file_name: str,
    content_type: str,
    content: str,
) -> str:
    """Upload file to storage.

    Args:
        space: Space Id
        token: Access token
        package_id: Datapackage id
        file_name: Name of the file
        content_type: Content type
        content: File content as string

    Returns:
        str
    """

    res = requests.post(
        f"{api_url}/store",
        json={
            "package_id": package_id,
            "content": content,
            "name": file_name,
            "content_type": content_type,
            "space": space,
            "token": token,
        },
    )

    return res.text


def index_document(space: str, token: str, doc: Dict,) -> str:
    """Add/update Elastic search item.

    Args:
        token: Access token
        space: Space id
        doc: Document (JSON) to add to index

    Returns:
        str
    """

    res = requests.post(
        f"{api_url}/index", json={"space": space, "token": token, "doc": doc}
    )

    return res.text
