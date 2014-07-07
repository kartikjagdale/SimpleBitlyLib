SimpleBitlyLib
==============
bitlylib - Simple Python Bitly Url Shorten library
===========================

Description
-----------

This module offers a simple interface to Shorten LongUrl using Bit.ly API.


Example
-------
import bitlylib #imports Bitly lib

bitlylib.lngurl = "http://example.com"
var = bitlylib.shorten() # shorten Url and store it in any variable
print var

#or

print bitylib.shorten()


Installation
------------

As root::

   # python setup.py install

or just copy bitlylib.py inside a directory in your sys.path, e.g.
`/usr/lib/python2.7/`.
