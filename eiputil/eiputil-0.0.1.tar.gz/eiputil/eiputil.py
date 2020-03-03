#!/usr/bin/env python

from __future__ import absolute_import, print_function

import ipaddress
import json
import os
import urllib.request

import boto3
import click
import click_completion
import click_completion.core
from botocore.exceptions import ClientError


def custom_startswith(string, incomplete):
    """
    A custom completion matching that supports case insensitive matching
    """
    if os.environ.get('_CLICK_COMPLETION_COMMAND_CASE_INSENSITIVE_COMPLETE'):
        string = string.lower()
        incomplete = incomplete.lower()
    return string.startswith(incomplete)


click_completion.core.startswith = custom_startswith
click_completion.init()
ec2 = boto3.client('ec2')
cmd_help = """Shell completion for click-completion-command

Available shell types:

\b
  %s

Default type: auto
""" % "\n  ".join('{:<12} {}'.format(k, click_completion.core.shells[k]) for k in sorted(
    click_completion.core.shells.keys()))


def is_network(addresses: tuple) -> bool:
    _flag = False
    for address in addresses:
        if(ipaddress.ip_network(address)):
            _flag = True
    return _flag


@click.group(help=cmd_help)
def eiputil():
    pass


@eiputil.command()
@click.option('--unassigned-only', '-u', type=bool, is_flag=True, default=False)
def describe(unassigned_only: bool):
    """
    Describe Elastic IP addresses.
    """
    result = []
    try:
        eips = ec2.describe_addresses()
        for eip in eips['Addresses']:
            allocation_id = eip['AllocationId']
            instance_id = ''
            public_ip = eip['PublicIp']

            if 'InstanceId' not in eip:
                pass
            else:
                instance_id = eip['InstanceId']

            if unassigned_only and instance_id != '':
                pass
            else:
                result.append({
                    'PublicIp': public_ip,
                    'InstanceId': instance_id,
                    'AllocationId': allocation_id
                })
        click.echo(json.dumps({'IPAddresses': result}, indent=2, ensure_ascii=False))
    except ClientError as e:
        click.echo(e)


@eiputil.command()
@click.argument('number', required=True, default=1)
@click.option('--include', '-i', required=False, multiple=True)
def allocate(number: int, include: str):
    """
    Allocate Elastic IP addresses.
    """
    result = []
    try:
        for i in range(number):
            eip = ec2.allocate_address(Domain='vpc')
            allocation_id = eip['AllocationId']
            public_ip = eip['PublicIp']
            if(len(include) == 0):
                result.append({
                    'PublicIp': public_ip,
                    'AllocationId': allocation_id
                })
            else:
                if(is_network(include)):
                    result.append({
                        'PublicIp': public_ip,
                        'AllocationId': allocation_id
                    })
        click.echo(json.dumps({'AllocatedIPAddresses': result}, indent=2, ensure_ascii=False))
    except ClientError as e:
        click.echo(e)


@eiputil.command()
@click.argument('addresses', type=int, required=True, nargs=-1)
def release(addresses: str):
    """
    Release Elastic IP addresses.
    """
    result = []
    try:
        eips = ec2.describe_addresses()
        for eip in eips['Addresses']:
            allocation_id = eip['AllocationId']
            public_ip = eip['PublicIp']
            if(public_ip in addresses):
                ec2.release_address(AllocationId=allocation_id)
                result.append({
                    'PublicIp': public_ip,
                    'AllocationId': allocation_id
                })
        click.echo(json.dumps({'ReleasedIPAddresses': result}, indent=2, ensure_ascii=False))
    except ClientError as e:
        click.echo(e)


@eiputil.command()
@click.option('--exclude', '-e', required=False, multiple=True)
def release_all(exclude: str):
    """
    Release all Elastic IP addresses.
    """
    result = []
    try:
        eips = ec2.describe_addresses()
        for eip in eips['Addresses']:
            allocation_id = eip['AllocationId']
            public_ip = eip['PublicIp']
            if(public_ip in exclude):
                pass
            else:
                if "InstanceId" not in eip:
                    ec2.release_address(AllocationId=allocation_id)
                    result.append({
                        'PublicIp': public_ip,
                        'AllocationId': allocation_id
                    })
        click.echo(json.dumps({'ReleasedIPAddresses': result}, indent=2, ensure_ascii=False))
    except ClientError as e:
        click.echo(e)


@eiputil.command()
def show_ipranges():
    """
    Show AWS ip-ranges.
    (https://ip-ranges.amazonaws.com/ip-ranges.json)
    """
    try:
        with urllib.request.urlopen('https://ip-ranges.amazonaws.com/ip-ranges.json') as response:
            data = json.loads(response.read())
            click.echo(json.dumps(data, indent=2, ensure_ascii=False))
    except Exception as e:
        click.echo(e)


@eiputil.command()
@click.option('--append/--overwrite', help="Append the completion code to the file", default=None)
@click.option('-i', '--case-insensitive/--no-case-insensitive', help="Case insensitive completion")
@click.argument('shell', required=False, type=click_completion.DocumentedChoice(click_completion.core.shells))
@click.argument('path', required=False)
def install(append, case_insensitive, shell, path):
    """
    Install the click-completion-command completion.
    """
    extra_env = {'_CLICK_COMPLETION_COMMAND_CASE_INSENSITIVE_COMPLETE': 'ON'} if case_insensitive else {}
    shell, path = click_completion.core.install(shell=shell, path=path, append=append, extra_env=extra_env)
    click.echo('%s completion installed in %s' % (shell, path))


if __name__ == "__main__":
    eiputil()
