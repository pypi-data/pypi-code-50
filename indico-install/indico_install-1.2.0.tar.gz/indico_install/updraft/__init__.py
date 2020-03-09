import json
from pathlib import Path

import click

from indico_install.cluster_manager import ClusterManager
from indico_install.config import merge_dicts, yaml
from indico_install.helm.apply import apply
from indico_install.helm.render import render
from indico_install.utils import options_wrapper, pretty_diff, string_to_tag


def refresh_cluster_manager(
    ctx, cluster_manager, deployment_root, yes, allow_image_overrides=False
):
    """
    Given recent changes, apply them to the cluster
    """
    cluster_manager.lock()
    try:
        ctx.invoke(
            render,
            cluster_manager=cluster_manager,
            deployment_root=deployment_root,
            allow_image_overrides=allow_image_overrides,
        )
        ctx.invoke(
            apply,
            cluster_manager=cluster_manager,
            deployment_root=deployment_root,
            yes=yes,
        )
    finally:
        cluster_manager.save()
        cluster_manager.unlock()


@click.group("updraft")
def updraft():
    """Manage deployments and versioning"""
    pass

@updraft.command("ls")
@click.pass_context
@click.option("-n", "--number", type=int, help="Max number of results")
@click.option("-o", "--ordered", is_flag=True, help="Order results most to least recent (expensive). Only available if REGEX is provided")
@click.argument("regex", required=False)
def list_versions(ctx, number=None, ordered=False, regex=None):
    """
    Display available versions of updraft, ordered most to least recent

    Use REGEX to filter the updraft tags.
    """
    if ordered and not regex:
        click.secho(f"Please provide REGEX to use --ordered")
        ordered = False

    results = ClusterManager.get_updraft_versions(regex, number, ordered)
    click.secho("\n".join(results))


@updraft.command("version")
@click.pass_context
def show_version(ctx):
    """
    Display version details about <TAG>. Defaults to current cluster rendered_tag
    """
    click.secho(f"Known version: {ClusterManager().indico_version}")


@updraft.command("current")
@click.pass_context
def show_current(ctx):
    """
    Display current configmap state (alias for viewing the configmap)
    """
    click.secho(ClusterManager().to_str())


@updraft.command("edit")
@click.pass_context
@click.option(
    "-I", "--interactive", is_flag=True, help=f"Open configmap in your editor"
)
@click.option("-v", "--version", help=f"Update to new updraft version")
@click.option(
    "--force", is_flag=True, help=f"Render and apply even if there are no changes"
)
@click.option("--patch-file", type=click.File("r"), help="JSON-formatted patch file")
@click.argument("patch", required=False)
@options_wrapper()
def edit_configmap(
    ctx,
    *,
    interactive,
    patch,
    force,
    patch_file,
    version,
    yes,
    deployment_root,
    **kwargs,
):
    """
    Edit configmap with some patch, or interactively.
    Only allows editing of the main cluster config portion

    PATCH - if not interactive, and no patch-file is provided,
    pass in a json string to patch the configmap with

    ex: indico updraft edit '{"apiDomain": "api-foo.indico.io"}'
    """
    cluster_manager = ClusterManager()
    if not cluster_manager.cm_exists:
        click.secho(
            "Cannot edit cluster config. Please initialize with indico updraft init",
            fg="red",
        )
        return
    changes = None
    replace = False
    service_state = cluster_manager.clean_services()
    if interactive:
        changes = click.edit(
            yaml.dump(cluster_manager.cluster_config, default_flow_style=False)
        )
        changes = yaml.safe_load(changes) if changes else changes
        replace = True
    elif patch_file:
        changes = json.load(patch_file)
    elif patch:
        changes = json.loads(patch)

    version = string_to_tag(version) if version else None
    if force or changes or (version and version != cluster_manager.indico_version):
        if force or version:
            click.secho(f"This will override any custom images as well!", fg="yellow")
        cluster_manager.edit_cluster_config(
            changes=merge_dicts(changes or {}, service_state),
            version=version,
            replace=replace
        )
    else:
        click.secho(
            f"No changes or new version provided. Use --force if required", fg="yellow"
        )
        return

    if yes or click.confirm("Render and apply with changes?"):
        cluster_manager.save(backup=True)
        refresh_cluster_manager(
            ctx,
            cluster_manager,
            deployment_root,
            yes,
            allow_image_overrides=not version,
        )


@updraft.command("restore")
@click.pass_context
@options_wrapper()
def restore_version(ctx, deployment_root, yes):
    """
    (Alpha) If an old version of the cluster_manager exists, pull it
    load the original state, and apply
    """
    cluster_manager = ClusterManager()
    if not cluster_manager.load_from_cluster(backup=True):
        click.secho("No backup available!", fg="red")
        return

    cluster_manager.lock()
    try:
        if yes or click.confirm("Apply backup?"):
            refresh_cluster_manager(
                ctx, cluster_manager, deployment_root, yes, allow_image_overrides=True
            )
    finally:
        cluster_manager.unlock()


@updraft.command("init")
@click.pass_context
@options_wrapper()
def init_tracking(ctx, input_yaml=None, yes=False, **kwargs):
    """
    Add or update version tracking to the cluster (idempotent)
    """
    if input_yaml and not Path(input_yaml).is_file():
        click.secho(
            f"Provided input yaml {input_yaml} does not exist. Ignoring", fg="yellow"
        )
        input_yaml = None
    cluster_manager = ClusterManager(reconcile=True, input_yaml=input_yaml)
    click.secho(cluster_manager.to_str())
    if yes or click.confirm("Save updated version cluster_manager?"):
        cluster_manager.save()


@updraft.command("diff")
@click.pass_context
@click.argument("versions", required=False, nargs=-1)
@click.option(
    "--all/--no-all",
    "show_all",
    default=False,
    show_default=True,
    help="Include matches in diff",
)
def compare_versions(ctx, versions=None, show_all=False):
    """
    Compare versions
    If no versions are provided, diff rendered_release with current state
    If 1 version, diff current state with version
    If 2 versions, diff the versions
    """
    if len(versions) > 2:
        click.secho(
            "More that 2 versions provided for comparison. Ignoring extra versions"
        )
        versions = versions[:2]
    if versions:
        versions = [string_to_tag(v) for v in versions]

    cluster_manager = ClusterManager()
    if len(versions) == 2:
        diff = cluster_manager.diff(*versions)
    else:
        diff = cluster_manager.diff_version(tag=versions[0] if versions else None)

    pretty_diff(diff, show_all=show_all)
