'''
A small script to connect the existing ssh agent

installation: 
  pip install ssh-connect

usage:

  eval $(python -m ssh-connect)

You can give this command an alias to simplify the it:   
Add the following line to you bashrc (Usually `~/.bashrc` (current user) or 
`/etc/bashrc` (global); if you use Git For Windows, it's `/etc/bash.bashrc`)

  alias ssh-connect='python -m ssh-connect'

Then you can use the command

  eval $(ssh-connect)

The command finds the first existing ssh agent and connect it.
Note: If you have more than one ssh agent running in the background, which agent
that would be connected is undefined. 
'''