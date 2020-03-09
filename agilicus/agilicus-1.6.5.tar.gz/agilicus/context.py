import agilicus
import jwt


class ApiHelper:
    def __init__(self):
        pass


def get_token(ctx):
    return ctx.obj["TOKEN"]


def header(ctx):
    return ctx.obj["HEADER"]


def get_apiclient(ctx, user_token=None):
    api = ApiHelper
    api.configuration = agilicus.Configuration()
    api.configuration.host = ctx.obj["API"]
    cacert = ctx.obj["CACERT"]
    if cacert is not True:
        api.configuration.ssl_ca_cert = cacert
    if user_token:
        api.configuration.access_token = user_token
    else:
        api.configuration.access_token = ctx.obj["TOKEN"]
    api.org_api = agilicus.OrganisationsApi(agilicus.ApiClient(api.configuration))
    api.application_api = agilicus.ApplicationsApi(agilicus.ApiClient(api.configuration))
    api.app_services_api = agilicus.ApplicationServicesApi(
        agilicus.ApiClient(api.configuration)
    )
    api.user_api = agilicus.UsersApi(agilicus.ApiClient(api.configuration))
    api.metrics_api = agilicus.MetricsApi(agilicus.ApiClient(api.configuration))
    api.issuers_api = agilicus.IssuersApi(agilicus.ApiClient(api.configuration))
    return api


def get_api(ctx):
    return ctx.obj["API"]


def get_cacert(ctx):
    return ctx.obj["CACERT"]


def get_client_id(ctx):
    return ctx.obj["CLIENT_ID"]


def get_auth_local_webserver(ctx):
    return ctx.obj["AUTH_LOCAL_WEBSERVER"]


def get_client_secret(ctx):
    return ctx.obj["CLIENT_SECRET"]


def get_issuer(ctx):
    return ctx.obj["ISSUER"]


def get_org(ctx):
    return ctx.obj["ORGANISATION"]


def get_org_id(ctx, user_token=None):
    # first check to see if an org is chosen
    # via context/env
    if ctx.obj["ORG_ID"] and ctx.obj["ORG_ID"]:
        return ctx.obj["ORG_ID"]

    # Next check to see if a token was passed in via
    # context/env
    if ctx.obj["TOKEN"]:
        token = jwt.decode(ctx.obj["TOKEN"], verify=False)
        if "org_id" in token:
            return token["org_id"]

    # finally check to see if the users token
    # has an org
    if user_token:
        token = jwt.decode(user_token, verify=False)
        if "org" in token:
            return token["org"]
