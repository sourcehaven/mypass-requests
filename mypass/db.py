from __future__ import annotations

import requests

from ._utils import bind_app_config, gen_proxy_from_port
from .exceptions import MyPassRequestException


@bind_app_config(needs_session=True)
def create_master_pw(pw: str, host: str = None, port: int = None, auth_token: str = None) -> int:
    url = f'{host}/api/db/master/create'
    headers = {'authorization': f'Bearer {auth_token}'}
    proxies = gen_proxy_from_port(host, port)
    json_obj = {'pw': pw}
    resp = requests.post(url=url, json=json_obj, headers=headers, proxies=proxies)
    if resp.status_code == 200:
        return resp.json()['id']
    raise MyPassRequestException(resp.status_code, resp.json())


@bind_app_config(needs_session=True)
def query_master_pw(host: str = None, port: int = None, auth_token: str = None) -> str:
    url = f'{host}/api/db/master/read'
    headers = {'authorization': f'Bearer {auth_token}'}
    proxies = gen_proxy_from_port(host, port)
    resp = requests.post(url=url, headers=headers, proxies=proxies)
    if resp.status_code == 200:
        return resp.json()['pw']
    raise MyPassRequestException(resp.status_code, resp.json())


@bind_app_config(needs_session=True)
def update_master_pw(pw: str, host: str = None, port: int = None, auth_token: str = None):
    url = f'{host}/api/db/master/update'
    headers = {'authorization': f'Bearer {auth_token}'}
    proxies = gen_proxy_from_port(host, port)
    json_obj = {'pw': pw}
    resp = requests.post(url=url, json=json_obj, headers=headers, proxies=proxies)
    if resp.status_code == 200:
        return resp.json()['id']
    raise MyPassRequestException(resp.status_code, resp.json())