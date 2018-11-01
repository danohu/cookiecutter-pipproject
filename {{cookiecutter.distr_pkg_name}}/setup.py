from io import open  # compatible enconding parameter
from setuptools import setup, find_packages
from os import path

__version__ = '{{cookiecutter.version}}'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [
    x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')
]

setup(
    name='{{cookiecutter.distr_pkg_name}}',
    version=__version__,
    description='{{cookiecutter.project_short_description}}',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.distr_pkg_name}}',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    license='GPL-3.0',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
)
