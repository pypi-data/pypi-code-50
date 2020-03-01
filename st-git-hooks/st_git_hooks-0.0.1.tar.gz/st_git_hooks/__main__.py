import os
import sys
import shutil
import logging
from git import Repo

from . import increment_version


if __name__ == "__main__":

	logging.basicConfig(level=logging.INFO)

	if len(sys.argv) > 2:
		version_filename = os.path.join(sys.argv[2], "version.py")
	else:
		version_filename = "version.py"

	_locs = {}
	try:
		_code_file = open(version_filename, "r")
		_code = _code_file.read()
		_code_file.close()
		exec(_code, {}, _locs)
	except IOError as e:
		logging.info("No such file: %s" % version_filename)

	version = _locs.get("version", "0.0.0")

	# get current branch
	branch = Repo("./").active_branch.name

	if sys.argv[1] == "precommit":

		version = increment_version(version)

		with open(version_filename, "w") as _code_file:
			_code = "branch = \"%s\"\nversion = \"%s\"\n" % (branch, version)
			_code_file.write(_code)

		# add changed version file
		Repo("./").git.add(version_filename)

	elif sys.argv[1] == "postcommit":

		Repo("./").git.tag("%s_%s" % (branch, version))

	elif sys.argv[1] == "init":
		_dirname = os.path.dirname(__file__)
		if len(sys.argv) > 2:
			_version_root = sys.argv[2]
		else:
			_version_root = "./"

		_pre_commit_fn = os.path.join(".git", "hooks", "pre-commit")
		_post_commit_fn = os.path.join(".git", "hooks", "post-commit")
		shutil.copy(os.path.join(_dirname, "pre-commit"), _pre_commit_fn)
		shutil.copy(os.path.join(_dirname, "post-commit"), _post_commit_fn)

		with open(_pre_commit_fn, "a") as _file:
			_file.write(" %s" % _version_root)

		with open(_post_commit_fn, "a") as _file:
			_file.write(" %s" % _version_root)
