#!/usr/bin/env python

import sys
import os
import subprocess

def enable_event(event):
    f = open("/sys/kernel/debug/tracing/events/%s"%event, mode='w')
    f.write('1')
    f.close()

def set_trace_buffer_size(buffer_size_kb):
    subprocess.call("echo %d > /sys/kernel/debug/tracing/buffer_size_kb"%buffer_size_kb,
                    shell=True)

def clear_trace_buffer():
    subprocess.call('echo "" > /sys/kernel/debug/tracing/trace', shell=True)
    
def main():
    enable_event("tcp/tcp_probe/enable")
    enable_event("tcp/tcp_retransmit_skb/enable")
    enable_event("tcp/tcp_retransmit_synack/enable")
    # enable_event("tcp/tcp_ca_event/enable")
    # enable_event("tcp/tcp_ca_state_change/enable")
    # enable_event("net_sch/enable")
    set_trace_buffer_size(500000)

    clear_trace_buffer()
    subprocess.call('cat /sys/kernel/debug/tracing/trace_pipe', shell=True)
