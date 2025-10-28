## MITMProxy SQLI injection

This is a simple Python 2.x script that checks if a custom URL is SQLi vulnerable by forcing *"LOL"* on each queryString params using Python's `MITMProxy` software for intercepting URLs.

Please test locally. If you are a developer, test your sites before shipping them to the cloud.

## MITMProxy

An HTTP Proxy is a server that acts as a middleman between two communications (client-server).

[MITMProxy](https://mitmproxy.org/) is an interactive console program that  allows traffic flow to be intercepted, modified, and more, with inline scripts features (basically an event-driven API with Python) for handling custom routines or infinite usage work  

## Local Setup

By default, `mitmproxy` runs on the `8080` port, so you will have to configure any browser (assuming the proxy is on the same machine) with some manual proxy settings, adding the localhost IP 127.0.0.1 and the same `8080` port of the `mitmproxy`

## Virtualenv

To isolate this whole working environment, I recommend using a Virtualenv instance with Python 2.7

For Linux: (assuming you have the virtualenv library installed)

`virtualenv -p /usr/bin/python [any name]`

## Usage

Simple: `mitmproxy -s mitm.py`

## Credits
[David Lares S](https://davidlares.com)

## License
[MIT](https://opensource.org/licenses/MIT)
