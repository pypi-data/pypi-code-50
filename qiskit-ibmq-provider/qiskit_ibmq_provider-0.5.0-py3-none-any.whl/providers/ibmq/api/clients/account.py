# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Client for accessing an individual IBM Quantum Experience account."""

import asyncio
import logging
import time
from collections import deque

from typing import List, Dict, Any, Optional
# Disabled unused-import because datetime is used only for type hints.
from datetime import datetime  # pylint: disable=unused-import

from qiskit.providers.ibmq.apiconstants import (API_JOB_FINAL_STATES, ApiJobStatus,
                                                ApiJobShareLevel)

from ..exceptions import (RequestsApiError, WebsocketError,
                          WebsocketTimeoutError, UserTimeoutExceededError)
from ..rest import Api
from ..session import RetrySession
from ..exceptions import ApiIBMQProtocolError
from .base import BaseClient
from .websocket import WebsocketClient

logger = logging.getLogger(__name__)


class AccountClient(BaseClient):
    """Client for accessing an individual IBM Quantum Experience account."""

    def __init__(
            self,
            access_token: str,
            project_url: str,
            websockets_url: str,
            use_websockets: bool,
            **request_kwargs: Any
    ) -> None:
        """AccountClient constructor.

        Args:
            access_token: IBM Quantum Experience access token.
            project_url: IBM Quantum Experience URL for a specific hub/group/project.
            websockets_url: URL for the websockets server.
            use_websockets: Whether to use webscokets.
            **request_kwargs: Arguments for the request ``Session``.
        """
        self.client_api = Api(RetrySession(project_url, access_token,
                                           **request_kwargs))
        self.client_ws = WebsocketClient(websockets_url, access_token)
        self._use_websockets = use_websockets

    # Backend-related public functions.

    def list_backends(self, timeout: Optional[float] = None) -> List[Dict[str, Any]]:
        """Return backends available for this provider.

        Args:
            timeout: Number of seconds to wait for the request.

        Returns:
            Backends available for this provider.
        """
        return self.client_api.backends(timeout=timeout)

    def backend_status(self, backend_name: str) -> Dict[str, Any]:
        """Return the status of the backend.

        Args:
            backend_name: The name of the backend.

        Returns:
            Backend status.
        """
        return self.client_api.backend(backend_name).status()

    def backend_properties(
            self,
            backend_name: str,
            datetime: Optional[datetime] = None
    ) -> Dict[str, Any]:
        """Return the properties of the backend.

        Args:
            backend_name: The name of the backend.
            datetime: Date and time for additional filtering of backend properties.

        Returns:
            Backend properties.
        """
        # pylint: disable=redefined-outer-name
        return self.client_api.backend(backend_name).properties(datetime=datetime)

    def backend_pulse_defaults(self, backend_name: str) -> Dict:
        """Return the pulse defaults of the backend.

        Args:
            backend_name: The name of the backend.

        Returns:
            Backend pulse defaults.
        """
        return self.client_api.backend(backend_name).pulse_defaults()

    def backend_job_limit(self, backend_name: str) -> Dict[str, Any]:
        """Return the job limit for the backend.

        Args:
            backend_name: The name of the backend.

        Returns:
            Backend job limit.
        """
        return self.client_api.backend(backend_name).job_limit()

    # Jobs-related public functions.

    def list_jobs_statuses(
            self,
            limit: int = 10,
            skip: int = 0,
            extra_filter: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Return a list of job data, with filtering and pagination.

        In order to reduce the amount of data transferred, the server only
        sends back a subset of the total information for each job.

        Args:
            limit: Maximum number of items to return.
            skip: Offset for the items to return.
            extra_filter: Additional filtering passed to the query.

        Returns:
            A list of job data.
        """
        return self.client_api.jobs(limit=limit, skip=skip,
                                    extra_filter=extra_filter)

    def job_submit(
            self,
            backend_name: str,
            qobj_dict: Dict[str, Any],
            use_object_storage: bool,
            job_name: Optional[str] = None,
            job_share_level: Optional[ApiJobShareLevel] = None,
            job_tags: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Submit a ``Qobj`` to the backend.

        Args:
            backend_name: The name of the backend.
            qobj_dict: The ``Qobj`` to be executed, as a dictionary.
            use_object_storage: ``True`` if object storage should be used.
            job_name: Custom name to be assigned to the job.
            job_share_level: Level the job should be shared at.
            job_tags: Tags to be assigned to the job.

        Returns:
            Job data.
        """
        submit_info = None
        if use_object_storage:
            # Attempt to use object storage.
            try:
                submit_info = self._job_submit_object_storage(
                    backend_name=backend_name,
                    qobj_dict=qobj_dict,
                    job_name=job_name,
                    job_share_level=job_share_level,
                    job_tags=job_tags)
            except Exception as ex:  # pylint: disable=broad-except
                # Fall back to submitting the Qobj via POST if object storage
                # failed.
                logger.info('Submitting the job via object storage failed: '
                            'retrying via regular POST upload: %s',
                            str(ex))
                logger.debug('Submitting via object storage extra info:',
                             exc_info=True)

        if not submit_info:
            # Submit Qobj via HTTP.
            submit_info = self._job_submit_post(
                backend_name=backend_name,
                qobj_dict=qobj_dict,
                job_name=job_name,
                job_share_level=job_share_level,
                job_tags=job_tags)

        return submit_info

    def _job_submit_post(
            self,
            backend_name: str,
            qobj_dict: Dict[str, Any],
            job_name: Optional[str] = None,
            job_share_level: Optional[ApiJobShareLevel] = None,
            job_tags: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Submit a ``Qobj`` to the backend using ``HTTP POST``.

        Args:
            backend_name: The name of the backend.
            qobj_dict: The ``Qobj`` to be executed, as a dictionary.
            job_name: Custom name to be assigned to the job.
            job_share_level: Level the job should be shared at.
            job_tags: Tags to be assigned to the job.

        Returns:
            Job data.
        """
        # Check for the job share level.
        _job_share_level = job_share_level.value if job_share_level else None

        return self.client_api.job_submit(
            backend_name,
            qobj_dict,
            job_name,
            job_share_level=_job_share_level,
            job_tags=job_tags)

    def _job_submit_object_storage(
            self,
            backend_name: str,
            qobj_dict: Dict[str, Any],
            job_name: Optional[str] = None,
            job_share_level: Optional[ApiJobShareLevel] = None,
            job_tags: Optional[List[str]] = None
    ) -> Dict:
        """Submit a ``Qobj`` to the backend using object storage.

        Args:
            backend_name: The name of the backend.
            qobj_dict: The ``Qobj`` to be executed, as a dictionary.
            job_name: Custom name to be assigned to the job.
            job_share_level: Level the job should be shared at.
            job_tags: Tags to be assigned to the job.

        Returns:
            Job data.
        """
        # Check for the job share level.
        _job_share_level = job_share_level.value if job_share_level else None

        # Get the job via object storage.
        job_info = self.client_api.submit_job_object_storage(
            backend_name,
            job_name=job_name,
            job_share_level=_job_share_level,
            job_tags=job_tags)

        # Get the upload URL.
        job_id = job_info['id']
        job_api = self.client_api.job(job_id)
        upload_url = job_api.upload_url()['url']

        # Upload the Qobj to object storage.
        _ = job_api.put_object_storage(upload_url, qobj_dict)

        # Notify the API via the callback.
        response = job_api.callback_upload()

        return response['job']

    def job_download_qobj(self, job_id: str, use_object_storage: bool) -> Dict:
        """Retrieve and return a ``Qobj``.

        Args:
            job_id: The ID of the job.
            use_object_storage: ``True`` if object storage should be used.

        Returns:
            ``Qobj`` in dictionary form.
        """
        if use_object_storage:
            return self._job_download_qobj_object_storage(job_id)
        else:
            return self.job_get(job_id).get('qObject', {})

    def _job_download_qobj_object_storage(self, job_id: str) -> Dict:
        """Retrieve and return a ``Qobj`` using object storage.

        Args:
            job_id: The ID of the job.

        Returns:
            ``Qobj`` in dictionary form.
        """
        job_api = self.client_api.job(job_id)

        # Get the download URL.
        download_url = job_api.download_url()['url']

        # Download the result from object storage.
        return job_api.get_object_storage(download_url)

    def job_result(self, job_id: str, use_object_storage: bool) -> Dict:
        """Retrieve and return the job result.

        Args:
            job_id: The ID of the job.
            use_object_storage: ``True`` if object storage should be used.

        Returns:
            Job result.

        Raises:
            ApiIBMQProtocolError: If unexpected data is received from the server.
        """
        if use_object_storage:
            return self._job_result_object_storage(job_id)

        try:
            return self.job_get(job_id)['qObjectResult']
        except KeyError as err:
            raise ApiIBMQProtocolError(str(err))

    def _job_result_object_storage(self, job_id: str) -> Dict:
        """Retrieve and return the job result using object storage.

        Args:
            job_id: The ID of the job.

        Returns:
            Job result.
        """
        job_api = self.client_api.job(job_id)

        # Get the download URL.
        download_url = job_api.result_url()['url']

        # Download the result from object storage.
        result_response = job_api.get_object_storage(download_url)

        # Notify the API via the callback
        try:
            _ = job_api.callback_download()
        except (RequestsApiError, ValueError) as ex:
            logger.warning("An error occurred while sending download completion acknowledgement: "
                           "%s", ex)
        return result_response

    def job_get(
            self,
            job_id: str
    ) -> Dict[str, Any]:
        """Return information about the job.

        Args:
            job_id: The ID of the job.

        Returns:
            Job information.
        """
        return self.client_api.job(job_id).get()

    def job_status(self, job_id: str) -> Dict[str, Any]:
        """Return the status of the job.

        Args:
            job_id: The ID of the job.

        Returns:
            Job status.

        Raises:
            ApiIBMQProtocolError: If unexpected data is received from the server.
        """
        return self.client_api.job(job_id).status()

    def job_final_status(
            self,
            job_id: str,
            timeout: Optional[float] = None,
            wait: float = 5,
            status_deque: Optional[deque] = None
    ) -> Dict[str, Any]:
        """Wait until the job progresses to a final state.

        Args:
            job_id: The ID of the job.
            timeout: Time to wait for job, in seconds. If ``None``, wait indefinitely.
            wait: Seconds between queries.
            status_deque: Deque used to share the latest status.

        Returns:
            Job status.

        Raises:
            UserTimeoutExceededError: If the job does not return results
                before the specified timeout.
            ApiIBMQProtocolError: If unexpected data is received from the server.
        """
        status_response = None
        # Attempt to use websocket if available.
        if self._use_websockets:
            start_time = time.time()
            try:
                status_response = self._job_final_status_websocket(
                    job_id=job_id, timeout=timeout, status_deque=status_deque)
            except WebsocketTimeoutError as ex:
                logger.info('Timeout checking job status using websocket, '
                            'retrying using HTTP: %s', ex)
            except (RuntimeError, WebsocketError) as ex:
                logger.info('Error checking job status using websocket, '
                            'retrying using HTTP: %s', ex)

            # Adjust timeout for HTTP retry.
            if timeout is not None:
                timeout -= (time.time() - start_time)

        if not status_response:
            # Use traditional http requests if websocket not available or failed.
            status_response = self._job_final_status_polling(
                job_id, timeout, wait, status_deque)

        return status_response

    def _job_final_status_websocket(
            self,
            job_id: str,
            timeout: Optional[float] = None,
            status_deque: Optional[deque] = None
    ) -> Dict[str, Any]:
        """Return the final status of the job via websocket.

        Args:
            job_id: The ID of the job.
            timeout: Time to wait for job, in seconds. If ``None``, wait indefinitely.
            status_deque: Deque used to share the latest status.

        Returns:
            Job status.

        Raises:
            RuntimeError: If an unexpected error occurred while getting the event loop.
            WebsocketError: If the websocket connection ended unexpectedly.
            WebsocketTimeoutError: If the timeout has been reached.
        """
        # As mentioned in `websocket.py`, in jupyter we need to use
        # `nest_asyncio` to allow nested event loops.
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError as ex:
            # Event loop may not be set in a child thread.
            if 'There is no current event loop' in str(ex):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            else:
                raise
        return loop.run_until_complete(
            self.client_ws.get_job_status(job_id, timeout=timeout, status_deque=status_deque))

    def _job_final_status_polling(
            self,
            job_id: str,
            timeout: Optional[float] = None,
            wait: float = 5,
            status_deque: Optional[deque] = None
    ) -> Dict[str, Any]:
        """Return the final status of the job via polling.

        Args:
            job_id: The ID of the job.
            timeout: Time to wait for job, in seconds. If ``None``, wait indefinitely.
            wait: Seconds between queries.
            status_deque: Deque used to share the latest status.

        Returns:
            Job status.

        Raises:
            UserTimeoutExceededError: If the user specified timeout has been exceeded.
        """
        start_time = time.time()
        status_response = self.job_status(job_id)
        while ApiJobStatus(status_response['status']) not in API_JOB_FINAL_STATES:
            # Share the new status.
            if status_deque is not None:
                status_deque.append(status_response)

            elapsed_time = time.time() - start_time
            if timeout is not None and elapsed_time >= timeout:
                raise UserTimeoutExceededError(
                    'Timeout while waiting for job {}'.format(job_id))

            logger.info('API job status = %s (%d seconds)',
                        status_response['status'], elapsed_time)
            time.sleep(wait)
            status_response = self.job_status(job_id)

        return status_response

    def job_properties(self, job_id: str) -> Dict:
        """Return the backend properties of the job.

        Args:
            job_id: The ID of the job.

        Returns:
            Backend properties.
        """
        return self.client_api.job(job_id).properties()

    def job_cancel(self, job_id: str) -> Dict[str, Any]:
        """Submit a request for cancelling the job.

        Args:
            job_id: The ID of the job.

        Returns:
            Job cancellation response.
        """
        return self.client_api.job(job_id).cancel()
