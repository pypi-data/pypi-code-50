from interactivity import ViewSubmissionHandler, ViewSubmissionPayload


class MyView(ViewSubmissionHandler):
    def execute(self):
        return


class TestViewSubmissionHandler:
    def test_state(self, view_submission_request_data):
        payload = ViewSubmissionPayload(**view_submission_request_data)
        handler = MyView(payload)
        assert handler.state == payload.view["state"]
