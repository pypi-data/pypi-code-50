import json
import traceback
from typing import Any

from podder_task_base import Context, settings
from podder_task_base.log import logger


@logger.class_logger
class TaskApiExecutor(object):
    def __init__(self, execution_task, gprc_pb2):
        self.execution_task = execution_task
        self.gprc_pb2 = gprc_pb2

    def execute(self, request: Any, _context: Any):
        settings.init()
        dag_id = request.dag_id
        context = Context(dag_id)

        inputs = []
        try:
            inputs = self._convert_to_input_data(request)
            outputs = self.execution_task(context).execute(inputs)
            task_response = self._convert_to_task_response(dag_id, outputs)
        except Exception as e:
            self.logger.error(traceback.format_exc())
            outputs = self._add_error_to_outputs(inputs, e)
            task_response = self._convert_to_task_response(dag_id, outputs)

        return task_response

    @staticmethod
    def _convert_to_input_data(request: dict) -> list:
        inputs = []
        for result in request.results:
            inputs.append({'job_id': result.job_id, 'job_data': json.loads(result.job_data)})
        return inputs

    def _convert_to_task_response(self, dag_id: str, outputs: list) -> Any:
        task_response = self.gprc_pb2.TaskResponse()
        task_response.dag_id = dag_id

        for output in outputs:
            task_response.results.add(job_id=output['job_id'],
                                      job_data=json.dumps(output['job_data']))
        return task_response

    def _add_error_to_outputs(self, outputs: list, error: Exception) -> list:
        error_params = {
            'has_error': True,
            'error_at': self.execution_task.TASK_NAME,
            'error_code': self.execution_task.ERROR_CODE_INTERNAL_SERVER_ERROR,
            'error_class': type(error).__name__,
            'error_message': str(error)
        }
        for output in outputs:
            output['job_data']['params']['metadata'] = {
                **output['job_data']['params'].get('metadata', {}),
                **error_params
            }
        return outputs
