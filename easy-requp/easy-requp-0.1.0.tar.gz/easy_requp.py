# Easy ReqUp - Easily manage Python packages based on requirements file specs.
# Copyright (C) 2020 Luca Trevisani
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""Easily manage Python packages based on requirements file specifications."""

__version__ = "0.1.0"


import argparse
import importlib
import json
import platform
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import List

import pkg_resources


def display(quiet: int, *args: str) -> None:
    """Display message."""
    if quiet < 2:
        print("\n".join(args))


def continue_or_exit(
    quiet: int,
    yes: bool,
    prompt_common: str,
    prompt_ask: str = ", continue anyway?",
    prompt_yes: str = ", continuing anyway.",
) -> None:
    """Prompt user to continue or exit."""
    if prompt_common.endswith("."):
        prompt_common = prompt_common[:-1]
    if prompt_ask.endswith("?"):
        prompt_ask = prompt_ask[:-1]
    if yes:
        display(quiet, f"{prompt_common}{prompt_yes}")
        return
    while True:
        ok = input(f"{prompt_common}{prompt_ask} ([y]/n)? ").lower().strip()
        if ok in ("", "y"):
            return
        if ok == "n":
            sys.exit(0)
        display(quiet, "Enter 'y' or 'n'.")


def exit_with_error(quiet: int, message_1: str, message_2: str = "") -> None:
    """Exit with error message."""
    if quiet > 2:
        sys.exit(1)
    if message_1.startswith("\n"):
        message_1 = message_1[1:]
        newline = "\n"
    else:
        newline = ""
    if message_2.startswith("\n"):
        message_2 = message_2[1:]
    if message_2 == "":
        sys.exit(f"{newline}ERROR: {message_1}")
    else:
        sys.exit(f"{newline}ERROR: {message_1}\nERROR: {message_2}")


def try_pip(
    verbose: int,
    quiet: int,
    yes: bool,
    args_1: List[str],
    args_2: List[str],
    max_pip_retries: int,
    message_prompt: str,
    message_exit: str,
    capture_output: bool = False,
) -> subprocess.CompletedProcess:
    """Run 'pip' with passed options, retry up to 'max_pip_retries' times if failing."""
    pip_cmd = [sys.executable, "-m", "pip", "--disable-pip-version-check"]
    pip_cmd.extend(
        ["--verbose" for _ in range(min(3, verbose))]
        + ["--quiet" for _ in range(min(3, quiet))]
        + args_1
        + args_2
    )
    message_prompt = "\n" + message_prompt
    message_exit = "\n" + message_exit
    retries = 0
    while True:
        try:
            output = subprocess.run(pip_cmd, capture_output=capture_output, check=True)
        except subprocess.SubprocessError as err:
            if max_pip_retries <= 0:
                exit_with_error(quiet, message_exit, str(err))
            elif retries == max_pip_retries:
                if message_exit.endswith("."):
                    message_exit = message_exit[:-1]
                exit_with_error(
                    quiet, f"{message_exit} after {retries} retries.", str(err)
                )
            else:
                if retries == 0:
                    message = f"{message_prompt}\n{err}\nFirst attempt failed."
                else:
                    message = f"{message_prompt}\n{err}\nRetry {retries} of {max_pip_retries} failed."
                continue_or_exit(
                    quiet, yes, message, ", try again?", ", trying again.",
                )
                display(yes, "")
                retries += 1
        else:
            return output


class ReqUp:
    """Object containing requirements file and packages working set data and methods."""

    def __init__(
        self,
        verbose: int = 0,
        quiet: int = 0,
        yes: bool = False,
        skip_python_version_check: bool = False,
        requirements_file: str = "easy_requp.txt",
    ) -> None:
        """Initialize new ReqUp object instance."""
        self.verbose = verbose
        self.quiet = quiet
        self.yes = yes
        if not skip_python_version_check:
            self.check_python_updates()
        self.requirements_file = self.find_requirements_file(requirements_file)
        self.requirements = self.parse_requirements_file()
        self.check_working_set()

    @property
    def working_set(self) -> List[pkg_resources.Distribution]:
        """Set 'working_set' attribute with current packages working set excluding uncleaned distributions."""
        importlib.reload(pkg_resources)
        return [
            dist for dist in pkg_resources.working_set if not dist.key.startswith("-")
        ]

    def eq_working_sets(
        self,
        working_set_1: List[pkg_resources.Distribution],
        working_set_2: List[pkg_resources.Distribution],
    ) -> bool:
        """Return true if 'working_set_1' and 'working_set_2' are equal."""
        wset_1 = {dist.key: dist.version for dist in working_set_1}
        wset_2 = {dist.key: dist.version for dist in working_set_2}
        return wset_1 == wset_2

    def diff_working_sets(
        self,
        working_set_1: List[pkg_resources.Distribution],
        working_set_2: List[pkg_resources.Distribution],
    ) -> None:
        """Compare 'working_set_1' with 'working_set_2', and show differences."""
        wset_1 = {dist.key: dist.version for dist in working_set_1}
        wset_2 = {dist.key: dist.version for dist in working_set_2}
        installed = [pkg for pkg in wset_2.keys() if pkg not in wset_1.keys()]
        uninstalled = [pkg for pkg in wset_1.keys() if pkg not in wset_2.keys()]
        upgraded = [
            pkg
            for pkg in wset_1.keys()
            if pkg in wset_2.keys() and wset_1[pkg] != wset_2[pkg]
        ]
        if not installed and not uninstalled and not upgraded:
            display(
                self.quiet, "\nNo packages were installed, uninstalled or upgraded."
            )
        else:
            if installed:
                display(
                    self.quiet,
                    "\nThe following packages were installed:",
                    "\n".join([f"  {pkg} {wset_2[pkg]}" for pkg in installed]),
                )
            if uninstalled:
                display(
                    self.quiet,
                    "\nThe following packages were uninstalled:",
                    "\n".join([f"  {pkg} {wset_1[pkg]}" for pkg in uninstalled]),
                )
            if upgraded:
                display(
                    self.quiet,
                    "\nThe following packages were upgraded:",
                    "\n".join(
                        [f"  {pkg} {wset_1[pkg]} => {wset_2[pkg]}" for pkg in upgraded]
                    ),
                )

    def check_python_updates(self) -> None:
        """Check for Python updates."""
        display(self.quiet, "\nChecking for Python updates...")
        try:
            with urllib.request.urlopen(
                "https://www.python.org/downloads/windows/"
            ) as f:
                html = f.read().decode("utf-8")
        except urllib.error.URLError:
            continue_or_exit(
                self.quiet, self.yes, "Could not connect to 'www.python.org'."
            )
        else:
            python_version_latest_match = re.search(
                r'<li>Download <a href="https://www\.python\.org/ftp/python/(\d\.\d\.\d)/python\d\d\d\.chm">Windows help file</a></li>',
                html,
            )
            if not python_version_latest_match:
                continue_or_exit(
                    self.quiet,
                    self.yes,
                    "Could not find Python version string on 'www.python.org', website layout may have changed.",
                )
            else:
                python_version_latest = python_version_latest_match.group(1)
                python_version_installed = sys.version[0:5]
                if python_version_latest != python_version_installed:
                    continue_or_exit(
                        self.quiet,
                        self.yes,
                        f"Installed version {python_version_installed}, latest version {python_version_latest}.",
                    )
                else:
                    display(
                        self.quiet,
                        f"Installed version {python_version_installed}, no updates available.",
                    )

    def find_requirements_file(self, requirements_file: str) -> Path:
        """Search requirements file and set 'requirements_file' attribute."""
        for path in [
            Path.cwd().joinpath(requirements_file),
            Path.home().joinpath(requirements_file),
        ]:
            if path.is_file():
                display(self.quiet, f"\nFound requirements file: '{path}'.")
                break
        else:
            exit_with_error(
                self.quiet, f"\nCould not find requirements file '{requirements_file}'."
            )
        return path

    def parse_requirements_file(self) -> List[pkg_resources.Requirement]:
        """Parse requirements file, verify its contents, and set 'requirements' attribute."""
        try:
            with open(self.requirements_file) as f:
                requirements = [
                    req for req in pkg_resources.parse_requirements(f.read())
                ]
        except PermissionError as err:
            exit_with_error(
                self.quiet,
                f"Could not read requirements file '{self.requirements_file}'.",
                str(err),
            )
        # TODO: once the following bug-fix is implemented remove the "type ignore" comment: https://github.com/pypa/setuptools/pull/1832
        except pkg_resources.RequirementParseError as err:  # type: ignore[attr-defined]
            exit_with_error(
                self.quiet,
                f"Could not parse requirements file '{self.requirements_file}'.",
                str(err),
            )
        if "easy-requp" not in [req.key for req in requirements]:
            exit_with_error(
                self.quiet,
                "'easy-requp' was not found in the requirements file, it is needed as otherwise it would try to uninstall itself, please add it manually.",
            )
        return requirements

    def check_working_set(self) -> None:
        """Check packages working set and warn if uncleaned distributions are found."""
        uncleaned_dists_key = {
            dist.key for dist in pkg_resources.working_set if dist.key.startswith("-")
        }
        uncleaned_dists_loc = {
            dist.location
            for dist in pkg_resources.working_set
            if dist.key.startswith("-")
        }
        if uncleaned_dists_key:
            display(
                self.quiet,
                "\nThe following uncleaned distributions were found:",
                "\n".join([f"  {key}" for key in uncleaned_dists_key]),
                "Located in:",
                "\n".join([f"  {loc}" for loc in uncleaned_dists_loc]),
                "\nUsually they are left over from previous unsuccessful installations, and do not harm.",
                "You can get rid of them by manually deleting all folders beginning with '~' in your 'site-packages' folders.",
            )
            continue_or_exit(
                self.quiet, self.yes, "\nBy continuing they will be ignored.",
            )

    def uninstall_orphaned(self) -> None:
        """Uninstall all packages that are not in the requirements tree."""
        display(self.quiet, "\nLooking for orphaned packages...")
        wset_deps = {dist.key: dist.requires() for dist in self.working_set}
        reqs_tree = list({req.key for req in self.requirements})
        for req in reqs_tree:
            if req not in wset_deps.keys():
                continue
            req_deps = [dist.key for dist in wset_deps[req]]
            for req_dep in req_deps:
                if req_dep not in reqs_tree:
                    reqs_tree.append(req_dep)
        orph = [pkg for pkg in wset_deps.keys() if pkg not in reqs_tree]
        if orph:
            continue_or_exit(
                self.quiet,
                self.yes,
                f"The following packages are unneeded: {', '.join(orph)}\n",
                "Proceed with uninstall?",
                "Proceeding with uninstall.",
            )
            try_pip(
                self.verbose,
                self.quiet,
                self.yes,
                ["uninstall", "--yes"] + orph,
                [],
                1,
                "",
                "Uninstall was not successful.",
            )
        else:
            display(
                self.quiet,
                "No orphaned packages were found, all installed packages are needed.",
            )

    def upgrade_requirements(self, options: List[str], max_pip_retries: int) -> None:
        """Upgrade all required packages, upgrade their dependencies only if needed."""
        display(self.quiet, "\nUpgrading required packages...")
        try_pip(
            self.verbose,
            self.quiet,
            self.yes,
            ["install", "--upgrade", "--requirement", str(self.requirements_file)],
            options,
            max_pip_retries,
            "Unexpected error while upgrading packages.",
            "Upgrade was not successful.",
        )

    def upgrade_dependencies(self, options: List[str], max_pip_retries: int) -> None:
        """Find remaining outdated dependencies and upgrade them if possible."""
        display(self.quiet, "\nUpgrading outdated dependencies...")
        output = try_pip(
            0,
            0,
            False,
            ["list", "--outdated", "--format=json"],
            [],
            1,
            "",
            "Could not detect outdated packages.",
            capture_output=True,
        )
        outdated_keys = [
            outdated["name"].lower() for outdated in json.loads(output.stdout)
        ]
        outdated_specs = []
        for outdated_key in outdated_keys:
            specs_reqs = [
                req.specs for req in self.requirements if req.key == outdated_key
            ]
            specs_wset = [
                dep.specs
                for dist in self.working_set
                for dep in dist.requires()
                if dep.key == outdated_key
            ]
            specs_sum = specs_reqs + specs_wset
            specs = [
                "".join(spec_tuple)
                for specs_list in specs_sum
                for spec_tuple in specs_list
            ]
            outdated_specs.append(outdated_key + ",".join(specs))
        try_pip(
            self.verbose,
            self.quiet,
            self.yes,
            ["install", "--upgrade"] + outdated_specs,
            options,
            max_pip_retries,
            "Unexpected error while upgrading package.",
            "Upgrade was not successful.",
        )

    def check_packages(self) -> None:
        """Verify that installed packages have compatible dependencies."""
        display(self.quiet, "\nChecking installed packages compatibility...")
        try_pip(
            self.verbose,
            self.quiet,
            self.yes,
            ["check"],
            [],
            1,
            "",
            "Installed packages have incompatible dependencies.",
        )

    def clean_cache(self, cache_limit: int) -> None:
        """Verify 'pip' cache size and clean it if needed."""
        # TODO: in future "pip" will include a command to manage cache:
        #   https://github.com/pypa/pip/issues/4685
        #   https://github.com/pypa/pip/issues/6956
        #   https://github.com/pypa/pip/issues/7350
        #   https://github.com/pypa/pip/issues/7372
        #   https://github.com/pypa/pip/pull/6391
        # Cache folder location: https://pip.pypa.io/en/latest/reference/pip_install/#caching
        if (system := platform.system()) == "Linux":
            cache_path = Path.home().joinpath(".cache", "pip")
        elif platform.system() == "Darwin":
            cache_path = Path.home().joinpath("Library", "Caches", "pip")
        elif platform.system() == "Windows":
            cache_path = Path.home().joinpath("AppData", "Local", "pip", "cache")
        else:
            exit_with_error(
                self.quiet, f"Operating system '{system}' is not supported."
            )
        cache_size = (
            sum(f.stat().st_size for f in cache_path.rglob("*") if f.is_file())
            / 1024
            / 1024
        )
        if cache_size <= cache_limit:
            display(
                self.quiet,
                f"\nCache size {cache_size:.0f} MB, cache limit {cache_limit} MB, cleaning not needed.",
            )
        else:
            display(
                self.quiet,
                f"\nCache size {cache_size:.0f} MB, cache limit {cache_limit} MB, cleaning cache...",
            )
            try:
                shutil.rmtree(cache_path)
            except FileNotFoundError:
                pass
            except PermissionError as err:
                exit_with_error(
                    self.quiet,
                    f"Could not delete cache folder '{cache_path}'.",
                    str(err),
                )

    def run(
        self,
        actions: List[str] = ["all"],
        invert_actions: bool = False,
        options: List[str] = [],
        max_pip_retries: int = 3,
        deps_complete: bool = False,
        cache_limit: int = 200,
    ) -> None:
        """Perform packages upgrade based on requirements file specifications."""
        upgrade_requirements = "reqs" in actions or "all" in actions
        upgrade_dependencies = "deps" in actions or "all" in actions
        uninstall_orphaned = "orph" in actions or "all" in actions
        check_packages = "check" in actions or "all" in actions
        clean_cache = "clean" in actions or "all" in actions
        if invert_actions:
            upgrade_requirements = not upgrade_requirements
            upgrade_dependencies = not upgrade_dependencies
            uninstall_orphaned = not uninstall_orphaned
            check_packages = not check_packages
            clean_cache = not clean_cache
        initial_working_set = self.working_set
        if uninstall_orphaned:
            self.uninstall_orphaned()
        prev_working_set = self.working_set
        if upgrade_requirements:
            self.upgrade_requirements(options, max_pip_retries)
        if upgrade_dependencies:
            self.upgrade_dependencies(options, max_pip_retries)
        curr_working_set = self.working_set
        if deps_complete and not self.eq_working_sets(
            curr_working_set, prev_working_set
        ):
            while True:
                display(self.quiet, "\nPackages working set has changed.")
                prev_working_set = curr_working_set
                if uninstall_orphaned:
                    self.uninstall_orphaned()
                if upgrade_dependencies:
                    self.upgrade_dependencies(options, max_pip_retries)
                curr_working_set = self.working_set
                if self.eq_working_sets(curr_working_set, prev_working_set):
                    break
        if check_packages:
            self.check_packages()
        if clean_cache:
            self.clean_cache(cache_limit)
        display(self.quiet, "\nAll done.")
        self.diff_working_sets(initial_working_set, curr_working_set)


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    # TODO: this can be avoided if the "max_text_width" will be added to "ArgumentParser", see: https://bugs.python.org/issue39809
    class RawDescriptionHelpFormatterWidth80(argparse.RawDescriptionHelpFormatter):
        """Override terminal width = 80."""

        def __init__(self, prog):
            argparse.RawDescriptionHelpFormatter.__init__(self, prog, width=80)

    parser = argparse.ArgumentParser(
        prog="python -m easy_requp",
        description=__doc__.splitlines()[0],
        epilog=(
            "examples:"
            "\n  %(prog)s                  # full system upgrade"
            "\n  %(prog)s -r FILE          # use given requirements file"
            "\n  %(prog)s -a reqs          # upgrade required packages"
            "\n  %(prog)s -na clean        # do not clean pip cache"
            "\n  %(prog)s -u               # pass --user flag to pip"
            "\n  %(prog)s -uo \\--log PATH  # pass --user and --log flags to pip"
            "\n\nReport any bugs to: <https://github.com/lucatrv/easy-requp>"
        ),
        formatter_class=RawDescriptionHelpFormatterWidth80,
        allow_abbrev=False,
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=(
            f"Easy ReqUp version {__version__}"
            "\nCopyright (C) 2020 Luca Trevisani"
            "\nLicense GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>."
            "\nThis is free software: you are free to change and redistribute it."
            "\nThere is NO WARRANTY, to the extent permitted by law."
        ),
        help="show version information and exit",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="let pip give more output, option is additive and can be used up to 3 times, try 'pip help' for more information",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="count",
        default=0,
        help="let pip give less output, option is additive and can be used up to 3 times, try 'pip help' for more information",
    )
    parser.add_argument(
        "-y", "--yes", action="store_true", help="don't ask for confirmations"
    )
    parser.add_argument(
        "-s",
        "--skip-python-version-check",
        action="store_true",
        help="don't check for Python updates",
    )
    parser.add_argument(
        "-r",
        "--requirement",
        action="store",
        default="easy_requp.txt",
        help="install from the given requirements file, try 'pip help install' for more information (default: easy_requp.txt)",
        metavar="FILE",
        dest="requirements_file",
    )
    parser.add_argument(
        "-a",
        "--actions",
        action="store",
        nargs="+",
        default="all",
        choices=["all", "reqs", "deps", "orph", "check", "clean"],
        help="perform selected actions: %(choices)s (default: all)",
        metavar="ACTION",
    )
    parser.add_argument(
        "-n",
        "--not",
        action="store_true",
        help="invert actions selection",
        dest="invert_actions",
    )
    parser.add_argument(
        "-u",
        "--user",
        action="store_true",
        help="pass the --user flag to pip, try 'pip help install' for more information",
    )
    parser.add_argument(
        "-o",
        "--options",
        action="store",
        nargs="+",
        default=[],
        help="additional pip options, escape leading '-' character with '\\', try 'pip help' for more information",
        metavar="OPTION",
    )
    parser.add_argument(
        "-m",
        "--max-pip-retries",
        action="store",
        default=3,
        type=int,
        help="maximum number of retries if pip fails (default: 3)",
        metavar="N",
    )
    parser.add_argument(
        "-d",
        "--deps_complete",
        action="store_true",
        help="repeat dependencies upgrade until no changes are detected",
    )
    parser.add_argument(
        "-c",
        "--cache",
        action="store",
        default=200,
        type=int,
        help="clean cache if folder size is above given limit, in MB (default: 200)",
        metavar="LIMIT",
        dest="cache_limit",
    )
    args = parser.parse_args()
    if args.verbose > 3:
        exit_with_error(
            0,
            "Option --verbose can be used up to 3 times, try 'pip help' for more information.",
        )
    if args.quiet > 3:
        exit_with_error(
            0,
            "Option --quiet can be used up to 3 times, try 'pip help' for more information.",
        )
    if args.user:
        args.options.append("--user")
    args.options = [opt[1:] if opt.startswith("\\-") else opt for opt in args.options]
    for option in [
        "-r",
        "--requirement",
        "-c",
        "--constraint",
        "--no-deps",
        "-U",
        "--upgrade",
        "--upgrade-strategy",
    ]:
        if option in args.options:
            exit_with_error(
                0, f"Option {option} cannot be passed as additional pip option.",
            )
    return args


def main() -> None:
    """Parse arguments, create ReqUp object, and run it."""
    args = parse_args()
    display(args.quiet, "Easy ReqUp")
    requp = ReqUp(
        args.verbose,
        args.quiet,
        args.yes,
        args.skip_python_version_check,
        args.requirements_file,
    )
    requp.run(
        args.actions,
        args.invert_actions,
        args.options,
        args.max_pip_retries,
        args.deps_complete,
        args.cache_limit,
    )


if __name__ == "__main__":
    main()
