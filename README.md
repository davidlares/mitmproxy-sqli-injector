# davidInjector

This is a simple Python 2.x script that checks if a custom URL is SQLi vulnerable by forcing *"LOL"* on each queryString params using Python's `MITMProxy` software for intercepting URLs.

Please test locally. If you are a developer, test your sites before shipping it to the cloud.

## MITMProxy

A HTTP Proxy is a server that acts as middle man between two communications (client - server).

[MITMProxy](https://mitmproxy.org/) is a interactive console program allows traffic flow to by intercepted, modified and more, with inline scripts features (basically is an event driven API with python) for handling custom routines or infinite usage work  

## Local Setup

By default `mitmproxy` runs on the `8080` port, so, you will have to configure any browser (assuming the proxy is on the same machine) with some manual proxy settings, adding the localhost IP 127.0.0.1 and the same `8080` port of the `mitmproxy`

## Virtualenv

In order to isolate this whole working environment, I recommend using a Virtualenv instance with the Python 2.7

For linux: (assuming you have the virtualenv library installed)

`virtualenv -p /usr/bin/python [any name]`

## Usage

Simple: `mitmproxy -s mitm.py`

## Credits

 - [David E Lares](https://twitter.com/davidlares3)

## License

 - [MIT](https://opensource.org/licenses/MIT)
