info = """This script checks if the APK version and the manifest version are identical

This is helpful since VersionCodes cannot be defined in buildozer.spec and AndroidManifest.xml will only be used
in the F-Droid build process for signing the APK. Therefore the VersionCode and VersionName must match the APK.
This script can be run locally (with a local tag) before the tag is pushed to the source repo and an F-Droid build job
is triggered.

The typical use case for this script would be:

1. Make changes to the source code
2. Commit changes
3. Add a local git tag
4. Build a release APK with 'ant release'
5. run this script - it will compare the VersionCode and VersionName of the APK with info in AndroidManifest.xml
    - if it differs will ask for patching AndroidManifest.xml
6. In case the AndroidManifest.xml has been patched:
    a. Delete the git tag on last commit
    b. Commit the changes (modified AndroidManifest.xml)
    c. Add the tag again on the new commit
7. push commits and tags to origin - i.e. F-Droid will see a new release and start a build job with correct VersionCode

"""

print(info)

import subprocess
import os
import re

# get APK info - assuming APK is in bin-folder
apk_file = None
for root, dirs, files in os.walk('bin'):
    for file in files:
        if '.apk' in file:
            apk_file = file
            break

if apk_file is None:
    raise FileNotFoundError('Could not find an APK file!')

# try to find aapt in buildtools
try:
    android_home = os.environ['ANDROID_HOME']
except KeyError:
    raise KeyError('Could not find Android SDK folder. Please set ANDROID_HOME environment variable accordingly.')

# try to get latest android build-tools
build_tool_latest = None
tool_code = 0
for root, dirs, files in os.walk('{}/build-tools'.format(android_home)):
    for folder in dirs:
        match_code = re.match(pattern='^[0-9]+\.[0-9]+\.[0-9]+', string=folder)
        if match_code:
            major = int(match_code.group().split('.')[0])
            minor = int(match_code.group().split('.')[1])
            patch = int(match_code.group().split('.')[2])
            new_tool_code = major * 10**6 + minor * 10**3 + patch
            if new_tool_code > tool_code:
                build_tool_latest = folder
                tool_code = new_tool_code

if build_tool_latest is None:
    raise FileNotFoundError('Could not find any version of Android SDK build-tools. Make sure build-tools is installed'
                            'in your ANDROID_HOME path.')

# check if aapt is present
aapt_found = os.path.isfile('{}/build-tools/{}/aapt'.format(android_home, build_tool_latest))
if not aapt_found:
    raise FileNotFoundError('Could not find \'aapt\' in build-tools!')

# run aapt to get APK infor
status, output = subprocess.getstatusoutput('{}/build-tools/{}/aapt dump badging bin/{}'.format(android_home,
                                                                                                build_tool_latest,
                                                                                                apk_file))

# extract versionCode and versionName
if status == 0:
    vercode_match = re.search('versionCode=\'[0-9]+\'', output)
    apk_versionCode = vercode_match.group().split('\'')[1]
    vername_match = re.search('versionName=\'[0-9]+.[0-9]+.[0-9]+\'', output)
    apk_versionName = vername_match.group().split('\'')[1]
    # print('APK versionCode: {}, versionName: {}'.format(apk_versionCode, apk_versionName))
else:
    raise ValueError('aapt command failed...')

with open('AndroidManifest.xml', 'r') as file:
    manifest_data = file.read()
    vercode_match = re.search('versionCode=\"[0-9]+\"', manifest_data)
    manifest_versionCode = vercode_match.group().split('\"')[1]
    vername_match = re.search('versionName=\"[0-9]+.[0-9]+.[0-9]+\"', manifest_data)
    manifest_versionName = vername_match.group().split('\"')[1]

# compare values
print('Result comparision\n'
      '------------------')
print('versionCodes - APK={} vs. AndroidManifest.xml={} - '.format(apk_versionCode, manifest_versionCode), end='')
if apk_versionCode == manifest_versionCode:
    versionCodes_match = True
    print('match')
else:
    versionCodes_match = False
    print('no match!')

print('versionNames - APK={} vs. AndroidManifest.xml={} - '.format(apk_versionName, manifest_versionName), end='')
if apk_versionName == manifest_versionName:
    versionNames_match = True
    print('match')
else:
    versionNames_match = False
    print('no match!')

if versionCodes_match and versionNames_match:
    print('versionCodes and versionNames okay - nothing to patch.\n\n'
          'You can now push commits and tags to origin - i.e. F-Droid will see a new release and start a build '
          'job with correct VersionCod"')
else:
    resp = input('Found mismatch between APK and AndroidManifest.xml - '
                 'shall AndroidManifest.xml be patched?[y/n=default]')
    if resp in ['y', 'Y']:
        # replace version code and name
        manifest_data = re.sub('versionCode=\"[0-9]+\"', 'versionCode=\"{}\"'.format(apk_versionCode), manifest_data)
        manifest_data = re.sub('versionName=\"[0-9]+.[0-9]+.[0-9]+\"', 'versionName=\"{}\"'.format(apk_versionName),
                               manifest_data)

        with open('AndroidManifest.xml', 'w') as file:
            file.write(manifest_data)
        print('\nAndroidManifest.xml has been updated. '
              'New versionCode=\"{}\", new versionName=\"{}\"'.format(apk_versionCode, apk_versionName))

        print("\nYou should do following steps:\n"
              "a. Delete the git tag on last commit\n"
              "b. Commit the changes (modified AndroidManifest.xml)\n"
              "c. Add the tag again on the new commit\n"
              "d. run this script again.")
