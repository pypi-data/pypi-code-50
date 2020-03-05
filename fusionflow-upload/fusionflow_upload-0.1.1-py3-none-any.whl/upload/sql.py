# caution: avoid cycle-import
from typing import Text

class Sql(object):
    """create sql statement for CURD
    
    :param t: [description]
    :type object: [type]
    """
    def __init__(self, t):
        self.t = t

    def stmt(self, stmt_type: Text) -> Text:
        """generate related stmt 
        """
        stmt_meth = getattr(self, "%s_stmt" % stmt_type)
        return stmt_meth()

    def create_stmt(self):

        return """create table {table_name} (
 \t{fields}
 )
        """.format(table_name=self.t._table_name, 
                   fields=",\n\t".join(
                       [
                           "{name}\t{type}".format(name=name, type=type_.name)
                            for name, type_ in  self.t.field_name_types]
                        )
                   )       

    def update_stmt(self):
        pass

    def insert_stmt(self):
        pass

    def delete_stmt(self):
        pass
    