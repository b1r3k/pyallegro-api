pyallegro-api
=============

Wrapper for Allegro WebAPI in Python

## Features

1. thin wrapper around original methods
1. default handling of session expiration
1. tests!

## Installation

Just `python setup.py install`

## Usage

```python
from pyallegroapi import SOAPClient

api = SOAPClient()
api.login('username', 'plain_password', 'apikey')
results = api.doShowCat(catId=54003)
print(results)
```

## Tests

In order to invoke tests put your sandbox credentials into `src/tests/config.py`.
Then you can invoke tests as usually: `python setup.py test`

## Contributing

Pull requests are welcome!

## License

MIT license
