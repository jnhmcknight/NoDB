from setuptools import setup, find_packages

exec(open('nodb/version.py').read())

install_requirements = [
    'boto3'
]

test_requirements = [
    'flake8',
    'moto',
    'pytest',
]

setup(
    name='pym_nodb',
    author='Anderson Reyes',
    author_email='anderson@pymetrics.com',
    version=__version__,  # noqa
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description="NoDB isn't a database.. but it sort of looks like one.",
    install_requires=install_requirements,
    tests_require=test_requirements,
    setup_requires=['pytest-runner'],
    extras_require={
        'dev': test_requirements
    }

)
