from mloyalty.base import Mloyalty


class TestMloyalty:
    def test_get_connection(self):
        mloyalty = Mloyalty()
        res = mloyalty.get_connection()
        assert isinstance(res, object)

    def test_get_access_token(self):
        mloyalty = Mloyalty()
        resp = mloyalty.get_access_token()
        assert isinstance(resp, int)

    def test_refresh_token(self):
        mloyalty = Mloyalty()
        db = mloyalty.get_connection()
        data = db.get()
        resp = mloyalty.refresh_token(data['refresh_token'])
        assert isinstance(resp, int)

    def test_get_request_params(self):
        mloyalty = Mloyalty()
        res = mloyalty.get_request_params()
        assert isinstance(res, dict)
        assert res['operator_id']
        assert res['partner_id']
        assert res['pos_code']
        assert res['token']
