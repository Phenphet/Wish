import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/html/wishapp')
from app import app as application