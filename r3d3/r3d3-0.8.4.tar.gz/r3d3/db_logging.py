import datetime
import os
import pandas as pd
from .experiment_db import ExperimentDB


class R3D3Logger(object):
    def __init__(self, db_path, experiment_id, run_id):
        self.experiment_db = ExperimentDB(db_path=db_path)
        self.experiment_db.init_logging_table(drop=False)

        self.experiment_id = experiment_id
        self.run_id = run_id

    def do_log(self, level, message):
        with self.experiment_db.db_cursor() as cur:
            ts = datetime.datetime.now().timestamp()

            cur.execute(
                f"""INSERT INTO logging VALUES (
                {self.experiment_id},
                {self.run_id},
                {ts},
                '{os.environ.get("USER", "unknown")}',
                '{level}',
                '{message}'
            )
            """
            )

    def info(self, message):
        self.do_log("INFO", message)

    def debug(self, message):
        self.do_log("DEBUG", message)

    def error(self, message):
        self.do_log("ERROR", message)

    def warning(self, message):
        self.do_log("WARNING", message)

    def get_full_log(self):
        with self.experiment_db.db_cursor() as cur:
            ret = list()
            for row in cur.execute(
                f"""
                SELECT * FROM logging
                WHERE run_id = '{self.run_id}' 
                AND experiment_id = '{self.experiment_id}'
                """
            ):
                ret.append(row)

            return pd.DataFrame(
                data=ret,
                columns=["experiment_id", "run_id", "timestamp", "owner", "level", "message"],
            )
