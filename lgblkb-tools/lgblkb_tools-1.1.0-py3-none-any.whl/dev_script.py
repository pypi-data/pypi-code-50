import subprocess

def run_cmd(commands,**kwargs):
	if isinstance(commands,str):
		steps=[commands]
	else:
		steps=commands
	for step in steps:
		print('step: ',step,'\n############################################')
		subprocess.run(step,**dict(dict(check=True,shell=True),**kwargs))

def export_reqs():
	steps=list()
	steps.append('poetry update')
	steps.append('poetry export -f requirements.txt > requirements.txt')
	run_cmd(steps)

def version_path():
	steps=list()
	steps.append('poetry version patch')
	run_cmd(steps)
