import mloyalty


class TestCheque:
    def test_get_cheques(self):
        cheque = mloyalty.Cheque()
        resp = cheque.get_cheques(233458, 1, 5)
        assert isinstance(resp, dict)

    def test_get_cheque_detail(self):
        cheque = mloyalty.Cheque()
        resp = cheque.get_cheque_detail(1)
        assert isinstance(resp, dict)
