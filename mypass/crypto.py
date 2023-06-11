from __future__ import annotations

import requests

from ._utils import gen_proxy_from_port, bind_app_config, bind_error_handlers
from .exceptions import MyPassRequestException


@bind_error_handlers
@bind_app_config()
def encrypt(secret: str, pw: str, host: str = None, port: int = None):
    proxies = gen_proxy_from_port(host, port)
    resp = requests.post(
        f'{host}/api/crypto/encrypt', json={'secret': secret, 'pw': pw}, proxies=proxies)
    son = resp.json()
    if resp.status_code == 200:
        return son['secret'], son['salt']
    raise MyPassRequestException(resp.status_code, son)


@bind_error_handlers
@bind_app_config()
def decrypt(secret: str, pw: str, salt: str, host: str = None, port: int = None):
    proxies = gen_proxy_from_port(host, port)
    resp = requests.post(
        f'{host}/api/crypto/decrypt', json={'secret': secret, 'pw': pw, 'salt': salt}, proxies=proxies)
    son = resp.json()
    if resp.status_code == 200:
        return son['message']
    raise MyPassRequestException(resp.status_code, son)
