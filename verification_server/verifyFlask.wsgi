import sys
import logging

logging.basicConfig(stream=sys.stderr)

# Add the verify-server directory to the system path
sys.path.insert(0, '/var/www/verify-server')

# Import the Flask app
from verify import app as application