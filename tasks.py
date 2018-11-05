'''
Some basic tasks related to deployment of mask_plasmids
'''

import logging
import os

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


@task(test, help={"new_version": "New version to use", "update_type": "Either patch, minor, or major.", "bump_version": "Whether or not to bump version."})
def deploy(c, new_version, update_type="patch", bump_version=True):
    '''
    Deploy a new version
    '''
    pbr_version = {"PBR_VERSION": f{new_version}}
    os.environ.update(pbr_version)
    c.run("pipenv run pipenv_to_requirements")
    if bump_version:
        c.run(
            f"pipenv run bumpversion --new-version {new_version} {update_type}")
    c.run("pipenv run python setup.py sdist bdist bdist_wheel")
    c.run(f"git commit -a -m 'Version {new_version}'")
    c.run(f"git tag {new_version}")
    c.run("git push --tags")
    c.run("pipenv run twine check dist/*")
    c.run("pipenv run twine upload dist/*")
