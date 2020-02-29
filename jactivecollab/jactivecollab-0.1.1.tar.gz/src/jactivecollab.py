import requests
from pprint import pprint
import numpy as np
import pandas as pd

import mysql.connector as mariadb

from datetime import datetime
import datetime as dt

MASTER_ID = 224


def login(host, user, password, database):
    return jActiveCollab(user=user, password=password, host=host, database=database)


class jActiveCollab:
    def __init__(self, user, password, host, database):
        self.db_connector = mariadb.connect(
            user=user, password=password, host=host, database=database
        )

    def time_records(self):
        """Returns all tracked hours in a DataFrame.

        It filters out the trashed records and sorts by record_date and
        then id. Additionally, for all the hours tracked on a task, the
        project_id of the project will be added
        """

        q = (
            "SELECT id, parent_type, parent_id, record_date, value, user_id,"
            "user_name, user_email, summary, updated_on,updated_by_email,is_trashed "
            "FROM time_records WHERE NOT is_trashed ORDER BY record_date,id"
        )
        df = pd.read_sql(q, self.db_connector)

        # If tracked on a Task one needs to add the project id to the DataFrame
        mytasks = self.tasks()
        tracked_on_project = df["parent_type"] == "Project"
        tracked_on_task = df["parent_type"] == "Task"
        df.loc[tracked_on_project, "project_id"] = df.loc[
            tracked_on_project, "parent_id"
        ]
        task_ids = df.loc[tracked_on_task, "parent_id"]
        # TODO find better solution for next line
        df.loc[tracked_on_task, "project_id"] = mytasks.loc[
            mytasks.index.intersection(task_ids), "project_id"
        ].values

        df = df.astype(
            {"record_date": "datetime64[ns]", "project_id": "int", "is_trashed": "bool"}
        )
        return df.set_index("id")

    # TODO refactor all functions to return Multiindex Series and to convert to df in the plotting code

    def project_hours_daily(self, start, end, remove_empty=True):
        """Returns the hours worked between start and end per day and per
        project.

        DataFrame with projects as rows and dates as columns. The values
        are the tracked hours on the project of that row on the date of
        that column. It is sorted by the average hours tracked in the
        timespan.

        Parameters
        ----------
        start: datetime64
        end: datetime64
        """
        records = self.time_records()
        hours = (
            records.groupby(["record_date", "project_id"])["value"].sum().sort_index()
        )
        timespan_mask = (hours.index.levels[0] >= start) & (
            hours.index.levels[0] <= end
        )

        project_hours = (
            hours.unstack(level=1)
            .transpose()
            .loc[:, timespan_mask]
            .dropna(how="all")
            .fillna(0)
        )
        avg = project_hours.mean(axis=1).sort_values()
        return project_hours.reindex(avg.index)

    def project_hours_weekly(self, start, end, remove_empty=True):
        records = self.time_records()

        # TODO convert start to monday and end to sunday
        timespan_mask = (records["record_date"] >= start) & (
            records["record_date"] <= end
        )
        records = records.loc[timespan_mask]
        records["week"] = [date.isocalendar()[1] for date in records["record_date"]]

        project_hours = records.groupby(["week", "project_id"])["value"].sum()
        project_hours = (
            project_hours.unstack(level=1).transpose().dropna(how="all").fillna(0)
        )
        avg = project_hours.mean(axis=1).sort_values()
        return project_hours.reindex(avg.index)

    def project_hours_cumsum(self, start, end, remove_empty=True):
        """
        start: Start date for the cumulative sum as a pandas or numpy datetime
        end: End date for the cumulative sum as a pandas or numpy datetime
        remove_empty: TODO implement case: False. If True, the emtpy projects will not be returned
        
        returns: DataFrame with projects as rows and dates as columns. The values are the summed up tracked hours on\
        the project of that row between start and the date of that column. It is sorted by the hours tracked on the\
        last day.
        """
        records = self.time_records()
        hours = (
            records.groupby(["record_date", "project_id"])["value"].sum().sort_index()
        )
        timespan_mask = (hours.index.levels[0] >= start) & (
            hours.index.levels[0] <= end
        )

        hours_this_month = hours.unstack(level=1).loc[timespan_mask, :]
        last = hours_this_month.index[-1]
        hours_this_month = (
            hours_this_month.transpose()
            .dropna(how="all")
            .fillna(0)
            .cumsum(axis=1)
            .sort_values(last)
        )
        return hours_this_month

    def project_total_hours(self, start, end, remove_empty=True):
        """
        start: Start date for the sum of tracked hours as a pandas or numpy datetime
        end: End date for the sum of tracked hours as a pandas or numpy datetime
        remove_empty: TODO implement case: False. If True, the emtpy projects will not be returned
        
        returns: DataFrame with the total tracked hours between start and end.
        """
        myprojects = self.projects()
        hours_cumsum = self.project_hours_cumsum(start, end, remove_empty=True)
        total_hours = hours_cumsum.iloc[:, -1].to_frame()
        total_hours["project name"] = myprojects.loc[total_hours.index, "name"]
        total_hours.rename(
            columns={total_hours.columns[0]: "total hours"}, inplace=True
        )
        return total_hours

    def tasks(self):
        q = "SELECT * FROM tasks"
        df = pd.read_sql(q, self.db_connector)
        return df.set_index("id")

    def projects(self):
        q = "SELECT * FROM projects"
        df = pd.read_sql(q, self.db_connector)
        return df.set_index("id")

    def users(self):
        q = "SELECT * FROM users"
        df = pd.read_sql(q, self.db_connector)
        return df.set_index("id")

    def user_hours(self, start, end, remove_empty=True):
        """
        start: Start date for the sum of tracked hours as a pandas or numpy datetime
        end: End date for the sum of tracked hours as a pandas or numpy datetime
        remove_empty: TODO implement case: False. If True, the emtpy projects will not be returned
        
        returns: Series with Mulitiindex. First level are the project_ids, second level the user_ids. Useful for salaries
        """
        records = self.time_records()
        timespan_mask = (records["record_date"] >= start) & (
            records["record_date"] <= end
        )
        records = records.loc[timespan_mask, :]
        user_hours = records.groupby(["project_id", "user_id"]).sum()["value"]
        if remove_empty:
            user_hours.dropna(inplace=True)

        return user_hours

    def user_expenses(self, start, end, remove_empty=True):
        """
        start: Start date for the sum of tracked expenses as a pandas or numpy datetime
        end: End date for the sum of tracked expenses as a pandas or numpy datetime
        remove_empty: TODO implement case: False. If True, the emtpy projects will not be returned
        
        returns: Series with Mulitiindex. First level are the project_ids, second level the user_ids. Useful for salaries
        """
        q = "SELECT * FROM expenses"
        expenses = pd.read_sql(q, self.db_connector)
        timespan_mask = (expenses["record_date"] >= start.date()) & (
            expenses["record_date"] <= end.date()
        )
        expenses = expenses.loc[timespan_mask, :]
        # If tracked on a Task one needs to add the project id to the DataFrame
        def get_project_id(parent_type, parent_id, tasks):
            if parent_type == "Task":
                return tasks.loc[parent_id, "project_id"]
            return parent_id

        mytasks = self.tasks()

        expenses["project_id"] = expenses.apply(
            lambda row: get_project_id(row["parent_type"], row["parent_id"], mytasks),
            axis=1,
        )

        user_expenses = expenses.groupby(["project_id", "user_id"]).sum()["value"]
        if remove_empty:
            user_expenses.dropna(inplace=True)

        return user_expenses

    def salaries_last_month(self):
        end = datetime.today().replace(
            day=1, hour=23, minute=59, second=59
        ) - dt.timedelta(1)
        start = end.replace(day=1, hour=0, minute=0, second=0)
        return self.user_hours(start, end, remove_empty=True)

    def user_hours_info(self, start, end, remove_empty=True):
        """
        start: Start date for the sum of tracked hours as a pandas or numpy datetime
        end: End date for the sum of tracked hours as a pandas or numpy datetime
        remove_empty: TODO implement case: False. If True, the emtpy projects will not be returned
        
        returns: DataFrame with the total tracked hours between start and end for each user. The index is a\
        multiindex with the project_id and the user_id with the are the user ids and the columns are the values.
        """
        records = self.time_records()
        myusers = self.users()
        myprojects = self.projects()
        timespan_mask = (records["record_date"] >= start) & (
            records["record_date"] <= end
        )
        records = records.loc[timespan_mask, :]
        hours_per_user = (
            records.groupby(["project_id", "user_id"]).sum()["value"].to_frame()
        )
        index = hours_per_user.index
        hours_per_user = hours_per_user.reset_index()
        hours_per_user.index = index

        def get_project_metadata(project_id):
            leader_id = myprojects.loc[project_id, "leader_id"]
            project_name = myprojects.loc[project_id, "name"]
            if leader_id in myusers.index:
                return (project_name, True, leader_id)
            return (project_name, False, MASTER_ID)

        # user data
        hours_per_user["first_name"] = hours_per_user["user_id"].transform(
            lambda user_id: myusers.loc[user_id, "first_name"]
        )
        hours_per_user["last_name"] = hours_per_user["user_id"].transform(
            lambda user_id: myusers.loc[user_id, "last_name"]
        )
        hours_per_user["email"] = hours_per_user["user_id"].transform(
            lambda user_id: myusers.loc[user_id, "email"]
        )

        # project data
        hours_per_user[
            ["project_name", "has_leader", "leader_id"]
        ] = hours_per_user.apply(
            lambda row: get_project_metadata(row["project_id"]),
            axis=1,
            result_type="expand",
        )

        # project manager data
        hours_per_user["leader_email"] = hours_per_user["leader_id"].transform(
            lambda leader_id: myusers.loc[leader_id, "email"]
        )
        print(hours_per_user["leader_email"].unique())
        hours_per_user["leader_first_name"] = hours_per_user["leader_id"].transform(
            lambda leader_id: myusers.loc[leader_id, "first_name"]
        )
        hours_per_user["leader_last_name"] = hours_per_user["leader_id"].transform(
            lambda leader_id: myusers.loc[leader_id, "last_name"]
        )

        return hours_per_user
