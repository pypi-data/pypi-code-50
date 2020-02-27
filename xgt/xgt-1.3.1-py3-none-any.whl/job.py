# -*- coding: utf-8 -*- --------------------------------------------------===#
#
#  Copyright 2018-2019 Trovares Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and 
#  limitations under the License.
#
#===----------------------------------------------------------------------===#

from datetime import datetime
import logging

from . import ErrorMessages_pb2 as err_proto
from . import JobService_pb2 as job_proto
from .common import (XgtError, _to_unicode, _to_str, _code_error_map)

log = logging.getLogger(__name__)

class Job(object):
  """
  Represents a user-scheduled Job.

  An instance of this object is created by job-scheduling functions like
  `xgt.Connection.run_job` and `xgt.Connection.schedule_job`.

  A `Job` is used as a proxy for a job in the server and allows the user
  to monitor its execution, possibly cancel it, and learn about its status
  during and after execution.

  """
  def __init__(self, conn, job_id):
    self._conn = conn
    self._id = job_id

  def _get_job_data(self):
    request = job_proto.GetJobsRequest()
    request.job_id.extend([self._id])
    response = self._conn.call(request, self._conn._job_svc.GetJobs)
    job = response.job_status[0]  # Retrieve only one job from the list.
    job_data = {
      'jobid': job.job_id,
      'status': job_proto.JobStatusEnum.Name(job.status).lower(),
      'start_time': job.start_time.ToDatetime().isoformat(),
      'end_time': job.end_time.ToDatetime().isoformat(),
      'error_type': None,
      'visited_edges': job.visited_edges }
    if job.error:
      if len(job.error) > 0:
        error_code_name = err_proto.ErrorCodeEnum.Name(job.error[0].code)
        job_data['error_type'] = _code_error_map[error_code_name]
        job_data['error'] = ', '.join([e.message for e in job.error])
        job_data['trace'] = ', '.join([e.detail for e in job.error])

    if log.getEffectiveLevel() >= logging.DEBUG:
      job_id = job_data['jobid']
      job_status = job_data['status']
      if 'error' in job_data:
        error = job_data['error']
      else:
        error = ''
      if 'trace' in job_data:
        trace = job_data['trace']
      else:
        trace = ''
      msg = u'Job: {0} Status: {1}'.format(_to_unicode(job_id),
                                          job_status)
      if error != '':
        msg = msg + "\nError: \n" + error
      if trace != '':
        msg = msg + "\nTrace: \n" + trace
      log.debug(msg)

    return job_data

  @property
  def id(self):
    """
    int: Identifier of the job.

    A 64-bit integer value that uniquely identifies a job. It is
    automatically incremented for each scheduled job over the lifetime of
    the `xgtd` server process.

    """
    return self._id

  @property
  def status(self):
    """
    str: Status of the job.

        ============  ===============================================
        Job status
        -------------------------------------------------------------
           Status                       Description
        ============  ===============================================
           scheduled  The state after the job has been created, but
                      before it has started running.
             running  The job is being executed.
           completed  The job finished successfully.
            canceled  The job was canceled.
              failed  The job failed. When the job fails the `error`
                      and `trace` properties are populated.
            rollback  The job had a transactional conflict with
                      another job and was rolled back.
        ============  ===============================================

    """
    data = self._get_job_data()
    if 'status' in data:
      return _to_unicode(data['status'])
    else:
      return ''

  @property
  def start_time(self):
    """
    str: Date and time when the job was scheduled.

    This is a formatted string that has a resolution of seconds.
    """
    data = self._get_job_data()
    if 'start_time' in data:
      return datetime.strptime(data['start_time'], '%Y-%m-%dT%H:%M:%S')
    else:
      return ''

  @property
  def end_time(self):
    """
    str: Date and time when the job finished running.

    This is a formatted string that has a resolution of seconds.
    """
    data = self._get_job_data()
    if 'end_time' in data:
      return datetime.strptime(data['end_time'], '%Y-%m-%dT%H:%M:%S')
    else:
      return ''

  @property
  def visited_edges(self):
    """
    int: A 64-bit integer giving the number of edges visited during the job.

    If the configuration variable stats.job_stats is not set to true, then the
    value returned is always 0.
    """
    return self._get_job_data()['visited_edges']

  @property
  def error_type(self):
    """
    object: Class that belongs to the XgtError hierarchy that corresponds to
            the original exception type thrown and caused the Job to fail.
    """
    data = self._get_job_data()
    if 'error_type' in data:
      return data['error_type']
    else:
      return XgtError

  @property
  def error(self):
    """
    str: User-friendly error message describing the reason a job failed.
    """
    data = self._get_job_data()
    if 'error' in data:
      return _to_unicode(data['error'])
    else:
      return ''

  @property
  def trace(self):
    """
    str: Very detailed error message for a failed job.

    This error message contains the friendly error message and a stack
    strace for the code that participated in the error.
    """
    data = self._get_job_data()
    if 'trace' in data:
      return _to_unicode(data['trace'])
    else:
      return ''

  def __str__(self):
    txt = (u'id:{0}, status:{1}').format(self.id, self.status)
    if len(self.error) > 0:
      txt = txt + (u', nerror:{0}').format(self.error)
    return _to_str(txt)

