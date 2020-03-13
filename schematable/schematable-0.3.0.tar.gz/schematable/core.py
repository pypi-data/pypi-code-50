import attr
import sqlalchemy as sa


@attr.s(frozen=True)
class SchemaTable(object):
  table: str = attr.ib()
  schema = attr.ib(default=None, validator=attr.validators.instance_of((str, type(None))))
  db_url: str = attr.ib(default='sqlite:///:memory:') # in-memory db

  schema_table: str = attr.ib(init=False)
  stab: str = attr.ib(init=False) # 🗡
  st: str = attr.ib(init=False)
  engine: sa.engine.base.Engine = attr.ib(init=False)
  url: str = attr.ib(init=False)

  @url.default
  def url_default(self):
    return '#'.join([self.db_url, self.schema_table])

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

  @staticmethod
  def parse(url: str):

    if '#' in url:
        db_url, schema_table = url.split('#')
        if db_url == '':
          db_url = 'sqlite:///:memory:' # 👃 hardcode
    else:
        db_url = 'sqlite:///:memory:' # 👃 hardcode again
        schema_table = url

    if '.' in schema_table:
        schema, table = schema_table.split('.')
        if schema == '':
          schema = None
    else:
        schema = None
        table = schema_table

    instance = SchemaTable(
        db_url=db_url,
        table=table,
        schema=schema
    )
    # print(instance)
    return instance