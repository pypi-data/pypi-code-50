from google.cloud import secretmanager_v1beta1 as secretmanager


def access_secret_string(secret_name):
    """
    Access the payload string for the latest secret version if one exists. See
    https://cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#secretmanager-access-secret-version-python
    """
    client = secretmanager.SecretManagerServiceClient()
    project_id = "294417890851"
    secret_version = "latest"
    name = client.secret_version_path(project_id, secret_name, secret_version)
    response = client.access_secret_version(name)
    return response.payload.data.decode("UTF-8")
