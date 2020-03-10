import pyodbc
from contextlib import contextmanager
import os
import webbrowser
from jinja2 import Environment, FileSystemLoader
import time
import datetime
from subprocess import check_output

def create_html(server_name, database_name, proj_name, command_type ="regular"):
    @contextmanager
    def connection():
        try:
            cnxn = pyodbc.connect(
                "Driver={SQL Server Native Client 11.0};Server=" + server_name + ";Database=" + database_name + ";Trusted_Connection=yes;MARS_Connection=Yes;",
                autocommit=True)
            yield cnxn

        except Exception as e:
            print(e)


    with connection() as conn:
        curr = conn.cursor()
        #Create new Project
        if command_type == "regular":
            new_project = f"SELECT TOP 20 [project_id],[project_name],[build_template_group] FROM [elt].project order by [project_name] "
        elif command_type == "connection":
            new_project = f"SELECT TOP (20) [project_id],[connection_name] FROM [elt].[project_oledb_connection] order by connection_name desc"
        curr.execute(new_project)
        resultSet_ = curr.fetchall()
        project_parameters = resultSet_

    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'html')
    env = Environment(loader=FileSystemLoader(templates_dir))
    if command_type == "regular":
        template = env.get_template('create_project_template.html')
    else:
        template = env.get_template('create_connection_template.html')

    # path = check_output(["where", "azuredatastudio"]).decode("utf-8")
    # path_to_azuredatastudio = path.split('\n')[0].strip('\r')
    # path_to_extension = os.path.join(path_to_azuredatastudio, '..', '..', 'resources', 'app', 'extensions', 'python')
    try:
        with connection() as conn:
            curr = conn.cursor()
            new_project = f"SELECT [use_value] FROM [elt].[application_config] WHERE setting='path to html files location';"
            curr.execute(new_project)
            PATH = curr.fetchall()[0][0]
            PATH = PATH if PATH else ''

            while not os.path.exists(PATH):
                print(
                    "There is no PATH to the directory in which eltSnap can build the html reports! Please provide absolute path for the directory")
                PATH = input()
                if not os.path.exists(PATH):
                    print("The PATH does not exists")
                else:
                    try:
                        insert_path = f"UPDATE [elt].[application_config] SET use_value = '{PATH}' WHERE setting = 'path to html files location'"
                        curr.execute(insert_path)
                    except Exception as e:
                        print(e)
    except Exception as ex:
        print(ex)

    if os.path.exists(PATH):
        filename = os.path.join(PATH, 'eltSnap_Project_HTML.html')
    else:
        raise ("Path is wrong ! Check your azuredatastudio installaton !")

    try:
        with open(filename, 'w') as writer:
            writer.write(template.render(
                h1="eltSnap Create Project",
                published=datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S'),
                project_name=proj_name,
                project_package_set=project_parameters,
                ))
    except Exception as e:
        print(e)

    time.sleep(0.1)
    webbrowser.open(filename, new=2)
    print(f'The HTML file destination is on the location : {filename}')

