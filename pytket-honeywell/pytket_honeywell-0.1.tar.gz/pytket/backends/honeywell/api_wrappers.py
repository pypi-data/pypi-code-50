# -*- coding: utf-8 -*-
""""
Functions used to submit jobs with Honeywell Quantum Solutions API.


"""
import asyncio
import json
import sys
from http import HTTPStatus
from typing import Union

import requests
import websockets
import nest_asyncio


# This is necessary for use in Jupyter notebooks to allow for nested asyncio loops
nest_asyncio.apply()


def submit_job(api_key: str,
               qasm_str: str,
               shots: int,
               machine: str,
               url: str,
               name: str = 'job') -> str:
    """
    Submits job to device and returns job ID.

    Args:
        api_key:    API key
        qasm_str:   OpenQASM file to run
        shots:      number of repetitions of qasm_str
        machine:    machine to run on
        url:        URL for submission
        name:       name of job (for error handling)

    Returns:
        (str):     id of job submitted

    """
    try:
        # send job request
        body = {
            'machine': machine,
            'name': name,
            'language': 'OPENQASM 2.0',
            'program': qasm_str,
            'priority': 'normal',
            'count': shots,
            'options': None
        }
        res = requests.post(
            url + 'job',
            json.dumps(body),
            headers={'x-api-key': api_key}
        )
        if res.status_code != HTTPStatus.OK:
            jr = res.json()
            raise RuntimeError(f'HTTP error while submitting job, {jr["error"]["text"]}')

        # extract job ID from response
        jr = res.json()
        job_id = jr['job']
        print('submitted ' + name + ' id={job}, submit date={submit-date}'.format(**jr))

    except ConnectionError:
        if len(sys.argv) > 2:
            print('{} Connection Error: Error during submit...'.format(name))
        else:
            print('Connection Error: Error during submit...')

    return job_id


def retrieve_job(api_key: str,
                 job_id: str,
                 url: str) -> dict:
    """
    Retrieves job from device.

    Args:
        api_key:    API key
        job_id:     unique id of job
        url:        URL for submission

    Returns:
        (dict):     output from API

    """
    res = requests.get(
        url + 'job/' + job_id + '?websocket=true',
        headers={'x-api-key': api_key}
    )
    jr = res.json()

    # print('checked on job={job}, status={status}'.format(**jr))

    if 'websocket' in jr and jr['status'] not in {'failed', 'completed', 'canceled', 'running'}:
        return asyncio.get_event_loop().run_until_complete(wait_on_websocket(api_key, jr, url))

    return jr


async def wait_on_websocket(api_key: str,
                            status_response: str,
                            url: str):

    task_token = status_response['websocket']['task_token']
    execution_arn = status_response['websocket']['executionArn']

    websocket_uri = url.replace('https://', 'wss://ws.')
    async with websockets.connect(websocket_uri, extra_headers={'x-api-key': api_key}) as websocket:
        body = {
            "action": "OpenConnection",
            "task_token": task_token,
            "executionArn": execution_arn
        }
        await websocket.send(json.dumps(body))
        resp = await asyncio.wait_for(websocket.recv(), timeout=6000)

        return json.loads(resp)


def run_job(api_key: str,
            qasm_str: str,
            shots: int,
            machine: str,
            url: str,
            name: str = 'job') -> dict:
    """
    Submits a job and waits to receives job result dictionary.

    Args:
        api_key:    API key
        qasm_file:  OpenQASM file to run
        name:       name of job (for error handling)
        shots:      number of repetitions of qasm_str
        machine:    machine to run on
        url:        URL for submission

    Returns:
        jr:         (dict) output from API

    """
    job_id = submit_job(api_key, qasm_str, shots, machine, name, url)

    jr = retrieve_job(api_key, job_id)

    return jr


def status(api_key: str,
           machine: str,
           url: str) -> str:
    """
    Check status of machine.

    Args:
        (str):    machine name

    """
    state = requests.get(url + 'machine/' + machine, headers={'x-api-key': api_key}).json()

    return state['state']


def cancel(api_key: str,
           job_id: str,
           url: str) -> dict:
    """
    Cancels job.

        Args:
            api_key:    API key
            job_id:     job ID to cancel
            url:        URL for submission

        Returns:
            jr:         (dict) output from API

        """

    res = requests.post(
            url + 'job/' + job_id + '/cancel',
            headers={'x-api-key': api_key}
        )
    jr = res.json()
    
    return jr