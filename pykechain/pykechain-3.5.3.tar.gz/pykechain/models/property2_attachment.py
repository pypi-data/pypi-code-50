import io
import json
import os

import requests
from six import string_types, text_type
from typing import Text, Any, Optional

from pykechain.exceptions import APIError
from pykechain.models.property2 import Property2


class AttachmentProperty2(Property2):
    """
    A virtual object representing a KE-chain attachment property.

    :ivar type: The property type of the property. One of the types described in :class:`pykechain.enums.PropertyType`
    :type type: str
    :ivar output: a boolean if the value is configured as an output (in an activity)
    :type output: bool
    :ivar part: The (parent) part in which this property is available
    :type part: :class:`Part`
    :ivar value: the property value, can be set as well as property
    :type value: Any
    :ivar filename: the filename and extension of the attachment
    :type filename: str or None
    :ivar validators: the list of validators that are available in the property
    :type validators: list(PropertyValidator)
    :ivar is_valid: if the property conforms to the validators
    :type is_valid: bool
    :ivar is_invalid: if the property does not conform to the validator
    :type is_invalid: bool
    """

    @property
    def value(self):
        """Retrieve the data value of this attachment.

        Will show the filename of the attachment if there is an attachment available otherwise None
        Use save_as in order to download as a file.

        Example
        -------
        >>> file_attachment_property = project.part('Bike').property('file_attachment')
        >>> if file_attachment_property.value:
        ...     file_attachment_property.save_as('file.ext')
        ... else:
        ...     print('file attachment not set, its value is None')

        """
        if self.has_value():
            return "[Attachment: {}]".format(self.filename)
        else:
            return None

    @value.setter
    def value(self, value):
        if value is None:
            self.clear()
        else:
            self.upload(data=value)

    def clear(self) -> None:
        """Clear the attachment from the attachment field.

        :raises APIError: if unable to remove the attachment
        """
        if self._put_value(None) is None:
            self._value = None
            self._json_data['value'] = None

    @property
    def filename(self) -> Optional[Text]:
        """Filename of the attachment, without the full 'attachment' path."""
        return self._value.split('/')[-1] if self.has_value() else None

    def json_load(self):
        """Download the data from the attachment and deserialise the contained json.

        :return: deserialised json data as :class:`dict`
        :raises APIError: When unable to retrieve the json from KE-chain
        :raises JSONDecodeError: When there was a problem in deserialising the json

        Example
        -------
        Ensure that the attachment is valid json data

        >>> json_attachment = project.part('Bike').property('json_attachment')
        >>> deserialised_json = json_attachment.json_load()

        """
        return self._download().json()

    def upload(self, data: Text, **kwargs: Any) -> None:
        """Upload a file to the attachment property.

        When providing a :class:`matplotlib.figure.Figure` object as data, the figure is uploaded as PNG.
        For this, `matplotlib`_ should be installed.

        :param data: File path
        :type data: basestring
        :raises APIError: When unable to upload the file to KE-chain
        :raises OSError: When the path to the file is incorrect or file could not be found

        .. _matplotlib: https://matplotlib.org/
        """
        try:
            import matplotlib.figure

            if isinstance(data, matplotlib.figure.Figure):
                self._upload_plot(data, **kwargs)
                return
        except ImportError:
            pass

        if isinstance(data, (string_types, text_type)):
            with open(data, 'rb') as fp:
                self._upload(fp)
        else:
            self._upload_json(data, **kwargs)
        self._value = data

    def save_as(self, filename: Optional[Text] = None) -> None:
        """Download the attachment to a file.

        :param filename: (optional) File path. If not provided, will be saved to current working dir
                         with `self.filename`.
        :type filename: basestring or None
        :raises APIError: When unable to download the data
        :raises OSError: When unable to save the data to disk
        """
        filename = filename or os.path.join(os.getcwd(), self.filename)

        with open(filename, 'w+b') as f:
            for chunk in self._download():
                f.write(chunk)

    def _upload_json(self, content, name='data.json'):
        data = (name, json.dumps(content), 'application/json')

        self._upload(data)

    def _upload_plot(self, figure, name='plot.png'):
        buffer = io.BytesIO()

        figure.savefig(buffer, format="png")

        data = (name, buffer.getvalue(), 'image/png')

        self._upload(data)
        self._value = name

    # custom for PIM2
    def _download(self):
        url = self._client._build_url('property2_download', property_id=self.id)

        response = self._client._request('GET', url)

        if response.status_code != requests.codes.ok:
            raise APIError("Could not download property value")

        return response

    # custom for PIM2
    def _upload(self, data):
        url = self._client._build_url('property2_upload', property_id=self.id)

        response = self._client._request('POST', url,
                                         data={"part": self._json_data['part_id']},
                                         files={"attachment": data})

        if response.status_code != requests.codes.ok:
            raise APIError("Could not upload attachment: {}".format(response.content))
