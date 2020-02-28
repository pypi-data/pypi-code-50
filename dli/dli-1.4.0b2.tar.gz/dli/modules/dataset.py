import textwrap
import warnings
import urllib
from collections import OrderedDict
from typing import Dict

from dli.models.paginator import Paginator
from dli.client.components.urls import search_urls, dataset_urls
from dli.models.dataset import DatasetModel


class DatasetModule:

    def __call__(self, search_term=None, only_mine=True) \
            -> Dict[str, DatasetModel]:
        """
        See datasets.

        :param str search_term: The search phrase to search the catalogue
        with, and to pull back datasets based on name, description etc.

        :param bool only_mine: Specify whether to collect datasets only
        accessible to you (True) or to discover packages that you may
        want to discover but may not have access to (False).

        If any combination of the two, then search term takes precedence
        of routing, followed by the application of only_mine flag.

        :returns: Ordered dictionary of ids to DatasetModel.
        :rtype: OrderedDict[id: str, DatasetModel]
        """
        query = {}
        if search_term:
            query['query'] = search_term

        p = Paginator(
            # Maybe refactor out into a DatasetPaginator
            search_urls.search_datasets + '?' + urllib.parse.urlencode(query),
            self._client.Dataset,
            self._client.Dataset._from_v1_response_to_v2,
            max_workers=5
        )

        warning_message = \
            textwrap.dedent("""
            Warning! There are duplicate short codes for
            datasets. The short code in the dictionary of dataset we are now 
            returning will refer to only one of the datasets. 
            If you are running in the production or UAT environments then
            please report the problem to the datalake 
            platform team at DataLake-Support_L1@ihsmarkit.com. 
            Please include this full warning message:
            """)

        if only_mine:
            len_before_filtering = len([v for v in p])
            count_has_access_unknown = len(
                [v for v in p if not isinstance(v.has_access, bool)])
            count_has_access_false = len([
                v for v in p if
                isinstance(v.has_access, bool) and not v.has_access
            ])
            count_has_access_true = len([
                v for v in p if
                isinstance(v.has_access, bool) and v.has_access
            ])

            o = OrderedDict([
                # Hack until better filtering
                (v.short_code, v) for v in p
                if isinstance(v.has_access, bool) and v.has_access
            ])

            len_after_dedup = len(o)

            if count_has_access_true != len_after_dedup:
                warnings.warn(
                    textwrap.dedent(f"""{warning_message}
                    \nLength before filtering '{len_before_filtering}',
                    \ncount has access unknown '{count_has_access_unknown}',
                    \ncount has access false '{count_has_access_false}',
                    \ncount has access true '{count_has_access_true}',
                    \nlength of de-duplicated dict '{len_after_dedup}',
                    \ndifference after de-duplicating 
                    '{count_has_access_true - len_after_dedup}'"""),
                    RuntimeWarning
                )

            return o
        else:
            len_before_dedup = len([v for v in p])

            o = OrderedDict([
                (v.short_code, v) for v in p
            ])

            len_after_dedup = len(o)

            if len_before_dedup != len_after_dedup:
                warnings.warn(
                    textwrap.dedent(f"""{warning_message}
                    \nlength before de-duplicating '{len_before_dedup}',
                    \nlength after de-duplicating '{len_after_dedup}',
                    \ndifference after de-duplicating
                    '{len_before_dedup - len_after_dedup}'"""),
                    RuntimeWarning
                )

            return o

    def _get(self, short_code) -> DatasetModel:
        """
        Returns a DatasetModel if it exists else None

        :param str short_code: The short code of the dataset to collect

        :returns: Dataset model with matching short code.
        :rtype: DatasetModel
        """
        warnings.warn(
            'Getting a dataset byname, and package name or package ID'
            'will be deprecated in future. Short-codes will replace this.',
            PendingDeprecationWarning
        )
        params = {}

        # todo this should be by short code but EP doesnt seem to exist for this yet
        # so pass d_id
        params["dataset_id"] = short_code
        response = self._client.session.get(
            dataset_urls.v2_instance.format(id=short_code)
        )
        return self._client.Dataset._from_v2_response(response.json())
