from os import path, chdir
from subprocess import call, check_output


def publish(script_path, version):
    # move to project root
    chdir(project_path(script_path))
    branch = check_output('git rev-parse --abbrev-ref HEAD').decode().strip()

    with open(version_path(script_path), 'w') as version_file:
        version_file.write(f"__version__ = '{version}'")

    call(f'git add {version_path(script_path)}')
    call(f'git commit -m "Release v{version}"')
    call(f'git push origin {branch}')
    call(f'git tag -a v{version} -m "Release v{version}"')
    call(f'git push origin v{version}')


def publish_patch(script_path: str):
    new_version = increment_patch(find_version(script_path))
    publish(script_path, new_version)


def publish_minor(script_path: str):
    new_version = increment_minor(find_version(script_path))
    publish(script_path, new_version)


def publish_major(script_path: str):
    new_version = increment_major(find_version(script_path))
    publish(script_path, new_version)


def find_version(script_path: str):
    version_dict = {}

    with open(version_path(script_path)) as version_file:
        exec(version_file.read(), version_dict)

    return version_dict['__version__']


def version_path(script_path: str) -> str:
    return path.join(package_path(script_path), '__version__.py')


def package_path(script_path: str) -> str:
    return path.join(project_path(script_path), package_name(script_path))


def package_name(script_path: str) -> str:
    return path.basename(project_path(script_path))


def project_path(script_path: str) -> str:
    return path.realpath(path.join(path.dirname(path.realpath(script_path)), '..'))


def increment_patch(version: str) -> str:
    major, minor, patch = version.split('.')

    return f'{major}.{minor}.{int(patch) + 1}'


def increment_minor(version: str) -> str:
    major, minor, patch = version.split('.')

    return f'{major}.{int(minor) + 1}.0'


def increment_major(version: str) -> str:
    major, minor, patch = version.split('.')

    return f'{int(major) + 1}.0.0'
