import os


class TokenProvider:
    @staticmethod
    def get_token():
        env_setting = os.getenv("TF_TOKEN", None)
        if env_setting:
            return env_setting

        with open(".credentials.conf", "r") as f:
            return f.read().strip()
