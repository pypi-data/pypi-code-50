# Copyright (C) 2018-2020  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

from typing import List, Tuple, Any, Dict, Union

import re
import click
import logging

from swh.indexer.indexer import OriginIndexer


class OriginHeadIndexer(OriginIndexer):
    """Origin-level indexer.

    This indexer is in charge of looking up the revision that acts as the
    "head" of an origin.

    In git, this is usually the commit pointed to by the 'master' branch."""

    USE_TOOLS = False

    def persist_index_computations(
        self, results: Any, policy_update: str
    ) -> None:
        """Do nothing. The indexer's results are not persistent, they
        should only be piped to another indexer."""
        pass

    # Dispatch

    def index(self, origin_url):
        latest_visit = self.storage.origin_visit_get_latest(
            origin_url, allowed_statuses=['full'], require_snapshot=True)
        if latest_visit is None:
            return None
        latest_snapshot = self.storage.snapshot_get(latest_visit['snapshot'])
        method = getattr(
            self, '_try_get_%s_head' % latest_visit['type'],
            self._try_get_head_generic)

        rev_id = method(latest_snapshot)
        if rev_id is not None:
            return {
                'origin_url': origin_url,
                'revision_id': rev_id,
                }

        # could not find a head revision
        return None

    # Tarballs

    _archive_filename_re = re.compile(
            rb'^'
            rb'(?P<pkgname>.*)[-_]'
            rb'(?P<version>[0-9]+(\.[0-9])*)'
            rb'(?P<preversion>[-+][a-zA-Z0-9.~]+?)?'
            rb'(?P<extension>(\.[a-zA-Z0-9]+)+)'
            rb'$')

    @classmethod
    def _parse_version(
        cls: Any, filename: str
    ) -> Tuple[Union[float, int], ...]:
        """Extracts the release version from an archive filename,
        to get an ordering whose maximum is likely to be the last
        version of the software

        >>> OriginHeadIndexer._parse_version(b'foo')
        (-inf,)
        >>> OriginHeadIndexer._parse_version(b'foo.tar.gz')
        (-inf,)
        >>> OriginHeadIndexer._parse_version(b'gnu-hello-0.0.1.tar.gz')
        (0, 0, 1, 0)
        >>> OriginHeadIndexer._parse_version(b'gnu-hello-0.0.1-beta2.tar.gz')
        (0, 0, 1, -1, 'beta2')
        >>> OriginHeadIndexer._parse_version(b'gnu-hello-0.0.1+foobar.tar.gz')
        (0, 0, 1, 1, 'foobar')
        """
        res = cls._archive_filename_re.match(filename)
        if res is None:
            return (float('-infinity'),)
        version = [int(n) for n in res.group('version').decode().split('.')]
        if res.group('preversion') is None:
            version.append(0)
        else:
            preversion = res.group('preversion').decode()
            if preversion.startswith('-'):
                version.append(-1)
                version.append(preversion[1:])
            elif preversion.startswith('+'):
                version.append(1)
                version.append(preversion[1:])
            else:
                assert False, res.group('preversion')
        return tuple(version)

    def _try_get_ftp_head(self, snapshot: Dict[str, Any]) -> Any:
        archive_names = list(snapshot['branches'])
        max_archive_name = max(archive_names, key=self._parse_version)
        r = self._try_resolve_target(snapshot['branches'], max_archive_name)
        return r

    # Generic

    def _try_get_head_generic(
        self, snapshot: Dict[str, Any]
    ) -> Any:
        # Works on 'deposit', 'pypi', and VCSs.
        try:
            branches = snapshot['branches']
        except KeyError:
            return None
        else:
            return (
                    self._try_resolve_target(branches, b'HEAD') or
                    self._try_resolve_target(branches, b'master')
                    )

    def _try_resolve_target(self, branches: Dict, target_name: bytes) -> Any:
        try:
            target = branches[target_name]
            if target is None:
                return None
            while target['target_type'] == 'alias':
                target = branches[target['target']]
                if target is None:
                    return None

            if target['target_type'] == 'revision':
                return target['target']
            elif target['target_type'] == 'content':
                return None  # TODO
            elif target['target_type'] == 'directory':
                return None  # TODO
            elif target['target_type'] == 'release':
                return None  # TODO
            else:
                assert False
        except KeyError:
            return None


@click.command()
@click.option('--origins', '-i',
              help='Origins to lookup, in the "type+url" format',
              multiple=True)
def main(origins: List[str]) -> None:
    rev_metadata_indexer = OriginHeadIndexer()
    rev_metadata_indexer.run(origins)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
