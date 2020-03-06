import datetime
import json
import logging
import os
import sqlite3
import typing
from contextlib import contextmanager
from functools import reduce

from .utils import dict_to_param_map

import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[ExperimentDB]")


class ExperimentDB(object):
    def __init__(self, db_path):
        self.db_path = db_path

    @contextmanager
    def db_cursor(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        try:
            yield cursor
        except Exception as e:
            logger.error("Error: {}".format(e))
            conn.rollback()
        else:
            conn.commit()

    # Initialize experiments table
    def init_experiment_table(self, drop=False):
        with self.db_cursor() as cur:
            if drop:
                cur.execute("DROP TABLE IF EXISTS experiments")

            cur.execute(
                """CREATE TABLE IF NOT EXISTS experiments
                         (
                         experiment_id integer,
                         run_id integer,
                         date text,
                         config text,
                         metrics text,
                         owner text,
                         PRIMARY KEY (experiment_id, run_id, owner)
                         )"""
            )

    def get_nb_experiments(self):

        with self.db_cursor() as cur:
            cur.execute("SELECT count(1) FROM experiments")
            nb_experiments = cur.fetchone()[0]

        return nb_experiments

    def add_experiment(self, experiment_id: int, run_id: int, config: typing.Dict):
        self.init_experiment_table(drop=False)

        with self.db_cursor() as cur:
            date = str(datetime.datetime.now().isoformat())

            cur.execute(
                f"""INSERT INTO experiments VALUES (
                {experiment_id},
                {run_id},
                '{date}',
                '{json.dumps(config)}',
                '',
                '{os.environ.get("USER", "unknown")}'
            )
            """
            )

    def update_experiment(self, experiment_id, run_id, metrics):
        with self.db_cursor() as cur:
            cur.execute(
                f"""
            UPDATE experiments
            SET metrics = '{json.dumps(metrics)}'
            WHERE run_id = '{run_id}' AND experiment_id = '{experiment_id}'"""
            )

    def list_all_experiments(self):
        with self.db_cursor() as cur:
            ret = list()
            for row in cur.execute("SELECT * FROM experiments"):
                ret.append(row)

        return pd.DataFrame(
            data=ret,
            columns=["experiment_id", "run_id", "date", "config", "metrics", "owner"],
        )

    @staticmethod
    def parse_json(s):
        try:
            return json.loads(s)
        except:
            return dict()

    @staticmethod
    def recursive_get(d: typing.Dict, path: str):
        path_spl = path.split(".")
        res = d
        for elem in path_spl:
            res = res.get(elem, dict())

        if isinstance(res, dict) and len(res) == 0:
            return None

        return res

    @staticmethod
    def isolate_common_config(config_list):
        """
        Given a list of config as dicts, infer which keys remains constant
        over all the configs and which keys are changing.
        This function works over nested dicts.

        :param config_list:
        :return:
        """
        keys = [set(config.keys()) for config in config_list]

        all_keys = reduce(lambda x, y: x.union(y), keys[1:], keys[0])

        common_config = dict()
        custom_config = dict()

        for key in all_keys:
            values = [config.get(key, None) for config in config_list]
            first_existing_value = next(item for item in values if item is not None)
            if not isinstance(first_existing_value, dict):
                if len(set(values)) == 1:
                    common_config[key] = values[0]
                else:
                    custom_config[key] = None
            else:
                (
                    common_config[key],
                    custom_config[key],
                ) = ExperimentDB.isolate_common_config(
                    [config[key] for config in config_list if key in config]
                )

        return common_config, custom_config

    @staticmethod
    def build_automatic_config(df):
        config_list = [ExperimentDB.parse_json(s) for s in list(df["config"])]
        common_config, custom_config = ExperimentDB.isolate_common_config(config_list)
        config = dict_to_param_map(custom_config)

        return common_config, config

    @staticmethod
    def list_metrics(metrics_list):
        keys = [set(metrics.keys()) for metrics in metrics_list]

        all_keys = reduce(lambda x, y: x.union(y), keys[1:], keys[0])

        ret = dict()

        for key in all_keys:
            values = [metrics.get(key, None) for metrics in metrics_list]
            first_existing_value = next(item for item in values if item is not None)
            if not isinstance(first_existing_value, dict):
                ret[key] = None
            else:
                ret[key] = ExperimentDB.list_metrics(
                    [metrics[key] for metrics in metrics_list if key in metrics]
                )

        return ret

    @staticmethod
    def build_automatic_metric(df):
        metrics_list = [ExperimentDB.parse_json(s) for s in list(df["metrics"])]
        all_metrics_dict = ExperimentDB.list_metrics(metrics_list)
        metrics = dict_to_param_map(all_metrics_dict)
        return metrics

    def show_experiment(
        self,
        experiment_id: int,
        params: typing.Optional[typing.Dict] = None,
        metrics: typing.Dict = None,
    ):
        with self.db_cursor() as cur:
            ret = list()
            for row in cur.execute(
                f"SELECT * FROM experiments WHERE experiment_id = '{experiment_id}'"
            ):
                ret.append(row)

        df = pd.DataFrame(
            data=ret,
            columns=["experiment_id", "run_id", "date", "config", "metrics", "owner"],
        )
        df["run_id"] = df["run_id"].apply(int)

        if params is None:
            common_config, params = ExperimentDB.build_automatic_config(df)
            print(f"Common configuration {common_config}")
        if metrics is None:
            metrics = ExperimentDB.build_automatic_metric(df)

        for name in params:
            df[name] = df["config"].apply(
                lambda s: ExperimentDB.recursive_get(
                    ExperimentDB.parse_json(s), params[name]
                )
            )
        for name in metrics:
            df[name] = df["metrics"].apply(
                lambda s: ExperimentDB.recursive_get(
                    ExperimentDB.parse_json(s), metrics[name]
                )
            )

        df.drop(
            columns=["experiment_id", "date", "metrics", "config", "owner"],
            inplace=True,
        )

        return df
