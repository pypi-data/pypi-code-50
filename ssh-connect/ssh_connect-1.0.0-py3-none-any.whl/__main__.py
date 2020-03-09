import sys, os, tempfile, re, argparse

parser = argparse.ArgumentParser(
  usage = 'eval $(python -m %(prog)s)'
  )
parser.parse_args()

agent_prop = {
  'pid': -1, 
  'sock': ''
}

sockdir_pattern = re.compile(r'^ssh-\w+')
# ssh-pffba81A3rZG
td = tempfile.gettempdir()

td_content = next(os.walk(td))

for diritem in td_content[1]:
  if sockdir_pattern.fullmatch(diritem):
    sockdir = td + os.sep + diritem
    agent_prop['sock'] = sockdir + os.sep + os.listdir(sockdir)[0]
    pid_span = re.search(r'\d+$', agent_prop['sock']).span()
    agent_prop['pid']  = int(agent_prop['sock'][pid_span[0] : pid_span[1]]) + 1
    break

# print(agent_prop)

if not (agent_prop['pid'] >= 0 and len(agent_prop['sock'])):
  print('No ssh agent found, use "eval $(ssh-agent -s)" to start an agent')
  exit()

print('''
SSH_AUTH_SOCK=\'{0}\'; export SSH_AUTH_SOCK;
SSH_AGENT_PID={1}; export SSH_AGENT_PID;
echo 'Connected to PID {1}'
'''.format(agent_prop['sock'], agent_prop['pid']));
# SSH_AUTH_SOCK=/tmp/ssh-LTXtFkwqQpxx/agent.507; export SSH_AUTH_SOCK;
# SSH_AGENT_PID=508; export SSH_AGENT_PID;
# echo Agent pid 508;
