import shutil

from progress.spinner import MoonSpinner
from pyfiglet import Figlet
from clint.textui import colored, puts
from urllib import request
import sys
import json
import os
from textwrap import wrap
import subprocess
import time


API_CALLS = '''from urllib import request
from http_types import HttpExchange
from http_types.utils import RequestBuilder, ResponseBuilder, HttpExchangeWriter
from io import StringIO

def make_pokemon_request(path):
    req = request.Request('http://localhost:8000%s' % path, headers={
        'user-agent': 'python', 'Host': 'pokeapi.co', 'X-Meeshkan-Scheme': 'https'
    })
    res = request.urlopen(req)
    res.read()

PATHS = [
    '/api/v2/pokemon/1/',
    '/api/v2/pokemon/2/',
    '/api/v2/pokemon/3/',
    '/api/v2/pokemon/4/',
    '/api/v2/pokemon/5/',
    '/api/v2/pokemon/6/',
    '/api/v2/pokemon/7/',
    '/api/v2/pokemon/8/',
    '/api/v2/pokemon/9/',
    '/api/v2/pokemon/10/',
    '/api/v2/pokemon/',
    '/api/v2/type/1/',
    '/api/v2/type/2/',
    '/api/v2/type/3/',
    '/api/v2/type/4/',
    '/api/v2/type/5/',
    '/api/v2/type/6/',
    '/api/v2/type/7/',
    '/api/v2/type/8/',
    '/api/v2/type/9/',
    '/api/v2/type/10/',
    '/api/v2/type/',
    '/api/v2/ability/1/',
    '/api/v2/ability/2/',
    '/api/v2/ability/3/',
    '/api/v2/ability/4/',
    '/api/v2/ability/5/',
    '/api/v2/ability/6/',
    '/api/v2/ability/7/',
    '/api/v2/ability/8/',
    '/api/v2/ability/9/',
    '/api/v2/ability/10/',
    '/api/v2/ability/',
]

for x, path in enumerate(PATHS):
    print("  ** Calling https://pokeapi.co%s, path %d of %d" % (path, x + 1, len(PATHS)))
    make_pokemon_request(path)
'''

MERGE_SPECS = '''from openapi_typed_2 import convert_to_openapi, convert_from_openapi
import json
from dataclasses import replace
import os

with open('__meeshkan__/replay/openapi.json', 'r') as replay_file:
    with open('__meeshkan__/gen/openapi.json', 'r') as gen_file:
        replay = convert_to_openapi(json.loads(replay_file.read()))
        gen = convert_to_openapi(json.loads(gen_file.read()))
        new = replace(replay, paths = { **replay.paths, **gen.paths })
        try:
            os.mkdir('__meeshkan__/both')
        except: pass # exists
        with open('__meeshkan__/both/openapi.json', 'w') as both_file:
            both_file.write(json.dumps(convert_from_openapi(new), indent=2))
'''

def m_print(s):
    print('\n'.join(wrap(s, width=60)))

def m_input(s):
    return input('\n'.join(wrap(s, width=60)))

def starting_server(message):
    bar = MoonSpinner(message)
    for i in range(100):
        time.sleep(0.1)
        bar.next()
        try:
            request.urlopen(request.Request("http://localhost:8888/admin/storage", method='DELETE'))
            bar.finish()
            return
        except:
            pass

    raise Exception('Unable to start Meeshkan in 10 seconds. Please, check your environment.')




def building():
    # for now do nothing
    pass

