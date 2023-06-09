from dataclasses import dataclass
from typing import Optional, Mapping


@dataclass
class MyPassConfig:
    host: Optional[str] = None
    port: Optional[int] = None
    session: Optional[Mapping] = None
    signin: callable = None
    logout: callable = None
