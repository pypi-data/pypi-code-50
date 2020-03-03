"""Testing basic functionality."""
from datatypes import Datatype, Datavalue


def test_translating():
    """Datatypes with dialects should translate."""
    dt = Datatype("region", domain="se/municipality")
    val = Datavalue("Arvika kommun", dt)
    assert(val.translate("short") == "Arvika")

    assert(dt.translate("Arvika kommun", "short") == "Arvika")
