# MyPass Login Manager package

Request helpers for MyPass python applications.

## Usage

The package has a main class called `MyPassRequests`.
In your application you can import this using the following command.

```python
from mypass_requests import MyPassRequests

app = MyPassRequests()
# configure package application
app.config.host = 'http://localhost'
app.config.port = 5757
...

# you can get your application manager importing current_app
from mypass_requests import current_app

# read configs as needed anywhere in your app
host = current_app().config.host
port = current_app().config.port
```

If configured correctly, requests under this package will be
made using these configurations, making your work easier.
