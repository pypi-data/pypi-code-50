import asyncio
import logging
import os
from ipaddress import IPv4Address

import pyroute2

from . import config

logger = logging.getLogger(__name__)


def get_ebpf_program_run_args(ebpf: config.EBPFModel):
    def _get_addr_interface(addr: IPv4Address, ipdb=pyroute2.IPDB()):
        for idx, (ifaddr, prefix) in ipdb.ipaddr.items():
            if IPv4Address(ifaddr) == addr:
                return ipdb.by_index[idx]['ifname']

        return None

    ebpf_runner_script_name = config.ebpf.script_path.as_posix()

    interface = None

    program = ebpf.executable
    args = [ebpf_runner_script_name]

    for server_name, server in config.servers:
        server_interface = _get_addr_interface(server.network.bind_ip)
        assert server_interface is not None, f"Can't get interface name for {server.network.bind_ip}"

        if interface is None:
            interface = server_interface

        if server_interface != interface:
            raise config.ConfigurationError(
                'Different interfaces dont supported yet: ' f'{server_interface} != {interface}'
            )

        args += ['-p', f'{server.network.server_port}:{server.network.bind_port}']

    args += ['-i', interface]

    return program, args


async def run_ebpf_redirection():
    if not config.ebpf or not config.ebpf.enabled:
        return

    program, args = get_ebpf_program_run_args(config.ebpf)
    process = await asyncio.create_subprocess_exec(program, *args, stdout=asyncio.subprocess.PIPE,)
    output, _ = await process.communicate()

    retcode = process.returncode
    if retcode != os.EX_OK:
        logger.exception('eBPF redirection exit with code %s', retcode)
        logger.debug(output)
        raise RuntimeError

    logger.info('eBPF redirection normally exit with 0 code')
    logger.debug(output)
