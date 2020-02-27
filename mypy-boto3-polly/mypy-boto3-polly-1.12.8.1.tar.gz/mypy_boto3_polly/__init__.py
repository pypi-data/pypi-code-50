"""
Main interface for polly service.

Usage::

    import boto3
    from mypy_boto3.polly import (
        Client,
        DescribeVoicesPaginator,
        ListLexiconsPaginator,
        ListSpeechSynthesisTasksPaginator,
        PollyClient,
        )

    session = boto3.Session()

    client: PollyClient = boto3.client("polly")
    session_client: PollyClient = session.client("polly")

    describe_voices_paginator: DescribeVoicesPaginator = client.get_paginator("describe_voices")
    list_lexicons_paginator: ListLexiconsPaginator = client.get_paginator("list_lexicons")
    list_speech_synthesis_tasks_paginator: ListSpeechSynthesisTasksPaginator = client.get_paginator("list_speech_synthesis_tasks")
"""
from mypy_boto3_polly.client import PollyClient, PollyClient as Client
from mypy_boto3_polly.paginator import (
    DescribeVoicesPaginator,
    ListLexiconsPaginator,
    ListSpeechSynthesisTasksPaginator,
)


__all__ = (
    "Client",
    "DescribeVoicesPaginator",
    "ListLexiconsPaginator",
    "ListSpeechSynthesisTasksPaginator",
    "PollyClient",
)
