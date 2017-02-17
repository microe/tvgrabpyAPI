# tvgrabpyAPI

[Goto the WIKI](https://github.com/tvgrabbers/tvgrabpyAPI/wiki)

###Summary

tv_grab_py_API is an API for creating xmltv compatible tv grabbers. It is the successor of [tv_grab_nl_py version 2.2](https://github.com/tvgrabbers/tvgrabnlpy) making all of its functionality available to the rest of the world.

###Requirements

 * Python 2.7.9 or higher (currently not python 3.x)
 * The [pytz module](http://pypi.python.org/pypi/pytz)
 * The [requests module](https://pypi.python.org/pypi/requests)
 * The [DataTreeGrab module](https://github.com/tvgrabbers/DataTree/)
 * Connection with the Internet

###Installation

* Especially under Windows, make sure Python 2.7.9 or higher is installed
* Make sure the above mentioned Python 2 packages are installed on your system
* Download the latest release and unpack it into a directory
* Run:
  * under Linux: `sudo ./setup.py install` from that directory
  * under Windows depending on how you installed Python:
    * `setup.py install` from that directory
    * Or: `Python setup.py install` from that directory

    (the frontend script(s) will install into `C:\Program Files\Python27\Scripts`)
* Run the frontend (presently only tv_grab_nl3.py) with --configure
* Check the created configuration file ~/.xmltv/tv_grab_nl3.conf and activate the desired channels.

###Some features

 * No need for anybody who wants to create a grabber to know much about Python. You mainly must write one or more json data_defs defining one or more sources. These are [DataTreeGrab data_defs](https://github.com/tvgrabbers/DataTree/wiki/data_def_language) with some specific extensions.
 * All retrieved data is stored in an sqlite database which:
  * speeds up data retrieval
  * makes it possible to repeatedly access the data again while off-line

 * Extensive list of user-settable options to give a user maximum opportunity to adapt the program to his or her need.
 * User settable genre translation tables with developer settable defaults.
 * Multiple language support (currently English and Dutch).
 * data_def updates are automatic.
 * theTVDB.com lookup.
