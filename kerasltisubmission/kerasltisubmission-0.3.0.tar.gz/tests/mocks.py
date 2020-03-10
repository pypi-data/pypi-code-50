import typing

import numpy as np

JSONType = typing.Dict[str, typing.Any]


class MockRequestsResponse:
    def __init__(self, json_data: JSONType, status_code: int) -> None:
        self.json_data = json_data
        self.status_code = status_code

    def json(self) -> JSONType:
        return self.json_data


class MockKerasModel:
    def __init__(self, prediction: np.ndarray) -> None:
        self.prediction = prediction

    def predict(self, _: np.ndarray) -> np.ndarray:
        return self.prediction
