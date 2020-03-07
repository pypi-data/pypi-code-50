import os

if os.environ.get('CI_COMMIT_TAG'):
    build = True
else:
    build = False
