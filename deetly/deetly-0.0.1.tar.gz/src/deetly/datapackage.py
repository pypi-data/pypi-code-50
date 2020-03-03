"""Datapackage class.

The class contains methods for building and publishing a datapackage.
"""
import datetime
import io
import json
from typing import Any, Dict, List

import pyarrow
import pandas as pd
import plotly.io as pio

import deetly.utils


class Datapackage:
    """Datapackage resource.

    Attributes:
        id: The id of the datapackage.
        name: The name of the datapackage.
    """

    def __init__(self, metadata: Dict) -> None:
        """Constructor."""
        self.resources: List = []
        self.views: List = []
        self.metadata: Dict = self._create_datapackage(dict(metadata))

    def _create_datapackage(self, metadata: Dict) -> Dict:
        """Create datapackage from metadata"""
        now = datetime.datetime.today().isoformat()
        metadata["version"] = metadata.get("version", "0.0.1")
        metadata["created"] = metadata.get("created", now)
        metadata["updated"] = now
        return metadata

    @property
    def id(self) -> str:
        """Datapackage id."""
        _id = self.metadata.get("id", deetly.utils.getIdFromMetadata(self.metadata))
        self.metadata["id"] = _id
        return _id

    @property
    def name(self) -> str:
        """Datapackage name."""
        return self.metadata.get("name", None)

    def plot(self, spec_type: str, spec: Dict, name: str, description: str) -> None:
        """Adds a plot/figure/view to the package.

        Creates a dict containg layout, data and metadata

        Args:
            spec_type: For example 'ploty', 'vega' or other type.
            spec: The JSON spec for the view.
            name: View name.
            description: Description of the view. Can be plain text or Markdown.
        """

        view = {
            "name": name.replace(" ", "_"),
            "description": description,
            "specType": spec_type,
            "spec": spec,
        }

        self.views.append(view)

    def plotly(self, fig: Dict, name: str, description: str) -> None:
        """Adds a plotly view to the package.

        Creates a dict containg layout, data and metadata

        Args:
            fig: The Plotly figure.
            name: View name.
            description: Description of the view. Can be plain text or Markdown.
        """

        self.plot("plotly", pio.to_json(fig), name, description)

    def vega(self, fig: Any, name: str, description: str) -> None:
        """Adds a Vega view to the package.

        Creates a dict containg layout, data and metadata

        Args:
            fig: The Vega chart.
            name: View name.
            description: Description of the view. Can be plain text or Markdown.
        """

        self.plot("vega", fig.to_dict(), name, description)

    def deck(self, fig: Any, name: str, description: str) -> None:
        """Adds a Deck view to the package.

        Creates a deck.gl view 

        Args:
            fig: The Deck chart.
            name: View name.
            description: Description of the view. Can be plain text or Markdown.
        """

        self.plot("deck", fig, name, description)

    def pydeck(self, fig: Any, name: str, description: str) -> None:
        """Adds a PyDeck view to the package.

        Creates a dpydeck view 

        Args:
            fig: The pydeck chart.
            name: View name.
            description: Description of the view. Can be plain text or Markdown.
        """

        self.plot("deck", json.loads(fig.to_json()), name, description)


    def barlist(self, fig: Any, name: str, description: str = "") -> None:
        """Adds a Barlist view to the package.

        Creates barlist view

        Args:
            fig: The specification.
            name: View name.
            description: Description of the view. Can be plain text or Markdown.
        """

        self.plot("barlist", fig, name, description)


    def data(self, df: pd.DataFrame, name: str, description: str = "") -> None:
        """Add a pandas dataframe to the package.

        Saves pandas dataframe to gzip'ed csv file.

        Args:
            df: The pandas dataframe
            name: The name of the datasett
            description: Description of the data. Can be plain text or Markdown

        Raises:
            TypeError: The first parameter (df) must be of type pandas.Dataframe().
        """

        if not isinstance(df, pd.DataFrame):
            raise TypeError(
                f"The first parameter df must be of type pandas.Dataframe()"
            )

        fields = []
        for name, dtype in zip(df.columns, df.dtypes):
            if str(dtype) == "object":
                dtype = "string"
            else:
                dtype = "number"
            fields.append({"name": name, "type": dtype})

        output = io.StringIO()
        df.to_csv(output, index=False)
        data = output.getvalue()
        output.close()

        resource = {
            "name": name,
            "description": description,
            "path": f"/resources/{name}.csv.gz",
            "format": "csv",
            "dsv_separator": ",",
            "mediatype": "text/csv",
            "schema": {"fields": fields},
            "data": data,
        }

        name = name.replace(" ", "_")
        self.resources.append(resource)

    def url(self, resource_url: str, description: str = "") -> None:
        """Add a downloadable dataresource to the package.

        Args:
            resource_url: The URL of the resource
            description: Description of the data. Can be plain text or Markdown
        """

        name = deetly.utils.get_name_from_url(resource_url)

        resource = {
            "name": name,
            "description": description,
            "path": resource_url,
        }

        name = name.replace(" ", "_")
        self.resources.append(resource)

    def publish(self, space: str, token: str) -> None:
        """Publishes the package to storage and the metadata to elastic seach.

        Args:
            space: The id of the space to publish to
            token: The users token
        """

        self.metadata["id"] = self.id
        self.metadata["views"] = self.views

        resources = []
        content = []
        # upload resources
        for resource in self.resources:
            public_url = deetly.utils.upload_file(
                space,
                token,
                self.id,
                f'resources/{resource["name"]}',
                resource["mediatype"],
                resource["data"],
            )

            _resource = {}
            for key, value in resource.items():
                if key not in ["data"]:
                    _resource[key] = value
   
            _resource['description'] = resource.get("description", ""),   
            _resource['type'] = 'dataset'
            _resource["url"] = json.loads(public_url).get("url","")
            resources.append(_resource)
            print(f'Dataset { resource["name"]}:  {_resource["url"] }','\n')

        for view in self.views:
            for key, value in view.items():
                if key == "name":
                    content.append(
                        {
                            "type": "view",
                            "name": value,
                            "description": view.get("description", ""),
                        }
                    )

        self.metadata["resources"] = resources
        self.metadata["content"] = content
        datapackage = json.dumps(self.metadata)
     
        # upload datapackage
        response = deetly.utils.upload_file(
            space, token, self.id, "datapackage.json", "application/json", datapackage,
        )
        datapackage_url = json.loads(response).get("url","")
        print(f'Datapackage: {datapackage_url}','\n')

        # extract metadata for elastic search
        metadata = {}
        for key, value in self.metadata.items():
            if key not in ["views"]:
                metadata[key] = value

        metadata["url"] = datapackage_url
        metadata["space"] = space

        res = json.loads(deetly.utils.index_document(token, space, metadata))
        body = res.get("body", None)

        if not body:
            print(f'Error updating metadata index: {res}','\n')

        result = body.get('result', None)

        if not result:
            print('\n', f'Error updating metadata index: {res}')

        print(f'Metadata index entry: {result}','\n')

        return metadata
