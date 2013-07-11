from os import path

from mock import patch, Mock
from twisted.internet import epollreactor

import vulcan


vulcan.initialize(path.join(path.dirname(__file__), "..", "..", "test.ini"))
epollreactor.install()