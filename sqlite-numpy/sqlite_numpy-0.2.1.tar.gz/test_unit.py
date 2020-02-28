import os
import sqlite3
import typing

import numpy
import pytest

import sqlite_numpy
import sqlite_numpy.asyncio


def simple_values() -> typing.Dict[str, numpy.array]:
    return {
        "x": numpy.array([i for i in range(10)]),
        "y": numpy.array([i + 0.1 for i in range(10)]),
        "z": numpy.array([i + 0.2 for i in range(10)]),
    }


@pytest.fixture(scope="class")
def simple_database(tmp_path_factory) -> typing.Generator[str, None, None]:
    filename = str(tmp_path_factory.mktemp("simple_database") / "simple_database.db")
    db = sqlite3.connect(filename)
    db.execute("CREATE TABLE test_table(x INTEGER, y REAL, z REAL)")

    x, y, z = list(simple_values().values())
    values = [[float(x[i]), float(y[i]), float(z[i])] for i in range(x.shape[0])]
    db.executemany("INSERT INTO test_table VALUES(?,?,?)", values)
    db.commit()
    yield filename
    db.close()
    os.remove(filename)


class TestDatabase:
    def test_unit__open_execute__ok__nominal_case(self, simple_database: str) -> None:
        expected_results = simple_values()
        with sqlite_numpy.Database(simple_database) as database:
            with database.execute("SELECT * FROM test_table") as proxy:
                arrays = proxy.fetchall()
        assert proxy.closed
        assert database.closed
        assert arrays.keys() == expected_results.keys()
        for result, expected in zip(arrays.values(), expected_results.values()):
            assert numpy.array_equal(result, expected)

    def test_unit__open_execute__ok__fetch_many(self, simple_database: str) -> None:
        count = 4
        expected_results = {
            key: array[0:count] for key, array in simple_values().items()
        }
        with sqlite_numpy.Database(simple_database) as database:
            with database.execute("SELECT * FROM test_table") as proxy:
                arrays = proxy.fetchmany(count)

                assert arrays.keys() == expected_results.keys()
                for result, expected in zip(arrays.values(), expected_results.values()):
                    assert numpy.array_equal(result, expected)

                arrays = proxy.fetchmany(7)
                assert arrays.keys() == expected_results.keys()
                assert 6 == list(arrays.values())[0].shape[0]
                assert proxy.closed

    @pytest.mark.parametrize("param", [2, 2.0, "2"])
    def test_unit__execute__ok__bound_parameters(
        self, simple_database: str, param: typing.Any
    ) -> None:
        with sqlite_numpy.Database(simple_database) as database:
            with database.execute(
                "SELECT * FROM test_table WHERE x>:param_1", {"param_1": param}
            ) as proxy:
                arrays = proxy.fetchall()
                assert 7 == list(arrays.values())[0].shape[0]

    def test_unit__execute__ok__statement_cache(self, simple_database: str) -> None:
        with sqlite_numpy.Database(
            simple_database, max_statement_cache_size=1
        ) as database:
            with database.execute("SELECT * FROM test_table WHERE x>2") as proxy:
                proxy.fetchall()
            assert 1 == database.statement_cache_size()
            with database.execute("SELECT * FROM test_table WHERE x>2") as proxy:
                arrays = proxy.fetchall()
                assert 7 == list(arrays.values())[0].shape[0]
            assert 1 == database.statement_cache_size()
            with database.execute("SELECT * FROM test_table") as proxy:
                pass
            assert 1 == database.statement_cache_size()

    @pytest.mark.asyncio
    async def test_unit__open_execute__ok__asyncio(self, simple_database: str) -> None:
        expected_results = simple_values()
        async with sqlite_numpy.asyncio.AsyncDatabase(simple_database) as database:
            async with database.execute("SELECT * FROM test_table") as proxy:
                arrays = await proxy.fetchall()
        assert proxy.closed
        assert database.closed
        assert arrays.keys() == expected_results.keys()
        for result, expected in zip(arrays.values(), expected_results.values()):
            assert numpy.array_equal(result, expected)
