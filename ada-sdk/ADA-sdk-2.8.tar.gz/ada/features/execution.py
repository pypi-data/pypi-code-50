from ada.base import BaseADA


class Execution(BaseADA):
    url = "execution/"

    def create(self, test_suite, project_id, total_test_cases=None, parent=None, **kwargs):
        data = {
            'test_suite': test_suite,
            'project_id': project_id,
            'total_test_cases': total_test_cases or 0,
            "parent": parent
        }
        data.update(kwargs)
        return super(Execution, self).create(data)

    def up_log(self, execution_id, **kwargs):
        url = "{}{}".format(self.url, execution_id)
        reps = self.send_request(url, data=kwargs, method="PATCH")
        return reps
