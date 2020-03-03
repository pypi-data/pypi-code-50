import pytest


CONFIG_DEFAULTS = {"timeout": 1}


class ExeTestConfig(dict):
    """
    A testsuite config

    Represents the "config" part of a yaml testsuite

    Built at test collection time.
    We are init by py.test hook "pytest_generate_tests"
    """

    def __init__(self, metafunc, *args, **kwargs):
        """
        metafunc provided by py.test
        """
        super().__init__(*args, **kwargs)

        for key, value in CONFIG_DEFAULTS.items():

            #  Sets defaults but does not overwrite
            self.setdefault(key, value)

        # Register markers
        for marker in self.get("markers", ()):
            metafunc.config.addinivalue_line("markers", marker)


class ExeTestData(dict):
    """
    A single test

    Built at test collection time.
    We are init by py.test hook "pytest_generate_tests"
    """

    def __init__(self, suite_config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, value in suite_config.items():
            if key == "markers":
                # NOT IMPORTING this key
                # meaning is different in config (declaration) and in tests
                # (usage)
                continue
            #  Sets defaults but does not overwrite
            self.setdefault(key, value)

        self.name = self.get("name", self["exe"])

        markers = self.get("markers", [])
        self.pytest_obj = pytest.param(
            self,
            id=self.name,
            marks=[getattr(pytest.mark, marker) for marker in markers],
        )

    def __repr__(self):
        if "args" not in self:
            return f"""{self.name}: {self["exe"]}"""
        return f"""{self.name}: {self["exe"]} {" ".join(self["args"])}"""
