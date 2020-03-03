"""
Tests for the async graphql_client library
"""

import pytest

from py_gql_test_client.async_client import AsyncGraphQLClient


# Graphql Client to test
@pytest.fixture(scope="module")
def client():
    return AsyncGraphQLClient(gql_uri="http://localhost:5000/graphql")


def test_async_client_query_execution(client):
    pass
