import mloyalty
from datetime import date


class TestOperator:
    def test_get_user_info(self):
        operator = mloyalty.Operator()
        resp = operator.get_user_info()
        assert isinstance(resp, dict)

    def test_get_gain_operator_period(self):
        operator = mloyalty.Operator()
        resp = operator.get_gain_operator_period(date(2020, 1, 1), date.today())
        assert isinstance(resp, dict)
