"""
Utilities for acting as an app and dealing with installations.

This is basically a dramatically reduced v3 REST client focusing just on the app
and installation features.
"""
import contextlib
import json

import aiohttp
import dateutil.parser
import gqlmod

from . import _build_accept
from ._app_base import GithubBaseApp


@contextlib.asynccontextmanager
async def call_rest(method, url, *, body=None, preview=None, bearer=None):
    """
    Performs an API request, in the form of GitHub v3 API.
    """
    # FIXME: Handle API request throttling
    if method == 'GET' and body:
        raise ValueError("Can't send a body in a GET")

    if url.startswith('/'):
        url = f"https://api.github.com{url}"

    headers = {}

    if body:
        data = json.dumps(body).encode('utf-8')
        headers['Content-Type'] = 'application/json'
    else:
        data = None

    if preview:
        headers['Accept'] = _build_accept(preview)

    if bearer:
        headers['Authorization'] = f"Bearer {bearer}"

    async with aiohttp.request(method, url, headers=headers, data=data, raise_for_status=True) as resp:
        yield resp


async def iter_pages(url, *, preview=None, bearer=None):
    """
    Run a request, and follow the "next" URL in the Link header, recursively.

    Note that only GET requests are supported due to the nature of pagination.

    Produces 3-tuples of (code, info, body).
    """
    nextpage = url
    while nextpage:
        async with call_rest('GET', url, preview=preview, bearer=bearer) as resp:
            yield resp

            if 'next' not in resp.links:
                break

            nexts = list(resp.links['next'].keys())
            assert 0 <= len(nexts) <= 1

            if nexts:
                nextpage = nexts[0]
            else:
                break


class GithubApp(GithubBaseApp):
    """
    Your Github Application

    Please note: Not thread safe.
    """
    async def get_app(self, slug):
        """
        Get the app information, by slug

        https://developer.github.com/v3/apps/#get-a-single-github-app
        """
        async with call_rest(
            'GET', f'/apps/{slug}', bearer=self.token, preview='machine-man-preview'
        ) as resp:
            return await resp.json(content_type=False)

    async def get_this_app(self):
        """
        Get the app information for the current app

        https://developer.github.com/v3/apps/#get-the-authenticated-github-app
        """
        async with call_rest(
            'GET', '/app', bearer=self.token, preview='machine-man-preview',
        ) as resp:
            return await resp.json(content_type=False)

    async def iter_installations(self):
        """
        Generate all installations.

        Traverses pagination.

        https://developer.github.com/v3/apps/#list-installations
        """
        async for resp in iter_pages(
            '/app/installations', bearer=self.token, preview='machine-man-preview',
        ):
            for inst in await resp.json(content_type=False):
                yield inst

    async def get_installation(self, installation_id):
        """
        Get an installation, by ID.

        https://developer.github.com/v3/apps/#get-an-installation
        """
        async with await call_rest(
            'GET', f'/app/installations/{installation_id}',
            bearer=self.token, preview='machine-man-preview',
        ) as resp:
            return await resp.json(content_type=False)

    async def delete_installation(self, installation_id):
        """
        Delete an installation, by ID.

        https://developer.github.com/v3/apps/#delete-an-installation
        """
        async with await call_rest(
            'DELETE', f'/app/installations/{installation_id}',
            bearer=self.token, preview=['machine-man-preview', 'gambit-preview'],
        ) as resp:
            assert resp.status == 204

    async def make_installation_token(self, installation_id, *, repository_ids=None, permissions=None):
        """
        Produce an installation token.

        repository_ids and permissions may be used to reduce the permissions of
        the token.

        https://developer.github.com/v3/apps/#create-a-new-installation-token
        """
        params = {}
        if repository_ids:
            params['repository_ids'] = repository_ids
        if permissions:
            params['permissions'] = permissions
        async with call_rest(
            'POST', f'/app/installations/{installation_id}/access_tokens',
            body=params, bearer=self.token, preview='machine-man-preview',
        ) as resp:
            assert resp.status == 201
            return await resp.json(content_type=False)

    async def get_org_installation(self, org):
        """
        Get an installation, by organization.

        https://developer.github.com/v3/apps/#get-an-organization-installation
        """
        async with call_rest(
            'GET', f'/orgs/{org}/installation',
            bearer=self.token, preview='machine-man-preview',
        ) as resp:
            assert resp.status == 200
            return await resp.json(content_type=False)

    async def get_repo_installation(self, owner, repo):
        """
        Get an installation, by owner and repository.

        https://developer.github.com/v3/apps/#get-a-repository-installation
        """
        async with call_rest(
            'GET', f'/repos/{owner}/{repo}/installation',
            bearer=self.token, preview='machine-man-preview',
        ) as resp:
            assert resp.status == 200
            return await resp.json(content_type=False)

    async def get_user_installation(self, username):
        """
        Get an installation, by user

        https://developer.github.com/v3/apps/#get-a-user-installation
        """
        async with call_rest(
            'GET', f'/users/{username}/installation',
            bearer=self.token, preview='machine-man-preview',
        ) as resp:
            assert resp.status == 200
            return await resp.json(content_type=False)

    @staticmethod
    async def create_app_from_manifest(code):
        """
        Create a new application from a previously-submitted manifest.

        https://developer.github.com/v3/apps/#create-a-github-app-from-a-manifest
        """
        async with call_rest(
            'POST', f'/app-manifests/{code}/conversions',
            preview='fury-preview',
        ) as resp:
            assert resp.status == 200
            return await resp.json(content_type=False)

    async def token_for_repo(self, owner_or_repo, repo=None, *, repo_id=None, permissions=None):
        """
        ga.token_for_repo("owner/repo") -> str
        ga.token_for_repo("owner", "repo") -> str

        Convenience shortcut to call get_repo_installation() and
        make_installation_token() in one go.

        Returns the token and expiration datetime

        The permissions for the token may be passed in.

        If the repo_id is passed in, the token will be scoped to it.
        """
        if repo is None:
            assert '/' in owner_or_repo
            owner, repo = owner_or_repo.split('/', 1)
        else:
            owner, repo = owner_or_repo, repo

        inst = await self.get_repo_installation(owner, repo)

        if repo_id is None:
            repository_ids = None
        else:
            repository_ids = [repo_id]

        token = await self.make_installation_token(
            inst['id'], permissions=permissions, repository_ids=repository_ids,
        )

        t = token['token']
        exp = dateutil.parser.isoparse(token['expires_at'])
        return t, exp

    @contextlib.contextmanager
    def for_app(self):
        """
        Convenience shortcut to make this app the current github credentials.
        """
        # FIXME: What if it expires?
        with gqlmod.with_provider('github', token=self.token):
            yield

    @contextlib.contextmanager
    def for_repo(self, *pargs, **kwargs):
        """
        Convenience shortcut to make a repo the current github credentials.

        Passes arguments to token_for_repo()
        """
        # FIXME: What if it expires?
        token, exp = self.token_for_repo(*pargs, **kwargs)
        with gqlmod.with_provider('github', token=token):
            yield

# TODO: Write class for interrogating installations, using an installation token.
