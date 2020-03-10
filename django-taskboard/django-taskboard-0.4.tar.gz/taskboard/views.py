import json
import os
from os import path

from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .controller.performance.CPU import CPU
from .controller.performance.Memory import Memory
from .controller.performance.Disk import Disk
from .controller.performance.Network import Network

from .controller.system.Process import Process


def authorization(view):
    def wrapper(*args, **kwargs):
        logged_in = args[0].session.get('logged_in', False)
        return view(*args, **kwargs) if logged_in else redirect(reverse('login'))

    return wrapper


def login(request):
    if request.session.get('logged_in', False):
        return redirect(reverse('index'))

    if request.method == 'POST':
        username, password = (request.POST.get('username', ''), request.POST.get('password', ''))

        with open('./taskboard/sessions/admins.txt', encoding='UTF-8') as file:
            lines = [line.strip() for line in file]
            admins = {username: [password, name] for line in lines for username, password, name in [line.split(';')]}

        if username in admins.keys() and password == admins.get(username)[0]:
            request.session['logged_in'] = True
            request.session['name'] = admins.get(username)[1]
            return redirect(reverse('index'))
        else:
            messages.error(request, 'Incorrect credentials')

    return render(request, 'taskboard/login.html')


@authorization
def logout(request):
    request.session.flush()
    return redirect(reverse('login'))


# Create your views here.
@authorization
def index(request):
    return render(request, 'taskboard/index.html', {'active': 'dashboard', 'header': 'Dashboard'})


@authorization
def performance(request, component):
    header = {
        'cpu': 'CPU',
        'gpu': 'GPU',
        'memory': 'Memory',
        'disk': 'Disk',
        'network': 'Network',
    }

    return render(request, f'taskboard/performance/{component}.html', {
        'active': component,
        'header': header.get(component)
    })


@authorization
def system(request, component):
    header = {
        'system': 'Processes',
        'services': 'Services',
    }

    return render(request, f'taskboard/system/{component}.html', {
        'active': component,
        'header': header.get(component)
    })


@authorization
def cpu(request, metric):
    option = {
        'brand_bits': CPU.brand_bits,
        'cores': CPU.cores,
        'utilization': CPU.utilization,
        'times': CPU.times,
        'statistics': CPU.statistics,
        'usage': CPU.usage,
    }

    return HttpResponse(json.dumps(option.get(metric)()))


@authorization
def memory(request, metric):
    option = {
        'virtual': Memory.virtual,
        'swap': Memory.swap,
    }

    return HttpResponse(json.dumps(option.get(metric)()))


@authorization
def disk(request, metric, device=None):
    option = {
        'partitions': Disk.partitions,
        'io_counters': Disk.io_counters,
        'usage': Disk.usage
    }

    response = option.get(metric)() if not device else option.get(metric)(device)
    return HttpResponse(json.dumps(response))


@authorization
def network(request, metric):
    option = {
        'io_counters': Network.io_counters,
        'connections': Network.connections,
        'if_addrs': Network.if_addrs,
        'if_stats': Network.if_stats,
    }

    return HttpResponse(json.dumps(option.get(metric)()))


@authorization
def processes(request, metric, pid=None):
    option = {
        'all': Process.all,
        'start': Process.start,
        'stop': Process.stop,
    }

    if request.method == 'POST':
        response = option.get(metric)(request.POST.get('path', ''), request.POST.get('args', None))
    else:
        response = option.get(metric)() if not pid else option.get(metric)(pid)

    return HttpResponse(json.dumps(response))


@authorization
def services(request, metric):
    return


@authorization
def handler404(request, *args, **argv):
    return render(request, 'taskboard/404.html')
