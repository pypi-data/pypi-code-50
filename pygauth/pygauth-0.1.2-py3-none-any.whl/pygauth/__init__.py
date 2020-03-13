# Copyright (c) 2020 Spazzlo

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pathlib import Path
from typing import List, Union, Dict
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

import google_auth_oauthlib
import json
import bson


def expand_scopes(short_scopes: List[str]) -> List[str]:
    """Turns a list of short scopes (like `drive` or `iam`) into a list of full scopes."""

    scopes = []
    for scope in short_scopes:
        if scope.startswith("https://"):
            scopes.append(scope)
        else:
            scopes.append("https://www.googleapis.com/auth/" + scope)

    return scopes


def get_sa_creds(sa_file: Union[str, Path], scopes: List[str] = None) -> service_account.Credentials:
    """Authenticates a service account given it's path and an optional list of scopes."""
    return service_account.Credentials.from_service_account_file(sa_file, scopes=expand_scopes(scopes))


def get_user_creds_file(creds_file: Union[str, Path], scopes: List[str] = None, create_cache: bool = True, refresh_cache: bool = False, remote: bool = False) -> Credentials:
    """Gets user credentials from a file, optionally creating a cached tokens file."""
    with open(creds_file) as creds_data:
        creds_dict = json.load(creds_data)
        return get_user_creds_dict(creds_dict, scopes=scopes, create_cache=create_cache, refresh_cache=refresh_cache, remote=remote)


def get_user_creds_dict(creds_dict: Dict[str, str], scopes: List[str] = None, create_cache: bool = True, refresh_cache: bool = False, remote: bool = False) -> Credentials:
    """Gets user credentials from a dict, optionally creating a cached tokens file."""

    scopes = expand_scopes(scopes)

    if create_cache:
        if Path(".pygauth").exists():
            cache_file = open(".pygauth", "rb")
        else:
            with open(".pygauth", "wb") as cache_file:
                cache_file.write(bson.dumps({}))
            cache_file = open(".pygauth", "rb")
        try:
            cache = bson.loads(cache_file.read())
        except Exception as e:
            cache_file.close()
            with open(".pygauth", "wb") as cache_file:
                cache_file.write(bson.dumps({}))
            refresh_cache = True
        else:
            if not refresh_cache:
                scopes.sort()
                scope_code = "+".join(scopes)
                if scope_code in cache:
                    cached_creds = json.loads(cache[scope_code])
                    creds = Credentials.from_authorized_user_info(
                        cached_creds, cached_creds["scopes"])
                    if (creds.expired and creds.refresh_token) or not creds.token:
                        creds.refresh(Request())
                    return creds
                else:
                    refresh_cache = True
            cache_file.close()

    flow = InstalledAppFlow.from_client_config(creds_dict, scopes=scopes or [])
    if remote:
        creds = flow.run_console()
    else:
        creds = flow.run_local_server()

    if refresh_cache:
        if Path(".pygauth").exists():
            with open(".pygauth", "rb") as cache_file:
                try:
                    cache = bson.loads(cache_file.read())
                except json.JSONDecodeError:
                    cache = {}
        else:
            cache = {}

        scopes.sort()
        scope_code = "+".join(scopes)
        cache[scope_code] = creds.to_json().replace(" ", "")

        with open(".pygauth", "wb") as cache_file:
            cache_file.write(bson.dumps(cache))

    return creds
