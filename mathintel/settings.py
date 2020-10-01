from pathlib import Path
from split_settings.tools import optional, include

BASE_DIR = Path(__file__).resolve().parent.parent

include(
    'components/*.py',
    optional('local.py')
)
