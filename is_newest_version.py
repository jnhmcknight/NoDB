import os
from distutils.version import StrictVersion
import requests


PACKAGE_NAME = 'pym_nodb'
exec(open('nodb/version.py').read())


def versions(package_name):
    url = '{}/{}/json'.format(
        os.environ.get('TWINE_REPOSITORY_URL'), package_name)
    user = os.environ.get('TWINE_USERNAME')
    password = os.environ.get('TWINE_PASSWORD')
    response = requests.get(url, auth=(user, password))
    data = response.json()
    versions = list(data["releases"].keys())
    versions.sort(key=StrictVersion)
    return versions

if not StrictVersion(__version__) > StrictVersion(versions(PACKAGE_NAME)[-1]):  # noqa
    print("Version would not be the newest version.")
    exit(1)
print("Version would be the newest version.")
