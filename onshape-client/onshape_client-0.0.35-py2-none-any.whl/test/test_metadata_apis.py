import pytest


@pytest.mark.parametrize('element', ['ps_configurable_cube'], indirect=True)
def test_change_configured_metadata(client, element):
    """Test to ensure configuring metadata is possible."""
    pass