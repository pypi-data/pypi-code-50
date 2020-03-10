# this script imports the p4a_dependencies.csv file and creates a formatted text to display attributions in the
# binary application (i.e. Android APK)
# p4a_dependencies.csv must be a tab separated file with " as delimiter for multiline arguments

import csv
# from simple_plotter4a import __version__
import os
import warnings


def read_version():
    """Reads the version.txt file"""
    try:
        with open('simple_plotter4a/version.txt', 'r') as file:
            version = file.read()
    except FileNotFoundError:
        raise FileNotFoundError('Could not find version.txt - run create_version_files.py first!')

    return version


def read_csv_deps():
    """Reads the csv file with the dependencies"""

    # read csv file
    dependencies = []
    header_items = []
    with open('Licenses/p4a_dependencies.csv', 'r') as file:
        csv_data = csv.reader(file, delimiter='\t', quotechar='\"')
        for i, entry in enumerate(csv_data):
            entry_dict = {}
            for j, attr in enumerate(entry):
                if i == 0:
                    header_items.append(attr)
                else:
                    entry_dict[header_items[j]] = attr
            if i > 0:
                dependencies.append(entry_dict)

    return dependencies


def create_android_bin_attributions(dependencies, sp4a_version):
    """Creates a file with the attributions for the Android binary version"""
    # extract special acknowledgements and create attribution strings
    special_acknowledgements = []
    attributions_str = ''
    for entry in dependencies:
        # print(entry)
        if entry['Special Conditions – Acknowledgements'] != '':
            special_acknowledgements.append(entry['Special Conditions – Acknowledgements'])

        if entry['version'] == '?':
            attributions_str = attributions_str + '{package}\n'.format(**entry)
        else:
            attributions_str = attributions_str + '{package} {version}\n'.format(**entry)
        if entry['Attribution'] == '':
            attributions_str = attributions_str + '{link}\n\n'.format(**entry)
        else:
            attributions_str = attributions_str + '{Attribution}\n{link}\n\n'.format(**entry)

    # prepend special acknowledgments
    ack_str = ''
    for ack in special_acknowledgements:
        ack_str = ack_str + ack + '\n\n'

    attributions_str = ack_str + attributions_str
    # print(attributions_str)

    attr_file = 'simple_plotter4a/data/attributions_android_{}.txt'.format(sp4a_version)
    with open(attr_file, 'w') as file:
        file.write(attributions_str)

    print('Exported {} attributions to {}'.format(len(dependencies), attr_file))


def create_python_attributions(dependencies, sp4a_version):
    """Creates a file for the attributions of the python interpreted GUI versions"""

    attributions_str = ''
    for entry in dependencies:
        if entry['platform'] == 'all':
            attributions_str = attributions_str + '{package}\n{link}\n\n'.format(**entry)

    # print(attributions_str)

    attr_file = 'simple_plotter4a/data/attributions_python_{}.txt'.format(sp4a_version)
    with open(attr_file, 'w') as file:
        file.write(attributions_str)

    print('Exported {} attributions to {}'.format(len(dependencies), attr_file))


def create_attributions_rst(dependencies, sp4a_version):
    """Creates an rst file with the attributions for the Android release"""

    # get list of available license files
    available_lic_files = []
    for root, dirs, files in os.walk('Licenses'):
        for file in files:
            if 'LICENSE' in file:
                available_lic_files.append(file)

    # check if license file exists for all dependencies
    for entry in dependencies:
        if entry['version'] == '?':
            warnings.warn('No version defined for {package}'.format(**entry))
            license_file_name = 'LICENSE.{package}'.format(**entry)
        else:
            license_file_name = 'LICENSE.{package}-{version}'.format(**entry)

        if license_file_name not in available_lic_files:
            raise FileNotFoundError('Could not find License file for {package}-{version}'.format(**entry))

        entry['license_file'] = license_file_name

    print('Found license files for all {} defined dependencies.'.format(len(dependencies)))



    # write the rst file
    # create header
    rst_file_content = 'simple-plotter4a rel. {}'.format(sp4a_version)
    underline = '=' * len(rst_file_content)
    rst_file_content = rst_file_content + '\n' + underline + \
                       '\n\n\nThis chapter shows the copyright and license notes of *simple-plotter4a* and the ' \
                       'dependencies used to build *simple-plotter4a*.\n\n\n.. code-block:: none\n\n'

    # open the simple-plotter4a NOTICE file
    with open('NOTICE', 'r') as notice_file:
        sp4a_license = notice_file.readlines()
    for line in sp4a_license:
        rst_file_content = rst_file_content + '    ' + line

    rst_file_content = rst_file_content + '\n\n\n' \
                                          'Dependencies\n' \
                                          '------------\n\n\n'

    for entry in dependencies:
        if entry['version'] != '?':
            dep_title = '{package} {version}'.format(**entry)
        else:
            dep_title = '{package}'.format(**entry)
        underline = '~' * len(dep_title)

        entry_str = dep_title + '\n' + underline + '\n\n'

        if entry['Attribution'] != '':
            entry_str = entry_str + entry['Attribution'] + '\n\n'

        entry_str = entry_str + entry['link'] + '\n\n\n\n.. code-block:: none\n\n'

        license_file = 'Licenses/' + entry['license_file']
        with open(license_file, 'r') as file:
            license_file_lines = file.readlines()

            # indent license file lines with 4 spaces
            for line in license_file_lines:
                entry_str = entry_str + '    ' + line

        rst_file_content = rst_file_content + entry_str + '\n\n\n'

    rst_filename = 'Licenses/attributions_{}.rst'.format(sp4a_version)
    with open(rst_filename, 'w') as rst_file:
        rst_file.write(rst_file_content)

    print('ReST file written to {}'.format(rst_filename))


if __name__ == '__main__':

    version = read_version()
    dependencies = read_csv_deps()
    create_android_bin_attributions(dependencies, version)
    create_python_attributions(dependencies, version)
    create_attributions_rst(dependencies, version)
