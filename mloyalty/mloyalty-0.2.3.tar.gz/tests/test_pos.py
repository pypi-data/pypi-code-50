import mloyalty


class TestPOS:
    def test_get_poses(self):
        pos = mloyalty.POS()
        resp = pos.get_poses()
        assert isinstance(resp, dict)
