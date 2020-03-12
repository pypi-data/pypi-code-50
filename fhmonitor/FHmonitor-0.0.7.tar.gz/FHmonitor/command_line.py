from FHmonitor.monitor import Monitor  # noqa
import textwrap
import os
import stat
init_class_text_list = textwrap.wrap(("1) Create an instance of the "
                                      "Monitor class."), 50)
init_sensor_text_list = textwrap.wrap(("2) Initialize the energy meter..."
                                       "This can be tricky because accurate "
                                       "readings are dependent on calibrating "
                                       "params to init_sensor().  The param "
                                       " values depend on the Power "
                                       "Transformer and Current Transformers "
                                       "you are using.  "), 50)


def hello():
    print(*(init_class_text_list[i]
            for i in range(len(init_class_text_list))), sep='\n')
    m = Monitor()
    print('==================================================')
    print('Success! Created an instance of the Monitor class.')
    print('==================================================')
    print(*(init_sensor_text_list[i]
            for i in range(len(init_sensor_text_list))), sep='\n')
    m.init_sensor()  # Using defaults, You may need to change settings.
    pA, pR = m.take_reading()
    print('==================================================')
    print('Success! Took a reading.')
    print('==================================================')
    print(f'Active Power: {pA:.2f}, Reactive Power: {pR:.2f}')
    print('==================================================')


def start():
    """Get the systemd service up and running that runs FHmonitor_main.py

    TODO: Still not quite right...
    """
    systemd_path = os.path.join(os.path.dirname(__file__), 'systemd')
    # Set perms so systemd can run the python file.
    code_filename = systemd_path+'/FHmonitor_main.py'
    st = os.stat(code_filename)
    os.chmod(code_filename, st.st_mode | stat.S_IEXEC)
    code_filename = systemd_path+'/run_FHmonitor_main.sh'
    st = os.stat(code_filename)
    os.chmod(code_filename, st.st_mode | stat.S_IEXEC)

    # Copy service file where systemd expects it to be.
    service_path = systemd_path + '/FHmonitor_main.service'
    cmd_str = 'sudo cp ' + service_path + ' /lib/systemd/system/.'
    os.system(cmd_str)
    # Copy the bash script..
    bash_path = systemd_path + '/run_FHmonitor_main.sh'
    cmd_str = 'sudo cp ' + bash_path + ' /lib/systemd/system/.'
    os.system(cmd_str)
    # Enable the service
    os.system('sudo systemctl enable FHmonitor_main')
    print('============================')
    print('FHmonitor_main service is...')
    os.system('systemctl is-enabled FHmonitor_main')
    print('============================')
    # Start the service
    os.system('sudo systemctl start FHmonitor_main')
    print('...status...')
    status()
    print('============================')


def status():
    os.system('systemctl status FHmonitor_main')


def main():
    pass


if __name__ == "__main__":
    main()
