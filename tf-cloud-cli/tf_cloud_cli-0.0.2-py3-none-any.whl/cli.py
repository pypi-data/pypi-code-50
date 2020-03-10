import click

from tf_cloud_cli import Api, TokenProvider

ORGANIZATION = "organization"
WORKSPACE = "workspace"
API_CLIENT = "API_CLIENT"


@click.group()
@click.pass_context
def cli(ctx):
    token = TokenProvider.get_token()
    ctx.obj[API_CLIENT] = Api(token)


@cli.command()
@click.pass_context
def list_organizations(ctx):
    api = ctx.obj[API_CLIENT]
    orgs = api.get_organizations()
    for o in orgs:
        print(f"* {o.get_name()}")


@cli.group()
@click.option("-o", "--organization", type=str, required=True)
@click.pass_context
def organization(ctx, organization):
    ctx.obj[ORGANIZATION] = organization


@organization.command()
@click.pass_context
def list_workspaces(ctx):
    organization = ctx.obj[ORGANIZATION]
    workspaces = ctx.obj[API_CLIENT].organization(organization).get_workspaces()
    print(f"Workspaces for {organization}:")
    for w in workspaces:
        print(f"* {w.get_name()}")


@organization.group()
@click.option("-w", "--workspace", type=str, required=True)
@click.pass_context
def workspace(ctx, workspace):
    ctx.obj[WORKSPACE] = workspace


@workspace.command()
@click.pass_context
def show(ctx):
    organization = ctx.obj[ORGANIZATION]
    workspace = ctx.obj[WORKSPACE]
    print(f"Showing {workspace} for {organization}")
    ctx.obj[API_CLIENT].organization(organization).workspace(workspace).show()


@workspace.command()
@click.pass_context
def set_local_execution(ctx):
    organization = ctx.obj[ORGANIZATION]
    workspace = ctx.obj[WORKSPACE]
    print(f"Showing {workspace} for {organization}")
    ctx.obj[API_CLIENT].organization(organization).workspace(workspace).set_local_execution()


def main():
    cli(obj={})


if __name__ == "__main__":
    main()
