import gqlmod


def test_get_schema():
    assert gqlmod.providers.query_for_schema('github')
    assert gqlmod.providers.query_for_schema('github-sync')
    assert gqlmod.providers.query_for_schema('github-async')


def test_import():
    gqlmod.enable_gql_import()
    import queries  # noqa
    # TODO: Actually check previews got detected


def test_async_import():
    gqlmod.enable_gql_import()
    import queries_async  # noqa
    # TODO: Actually check previews got detected
