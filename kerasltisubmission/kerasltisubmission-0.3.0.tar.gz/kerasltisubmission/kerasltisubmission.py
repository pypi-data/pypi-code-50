# -*- coding: utf-8 -*-

"""Main module."""

from typing import TYPE_CHECKING

import kerasltisubmission.provider as provider

if TYPE_CHECKING:  # pragma: no cover
    import keras.models


class Submission:
    def __init__(
        self, assignment_id: provider.AnyIDType, model: "keras.models.Model"
    ) -> None:
        self.assignment_id = assignment_id
        self.model = model

    def submit(self, server: provider.LTIProvider) -> None:
        # Convenience method, it is preferred to use the server interface in the first place
        server.submit(self)
