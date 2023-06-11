from dataclasses import dataclass
from typing import Optional, Mapping


@dataclass
class MyPassConfig:
    """
    Class for storing application configurations.

    Attributes:
        host: Requests will be made using this default host.
        port: Requests made will be using this port.
        session: Session object configured by your application.
            Basically a mapping to your application configuration, storing access tokens and such.
        login: Login callback as needed. Usually takes one necessary argument, the password.
        logout: Logout callback. Possibly needed by update password logic,
            to log you out, and back in with your new password.
        refresh: Refresh callback if needed.
    """

    host: Optional[str] = None
    port: Optional[int] = None
    session: Optional[Mapping] = None
    login: callable = None
    logout: callable = None
    refresh: callable = None
