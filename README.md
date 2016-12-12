# sopel-http-codes
Sopel module that fetches HTTP status codes' descriptions from `httpstatuses.com`


## Requirements
The module uses HTML scraping, not an API (as httpstatuses has none). Therefore it
requires the following dependencies:

* `re` (part of Python's standard library)
* `requests` (really should be in standard Python library)
* `lxml` (XML/HTML parsing)
* `bleach` (HTML sanitization)

## Usage
Commands & arguments:

* `.http <code>`
  * `<code>`: the HTTP status code to look up

Returns the official name of the status code, and the main description snippet
from httpstatuses indicating in more detail what it's used for.

