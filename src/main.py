import os
from spartan import app

__author__ = "PyMicron"
__version__ = "1.0.0"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
