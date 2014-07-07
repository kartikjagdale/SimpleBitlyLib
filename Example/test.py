#!/usr/local/bin/python
"""
This is .py Script
A Sample Example to show how to use the Simple Python Bitly Library
"""
import bitlylib #imports Bitly lib

bitlylib.lngurl = "http://example.com" #Your Url here
var = bitlylib.shorten() # shorten Url adn store it in any variable
print var

#or

print bitylib.shorten()


