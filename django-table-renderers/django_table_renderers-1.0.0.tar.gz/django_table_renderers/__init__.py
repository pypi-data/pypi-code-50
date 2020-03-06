"""
:description: Simple renderers meant to convert tabular data into formats more
commonly used and understood by end users.
:license: AGPLv3+
:authors: Josh Marshall (joshua.r.marshall.1991 (at) gmail.com)
:copyright: Jackson Laboratory (2020)
"""
import pandas as pd

import tarfile
from io import BytesIO
from rest_framework import renderers


class MultiCSVRenderer(renderers.BaseRenderer):
    """
    :description: Take a dict of Column Major table representations and convert
    them into a set of .csv files in a .tgz archive.  This triggers when a
    "text/csv" request format comes in a HTTP header for endpoints enables with
    this renderer.

    The particular Column Major format used is {str: {str: []}}.
    """

    media_type = "application/tgz"
    format = "tgz"
    render_style = None
    charset = None

    def render(self, data: dict, media_type=None, renderer_context=None) -> bytes:
        """
        :description: Convert an unserialized response from an HTTP endpoint
        into a .tgz with a number of .csv files representing each table in the
        data.

        :note: This operates purely in memory as to not create temporary files.
        As a consequence, the memory used could be higher than expected, and at
        a maximum matches the memory used to represnt the input data.  This is
        unlikely to be a problem for most use cases.

        :returns: A bytes like object holding the contents of a .tgz
        """

        tared_experiments = BytesIO()
        with tarfile.open(mode="w:gz", fileobj=tared_experiments) as tar_obj:

            for experiment_name, experiment_data in data.items():
                file_info = tarfile.TarInfo(name=f"{experiment_name}.csv")
                file_content = BytesIO(
                    str.encode(
                        pd.DataFrame.from_dict(experiment_data).to_csv(index=False)
                    )
                )
                file_info.size = len(file_content.getbuffer())
                tar_obj.addfile(
                    file_info, fileobj=file_content,
                )

        return tared_experiments.getvalue()


class XLSXRenderer(renderers.BaseRenderer):
    """
    :description: Take a dict of Column Major table representations and convert
    them into a multi-sheet excell 2007+ (.xlsx) filee.  This triggers when a
    "application/xlsx" request format comes in a HTTP header for endpoints
    enables with this renderer.


    :note: This operates purely in memory as to not create temporary files.
    As a consequence, the memory used could be higher than expected, and at
    a maximum matches the memory used to represnt the input data.  This is
    unlikely to be a problem for most use cases.

    :returns: A bytes like object holding the contents of a .xlsx
    """

    media_type = "application/xlsx"
    format = "xlsx"
    render_style = None
    charset = None

    def render(self, data, media_type=None, renderer_context=None) -> bytes:

        output_stream = BytesIO()
        excel_obj = pd.ExcelWriter(output_stream, engine="xlsxwriter")

        for experiment_name, experiment_data in data.items():
            experiment_name = (
                experiment_name[0:30] if len(experiment_name) > 30 else experiment_name
            )
            pd.DataFrame.from_dict(experiment_data).to_excel(
                excel_obj, sheet_name=experiment_name
            )

        excel_obj.save()
        return output_stream.getvalue()
