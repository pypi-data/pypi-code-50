# your package information
name = "greendeck-redis"
__version__ = "1.0.2"
author = "Yashvardhan Srivastava"
author_email = "yash@greendeck.co"
url = ""

# import sub packages
from .src.redis.redis import Redis
from .src.redis.redis import RedisSet
from .src.redis.redis import RedisQueue
