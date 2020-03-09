
# def wait_postgres_ready(db_name, db_user, db_pwd, db_host):
#     while True:
#         try:
#             psycopg2.connect(dbname=db_name, user=db_user, password=db_pwd, host=db_host)
#         except psycopg2.OperationalError:
#             print("Postgres is unavailable - sleeping")
#             time.sleep(1)
#             continue
#         break
#     print("Postgres is up - continuing...")
#
#
# def set_postgres_env():
#     os.environ.setdefault("POSTGRES_USER", "postgres")
#     db_user = os.environ.get("POSTGRES_USER")
#     os.environ.setdefault("POSTGRES_DB", db_user)
#     db_name = os.environ.get("POSTGRES_DB")
#     os.environ.setdefault("POSTGRES_HOST", "postgres")
#     db_host = os.environ.get("POSTGRES_HOST")
#     db_pwd = os.environ.get("POSTGRES_PASSWORD", "")
#     db_url = f'postgres://{db_user}:{db_pwd}@{db_host}:5432/{db_name}'
#     os.environ["DATABASE_URL"] = db_url
#     return db_name, db_user, db_pwd, db_host
import re
import subprocess

load_once = False


def get_env_path():
    env = environ.Env()
    REMO_HOME = env('REMO_HOME', default=str(Path.home().joinpath('.remo')))
    os.makedirs(REMO_HOME, exist_ok=True)
    cfg_file = '.env'
    cfg_path = env('REMO_CONFIG', default=str(os.path.join(REMO_HOME, cfg_file)))

    if os.path.exists(cfg_path):
        return cfg_path

    if os.path.exists(cfg_file):
        return cfg_file

    # print(f"""
    # WARNING: Config file was not found.
    #
    # By default config file should be at {str(Path.home().joinpath('.remo').joinpath('.env'))}
    # but you can change Remo home directory via REMO_HOME (env file expected in REMO_HOME/.env)
    # also you can specify directly location of env file via REMO_CONFIG
    # """)


def load_env():
    global load_once
    if load_once:
        return

    commented_line = re.compile(r"^\s*#")
    empty_line = re.compile(r"^\W*$")
    config_path = get_env_path()
    if config_path:
        env_file = open(config_path).readlines()
        envs = list(filter(lambda line: not commented_line.match(line) and not empty_line.match(line), env_file))

        for line in envs:
            line = line.strip()
            key, val = line.split('=')
            os.environ[key] = val

    load_once = True

    # db_name, db_user, db_pwd, db_host = set_postgres_env()
    # wait_postgres_ready(db_name, db_user, db_pwd, db_host)


def install_packages(*requirements):
    # No more convenient way until PEP 518 is implemented; setuptools only handles eggs
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + list(requirements))


def install_package(name, version=None):
    """ If a package is already installed, build against it. If not, install """
    # Do not import 3rd-party modules into the current process
    import json
    js_packages = json.loads(
        subprocess.check_output([sys.executable, "-m", "pip", "list", "--format", "json"]).decode(
            'ascii'))  # valid names & versions are ASCII as per PEP 440
    try:
        [package] = (package for package in js_packages if package['name'] == name)
    except ValueError:
        install_packages("%s==%s" % (name, version) if version else name)
        return version
    else:
        return package['version']

# install_package('Cython', '0.29.13')
# install_package('git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI')
