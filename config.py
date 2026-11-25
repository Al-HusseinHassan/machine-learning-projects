import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PAGES_PATH = os.path.join(PROJECT_ROOT, 'pages')
PROJECTS_PATH = os.path.join(PROJECT_ROOT, 'projects')
CORE_PATH = os.path.join(PROJECT_ROOT, 'core')


if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)