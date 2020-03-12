import pytest

from viresclient import SwarmRequest


# def test_available():
#     request = SwarmRequest()
#     request.available_collections()
#     request.available_measurements()
#     request.available_auxiliaries()


# def test_model_queries():
#     request = SwarmRequest()
#     request.available_models()
#     request.get_model_info(["CHAOS-Core"])
#
#
# # see http://doc.pytest.org/en/latest/example/parametrize.html
# server_urls = [
#     "https://vires.services/ows",
#     "https://staging.vires.services/ows",
#     "https://staging.viresdisc.vires.services/ows"]
#
#
# @pytest.mark.parametrize("url", server_urls)
# def test_fetch(url):
#     request = SwarmRequest(url)
