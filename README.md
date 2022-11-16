# sopel-http-codes
Sopel plugin to look up standard HTTP status codes


## Requirements
This plugin is written for:

* Python 3.5+
* Sopel 7.1+


## Usage
Commands & arguments:

* `.http <code>`
  * `<code>`: the HTTP status code to look up

Returns the name of the status code and a brief description of its purpose
from Python's `http` module.
