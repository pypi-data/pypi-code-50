# -*- coding: utf-8 -*-

import pytest
import tuxbuild.build
import requests
import requests_mock
from mock import patch
import unittest
import tuxbuild.exceptions


@pytest.mark.parametrize(
    "url,result",
    [
        ("git@github.com:torvalds/linux.git", False),  # ssh type urls not supported
        ("https://github.com/torvalds/linux.git", True),
        ("http://github.com/torvalds/linux.git", True),
        ("git://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git", True),
        ("https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git", True),
        (
            "https://kernel.googlesource.com/pub/scm/linux/kernel/git/torvalds/linux.git",
            True,
        ),
    ],
)
def test_is_supported_git_url(url, result):
    assert tuxbuild.build.Build.is_supported_git_url(url) == result


headers = {
    "Content-type": "application/json",
    "Authorization": "header",
}


@patch("time.sleep")
class post_request_testCase(unittest.TestCase):
    def test_post_request_pass(self, stub_sleep):
        request = {"a": "b"}
        with requests_mock.mock() as m:
            m.post("http://foo.bar.com/pass", json={"a": "b"}, status_code=200)
            assert tuxbuild.build.post_request(
                url="http://foo.bar.com/pass", headers=headers, request=request
            ) == {"a": "b"}

    def test_post_request_timeout(self, stub_sleep):
        request = {"a": "b"}
        with requests_mock.mock() as m:
            m.post("http://foo.bar.com/timeout", json={"a": "b"}, status_code=504)
            with self.assertRaises(requests.exceptions.HTTPError):
                tuxbuild.build.post_request(
                    url="http://foo.bar.com/timeout", headers=headers, request=request
                )
            assert stub_sleep.call_count == 2

    def test_post_request_bad_request(self, stub_sleep):
        request = {"a": "b"}
        with requests_mock.mock() as m:
            m.post(
                "http://foo.bar.com/bad_request",
                json={"tuxbuild_status": "a", "status_message": "b"},
                status_code=400,
            )
            with self.assertRaises(tuxbuild.exceptions.BadRequest):
                tuxbuild.build.post_request(
                    url="http://foo.bar.com/bad_request",
                    headers=headers,
                    request=request,
                )
            assert stub_sleep.call_count == 0


@patch("time.sleep")
class get_request_testCase(unittest.TestCase):
    def test_get_request_pass(self, stub_sleep):
        with requests_mock.mock() as m:
            m.get("http://foo.bar.com/pass", json={"a": "b"}, status_code=200)
            assert tuxbuild.build.get_request(
                url="http://foo.bar.com/pass", headers=headers
            ) == {"a": "b"}

    def test_get_request_timeout(self, stub_sleep):
        with requests_mock.mock() as m:
            m.get("http://foo.bar.com/timeout", json={"a": "b"}, status_code=504)
            with self.assertRaises(requests.exceptions.HTTPError):
                tuxbuild.build.get_request(
                    url="http://foo.bar.com/timeout", headers=headers
                )
            assert stub_sleep.call_count == 29

    def test_get_request_500(self, stub_sleep):
        with requests_mock.mock() as m:
            m.get("http://foo.bar.com/timeout", json={"a": "b"}, status_code=500)
            with self.assertRaises(requests.exceptions.HTTPError):
                tuxbuild.build.get_request(
                    url="http://foo.bar.com/timeout", headers=headers
                )
            assert stub_sleep.call_count == 29

    def test_get_request_bad_request(self, stub_sleep):
        with requests_mock.mock() as m:
            m.get("http://foo.bar.com/bad_request", json={"a": "b"}, status_code=400)
            with self.assertRaises(requests.exceptions.HTTPError):
                tuxbuild.build.get_request(
                    url="http://foo.bar.com/bad_request", headers=headers
                )
            assert stub_sleep.call_count == 0

    def test_get_request_connectionfailure(self, stub_sleep):
        with requests_mock.mock() as m:
            m.get(
                "http://foo.bar.com/connection_failure",
                exc=requests.exceptions.ConnectionError,
            )
            with self.assertRaises(requests.exceptions.ConnectionError):
                tuxbuild.build.get_request(
                    url="http://foo.bar.com/connection_failure", headers=headers
                )
            assert stub_sleep.call_count == 29


@pytest.fixture
def global_var():
    pytest.start_time = 0


def mock_get_status(self):
    self.status["tuxbuild_status"] = "Queued"


def mock_time():
    pytest.start_time += 1
    return pytest.start_time


@patch.object(tuxbuild.build.Build, "get_status", mock_get_status)
@patch("time.time", mock_time)
@patch("time.sleep")
def test_get_status(stub_sleep, global_var):
    git_repo = "http://github.com/torvalds/linux"
    git_ref = "master"
    target_arch = "arm"
    kconfig = "defconfig"
    toolchain = "gcc-9"
    token = "test_token"
    kbapi_url = "http://test/foo/"
    b = tuxbuild.build.Build(
        git_repo, git_ref, target_arch, kconfig, toolchain, token, kbapi_url
    )
    b.status["tuxbuild_status"] = "Queued"
    with pytest.raises(tuxbuild.exceptions.Timeout):
        b.wait_on_status("Queued")


def test_global_var(global_var):
    assert pytest.start_time == 0
