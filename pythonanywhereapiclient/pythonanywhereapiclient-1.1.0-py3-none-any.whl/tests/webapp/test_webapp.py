import pytest

from pythonanywhereapiclient import webapp
from pythonanywhereapiclient.utils import construct_request_payload


def test_base_is_valid(webapp_client):
    assert 'webapps/' == webapp.base_endpoint
    assert webapp.client
    assert webapp_client.base_url == webapp.client.base_url


def test_create_is_successful(webapp_response_create, webapp_new):
    assert webapp_new == webapp.create(**webapp_new)


def test_create_requires_domain_name_and_python_version_as_argument():
    with pytest.raises(TypeError) as exc:
        webapp.create()

    assert 'required positional argument' in str(exc.value)
    assert 'domain_name' in str(exc.value)
    assert 'python_version' in str(exc.value)


def test_create_raises_quotaerror(webapp_response_create_forbidden, webapp_new):
    with pytest.raises(webapp.QuotaError):
        webapp.create(**webapp_new)


def test_create_raises_responseerror(webapp_response_create_unknown, webapp_new):
    with pytest.raises(webapp.ResponseError):
        webapp.create(**webapp_new)


def test_create_static_is_successful(webapp_response_create_static, webapp_static_new):
    domain_name, body = webapp_static_new

    assert body == webapp.create_static(domain_name=domain_name, **body)


def test_create_static_raises_responseerror(webapp_response_create_static_unknown, webapp_static_new):
    domain_name, body = webapp_static_new

    with pytest.raises(webapp.ResponseError):
        webapp.create_static(domain_name, **body)


def test_delete_is_successful(webapp_response_delete, webapp_existing):
    domain_name, body = webapp_existing

    assert webapp.delete(domain_name=domain_name) is None


def test_delete_raises_responseerror(webapp_response_delete_unknown, webapp_existing):
    domain_name, body = webapp_existing

    with pytest.raises(webapp.ResponseError):
        webapp.delete(domain_name=domain_name)


def test_delete_ssl_not_implemented():
    with pytest.raises(NotImplementedError):
        webapp.delete_ssl()


def test_delete_static_not_implemented():
    with pytest.raises(NotImplementedError):
        webapp.delete_static()


def test_disable_is_successful(webapp_response_disable, webapp_existing):
    domain_name, body = webapp_existing

    assert webapp.disable(domain_name=domain_name) is None


def test_disable_raises_responseerror(webapp_response_disable_unknown, webapp_existing):
    domain_name, body = webapp_existing

    with pytest.raises(webapp.ResponseError):
        webapp.disable(domain_name=domain_name)


def test_enable_is_successful(webapp_response_enable, webapp_existing):
    domain_name, body = webapp_existing

    assert webapp.enable(domain_name=domain_name) is None


def test_enable_raises_responseerror(webapp_response_enable_unknown, webapp_existing):
    domain_name, body = webapp_existing

    with pytest.raises(webapp.ResponseError):
        webapp.enable(domain_name=domain_name)


def test_get_not_implemented():
    with pytest.raises(NotImplementedError):
        webapp.get()


def test_get_ssl_not_implemented():
    with pytest.raises(NotImplementedError):
        webapp.get_ssl()


def test_get_static_not_implemented():
    with pytest.raises(NotImplementedError):
        webapp.get_static()


def test_list_is_successful(webapp_response_list, webapp_existing):
    domain_name, body = webapp_existing

    assert [body] == webapp.list()


def test_list_raises_responseerror(webapp_response_list_unknown, webapp_existing):
    with pytest.raises(webapp.ResponseError):
        webapp.list()


def test_list_static_not_implemented():
    with pytest.raises(NotImplementedError):
        webapp.list_static()


def test_modify_is_successful(webapp_response_modify, webapp_existing):
    domain_name, body = webapp_existing
    params = construct_request_payload(
        body.copy(),
        exclude=['id', 'domain_name', 'user', 'expiry']
    )

    assert body == webapp.modify(domain_name=domain_name, **params)


def test_modify_raises_responseerror(webapp_response_modify_unknown, webapp_existing):
    domain_name, body = webapp_existing
    params = construct_request_payload(
        body.copy(),
        exclude=['id', 'domain_name', 'user', 'expiry']
    )

    with pytest.raises(webapp.ResponseError):
        webapp.modify(domain_name=domain_name, **params)


def test_modify_ssl_not_implemented():
    with pytest.raises(NotImplementedError):
        webapp.modify_ssl()


def test_modify_static_not_implemented():
    with pytest.raises(NotImplementedError):
        webapp.modify_static()


def test_reload_is_successful(webapp_response_reload, webapp_existing):
    domain_name, body = webapp_existing

    assert webapp.reload(domain_name=domain_name) is None


def test_reload_raises_responseerror(webapp_response_reload_unknown, webapp_existing):
    domain_name, body = webapp_existing

    with pytest.raises(webapp.ResponseError):
        webapp.reload(domain_name=domain_name)
