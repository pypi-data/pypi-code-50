import os
import sys
import subprocess
import jinja2
import platform

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    )
)

def ask(question, *answers):
    """
    This function will prompt user with ``question``. User can only respond with possible ``answers``.
    If user respond with empty string (return pressed), a default (first) answer is selected.
    If no answer is provided, a question will be displayed, awaiting some user input. That input will be returned
    :param question: *string*, questin that will be asked.
    :param *answers: Sequence of *string*, possible answers. Default answer is first answer provided. 
    :return: answer selected by user, one of the ``answers`` or ``None``.
    """
    asked = False
    lower_answers = [answer.lower() for answer in answers]
    options = ": ({}) [{}]".format("/".join(answers), answers[0]) if len(answers) >= 1 else ""
    while True:
        ans = input("{} {}".format(question, options) if not asked else "Choose one of {}: ".format(options))
        
        if len(answers) == 0:
            return ans
        elif ans == "":
            return answers[0]
        elif ans.lower() not in lower_answers:
            asked = True
        else:
            return answers[lower_answers.index(ans.lower())]


class SystemRecord:
    def __init__(self, name, parent=None, content=None, *children):
        if parent is not None and not isinstance(parent, self.__class__):
            raise ValueError(f"Parent must be instance of {self.__class__}")

        self._children = list(children)
        self.name = name
        self.parent = parent
        self._content = content

    def write(self, data):
        if len(self._children) != 0:
            raise AttributeError(f"{self.name} is a directory")
        
        self._content = data

    def read(self):
        if len(self._children) != 0:
            raise AttributeError(f"{self.name} is a directory")

        return self._content

    def new(self, name, *children):
        if self._content is not None:
            raise AttributeError(f"{self.name} is a file, new records can be created only on directory")
        
        new_record = self.__class__(name, parent=self, content=None, *children)
        self._children.append(new_record)
        return new_record

    def spawn(self, origin, renderer=lambda x: x):
        """
        Creates files/direcories on machine filesystem starting from the root path given in 
        ``origin`` parameter. This method will create files starting from self, to the last children.
        :param origin: root path taken by the renderer, either list of folders or valid os path
        :param renderer: callable, files content will be passed by renderer before writing it on disk
        :return: None
        """
        org = origin
        print("Processiong {} in origin {}".format(self.name, org))

        # directory
        if self._content is None:
            # first, mkdir
            try:
                print("Attemt to create directory {} in origin {} ... ".format(self.name, org), end='')
                os.mkdir(os.path.join(org, self.name), mode=0o775)
                print("Done.")
            except FileExistsError:
                print("Done - directory already exist.")

            # then all dependent nodes
            for child in self._children:
                print("Spawning child {} ...".format(child.name))
                child.spawn(origin=os.path.join(org, self.name))

        # file
        else:
            print("Writing {} in the origin {}".format(self.name, org))
            with open(os.path.join(org, self.name), "w", encoding="utf-8") as f:
                f.write(renderer(self._content))
    

