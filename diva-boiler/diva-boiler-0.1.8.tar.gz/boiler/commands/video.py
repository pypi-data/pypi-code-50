from pathlib import Path
import sys

import click
from tabulate import tabulate

from boiler import BoilerSession, cli
from boiler.commands.utils import exit_with, handle_request_error
from boiler.definitions import CameraLocation, ReleaseBatches, Scenarios


def ingest_video(video_path: str, release_batch: str, session: BoilerSession):
    video_name = Path(video_path).stem

    r = session.get('video', json={'name': video_name})
    out = handle_request_error(r)
    if r.ok and len(out['response']):
        click.echo(f'name={video_name} already exists', err=True)
        return out
    elif not r.ok:
        click.echo(f'Could not query server for video={video_name}', err=True)
        return out

    data = {'video_name': video_name, 'release_batch': release_batch}
    r = session.post('video/name', json=data)
    out = handle_request_error(r)

    if r.ok:
        v = out['response']
        click.echo(f'id={v["id"]} created for name={video_name}', err=True)
        click.echo(f'sending name={video_name} id={v["id"]} to S3', err=True)
        # TODO: upload to s3
        return out
    else:
        click.echo(f'name={video_name} creation failed', err=True)
        return out


@click.group(name='video', short_help='ingest and query video')
@click.pass_obj
def video(ctx):
    pass


@video.command(name='status', help='status of video annotation')
@click.argument('name', type=click.STRING)
@click.pass_obj
def status(ctx, name):
    r = ctx['session'].get('video', params={'name': name})
    if not r.ok and r.status_code != 404:
        exit_with(handle_request_error(r))
    elif r.status_code == 404 or not r.json():
        click.echo('Video not found, has it been ingested?', err=True)
        sys.exit(1)

    video_id = r.json()[0]['id']
    r = ctx['session'].get(f'video/{video_id}/status')
    headers = ['video', 'activity type', 'status']
    table = []

    for row in r.json()['vat_statuses']:
        table.append(
            [r.json()['video_name'], row['video_activity_type']['activity_type'], row['status'],]
        )
    # sort by activity type
    click.echo(
        tabulate(sorted(table, key=lambda row: row[1]), headers, tablefmt='github')  # type:ignore
    )


@video.command(name='search', help='search for video')
@click.option('--name', type=click.STRING)
@click.option('--gtag', type=click.STRING)
@click.option('--location', type=click.Choice([e.value for e in CameraLocation]))
@click.option('--release-batch', type=click.Choice([e.value for e in ReleaseBatches]))
@click.option('--scenario', type=click.Choice([e.value for e in Scenarios]))
@click.option('--page', type=click.INT)
@click.option('--size', type=click.INT)
@click.pass_obj
def search(ctx, **kwargs):
    data = {}
    for key, value in kwargs.items():
        if value is not None:
            data[key] = value
    r = ctx['session'].get('video', params=data)
    exit_with(handle_request_error(r))


@video.command(name='add', help='ingest video into stumpf from file')
@click.option(
    '--video-path', type=click.Path(exists=True, dir_okay=False, resolve_path=True),
)
@click.option(
    '--release-batch', type=click.Choice([e.value for e in ReleaseBatches]), required=True
)
@click.pass_obj
def add(ctx, video_path, release_batch):
    exit_with(ingest_video(video_path, release_batch, ctx['session']))


cli.add_command(video)
