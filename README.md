SimpleBitlyLib
==============

Description
-----------

This is Simple Python Bitly Url Shorten library.
This module offers a simple interface to Shorten LongUrl using Bit.ly API.


Example
-------
import bitlylib    #imports Bitly lib

bitlylib.lngurl = "http://example.com"

print bitylib.shorten()     # shorten Url and store it in any variable

Installation
------------

As root::

   # python setup.py install

or just copy bitlylib.py inside a directory in your sys.path, e.g.
`/usr/lib/python2.7/`.
