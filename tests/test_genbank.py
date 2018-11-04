'''
A test of mask_plasmids when the input is Genbank.
'''

import pathlib
import pytest
import click
from click.testing import CliRunner
from mask_plasmid import run_mask_plasmid

fn = pathlib.Path(__file__).parent / \
    "GCF_000015525.1_ASM1552v1_genomic.gbff.gz"


def test_with_genbank():
    runner = CliRunner()
    result = runner.invoke(run_mask_plasmid.run_mask, [str(fn)])
    assert result.exit_code == 0
    assert result.output == 'NC_008787.1\t1\t1616554\nNC_008790.1\t1\t45025\nNC_008770.1\t1\t37473\n'
