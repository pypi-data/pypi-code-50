import argparse
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

from r3d3 import ExperimentDB, R3D3ExperimentPlan

root_dir = "{}/..".format(os.path.dirname(os.path.abspath(__file__)))


class ExperimentLauncher(object):
    def __init__(self, db_path):
        self.db = ExperimentDB(db_path)
        self.experiment_id = None

    def run(self, experiment_plan: R3D3ExperimentPlan, max_nb_processes: int):
        self.db.init_experiment_table()

        def launcher_with_environment(env, debug):
            def launch_command_line(command):
                tab = command.split()
                print("Executing {}".format(command))
                if not debug:
                    print(tab)
                    try:
                        myPopen = subprocess.Popen(
                            tab, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE
                        )
                        for l in myPopen.stderr:
                            print(l)
                        myPopen.stdout.close()
                        myPopen.stderr.close()
                        return myPopen.wait()
                    except subprocess.CalledProcessError as e:
                        print(e.output)

            return launch_command_line

        # Creating env for the runs
        env = os.environ.copy()
        if experiment_plan.debug:
            print("Using env {}".format(env))

        nb_tests = len(experiment_plan.experiments)
        print("%d experiments to launch..." % nb_tests)

        # Creating executors with max nb processes from the config
        executor = ThreadPoolExecutor(max_workers=max_nb_processes)

        # Running the tests
        now = datetime.now()
        self.experiment_id = int(time.mktime(now.timetuple()))

        futures = list()

        for run_id, experiment in enumerate(experiment_plan.experiments):
            # The python binary is available in sys.executable
            args = ["{} {}".format(sys.executable, f"{experiment.binary}")]
            for a in experiment.config:
                args.append("--" + a + " " + str(experiment.config[a]))

            # Passing launcher information to the experiment
            args.append(
                "--max_nb_processes {}".format(min([max_nb_processes, nb_tests]))
            )
            args.append(f"--experiment_id {self.experiment_id}")
            args.append(f"--run_id {run_id}")

            self.db.add_experiment(
                experiment_id=self.experiment_id,
                run_id=run_id,
                config=experiment.get_config_with_binary(),
            )

            command = " ".join(args)
            future = executor.submit(launcher_with_environment(env, debug=False), command)
            futures.append(future)

        while not all([f.done() for f in futures]):
            time.sleep(5)
        for i, future in enumerate(futures):
            print(f"Run id {i} finished with return code {future.result()}")


def main(experiment_file: str) -> ExperimentLauncher:
    print(experiment_file)

    variables = dict()
    with open(experiment_file) as f:
        exec(f.read(), variables)

    my_experiment_plan: R3D3ExperimentPlan = variables["experiment_plan"]

    my_launcher = ExperimentLauncher(my_experiment_plan.db_path)
    my_launcher.run(
        experiment_plan=my_experiment_plan,
        max_nb_processes=my_experiment_plan.max_nb_processes,
    )

    return my_launcher


def main_cli():
    parser = argparse.ArgumentParser(description="Experiment Launcher")
    parser.add_argument("--experiment_file", type=str)
    args = parser.parse_args()

    main(experiment_file=args.experiment_file)
