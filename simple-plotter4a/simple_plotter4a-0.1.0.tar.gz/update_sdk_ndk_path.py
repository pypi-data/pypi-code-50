#!/bin/python3
import sys

"""Script to update SKD and NDK path in buildozer.spec for F-Droid build
This scrip should be called in prebuild stage with cmd args $$SDK$$ $$NDK$$ - i.e.
python3 update_sdk_ndk_path.py $$SDK$$ $$NDK$$
"""

if __name__ == '__main__':

    if len(sys.argv) != 3:
        raise AssertionError('Needs exactly two arguments: SDK- and NDK-path')

    with open('buildozer.spec', 'r') as file:
        spec_lines = file.readlines()

    for i, line in enumerate(spec_lines):
        if 'android.sdk_path =' in line:
            spec_lines[i] = 'android.sdk_path = {}\n'.format(sys.argv[1])
            print('Found SDK path definition in line', i+1)
        if 'android.ndk_path =' in line:
            spec_lines[i] = 'android.ndk_path = {}\n'.format(sys.argv[2])
            print('Found NDK path definition in line', i + 1)

    with open('buildozer.spec', 'w') as file:
        file.writelines(spec_lines)

    print('buildozer.spec updated.')
