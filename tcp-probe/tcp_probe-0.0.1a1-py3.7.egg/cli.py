#!/usr/bin/env python

import sys
import os
import subprocess
import click

def enable_event(event):
    f = open("/sys/kernel/debug/tracing/events/%s"%event, mode='w')
    f.write('1')
    f.close()

def set_trace_buffer_size(buffer_size_kb):
    subprocess.call("echo %d > /sys/kernel/debug/tracing/buffer_size_kb"%buffer_size_kb,
                    shell=True)

def clear_trace_buffer():
    subprocess.call('echo "" > /sys/kernel/debug/tracing/trace', shell=True)

@click.command()
@click.option('-n', '--no-clear', default=False, help="Don't clear the kernel trace buffer before starting the trace")
@click.option('-b', '--buffer', default=500000, help="Size of trace buffer")
def main(no_clear, buffer_size):
    """Prints out assorted tcp-related tracing in the Linux kernel"""
    try:
        enable_event("tcp/tcp_probe/enable")
        enable_event("tcp/tcp_retransmit_skb/enable")
        enable_event("tcp/tcp_retransmit_synack/enable")
    except IOError as e:
        if (e[0] == errno.EPERM):
            print >> sys.stderr, "%s needs root permissions"%(sys.argv[0])
            sys.exit(1)

    
    set_trace_buffer_size(buffer_size)

    if not no_clear:
        clear_trace_buffer()
        
    subprocess.call('cat /sys/kernel/debug/tracing/trace_pipe', shell=True)
