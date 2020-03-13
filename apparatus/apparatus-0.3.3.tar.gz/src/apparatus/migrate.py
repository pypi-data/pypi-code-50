import logging
import os

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
        HELP = "Perform database migrations"
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
        _run_alembic(settings, remainder)

    def init():
        parser = base.SUBPARSERS.add_parser(Constant.COMMAND, help=Constant.HELP)
        text = "path to the database initialization SQL script"
        parser.add_argument("--init", type=str, help=text, default=Constant.INIT)
        text = "key for the database configuration in the config map"
        parser.add_argument("--key", type=str, help=text, default=Constant.DB_KEY)
        text = "each migration should execute in a separate transaction"
        parser.add_argument("--separate", help=text, action="store_true")
        parser.set_defaults(fn=handle)
        return parser.parse_known_args()

    init()


log = logging.getLogger(__name__)


def _run_alembic(settings, remainder):
    alembic_args = remainder or Constant.ALEMBIC_ARGS
    if settings.separate is True and alembic_args == ["upgrade", "head"]:
        while True:
            try:
                alembic.config.main(["upgrade", "+1"])
            except SystemExit:
                # The alembic console runner did not produce anymore migrations
                # TODO: Do not print an alembic ERROR to the log
                # This is likely difficult to fix when using the default alembic command
                # line program. Finding a proper solution probably requires understanding
                # the internals of alembic better.
                break
    else:
        alembic.config.main(alembic_args)


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
        if os.path.isfile(settings.init):
            with open(settings.init) as h:
                sql = h.read()

            log.info("Applying %s to %r", settings.init, engine.url)
            conn.execute(sql)
        else:
            log.info("No file at %s", settings.init)
    finally:
        if conn is not None:
            conn.close()
