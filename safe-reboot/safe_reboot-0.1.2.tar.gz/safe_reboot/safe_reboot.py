"""Console script for safe_reboot."""
import subprocess
import sys
import click
import shlex
import platform
import pwd


def get_all_user_tty_mac():
    cmd = shlex.split("ps axo user,tty")
    out = subprocess.check_output(cmd).decode("utf-8")
    lines = out.strip().split('\n')
    lines = [x.split() for x in lines[1:]]
    users = dict()
    for line in lines:
        # Only consider non root and non system user ttys
        if line[0].startswith("_") or line[0] == 'root' or line[1] == "??":
            continue
        else:
            if line[0] not in users.keys():
                users[line[0]] = set()
            users[line[0]].add(line[1])
    return users


def get_all_user_tty_linux():
    cmd = shlex.split("ps axno user,tty")
    out = subprocess.check_output(cmd).decode("utf-8")
    lines = out.strip().split('\n')
    lines = [x.split() for x in lines[1:]]
    users = dict()
    for line in lines:
        # Only cconsider user ids
        if int(line[0]) < 1000 or int(line[0]) >= 65530 or line[1] == "?":
            continue
        else:
            if line[0] not in users.keys():
                users[line[0]] = set()
            users[line[0]].add(line[1])
    # Assign names to users:
    u = dict()
    for key in users.keys():
        user_name = pwd.getpwuid(int(key))[0]
        u[user_name] = users[key]
    return u


def is_it_safe_to_reboot(show=False):
    if platform.system() == 'Darwin':
        users = get_all_user_tty_mac()
    elif platform.system() == 'Linux':
        users = get_all_user_tty_linux()
    else:
        print("OS not supported!: {}"
              .format(platform.system()), file=sys.stderr)
        sys.exit(-1)
    if len(users.keys()) > 1 or show:
        print("Following users are active on the system:")
        for key in users.keys():
            print("{} has {} active ttys.".format(key, len(users[key])))

        if len(users.keys()) > 1:
            print("WARNING: It is not safe to reboot this machine. "
                  "Other users are currently working here!")

    if len(users.keys()) > 1:
        return False
    else:
        return True


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.option('--force', '-f', help="Force reboot",
              default=False, is_flag=True)
@click.option('--show', '-s', help="Only show active users",
              default=False, is_flag=True)
@click.option('--dry', '-d', help="Do not perform reboot",
              default=False, is_flag=True)
def main(force, show, dry):
    """Console script for safe_reboot."""
    safe = is_it_safe_to_reboot(show)

    if (safe or force) and not dry:
        print("rebooting ...")
        try:
            subprocess.check_output("/sbin/reboot")
        except subprocess.CalledProcessError:
            print("Do you have the correct permissions?", file=sys.stderr)
            sys.exit(-1)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
