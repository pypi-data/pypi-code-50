"""Console script for safe_reboot."""
import subprocess
import sys
import argparse
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


def main():
    end_param = []
    if '--' in sys.argv:
        idx = sys.argv.index('--')
        begin_param = sys.argv[:idx]
        end_param = sys.argv[idx:]
        end_param.pop(0)
    else:
        begin_param = sys.argv

    parser = argparse.ArgumentParser(description="Wrapper around reboot. Checks if other users are logged in or have active screen or tmux sessions. All arguments after '--' are passed to the reboot command.")
    parser.add_argument('-f', '--force', help="Force reboot", action="store_true")
    parser.add_argument('-s', '--show', help="Only show active users", action="store_true")
    parser.add_argument('-d', '--dry', help="Do not perform reboot", action="store_true")

    args = parser.parse_args(begin_param[1:])

    """Console script for safe_reboot."""
    safe = is_it_safe_to_reboot(args.show)

    try:
        if (safe or args.force) and not args.dry and not args.show:
            print("CAUTION! Do you really want to restart? If so type 'yes':")
            response = input('').lower().strip()
            if response == "yes":
                print("rebooting ...")
                try:
                    subprocess.check_output(["/sbin/reboot"] + end_param)
                except subprocess.CalledProcessError:
                    print("Do you have the correct permissions?", file=sys.stderr)
                    sys.exit(-1)
            else:
                print("abort reboot")
    except KeyboardInterrupt:
        print("abort reboot")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
