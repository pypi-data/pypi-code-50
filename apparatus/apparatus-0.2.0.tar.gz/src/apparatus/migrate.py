import logging
from retry import retry
from apparatus import base


try:
    import alembic.config
    import sqlalchemy
except ImportError:
    pass
else:

    class Constant:
        COMMAND = "migrate"
        INIT = "migrations/init.sql"
        ALEMBIC_ARGS = ["upgrade", "head"]
        DB_KEY = "database"
        RETRY_PARAMS = {
            "exceptions": sqlalchemy.exc.OperationalError,
            "tries": 20,
            "max_delay": 1,
            "delay": 0.2,
            "backoff": 1.5,
        }

        @classmethod
        def wait_for(cls):
            delay = cls.RETRY_PARAMS["delay"]
            backoff = cls.RETRY_PARAMS["backoff"]
            max_delay = cls.RETRY_PARAMS["max_delay"]
            result = 0
            for i in range(cls.RETRY_PARAMS["tries"] + 1):
                result += min(delay * (backoff ** i), max_delay)
            return result

    def handle(settings, remainder):
        config = base.read_config()
        _initialize(settings, config)
        alembic.config.main(remainder or Constant.ALEMBIC_ARGS)

    def init():
        parser = base.SUBPARSERS.add_parser(Constant.COMMAND)
        parser.add_argument("--init", type=str, default=Constant.INIT)
        parser.add_argument("--key", type=str, default=Constant.DB_KEY)
        parser.set_defaults(fn=handle)
        return parser.parse_known_args()

    init()


log = logging.getLogger(__name__)


def _database_url(settings, config):
    config = config[settings.key]
    return "{dialect}://{user}:{password}@{host}:{port}/{database}".format(
        dialect=config.get("dialect", "postgresql"),
        user=config["user"],
        password=config["password"],
        host=config["host"],
        port=config["port"],
        database=config["database"],
    )


def _initialize(settings, config=None):
    engine = sqlalchemy.create_engine(_database_url(settings, config))

    @retry(**Constant.RETRY_PARAMS, logger=None)
    def connect():
        return engine.connect()

    log.info("Waiting at most %.02f seconds for connection", Constant.wait_for())
    conn = None
    try:
        conn = connect()
        log.info("Applying %s to %r", settings.init, engine.url)
        with open(settings.init) as h:
            sql = h.read()
        conn.execute(sql)
    finally:
        if conn is not None:
            conn.close()
