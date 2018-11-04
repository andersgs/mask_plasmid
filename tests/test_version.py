'''
A test of mask_plasmid --version option
'''

import pathlib
import pytest
import click
from click.testing import CliRunner
from mask_plasmid import run_mask_plasmid
from mask_plasmid import __version__ as VERSION


def test_version_string():
    runner = CliRunner()
    result = runner.invoke(run_mask_plasmid.run_mask, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"mask-plasmid {VERSION}\n"
