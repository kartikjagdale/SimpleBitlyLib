from distutils.core import setup


long_description = """
bitlylib - Simple Python Bitly Url Shorten library
===========================

Description
-----------

This module offers a simple interface to Shorten LongUrl using Bit.ly API.


Example
-------
import bitlylib #imports Bitly lib

bitlylib.lngurl = "http://example.com" #Your Url here
var = bitlylib.shorten() # shorten Url adn store it in any variable
print var

#or

print bitylib.shorten()


Installation
------------

As root::

   # python setup.py install

or just copy bitlylib.py inside a directory in your sys.path, e.g.
`/usr/lib/python2.7/`.
"""


setup(name='bitlylib',
      version='0.1',
      description='Simple Python Bitly URL Shorten library',
      author='Kartik jagdale',
      author_email='cf.natali@gmail.com',
      url='http://pythango.blogspot.coms',
      py_modules=['bitlylib'],
      license='GNU',
      classifiers=[
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Topic :: Networking :: Url Shorten'
      ],
      long_description=long_description
     )
