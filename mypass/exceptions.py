from __future__ import annotations

from requests import RequestException


class MyPassRequestException(RequestException):
    def __init__(self, status_code: int, resp: dict | str = None):
        self.status_code = status_code
        self.resp = resp


class NoSessionException(ValueError):
    pass
