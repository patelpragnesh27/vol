import sys
import os

# Add your project directory to the sys.path
sys.path.insert(0, os.path.dirname(__file__))

# Import your application as `application`
from app import app as application

# This ensures that the app runs on the appropriate port
if __name__ == "__main__":
    application.run()
