"""
Functions for manipulating Fairplay DRM
"""
import uuid


FAIRPLAY_SYSTEM_ID = uuid.UUID("94CE86FB-07FF-4F43-ADB8-93D2FA968CA2")


def generate_key_tag(
    uri, iv=None, keyformat=None, method="SAMPLE-AES", tag="#EXT-X-KEY"
):
    """
    Generate key tags, minimally requires uri to be specified
    """
    if iv:
        iv = f",IV={iv}"
    if keyformat:
        keyformat = f",KEYFORMAT={keyformat}"
    return f"{tag}:METHOD={method},URI={uri}{keyformat}{iv}"
