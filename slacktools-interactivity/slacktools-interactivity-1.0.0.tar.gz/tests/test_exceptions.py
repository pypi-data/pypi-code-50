from interactivity import InteractivityError


class TestInteractivityError:
    def test(self):
        e = InteractivityError("message")
        assert e.message == "message"
