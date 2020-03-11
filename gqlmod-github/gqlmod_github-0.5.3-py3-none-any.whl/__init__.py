"""
Provider for GitHub's v4 GraphQL API.
"""
import itertools
import urllib.request

import graphql

from gqlmod.helpers.utils import walk_query, walk_variables, unwrap_type


def find_directive(ast_node, name):
    if ast_node is None:
        return
    for d in ast_node.directives:
        if d.name.value == name:
            break
    else:
        return

    return {
        arg.name.value: graphql.value_from_ast_untyped(arg.value)
        for arg in d.arguments
    }


def _build_accept(previews):
    if isinstance(previews, (list, tuple, set)):
        if previews:
            return ', '.join(
                f"application/vnd.github.{p}+json"
                for p in previews
            )
        else:
            return "application/json"
    elif isinstance(previews, str):
        return f"application/vnd.github.{previews}+json"
    else:
        raise TypeError(f"Can't handle preview {previews!r}")


class GitHubBaseProvider:
    endpoint = 'https://api.github.com/graphql'

    def __init__(self, token=None):
        self.token = token

    def _build_accept_header(self, variables):
        previews = variables.pop('__previews', None)
        return _build_accept(previews)

    def _build_authorization_header(self, variables):
        return f"Bearer {self.token}"

    # This can't be async
    def get_schema_str(self):
        with urllib.request.urlopen("https://developer.github.com/v4/public_schema/schema.public.graphql") as fobj:
            return fobj.read().decode('utf-8')

    def codegen_extra_kwargs(self, gast, schema):
        previews = set()
        # Find all the @preview directives and pull out their names
        for field in itertools.chain(
            (f for _, _, f in walk_query(gast, schema)),
            (f for _, f in walk_variables(gast, schema)),
        ):
            d = find_directive(field.ast_node, 'preview')
            if d and 'toggledBy' in d:
                previews.add(d['toggledBy'])

            typ, *_ = unwrap_type(field.type)
            d = find_directive(typ.ast_node, 'preview')
            if d and 'toggledBy' in d:
                previews.add(d['toggledBy'])
        return {
            '__previews': previews,
        }


try:
    from gqlmod.helpers.urllib import UrllibJsonProvider
except ImportError:
    pass
else:
    class GitHubSyncProvider(GitHubBaseProvider, UrllibJsonProvider):
        def build_request(self, query, variables):
            qvars = variables.copy()
            qvars.pop('__previews')
            req = super().build_request(query, qvars)
            req.add_header('Accept', self._build_accept_header(variables))
            req.add_header('Authorization', self._build_authorization_header(variables))
            return req


try:
    from gqlmod.helpers.aiohttp import AiohttpProvider
except ImportError:
    pass
else:
    class GitHubAsyncProvider(GitHubBaseProvider, AiohttpProvider):
        use_json = True

        def modify_request_args(self, variables, kwargs):
            super().modify_request_args(kwargs)
            kwargs.setdefault('headers', {}).update({
                'Accept': self._build_accept_header(variables),
                'Authorization': self._build_authorization_header(variables)
            })
            kwargs['json'].pop('__previews')
