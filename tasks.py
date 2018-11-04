'''
Some basic tasks related to deployment of mask_plasmids
'''

import logging

from invoke import task


@task
def test(c):
    '''
    Run tests
    '''
    c.run("pipenv run pytest")


@task(help={"new_version": "New version to use", "update_type": "Either patch, minor, or major."})
def test_version_bump(c, new_version, update_type="patch"):
    '''
    Test version bump
    '''
    c.run(
        f"pipenv run bumpversion --verbose --dry-run --new-version {new_version} {update_type}")


@task(test, help={"new_version": "New version to use", "update_type": "Either patch, minor, or major."})
def deploy(c, new_version, update_type="patch"):
    '''
    Deploy a new version
    '''
    c.run(f"pipenv run bumpversion --new-version {new_version} {update_type}")
    c.run("git push")
    c.run("pipenv run python setup.py sdist bdist_wheel")
    c.run("pipenv run twine check dist/*")
    c.run("pipenv run twine upload dist/*")
