import os

import sentry_sdk  # type: ignore

if os.getenv("TREEBEARD_ENVIRONMENT") is None:
    env = "production"
else:
    env = os.getenv("TREEBEARD_ENVIRONMENT")

sentry_sdk.init(
    "https://58543632a309471a88bb99f4f6bbdca0@sentry.io/2846147", environment=env
)
