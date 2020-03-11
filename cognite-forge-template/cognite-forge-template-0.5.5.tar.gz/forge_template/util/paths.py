import os

TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), "..", "templates")

# Databricks constants
DATABRICKS_TEMPLATE_PATH = os.path.join(TEMPLATES_PATH, "databricks" + os.sep)
DATABRICKS_PATH = "databricks" + os.sep
notebooks_to_copy = [
    (
        os.path.join(DATABRICKS_TEMPLATE_PATH, "setup", "setup-environment-template.py"),
        os.path.join(DATABRICKS_PATH, "setup", "setup-environment.py"),
    ),
    (
        os.path.join(DATABRICKS_TEMPLATE_PATH, "setup", "basemodel-template.py"),
        os.path.join(DATABRICKS_PATH, "setup", "basemodel.py"),
    ),
    (
        os.path.join(DATABRICKS_TEMPLATE_PATH, "jobs", "powerbi-dataset-refresh-template.py"),
        os.path.join(DATABRICKS_PATH, "jobs", "powerbi-dataset-refresh.py"),
    ),
    (
        os.path.join(DATABRICKS_TEMPLATE_PATH, "notebooks", "sample-spark-model-template.py"),
        os.path.join(DATABRICKS_PATH, "notebooks", "sample-spark-model-template.py"),
    ),
]

# Power BI constants
POWERBI_TEMPLATE_PATH = os.path.join(TEMPLATES_PATH, "powerbi" + os.sep)
POWERBI_PATH = "powerbi" + os.sep
POWERBI_BASE_DATASET_PATH = os.path.join(POWERBI_PATH, "datasets", "base_dataset.pbix")
POWERBI_BASE_REPORT_PATH = os.path.join(POWERBI_PATH, "reports", "base_report.pbix")

# Github Actions constants
SCRIPT_TEMPLATE_FOLDER = os.path.join(TEMPLATES_PATH, "infra_scripts")
WORKFLOW_TEMPLATE_FOLDER = os.path.join(TEMPLATES_PATH, "github_workflows")
POWERBI_SCRIPT_NAME = "deploy_powerbi.py"
DATABRICKS_SCRIPT_NAME = "deploy_databricks.py"
POWERBI_SCRIPT_PATH = os.path.join(SCRIPT_TEMPLATE_FOLDER, POWERBI_SCRIPT_NAME)
DATABRICKS_SCRIPT_PATH = os.path.join(SCRIPT_TEMPLATE_FOLDER, DATABRICKS_SCRIPT_NAME)
POWERBI_WORKFLOW_TEMPLATE_NAME = "deploy_powerbi.yaml"
DATABRICKS_WORKFLOW_TEMPLATE_NAME = "deploy_databricks.yaml"
POWERBI_WORKFLOW_TEMPLATE_PATH = os.path.join(WORKFLOW_TEMPLATE_FOLDER, POWERBI_WORKFLOW_TEMPLATE_NAME)
DATABRICKS_WORKFLOW_TEMPLATE_PATH = os.path.join(WORKFLOW_TEMPLATE_FOLDER, DATABRICKS_WORKFLOW_TEMPLATE_NAME)
