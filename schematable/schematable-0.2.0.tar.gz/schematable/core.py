import attr
import sqlalchemy as sa

@attr.s(frozen=True)
class SchemaTable(object):
  table: str = attr.ib()
  schema = attr.ib(default=None, validator=attr.validators.instance_of((str, type(None))))
  schema_table: str = attr.ib()
  stab: str = attr.ib() # 🗡
  st: str = attr.ib()
  db_url: str = attr.ib(default='sqlite:///:memory:') # in-memory db
  engine: sa.engine.base.Engine = attr.ib()

  @db_url.validator
  def check_url(self, attribute, value):
    pass

  @schema_table.default
  def schema_table_default(self):
    return self.table if self.schema is None else self.schema + '.' + self.table

  @stab.default # alias of schema_table
  def stab_default(self):
    return self.schema_table

  @st.default # even shorter alias of schema_table
  def st_default(self):
    return self.schema_table

  @engine.default
  def engine_default(self):
    return sa.create_engine(self.db_url)

  def todict(self):
    return attr.asdict(self) # TODO: exclude engine attr

