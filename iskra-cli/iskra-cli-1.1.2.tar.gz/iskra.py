#!/usr/bin/env python

import resource
import asyncio
import json
import logging
import sys
import webbrowser
import os
from os import environ as env
from os.path import isfile, isdir, exists, join, basename
from glob import glob
from pathlib import Path
from subprocess import check_output, CalledProcessError, DEVNULL
from threading import Lock
from concurrent.futures import ThreadPoolExecutor

import requests
import websockets
from websockets.exceptions import ConnectionClosedOK
import colorama
from tqdm import tqdm

__version__ = '1.1.2'

logger = logging.getLogger('websockets')
logger.setLevel(logging.DEBUG if '--debug' in sys.argv else logging.INFO)
logger.addHandler(logging.StreamHandler())

MEGA_BYTE = 1024 ** 2
MINUTE = 60
MAX_OPEN_FILES, _ = resource.getrlimit(resource.RLIMIT_NOFILE)
UPLOAD_WORKERS = 5
FILE_CHUNK_SIZE = 20


class WebSocketClient:

    async def loop(self):
        try:
            async with websockets.connect(
                self.websocket_url,
                max_size=2 * MEGA_BYTE,
                ping_interval=5 * MINUTE,
                ping_timeout=5 * MINUTE,
            ) as ws:
                self.ws = ws
                await self.on_open()
                while await self.on_message():
                    pass
        finally:
            await self.on_close()

    async def on_open(self):
        pass

    async def on_message(self):
        try:
            message = await self.ws.recv()
        except ConnectionClosedOK:
            return False

        message = json.loads(message)
        message_type = message.pop('type', None)
        handler = getattr(self, 'receive_' + message_type, None)
        if handler:
            await handler(**message)
            return True
        else:
            await self.receive_print(
                [
                    'Did not understand message from server:',
                    message_type,
                    message
                ],
                {'color': 'RED'}
            )
            return False

    async def on_close(self):
        pass

    # Data transmission

    async def send(self, **kwargs):
        await self.ws.send(json.dumps(kwargs))

    async def send_bytes(self, data):
        await self.ws.send(data)

    async def receive(self):
        return json.loads(await self.ws.recv())

    # Receivers

    async def receive_print(self, args, kwargs):
        color = kwargs.pop('color', None)
        if color:
            color = color and getattr(colorama.Fore, color, None)
            print(
                color + colorama.Style.BRIGHT + ':: ',
                end=colorama.Style.RESET_ALL
            )
        print(*args, **kwargs)


