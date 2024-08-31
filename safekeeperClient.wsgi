import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/safekeeper-client-apps")

from server import app as application  