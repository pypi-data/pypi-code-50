import json
import logging
import typing
from typing import TYPE_CHECKING

import numpy as np
import progressbar
import requests

from kerasltisubmission.exceptions import (
    KerasLTISubmissionBadResponseException,
    KerasLTISubmissionConnectionFailedException,
    KerasLTISubmissionInvalidSubmissionException,
    KerasLTISubmissionNoInputException,
)

if TYPE_CHECKING:  # pragma: no cover
    from kerasltisubmission.kerasltisubmission import Submission  # noqa: F401

log = logging.getLogger("kerasltisubmission")
log.addHandler(logging.NullHandler())

AnyIDType = typing.Union[str, int]
InputsType = typing.List[typing.Dict[str, typing.Any]]
PredictionsType = typing.Dict[str, typing.Any]


class LTIProvider:
    def __init__(
        self,
        input_api_endpoint: str,
        submission_api_endpoint: str,
        user_token: AnyIDType,
    ) -> None:
        self.user_token = user_token
        self.input_api_endpoint = input_api_endpoint
        self.submission_api_endpoint = submission_api_endpoint

    def request_inputs(
        self, assignment_id: AnyIDType
    ) -> typing.Dict[str, PredictionsType]:
        try:
            r = requests.get(
                f"{self.input_api_endpoint}/assignment/{assignment_id}/inputs"
            )
            rr = r.json()
        except Exception as e:
            raise KerasLTISubmissionConnectionFailedException(
                self.submission_api_endpoint, e
            ) from None
        if r.status_code == 200 and rr.get("success", True) is True:
            inputs = rr.get("predict")
            log.debug(f"Received {len(inputs)} inputs")
            return dict(predict=inputs)
        else:
            raise KerasLTISubmissionBadResponseException(
                api_endpoint=self.input_api_endpoint,
                return_code=r.status_code,
                assignment_id=assignment_id,
                message=rr.get("error"),
            )

    def guess(self, assignment_id: AnyIDType, predictions: PredictionsType) -> None:
        log.debug(
            f"Submitting {len(predictions)} predictions to the provider for grading"
        )
        headers = {"content-type": "application/json"}
        if not len(predictions) > 0:
            raise KerasLTISubmissionInvalidSubmissionException(predictions)
        try:
            r = requests.post(
                self.submission_api_endpoint,
                data=json.dumps(
                    dict(
                        predictions=predictions,
                        user_token=self.user_token,
                        assignment_id=assignment_id,
                    )
                ),
                headers=headers,
            )
            rr = r.json()
        except Exception as e:
            raise KerasLTISubmissionConnectionFailedException(
                self.submission_api_endpoint, e
            ) from None
        if r.status_code == 200 and rr.get("success"):
            log.debug(
                f"Sent {len(predictions)} predictions to the provider for grading"
            )
            log.info(f"Successfully submitted assignment {assignment_id} for grading")
        else:
            raise KerasLTISubmissionBadResponseException(
                api_endpoint=self.submission_api_endpoint,
                return_code=r.status_code,
                assignment_id=assignment_id,
                message=rr.get("error"),
            )

    def submit(self, s: typing.Union["Submission", typing.List["Submission"]]) -> None:
        if isinstance(s, list):
            submissions = s
        else:
            submissions = [s]
        for sub in submissions:

            # Get assignment inputs and propagate errors
            inputs: PredictionsType = self.request_inputs(sub.assignment_id).get(
                "predict", dict()
            )
            if not len(inputs) > 0:
                raise KerasLTISubmissionNoInputException(
                    self.input_api_endpoint, sub.assignment_id
                )

            # Build prediction mapping
            predictions: PredictionsType = dict()
            for i in progressbar.progressbar(inputs, redirect_stdout=True):
                input_matrix = i.get("matrix")
                input_hash = i.get("hash")
                probabilities = sub.model.predict(
                    np.expand_dims(np.asarray(input_matrix), axis=0)
                )
                prediction = np.argmax(probabilities)
                predictions[input_hash] = int(prediction)

            self.guess(sub.assignment_id, predictions)
