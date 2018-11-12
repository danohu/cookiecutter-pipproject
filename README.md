CookieCutter Pip-Project
========================

A cookiecutter template for python projects intended to be pip-installed, based on [cookiecutter](https://github.com/audreyr/cookiecutter)

Features
--------

* Testing environment with [tox](https://github.com/tox-dev/tox) for Python 2.7 and 3.6, with
  * Tests with [pytest](https://docs.pytest.org/en/latest/)
  * Style checking with [Flake8](http://flake8.pycqa.org/en/latest/)
* Continuous integration with [Travis-CI](https://travis-ci.org)
* Coverage with [coveralls](http://coveralls.io/)
* Automated [PyPI](https://pypi.org/) releases [via Travis-CI](https://docs.travis-ci.com/user/deployment/pypi/)
* Configuration for
  * [bumpversion](https://github.com/peritus/bumpversion)
  * [yapf](https://github.com/google/yapf)


Usage
-----------------------------------

1. Generate a Python package project with [cookiecutter](https://github.com/audreyr/cookiecutter) as in 

        pip install cookiecutter
        cookiecutter https://github.com/martibosch/cookiecutter-pipproject.git
        
    You will be asked about your basic info (name, project name, short description, etc.), which will be used in your new project.
  
2. Create a git repository for the project

3. Add the repository to your [Travis-CI](https://travis-ci.org) account

4. Add the repository to your [coveralls](http://coveralls.io/) account

5. Register your project to [PyPI](https://pypi.org/) e.g. via [twine](https://github.com/pypa/twine)

        pip install twine
        python setup.py sdist bdist_wheel
        twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

6. Add your encrypted PyPI password to the `.travis.yml` file for automated PyPI deployment. Note that this requires the [Travis command line tool](https://github.com/travis-ci/travis)

        travis encrypt --add deploy.password

Thereupon, each time you push a tag to the master branch, successful [Travis-CI](https://travis-ci.org) builds will automatically deploy your package to PyPI
