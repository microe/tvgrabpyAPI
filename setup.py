#!/usr/bin/env python2

'''
This Package contains an API for tv_grabbers Alle data is defined in JSON files
Including where and how to get the tv data. Multiple sources can be defined
and the resulting data is integrated into one XMLTV output file.
The detailed behaviour is highly configurable. See our site for more details.
'''

from distutils.core import setup
from os import environ, name
from tvgrabpyAPI import version, __version__

if name == 'nt':
    if 'USERPROFILE' in environ:
        home_dir = environ['USERPROFILE']
    elif 'HOMEPATH' in environ:
        home_dir = environ['HOMEPATH']
    elif 'HOME' in environ:
        home_dir = environ['HOME']

    source_dir = u'%s/.xmltv/sources' % home_dir
else:
    source_dir = u'/var/lib/tvgrabpyAPI'

setup(
    name = version()[0],
    version =  __version__,
    description = 'xlmtv API based on JSON datafiles',
    packages = ['tvgrabpyAPI'],
    package_data={'tvgrabpyAPI': ['texts/tv_grab_text.*']},
    scripts=['tv_grab_nl3.py', 'tv_grab_test_json.py', 'tv_grab_test_source.py'],
    data_files=[(source_dir, ['sources/tv_grab_API.json',
                            'sources/tv_grab_nl.json'])],
    requires = ['pytz', 'requests', 'DataTreeGrab'],
    provides = ['%s (%s.%s)' % (version()[0], version()[1], version()[2])],
    long_description = __doc__,
    maintainer = 'Hika van den Hoven',
    maintainer_email = 'hikavdh at gmail dot com',
    license='GPL',
    url='https://github.com/tvgrabbers/tvgrabpyAPI',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: Public Domain',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search']
)
