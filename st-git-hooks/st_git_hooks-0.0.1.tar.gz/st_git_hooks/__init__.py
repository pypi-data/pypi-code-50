import os
import logging


def increment_version(version):
	res = version.split("-")
	if len(res) == 1:
		res = res[0].split(".")
		for i in range(len(res) - 1, -1, -1):
			try:
				_ind = int(res[i])
				res[i] = str(_ind + 1)
				break
			except ValueError:
				pass

		return ".".join(res)
	else:
		for i in range(len(res) - 1, -1, -1):
			_out = increment_version(res[i])
			if _out:
				res[i] = _out
				break
		return "-".join(res)


def get_version(root="."):
	_version_filename = os.path.join(root, "version.py")

	_locs = {}
	try:
		_code_file = open(_version_filename, "r")
		_code = _code_file.read()
		_code_file.close()
		exec(_code, {}, _locs)
	except IOError:
		logging.info("No such file: %s" % _version_filename)

	version = _locs.get("version", None)
	branch = _locs.get("branch", None)

	return branch, version


def print_version(root="./"):
	branch, version = get_version(root)

	print("Branch: %s" % branch)
	print("Version: %s" % version)

	return
