from contextlib import contextmanager
from sqlalchemy.schema import CreateTable
from ..records.records_format import BaseRecordsFormat, DelimitedRecordsFormat
from tempfile import TemporaryDirectory
from ..url.filesystem import FilesystemDirectoryUrl
import logging
import sqlalchemy
from sqlalchemy import MetaData
from sqlalchemy.schema import Table
from ..url.base import BaseDirectoryUrl
from ..records.unload_plan import RecordsUnloadPlan
from ..records.load_plan import RecordsLoadPlan
from ..records.types import RecordsFormatType
from ..records.records_directory import RecordsDirectory
from records_mover.db.quoting import quote_group_name, quote_user_name, quote_schema_and_table
from records_mover.records import RecordsSchema
from typing import Union, Dict, List, IO, Tuple, Iterator, Optional, Type, TYPE_CHECKING
if TYPE_CHECKING:
    from typing_extensions import Literal  # noqa

logger = logging.getLogger(__name__)


class DBDriver:
    def __init__(self,
                 db: Union[sqlalchemy.engine.Engine,
                           sqlalchemy.engine.Connection], **kwargs) -> None:
        self.db = db
        self.db_engine = db.engine
        self.meta = MetaData()

    def best_scheme_to_load_from(self) -> str:
        return 'file'

    def has_table(self, schema: str, table: str) -> bool:
        return self.db.dialect.has_table(self.db, table_name=table, schema=schema)

    def table(self,
              schema: str,
              table: str) -> Table:
        return Table(table, self.meta, schema=schema, autoload=True, autoload_with=self.db_engine)

    def schema_sql(self,
                   schema: str,
                   table: str) -> str:
        """Generate DDL which will recreate the specified table and return it
        as a string.  Returns None if database or permissions don't
        support operation.

        """
        # http://docs.sqlalchemy.org/en/latest/core/reflection.html
        table_obj = self.table(schema, table)
        return str(CreateTable(table_obj, bind=self.db))

    def unload(self,
               schema: str,
               table: str,
               unload_plan: RecordsUnloadPlan,
               directory: RecordsDirectory) -> int:
        """Writes table specified to the RecordsDirectory instance named 'directory'
        per the UnloadPlan named 'unload_plan'.  Guarantees a manifest
        file named 'manifest' is written to the target directory pointing
        to the target records.  After ensuring other records-related
        metadata is provided, you can call directory.finalize_manifest()
        to move this to the final location of _manifest, signaling to
        readers that the Records directory is finalized.

        Returns number of rows unloaded.
        """
        raise NotImplementedError(f"unload not implemented for this database type")

    def can_unload_this_format(self, target_records_format: BaseRecordsFormat) -> bool:
        """Return true if the specified format is compatible with the unload()
        method"""
        return False

    def known_supported_records_formats_for_unload(self) -> List[BaseRecordsFormat]:
        """Candidates to look through when negotiating a common records format
        with a records target"""
        return []

    def load(self,
             schema: str,
             table: str,
             load_plan: RecordsLoadPlan,
             directory: RecordsDirectory) -> Optional[int]:
        """Loads the data from the data specified to the RecordsDirectory
        instance named 'directory'.  Guarantees a manifest file named
        'manifest' is written to the target directory pointing to the
        target records.

        Returns number of rows loaded (if database provides that
        info).
        """
        raise NotImplementedError(f"load not implemented for this database type")

    def can_load_this_format(self, source_records_format: BaseRecordsFormat) -> bool:
        """Return true if the specified format is compatible with the load()
        method"""
        return False

    def known_supported_records_formats_for_load(self) -> List[BaseRecordsFormat]:
        """Candidates to look through when negotiating a common records format
        with a records source.  Will be looked through in order, so
        the better formats (higher fidelity and/or more efficient to
        process) should appear first in the list.
        """
        return []

    def best_records_format_variant(self,
                                    records_format_type: RecordsFormatType) -> \
            Optional[str]:
        """Return the most suitable records format delimited variant for
        loading and unloading.  This is generally the format that the
        database unloading and loading natively, which won't require
        translation before loading or after unloading.
        """
        if records_format_type == 'delimited':
            return 'bluelabs'
        else:
            return None

    def best_records_format(self) -> BaseRecordsFormat:
        variant = self.best_records_format_variant('delimited')
        assert variant is not None  # always provided for 'delimited'
        return DelimitedRecordsFormat(variant=variant)

    def can_load_from_fileobjs(self) -> bool:
        return False

    def load_from_fileobj(self, schema: str, table: str,
                          load_plan: RecordsLoadPlan, fileobj: IO[bytes]) -> Optional[int]:
        """Loads the data from the file stream provided.
        """
        raise NotImplementedError(f"load_from_fileobj not implemented for this database type")

    def varchar_length_is_in_chars(self) -> bool:
        """True if the 'n' in VARCHAR(n) is represented in natural language
        characters, rather than in post-encoding bytes.  This varies by database -
        override it to control"""
        return False

    def set_grant_permissions_for_groups(self, schema_name: str, table: str,
                                         groups: Dict[str, List[str]],
                                         db: Union[sqlalchemy.engine.Engine,
                                                   sqlalchemy.engine.Connection]) -> None:
        schema_and_table: str = quote_schema_and_table(self.db.engine, schema_name, table)
        for perm_type in groups:
            groups_list = groups[perm_type]
            for group in groups_list:
                group_name: str = quote_group_name(self.db.engine, group)
                if not perm_type.isalpha():
                    raise TypeError("Please make sure your permission types"
                                    " are an acceptable value.")
                perms_sql = f'GRANT {perm_type} ON TABLE {schema_and_table} TO {group_name}'
                db.execute(perms_sql)

    def set_grant_permissions_for_users(self, schema_name: str, table: str,
                                        users: Dict[str, List[str]],
                                        db: Union[sqlalchemy.engine.Engine,
                                                  sqlalchemy.engine.Connection]) -> None:
        schema_and_table: str = quote_schema_and_table(self.db.engine, schema_name, table)
        for perm_type in users:
            user_list = users[perm_type]
            for user in user_list:
                user_name: str = quote_user_name(self.db.engine, user)
                if not perm_type.isalpha():
                    raise TypeError("Please make sure your permission types"
                                    " are an acceptable value.")
                perms_sql = f'GRANT {perm_type} ON TABLE {schema_and_table} TO {user_name}'
                db.execute(perms_sql)

    def load_failure_exception(self) -> Type[Exception]:
        return sqlalchemy.exc.InternalError

    @contextmanager
    def temporary_loadable_directory_loc(self) -> Iterator[BaseDirectoryUrl]:
        with TemporaryDirectory(prefix='temporary_loadable_directory_loc') as dirname:
            yield FilesystemDirectoryUrl(dirname)

    def supports_time_type(self):
        return True

    def type_for_date_plus_time(self, has_tz: bool=False) -> sqlalchemy.sql.sqltypes.DateTime:
        """Different DB vendors have different names for a date, a time, and
        an optional timezone"""
        return sqlalchemy.sql.sqltypes.DateTime(timezone=has_tz)

    def type_for_integer(self,
                         min_value: Optional[int],
                         max_value: Optional[int]) -> sqlalchemy.types.TypeEngine:
        """Find correct integral column type to fit data matching the given
        min and max integer values"""
        logger.warning("Using default integer type")
        return sqlalchemy.sql.sqltypes.Integer()

    def type_for_fixed_point(self,
                             precision: int,
                             scale: int) -> sqlalchemy.sql.sqltypes.Numeric:
        """Find correct decimal column type to fit data from the given fixed point type"""
        return sqlalchemy.sql.sqltypes.Numeric(precision=precision,
                                               scale=scale)

    def type_for_floating_point(self,
                                fp_total_bits: int,
                                fp_significand_bits: int) -> sqlalchemy.sql.sqltypes.Numeric:
        """Find correct decimal column type to fit data from the given floating point type"""

        # SQL spec (at least in the publically available pre-release
        # 1992 version) declares the meaning of the precision in type
        # "FLOAT(precision)" to be defined by the database vendor:
        #
        # 49)Subclause 6.1, "<data type>": The binary precision of a
        # data type defined as FLOAT for each value specified by
        # <precision> is implementation-defined.
        #
        # http://www.contrib.andrew.cmu.edu/~shadow/sql/sql1992.txt
        #
        # That said, at least Postgres, MySQL and ORacle agree that
        # the 'precision' in their cases mean the significand_bits of
        # either an IEEE or Intel-flavored float , so let's default to
        # that:
        #
        # https://dev.mysql.com/doc/refman/8.0/en/floating-point-types.html#targetText=MySQL%20permits%20a%20nonstandard%20syntax,look%20like%20%2D999.9999%20when%20displayed.
        # https://docs.oracle.com/javadb/10.8.3.0/ref/rrefsqlj27281.html
        # https://www.postgresql.org/docs/10/datatype-numeric.html
        return sqlalchemy.sql.sqltypes.Float(precision=fp_significand_bits)

    def make_column_name_valid(self, colname: str) -> str:
        return colname

    def integer_limits(self,
                       type_: sqlalchemy.types.Integer) ->\
            Optional[Tuple[int, int]]:
        """returns the integer limits (min and max value as a tuple) of the
        given column type for this database type.  These are
        represented as a Python int, which is of arbitrary length.

        Since SQLAlchemy doesn't track this detail, if details of this
        database type aren't known in the DBDriver hierarchy, None
        will be returned.
        """
        logger.warning(f"{type(self)} does not know how to gather limits of {type(type_)}")
        return None

    def fp_constraints(self,
                       type_: sqlalchemy.types.Float) ->\
            Optional[Tuple[int, int]]:
        """returns the floating point representation (total floating point bits minus padding
        and significand bits as a tuple) of the given column type for
        this database type.

        Since SQLAlchemy doesn't track this detail, if details of this
        database type aren't known in the DBDriver hierarchy, None
        will be returned.
        """
        logger.warning(f"{type(self)} does not know how to gather limits of {type(type_)}")
        return None

    def fixed_point_constraints(self,
                                type_: sqlalchemy.types.Numeric) ->\
            Optional[Tuple[int, int]]:
        """returns the fixed-point representation - total number of digits
        (precision) and number of those digits to the right of the
        decimal point (scale) - as a tuple for the given column type
        for this database type.
        """
        if type_.precision is None or type_.scale is None:
            return None
        return (type_.precision, type_.scale)

    def tweak_records_schema_for_load(self,
                                      records_schema: RecordsSchema,
                                      records_format: BaseRecordsFormat) -> RecordsSchema:
        return records_schema
