from setuptools import setup, find_packages

exec(open('version.py').read())

install_requirements = [
    'appdirs>=1.4.3',
    'boto3',
    'botocore',
    'docutils>=0.13.1',
    'flake8',
    'funcsigs>=1.0.2',
    'futures>=3.0.5',
    'jmespath>=0.9.2',
    'packaging>=16.8',
    'pbr>=2.0.0',
    'pyparsing>=2.2.0',
    'python-dateutil==2.6.0',
    's3transfer',
    'six>=1.10.0',
]

test_requirements = [
    'pytest',
    'moto'
]

setup(
    name='pym-nodb',
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
