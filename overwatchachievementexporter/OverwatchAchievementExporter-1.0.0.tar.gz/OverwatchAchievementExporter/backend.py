import requests

class Backend:
    async def get_user_profile(self, username: str):
        url = f"https://playoverwatch.com/en-us/career/pc/{username.replace('#', '-')}"
        r = requests.get(url, {})
        return r.text