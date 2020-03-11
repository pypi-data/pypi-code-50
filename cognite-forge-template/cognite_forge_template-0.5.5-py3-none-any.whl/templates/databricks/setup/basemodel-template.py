# Databricks notebook source
# MAGIC %md # Setup base model (database and views)
# MAGIC
# MAGIC ### Prerequisites
# MAGIC Python 3.7+
# MAGIC
# MAGIC ### About this notebook
# MAGIC This notebook create a database with views. There is one view for each of the following CDF resource types: assets, events, datapoints, timeseries, files, 3dmodels.
# MAGIC
# MAGIC - **Cmd 2**: The setup-environment notebook is run to setup the development environment (installing commonly used libraries and reading a configuration file). The parameters from the configuration file is available as a Python dictionary called _config_. The 00-setup-environment notebook expects that the 'notebook_path' variable is properly set (done by cmd 2). If this widget is not set, the 00-setup-environment notebook will just print an error message.

# COMMAND ----------

# MAGIC %run ../setup/setup-environment.py

# COMMAND ----------

# Create database:
spark.sql(
    """
    CREATE DATABASE IF NOT EXISTS {database_name} 
    COMMENT '{project_description}'
    """.format(
        **config
    )
)

# COMMAND ----------

# Grant permissions:
spark.sql("GRANT ALL PRIVILEGES ON DATABASE {database_name} TO `{group_name}`".format(**config))

# COMMAND ----------

# Create table with assets
spark.sql("DROP TABLE IF EXISTS {database_name}.api_assets".format(**config))
spark.sql(
    """
CREATE TABLE IF NOT EXISTS {database_name}.api_assets USING cognite.spark.v1
OPTIONS (type 'assets',
         apiKey '{api_key}',
         partitions '80')
COMMENT 'View of assets in CDF from base model'
""".format(
        **config
    )
)

# COMMAND ----------

# Create table with events
spark.sql("DROP TABLE IF EXISTS {database_name}.api_events".format(**config))
spark.sql(
    """
  CREATE TABLE IF NOT EXISTS {database_name}.api_events USING cognite.spark.v1
  OPTIONS (type 'events',
           apiKey '{api_key}',
           partitions '80')
  COMMENT 'View of events in CDF from base model'
  """.format(
        **config
    )
)

# COMMAND ----------

# Create table with datapoints
spark.sql("DROP TABLE IF EXISTS {database_name}.api_datapoints".format(**config))
spark.sql(
    """
  CREATE TABLE IF NOT EXISTS {database_name}.api_datapoints USING cognite.spark.v1
  OPTIONS (type 'datapoints',
           apiKey '{api_key}')
  COMMENT 'View of datapoints in CDF from base model'
  """.format(
        **config
    )
)

# COMMAND ----------

# Create table with timeseries
spark.sql("DROP TABLE IF EXISTS {database_name}.api_timeseries".format(**config))
spark.sql(
    """
  CREATE TABLE IF NOT EXISTS {database_name}.api_timeseries USING cognite.spark.v1
  OPTIONS (type 'timeseries',
           apiKey '{api_key}')
  COMMENT 'View of time series in CDF from base model'
  """.format(
        **config
    )
)

# COMMAND ----------

# Create table with files metadata
spark.sql("DROP TABLE IF EXISTS {database_name}.api_files".format(**config))
spark.sql(
    """
  CREATE TABLE IF NOT EXISTS {database_name}.api_files USING cognite.spark.v1
  OPTIONS (type 'files',
           apiKey '{api_key}')
  COMMENT 'View of files metadata in CDF from base model'
  """.format(
        **config
    )
)

# COMMAND ----------

# Create table with 3D models and revisions metadata
spark.sql("DROP TABLE IF EXISTS {database_name}.api_3dmodels".format(**config))
spark.sql(
    """
  CREATE TABLE IF NOT EXISTS {database_name}.api_3dmodels USING cognite.spark.v1
  OPTIONS (type '3dmodels',
           apiKey '{api_key}')
  COMMENT 'View of 3D models and revisions metadata in CDF from base model'
  """.format(
        **config
    )
)

# COMMAND ----------

# Display database table metadata
display(spark.catalog.listTables(config["database_name"]))

# COMMAND ----------

# Display schemas for database tables
for t in ["api_assets", "api_datapoints", "api_events", "api_timeseries", "api_files", "api_3dmodels"]:
    print(">>", t)
    spark.table("%s.%s" % (config["database_name"], t)).printSchema()
