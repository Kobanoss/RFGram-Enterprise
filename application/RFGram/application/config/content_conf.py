import os
from pathlib import Path


class CONTENT_CONF:
    ROOT = os.getcwd()
    CONTENT_DIR = 'static/'
    CONTENT_PATH = Path(ROOT, 'application/', CONTENT_DIR)