def cli():
    f = Figlet(font='slant')
    print(f.renderText('meeshkan'))
    puts(colored.cyan('The tutorial!!', bold=True))
    m_input('Press ENTER to continue...')
    ############################
    m_print("")
    m_print("##############################")
    m_print("")
    m_print("Meeshkan allows you to create mocks of APIs from server traffic and OpenAPI specs.  To start, we'll record some server traffic.  But before we get started, there are a few things you should know.")
    m_print("")
    m_print("First, Meeshkan will create a directory called __meeshkan__ in the current working directory.  Don't put anything special in there, as it may get overwritten by this tutorial!")
    m_print("")
    m_print("Next, this tutorial makes some network calls to the Pokemon API (pokeapi.co).  Please make sure you have a working internet connection.")
    m_print("")
    i = m_input('With that in mind, press ENTER to continue (or the q key followed by ENTER to quit): ')
    if i == 'q':
        m_print("If you change your mind, come back anytime.  Goodbye!")
        sys.exit(0)
    m_print("")
    m_print("##############################")
    m_print("")
    m_print("Let's record a bit of server traffic.  We've written a file to `__meeshkan__/api_calls.py` to make our recordings.  Meeshkan expects recordings to be in the http-types format (github.com/meeshkan/http-types), so we'll use that.")
    m_print("")
    m_print("Open up `__meeshkan__/api_calls.py`.  You'll see that we call the API 33 times using Meeshkan as a forward proxy.")
    m_print("")
    if os.path.exists("__meeshkan__"):
        shutil.rmtree("__meeshkan__")
    os.mkdir("__meeshkan__")

    with open('__meeshkan__/api_calls.py', 'w') as fi:
        fi.write(API_CALLS)
    m_input("After you've checked out `__meeshkan__/api_calls.py`, press ENTER to launch the proxy and execute the script!")

    with subprocess.Popen("meeshkan record -r -l __meeshkan__".split(" "), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) as p: #
        try:
            starting_server('Starting proxy')
            m_print("")
            m_print("##############################")
            m_print("")
            subprocess.call('python __meeshkan__/api_calls.py', shell=True)
            m_print("")
            m_input("Now, if you check out `__meeshkan__/recordings.jsonl`, you'll see all of the recorded server traffic. Press ENTER to continue.")
            m_print("")
            m_print("##############################")
            m_print("")
            m_input("The command `meeshkan build` transforms your recordings into an OpenAPI spec.  The `replay` flag tells Meeshkan to build a spec that's identical to the recorded traffic. Press ENTER to invoke `meeshkan build` in `replay` mode.")
            m_print("")
            m_print("##############################")
            m_print("")
            print("$ meeshkan build -i __meeshkan__/recordings.jsonl -o __meeshkan__/replay -m replay`")
            m_print("")
            subprocess.call("meeshkan build -i __meeshkan__/recordings.jsonl -o __meeshkan__/replay -m replay",
                            shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            building()
            m_print("")
            m_print("Done.  Now, open up __meeshkan__/replay/openapi.json. Search within this document for `/api/v2/pokemon/10/:`.  This is a translation of the `GET` request you got from the Pokemon API into OpenAPI.")
            m_print("")
            m_input("Let's use this spec to create a server that serves back our recordings.  Press ENTER to boot up the mock server.")
            m_print("")
        finally:
            p.kill()

    with subprocess.Popen("meeshkan mock -s __meeshkan__/replay -r".split(" "), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) as p:
        try:
            starting_server('Starting server')
            m_print("")
            m_print("##############################")
            m_print("")
            m_input("The server is up and running.  Press ENTER to send a `GET` request to the endpoint `/api/v2/pokemon/10/`.")
            req = request.Request("http://localhost:8000/api/v2/pokemon/10/", headers={
                'Host': 'pokeapi.co',
                'X-Meeshkan-Scheme': 'https'
            })
            res = request.urlopen(req)
            body = res.read()
            m_print("")
            m_print("##############################")
            m_print("")
            m_print("Here is the response we got back from the server.")
            m_print("")
            # vanilla print as thre should not be any line wraps
            # may put in function later
            print(json.dumps(json.loads(body
                        if isinstance(body, str)
                        else body.decode("utf8")
                        if isinstance(body, bytes)
                        else ""), indent=2))
            m_print("..............................")
            m_print("It's the exact same response we got back from the Pokemon API.  Pretty cool, huh?")
            m_print("")
            m_print("You can try the same thing.  From curl, Postman or your web browser, try calling endpoints like http://localhost:8000/api/v2/ability/ or http://localhost:8000/api/v2/type/2/.  When doing so, make sure to set the following headers:")
            m_print("")
            print("""{
            "Host": "pokeapi.co",
            "X-Meeshkan-Scheme": "https"
            }""")
            m_print("")
            m_input("Once you're done exploring, press ENTER to turn off the server and continue.")
            m_print("")
        finally:
            p.kill()

    m_print("")
    m_print("##############################")
    m_print("")
    m_print("Now, let's build a new spec.  This time, instead of serving back fixed data, we will use the recordings to create _synthetic_ data.   We do this by invoking `meeshkan build --mode gen`.")
    m_print("")
    m_input("Press ENTER to build the new spec.")
    m_print("")
    m_print("Hang tight, we're building your spec!")
    m_print("")
    print("$ meeshkan build -i __meeshkan__/recordings.jsonl -o __meeshkan__/gen -m gen`")
    m_print("")
    subprocess.call("meeshkan build -i __meeshkan__/recordings.jsonl -o __meeshkan__/gen -m gen", shell=True, stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
    m_print("")
    building()
    m_print("")
    m_print("Done.  In __meeshkan__/gen/, you'll see a new OpenAPI spec.")
    m_print("")
    m_input("Let's use this spec to create some _synthetic_ data.  Press ENTER to reboot the mock server on port 8000.")
    m_print("")
    with subprocess.Popen("meeshkan mock -s __meeshkan__/gen -r".split(" "), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) as p:
        try:
            m_print("##############################")
            m_print("")
            starting_server('Starting server')
            m_print("")
            m_input("The server is up and running.  Press ENTER to send a `GET` request to the endpoint `/api/v2/pokemon/10/`.")
            req = request.Request("http://localhost:8000/api/v2/pokemon/10/", headers={
                'Host': 'pokeapi.co',
                'X-Meeshkan-Scheme': 'https'
            })
            res = request.urlopen(req)
            body = res.read()
            m_print("")
            m_print("##############################")
            m_print("")
            m_print("Here is the response we got back from the server.")
            m_print("")
            # vanilla print as thre should not be any line wraps
            # may put in function later
            print(json.dumps(json.loads(body
                        if isinstance(body, str)
                        else body.decode("utf8")
                        if isinstance(body, bytes)
                        else ""), indent=2))
            m_print("..............................")
            m_print("")
            m_print("The data above is synthetic, but it has the same layout as the recorded data.")
            m_print("")
            m_print("Why synthetic data?  Well, I'm glad you asked!  Two main reasons.")
            m_print("")
            m_print("1. Security breaches are most common when dealing with log files and in test environments.  So, when testing, you never want to use real data if possible.")
            m_print("2. Using synthetic data forces you write tests that focus on business logic rather than focusing on the content of fixtures, which is (in our opinion) a cleaner way to do testing.")
            m_print("")
            m_print("From curl, postman or your web browser, try calling http://localhost:8000/api/v2/pokemon/\{id\}/ , where `\{id\}` is _any_ positive integer. And when doing so, make sure to set following two headers:")
            m_print("")
            print("""{
            "Host": "pokeapi.co",
            "X-Meeshkan-Scheme": "https"
        }""")
            m_print("")
            m_input("You'll see that Meeshkan generates a synthetic response for an arbitrary Pokemon. Once you're done exploring, press ENTER to turn off the server and continue.")
            m_print("")
        finally:
            p.kill()

    m_print("")
    m_print("##############################")
    m_print("")
    with open('__meeshkan__/merge_specs.py', 'w') as fi:
        fi.write(MERGE_SPECS)
    m_input("Finally, open the file `merge_specs.py` that we created in the __meeshkan__ directory.  It's a script that merges together the two OpenAPI specs - replay and gen - created by Meeshkan.  After you've looked at it, press ENTER to execute it.")
    m_print("")
    m_print("$ python __meeshkan__/merge_specs.py")
    m_print("")
    subprocess.call('python __meeshkan__/merge_specs.py', shell=True)
    m_print("Done.  In `__meeshkan__/both/`, you'll see an OpenAPI spec that combines _both_ the fixtures from `__meeshkan__/replay/openapi.json` and the synthetic spec from `__meeshkan__/replay/openapi.json`.")
    m_print("")
    m_input("Like the other two specs, this one can be used to create a mock server.  Try it yourself!  After this tutorial, run `meeshkan mock -i __meeshkan__/both -r`, making sure to set the same headers as before, and see how the server responds.  Press ENTER to continue.")
    m_print("")
    m_print("##############################")
    m_print("")
    m_print("Thanks for checking out Meeshkan!  There are several other cool features, like callbacks to implement stateful logic and various connectors from libraries and platforms like Express and Kong.")
    m_print("")
    m_print("If you have a moment, please fill out our post-tutorial survey on https://meeshkan.typeform.com/to/FpRakX.  Besides helping us improve Meeshkan, it will help us improve this and other tutorials.")
    m_print("")
    m_print("Take care and happy mocking!")

if __name__ == '__main__':
    cli()