def get_user_options():
    """
    This function collects all necesary information about project structure and required dependencies.
    :return: *dict*, collected options.
    """
    # this will contain  options choosen by user.
    # from this dict an project will be rendered.
    options = {}

    # project name
    options["project_name"] = ask("Type Your project (repo) name: ")

    # SQLAlchemy
    add_sqlalchemy = ("y" == ask(
        "Add SQLAlchemy to the project?",
        "y", "n"
    ))
    if add_sqlalchemy:
        # register and prepare for other specials
        options['sqlalchemy'] = {}

        # # db engine, consider futher implementation
        # db_engine = ask(
        #     "Select Your database engine",
        #     "postgresql", "mysql", "oracle", "mssql", "sqlite"
        # )
        # options['sqlalchemy']['db_engine'] = db_engine
        options['sqlalchemy']['db_engine'] = "postgresql"

        # # driver, consider futher implementation
        # allowed_drivers = {
        #     "postgresql": ["psycopg", "pg8000"],
        #     "mysql": ["mysqldb", "pymsql"],
        #     "oracle": ["cx_oracle"],
        #     "mssql": ["pyodbc", "pymssql"],
        #     "sqlite" ["sqlite3"]
        # }
        # db_driver = ask(
        #     "Select driver for engine {}".format(db_engine),
        #     allowed_drivers[db_engine]
        # )
        # options['sqlalchemy']['driver'] = db_driver
        options['sqlalchemy']['driver'] = "psycopg2"

        # database name etc
        print("Now You will be asked for connection-specific informations about database.")
        ask("Note that You have to provide existing user and database consistent with those given below.")
        options['sqlalchemy']['db_name'] = ask("Enter name for your database: ")
        options['sqlalchemy']['db_user'] = ask("Enter user name that will be connecting into database: ")
        options['sqlalchemy']['db_pass'] = ask("Enter password for given user: ")

        # alembic
        is_alembic = ("y" == ask(
            "Use alembic as migration tool?",
            "y", "n"
        ))
        options['sqlalchemy']['alembic'] = is_alembic
    
    use_sphinx = ( "y" == ask(
        "Use Sphinx for documentig project?",
        "y", "n"
    ))

    if use_sphinx:
        options['sphinx'] = {}

        options['sphinx']["name"] = ask("SPHINX: Enter Project name: ")
        options['sphinx']["author"] = ask("SPHINX: Enter Author: ")
        options['sphinx']["version"] = ask("SPHINX: Enter project version: ")
        options['sphinx']["release"] = ask("SPHINX: Enter project release: ")
        
    use_mail = ( "y" == ask(
        "Use Flask-Mail extension?",
        "y", "n"
    ))
    options['mail'] = use_mail

    use_socketio = ( "y" == ask(
        "Use Flask-SocketIO extension?",
        "y", "n"
    ))
    options['socketio'] = use_socketio

    # generate secret key
    options['secret_key'] = os.urandom(128).hex()

    return options



def generate_records(options):
    """
    Generates SystemRecord according to selected options.
    :param options: dictionary with selected generating options.
    :return: SystemRecord
    """
    # root dir
    project_root = SystemRecord(
        name=options["project_name"],
        parent=None,
        content=None
    )

    # add always-required files
    requirements = project_root.new(name="requirements.txt")
    requirements.write(jinja_env.get_template("requirements.jinja-txt").render(**options))

    prod_wsgi = project_root.new(name="prod-wsgi.ini")
    prod_wsgi.write(jinja_env.get_template("prod-wsgi.jinja-ini").render(**options))

    deploy = project_root.new(name="deploy.sh")
    deploy.write(jinja_env.get_template("deploy.jinja-sh").render(**options))

    ignore = project_root.new(name=".gitignore")
    ignore.write(jinja_env.get_template("gitignore.jinja").render(**options))

    run_wsgi = project_root.new(name="run_wsgi.py")
    run_wsgi.write(jinja_env.get_template("flask/run_wsgi.jinja-py").render(**options))

    app_dir = project_root.new(name="app")

    app_init = app_dir.new(name="__init__.py")
    app_init.write(jinja_env.get_template("flask/app/__init__.jinja-py").render(**options))

    app_exc = app_dir.new(name="exc.py")
    app_exc.write(jinja_env.get_template("flask/app/exc.jinja-py").render(**options))

    app_utils = app_dir.new(name="utils.py")
    app_utils.write(jinja_env.get_template("flask/app/utils.jinja-py").render(**options))

    templates = app_dir.new(name="templates")

    ep_doc = templates.new(name="endpoint_doc.rst-jinja")
    ep_doc.write(jinja_env.get_template("flask/app/templates/endpoint_doc.rst-jinja").render(**options))

    rest = app_dir.new(name="rest")

    rest_ctrl = rest.new(name="controllers.py")
    rest_ctrl.write(jinja_env.get_template("flask/app/rest/controllers.jinja-py").render(**options))
    
    rest_schema = rest.new(name="schema.py")
    rest_schema.write(jinja_env.get_template("flask/app/rest/schema.jinja-py").render(**options))
    
    config = app_dir.new(name="config")

    conf_config = config.new("config.prod.yaml")
    conf_config.write(jinja_env.get_template("flask/app/config/config.prod.jinja-yaml").render(**options))

    #################################
    # rendering optional components #

    # sqlalchemy
    if "sqlalchemy" in options:

        # rendering alembic stuff
        if options['sqlalchemy'].get("alembic", False):
            alembic_ini = project_root.new(name="alembic.ini")
            alembic_ini.write(jinja_env.get_template("alembic/alembic.jinja-ini").render(**options))

            alembic = project_root.new(name="alembic")
            alembic_env = alembic.new(name="env.py")
            alembic_env.write(jinja_env.get_template("alembic/env.py").render(**options))

        # rendering app stuff
        app_auth = app_dir.new(name="auth.py")
        app_auth.write(jinja_env.get_template("flask/app/auth.jinja-py").render(**options))

        app_models = app_dir.new(name="models.py")
        app_models.write(jinja_env.get_template("flask/app/models.jinja-py").render(**options))

    # sphinx will be done by sphinx quickstart script

    if options.get("mail", False):
        # flask_mail
        app_mail = app_dir.new(name="mail.py")
        app_mail.write(jinja_env.get_template("flask/app/mail.jinja-py").render(**options))

    if options.get("socketio", False):
        # socketio
        app_socketio = app_dir.new(name="io.py")
        app_socketio.write(jinja_env.get_template("flask/app/io.jinja-py").render(**options))

        events_dir = app_dir.new(name="events")
        events_ctrl = events_dir.new(name="controllers.py")
        events_ctrl.write(jinja_env.get_template("flask/app/events/controllers.jinja-py").render(**options))
        
        events_schema = events_dir.new(name="schema.py")
        events_schema.write(jinja_env.get_template("flask/app/events/schema.jinja-py").render(**options))

        events_utils = events_dir.new(name="event_utils.py")
        events_utils.write(jinja_env.get_template("flask/app/events/event_utils.jinja-py").render(**options))
        
        ev_doc = templates.new(name="event_doc.rst-jinja")
        ev_doc.write(jinja_env.get_template("flask/app/templates/event_doc.rst-jinja").render(**options))

    return project_root

