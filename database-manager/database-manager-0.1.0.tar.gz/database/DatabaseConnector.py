import mysql.connector
import logging
from mysql.connector import Error
from .DatabaseEntity import DBEntity


class DatabaseConnector:

    def __init__(self, db_host, db_username, db_password, db_name):
        self.logger = logging.getLogger(__name__)
        self.logger.debug("Attempting connection to " +
                          db_name +
                          " on " +
                          db_host +
                          " with user " +
                          db_username +
                          " and password " +
                          db_password)
        try:
            self.database = mysql.connector.connect(
                host=db_host,
                user=db_username,
                passwd=db_password,
                database=db_name,
                auth_plugin="mysql_native_password"
            )
        except Error as e:
            self.logger.exception("Error connecting to DB: " + db_name)
            raise e
        else:
            self.logger.info("Successfully connected to DB: " + db_name)
        self.cursor = self.database.cursor(dictionary=True, buffered=True)
        self.select_statement = ""
        self.insert_statement = ""
        self.update_statement = ""
        self.delete_statement = ""

    def create_select(self, entity):
        self.logger.debug("Creating select statement for table " + entity.table.table_name())
        self.select_statement = "SELECT "
        self.select_statement += entity.select_col_clause
        self.select_statement += " FROM "
        self.select_statement += entity.table.table_name()
        if entity.where_clause is not None:
            self.select_statement += entity.where_clause
        if entity.order_by_clause is not None:
            self.select_statement += entity.order_by_clause
        self.select_statement += ";"
        self.logger.debug("Created statement: '" + self.select_statement + "'")

    def execute_select(self, table, single=False):
        self.logger.debug("Executing select statement for table: " + table.table_name() + " As single: " + str(single))
        try:
            self.cursor.execute(self.select_statement)
            if single:
                select_dict = self.cursor.fetchone()
            else:
                select_dict = self.cursor.fetchall()
        except Error as e:
            self.logger.exception("Error executing select statement: '" + self.select_statement + "'")
            raise e
        else:
            if select_dict is None:
                self.logger.info("Executed statement: '" + self.select_statement + "' NO ROWS SELECTED")
                return None
            else:
                if single:
                    self.logger.info("Executed statement: '" + self.select_statement + "' Rows: 1")
                    db_obj = DBEntity(table, select_dict)
                    return db_obj
                else:
                    rows = str(len(select_dict))
                    self.logger.info("Executed statement: " + self.select_statement + "' Rows: " + rows)
                    db_objs = []
                    for record in select_dict:
                        db_objs.append(DBEntity(table, record))
                    return db_objs

    def create_insert(self, entity):
        self.logger.debug("Creating insert statement for table " + entity.table.table_name())
        self.insert_statement = "INSERT INTO "
        self.insert_statement += entity.table.table_name() + " "
        self.insert_statement += entity.insert_col_val_clause
        self.insert_statement += ";"
        self.logger.debug("Created statement: '" + self.insert_statement + "'")

    def execute_insert(self):
        self.logger.debug("Executing insert statement.")
        try:
            row_count = self.cursor.execute(self.insert_statement)
        except Error as e:
            self.logger.exception("Error executing insert statement: '" + self.insert_statement + "'")
            raise e
        else:
            self.logger.info("Executed statement: '" + self.insert_statement + "' Row Count: " + str(row_count))
            return self.cursor.lastrowid

    def create_update(self, entity):
        self.logger.debug("Creating update statement for table " + entity.table.table_name())
        self.update_statement = "UPDATE "
        self.update_statement += entity.table.table_name() + " "
        self.update_statement += entity.update_clause + " "
        self.update_statement += entity.where_clause + ";"
        self.logger.debug("Created statement: '" + self.update_statement + "'")

    def execute_update(self):
        self.logger.debug("Executing update statement.")
        try:
            row_count = self.cursor.execute(self.update_statement)
        except Error as e:
            self.logger.exception("Error executing update statement: '" + self.update_statement + "'")
            raise e
        else:
            self.logger.info("Executed statement: '" + self.update_statement + "' Row Count: " + str(row_count))
            return self.cursor.lastrowid

    def create_delete(self, entity):
        self.logger.debug("Creating delete statement for table " + entity.table.table_name())
        self.delete_statement = "DELETE FROM "
        self.delete_statement += entity.table.table_name() + " "
        try:
            self.delete_statement += entity.where_clause
        except Error as e:
            self.logger.exception("Delete statement required where clause is missing.")
            raise e
        else:
            self.delete_statement += ";"
            self.logger.debug("Create statement: '" + self.delete_statement + "'")

    def execute_delete(self):
        self.logger.debug("Executing delete statement.")
        try:
            row_count = self.cursor.execute(self.delete_statement)
        except Error as e:
            self.logger.exception("Error executing delete statement: '" + self.delete_statement + "'")
            raise e
        else:
            self.logger.info("Executed statement: '" + self.delete_statement + "' Row Count: " + str(row_count))
            return self.cursor.lastrowid

    def commit_execute(self):
        self.logger.debug("Attempting commit")
        try:
            self.database.commit()
        except Error as e:
            self.logger.exception("Error in committing execution.")
            raise e
        else:
            self.logger.info("Committed execution.")
            return self.cursor.lastrowid

    def get_table_information(self):
        self.logger.debug("Attempting to get table information.")
        self.select_statement = "SHOW TABLES;"
        try:
            self.cursor.execute(self.select_statement)
            tables_dict = self.cursor.fetchall()
        except Error as e:
            self.logger.exception("Error in executing select statement: '" + self.select_statement + "'")
            raise e
        else:
            tables = {}
            for table_dict in tables_dict:
                for schema, table_name in table_dict.items():
                    self.select_statement = "DESCRIBE " + table_name
                    try:
                        self.cursor.execute(self.select_statement)
                        table_description_dict = self.cursor.fetchall()
                    except Error as e:
                        self.logger.exception("Error in executing select statement: '")
                        raise e
                    else:
                        tables[table_name] = table_description_dict
            return tables