class Iskra(WebSocketClient):
    def __init__(
        self,
        host,
        argv,
        ws_path='/api/cli',
        upload_path='/upload',
        insert_implicit_train_command=True,
    ):
        if host.startswith('localhost'):
            ws_schema = 'ws://'
            http_schema = 'http://'
        else:
            ws_schema = 'wss://'
            http_schema = 'https://'

        self.host = host
        self.ws_schema = ws_schema
        self.http_schema = http_schema
        self.ws_path = ws_path
        self.upload_path = upload_path
        self.argv = argv
        self.insert_implicit_train_command = insert_implicit_train_command
        self.read_configuration()

    @property
    def websocket_url(self):
        return self.ws_schema + self.host + self.ws_path

    @property
    def upload_url(self):
        return self.http_schema + self.host + self.upload_path

    async def loop(self):
        command = self.argv[:1]

        # If first argument is a file run training
        if (self.insert_implicit_train_command
                and command and Path(command[0]).is_file()):
            self.argv.insert(0, 'train')

        # Dispatch local command
        if command:
            command_handler = getattr(self, 'cmd_' + command[0], None)
            if command_handler:
                await command_handler(*sys.argv[2:])
                return

        await super().loop()

    # Configuration

    def get_config(self, keys, defalut=None):
        value = self.config
        for key in keys.split('.'):
            value = value.get(key) or {}
        return value or defalut

    def read_configuration(self):
        self.config_dir = Path.home().joinpath('.iskra')
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir.joinpath('config.json')
        self.config_file.touch()
        self.config = json.loads(self.config_file.read_text() or '{}')

    def write_configuration(self, **kwargs):
        self.config = kwargs
        self.config_file.write_text(json.dumps(self.config, indent=4))

    # WebSocket event handlers

    async def on_open(self):
        await self.run_command()

    async def run_command(self, *argv):
        await self.send(type='command', argv=self.argv)

    # Local commands

    async def cmd_logout(self):
        self.config.pop('jwt', None)
        self.write_configuration()
        await self.receive_print(['Bye bye...'], {'color': 'GREEN'})

    # Receivers

    async def receive_jwt(self, refresh, access):
        self.write_configuration(jwt={
            'refresh': refresh,
            'access': access,
        })

    async def receive_machine(self, host, command, argv):
        self.talk_to_server = type(self)(
            host, argv,
            ws_path='/cli/' + command,
            upload_path='/upload',
            insert_implicit_train_command=False,
        )

    async def receive_open_browser(self, url):
        webbrowser.open(url)

    async def receive_write_metadata(self, **kwargs):
        file = Path.cwd().joinpath('.iskra.json')
        file.write_text(json.dumps(kwargs))

    # Responders

    async def receive_prompt(self, request_id, msg):
        await self.send(request_id=request_id, value=input(msg + ': '))

    async def receive_send_access_token(self, request_id=None):
        access_token = self.get_config('jwt.access', '')
        await self.send(access_token=access_token, request_id=request_id)

    async def receive_send_refresh_token(self, request_id):
        refresh_token = self.get_config('jwt.refresh', '')
        await self.send(refresh_token=refresh_token, request_id=request_id)

    async def receive_send_metadata(self, request_id):
        conf_file = Path.cwd().joinpath('.iskra.json')
        if not conf_file.exists():
            conf_file.write_text(json.dumps({'name': Path.cwd().name}))
        conf = json.loads(conf_file.read_text())
        await self.send(**dict(conf, request_id=request_id))

    async def receive_send_env_metadata(self):
        await self.send(**get_env_metadata())

    # File transfers:

    async def receive_start_file_transfer(self):
        metadata = self.get_local_files_metadata()
        total_size = sum(f['size'] for f in metadata)
        progress = tqdm(
            total=total_size,
            desc='Uploading',
            unit='b',
            unit_scale=True,
            unit_divisor=1024,
        )
        progress.lock = Lock()
        with ThreadPoolExecutor(max_workers=UPLOAD_WORKERS) as executor:
            files = {}
            for file in metadata:
                files[file['path']] = file
                if len(files) == FILE_CHUNK_SIZE:
                    await self.send_files(executor, progress, files)
                    files = {}

            # Send remaining files
            await self.send_files(executor, progress, files)

            # Keep the socket open during upload
            queue_empty = False
            while not queue_empty:
                with executor._shutdown_lock:
                    queue_empty = executor._work_queue.empty()
                    await self.send(type='ping')
                    await self.receive()
                    await asyncio.sleep(1)

        with progress.lock:
            progress.close()

        await self.send(type='EOT')

    async def send_files(self, executor, progress, files):
        await self.send(
            type='files',
            files=[
                [f['path'], f['size'], f['mtime']]
                for f in files.values()
            ]
        )
        paths_to_send = await self.receive()
        files_to_send = []
        total_size = 0
        for path in paths_to_send:
            file = files.pop(path)
            files_to_send.append(file)
            total_size += file['size']
            if total_size >= MEGA_BYTE:
                executor.submit(self.upload_file, progress, files_to_send)
                files_to_send = []
                total_size = 0

        if files_to_send:
            executor.submit(self.upload_file, progress, files_to_send)

        with progress.lock:
            progress.update(sum(f['size'] for f in files.values()))

    def upload_file(self, progress, files):
        try:
            data = {f'p_{i}': f['path'] for i, f in enumerate(files)}
            data.update({f'mt_{i}': f['mtime'] for i, f in enumerate(files)})
            r = requests.post(
                self.upload_url,
                data=data,
                files={
                    str(i): FakeFile(f['path']) for i, f in enumerate(files)
                },
                headers={
                    'Authorization': 'JWT ' + self.config['jwt']['access']
                },
            )
            if r.ok:
                with progress.lock:
                    progress.update(sum(f['size'] for f in files))
            else:
                print(r.json())
                r.raise_for_status()
        except Exception as e:
            import traceback
            traceback.print_exc()
            raise e

    def get_local_files_metadata(self):
        metadata = []
        paths = glob('**', recursive=True)
        dirs_to_ignore = set()
        for path in tqdm(paths, desc="Checksum", unit='file'):
            if any(path.startswith(d) for d in dirs_to_ignore):
                continue

            ignore_this = (
                isdir(path) and (
                    basename(path) in ('__pycache__', '.git') or
                    exists(join(path, 'bin', 'activate'))
                )
            )
            if ignore_this:
                dirs_to_ignore.add(path)
                continue

            if isfile(path):
                stat = os.stat(path)
                metadata.append({
                    'path': path,
                    'size': stat.st_size,
                    'mtime': stat.st_mtime_ns,
                })
        return metadata


class FakeFile:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'rb') as f:
            return f.read()

# Introspection


def get_env_metadata():
    data = {'cwd': os.getcwd()}
    try:
        return dict(
            data,
            conda=check_output(
                ['conda', 'env', 'export'],
                stderr=DEVNULL
            ).decode(),
        )
    except (FileNotFoundError, CalledProcessError):
        major, minor, *_ = sys.version_info
        return dict(
            data,
            pip={
                'python': str(major) + '.' + str(minor),
                'requirements': check_output(['pip', 'freeze']).decode(),
            }
        )


async def main():
    try:
        data = requests.get('https://pypi.org/pypi/iskra-cli/json').json()
    except Exception:
        pass
    else:
        if data['info']['version'] != __version__:
            print(
                colorama.Back.RED +
                colorama.Fore.BLACK +
                "!! You are using an outdated iskra-cli, ugrade:" +
                colorama.Style.RESET_ALL
            )
            print()
            print("    pip install --upgrade iskra-cli")
            print()

    iskra = Iskra(
        host=env.get('ISKRA_HOST', 'app.iskra.ml'),
        argv=sys.argv[1:]
    )
    while iskra:
        await iskra.loop()
        iskra = getattr(iskra, 'talk_to_server', None)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