def main():

    options = get_user_options()
    
    # create project directory
    try:
        print("Creating project directory '{}'... ".format(options["project_name"]), end='')
        os.mkdir(options["project_name"], mode=0o775)
        print("Done")
    except FileExistsError:
        print("Directory with such name aleady exist.")
        return 1

    print("Entering into project directory ...", end='')
    os.chdir(options["project_name"])
    print("Done")
        
    # create environment and install requirements
    print("Creating virtual environment ... ", end='')
    subprocess.run([
        "python3", "-m", "venv", "venv"
    ], stdout=subprocess.DEVNULL)
    print("Done")

    if platform.system() == "Windows":
        venv_path = os.path.join("venv", "Scripts")
    else:
        venv_path = os.path.join("venv", "bin")

    for dependency in jinja_env.get_template("requirements.jinja-txt").render(**options).split():
        print(f"Installing dependency {dependency} ...", end='')
        subprocess.run([
            os.path.join(venv_path, "python3"),
            "-m", "pip", "install", dependency
        ], stdout=subprocess.DEVNULL)
        print("Done")


    if options["sphinx"]:
        print("Generating sphinx docs ... ", end='')
        subprocess.run([
            os.path.join(venv_path, "sphinx-quickstart"),
            "-p", options['sphinx']["name"],
            "-a", options['sphinx']["author"],
            "-v", options['sphinx']["version"],
            "-r", options['sphinx']["release"],
            "--ext-autodoc",
            "-t", os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates", "sphinx"), 
            "--sep",
            "-l", "en",
            "-q", # quiet
            "doc"
        ], stdout=subprocess.DEVNULL)
        print("Done")
    
    # we are staring from commandline initialization scripts
    # alembic
    if options.get("sqlalchemy", {}).get("alembic", False):
        print("Initializing alembic ... ", end='')
        subprocess.run([
            os.path.join(venv_path, "alembic"),
            "init",
            "alembic"
        ], stdout=subprocess.DEVNULL)
        print("Done")

    # render
    print("Rendering and spawning templates:")
    records = generate_records(options)
    records.spawn(os.path.abspath(os.path.join(os.getcwd(), "..")))

    print("DONE")
    return 0


if __name__ == "__main__":

    sys.exit(main())
