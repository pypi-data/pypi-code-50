import json
from urllib.parse import urlparse, parse_qs
from ..config.connectionConfig import TEST_URL
from ..config.loginConfig import ERROR_CODE_TO_MSG
from ..exceptions.loginException import LoginException


def login_check(s):
    r = s.get(TEST_URL)
    try:
        r.json()
    except json.decoder.JSONDecodeError:
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(r.text)
        res = soup.find_all(lambda tag: "alert" in tag.get("class", []))
        if not res:
            raise LoginException("未知错误!")
        else:
            raise LoginException(list(res[0].children[-1]).strip())
    return True


def check_error_code(r):
    error = parse_qs(urlparse(r.url).query).get("errorCode")
    if error:
        raise LoginException(ERROR_CODE_TO_MSG[error[0]])
