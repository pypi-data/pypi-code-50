import random, string
from subprocess import Popen, PIPE
import shlex
from colab_ssh._command import run_command, run_with_pipe
import time



def launch_ssh(password, token):

  run_command("kill $(ps aux | grep 'ngrok' | awk '{print $2}')")
  #Download ngrok
  run_command("wget -q -nc https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
  run_command("unzip -qq -n ngrok-stable-linux-amd64.zip")
  run_command("apt-get install -qq -o=Dpkg::Use-Pty=0 openssh-server pwgen")
  run_command("echo root:$password | sudo chpasswd")
  run_command("mkdir -p /var/run/sshd")
  run_command("echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config")
  run_command('echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config')
  run_command('echo "LD_LIBRARY_PATH=/usr/lib64-nvidia" >> /root/.bashrc')
  run_command('echo "export LD_LIBRARY_PATH" >> /root/.bashrc')
  run_command('/usr/sbin/sshd -D')
  print("Copy authtoken from https://dashboard.ngrok.com/auth")
  import getpass

  #Create tunnel
  #get_ipython().system_raw('./ngrok authtoken $authtoken && ./ngrok tcp 22 &')
  Popen(shlex.split('./ngrok tcp --authtoken {} 22'.format(token)), stdout=PIPE,stderr=PIPE,stdin=PIPE)
  time.sleep(1)

  #Print root password
  print("Root password: {}".format(password))

  #Get public address
  info = run_with_pipe('''curl http://localhost:4040/api/tunnels | python3 -c "import sys, json; print(json.load(sys.stdin)['tunnels'][0]['public_url'])"''')
  
  print("Successfully running", info)
  

