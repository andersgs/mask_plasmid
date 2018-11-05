## mask-plasmid: Create a quick BED file from an assembled genome

[![Build Status](https://travis-ci.org/andersgs/mask_plasmid.svg?branch=master)](https://travis-ci.org/andersgs/mask_plasmid)

## Background

When building phylogenetic trees with microbial genomic data, it is essential to
get as close as possible to the clonal frame.

A common technique for identifying the clonal frame is to map reads to a reference
genome, and then filter out any sites that are not present in all the samples of
interest.

In general, plasmids should not be part of the clonal frame. While theoretically
it is possible they are part of the clonal frame, with short read data it is
hard to say if the plasmids are all the same. More importantly, however, it is
quite impossible to say that the plasmid(s) and the chromosomes have been
vertically inherited from the most recent common ancestor of a sample.

Thus, it is generally recommended that plasmids be removed from the analyses.

The problem arises in small read data when it is not quite possible to say with
certainty if a read belongs in the plasmid or in the chromosomes. Sometimes plasmids
get inserted in chromosomes, sometimes reads should map to a plasmid but erroneously
map to the chromosome because the plasmid was not included in the analysis.
Thus, in the context of mapping reads to a reference to identify potential variants and
the clonal frame, the ambiguous reads (i.e., that could either map on the chromosome or
on a plasmid) should be removed from the pool of potential reads used to identify variant sites.

If one removes the plasmids from the reference dataset before attempting to map the
reads then it is not possible to identify ambiguous reads. Thus, a better strategy
might be to keep the plasmids in the reference dataset, map all the reads, identify
variable sites, and then mask the plasmid sites.

This can be achieved using [Snippy 4](https://github.com/tseemann/snippy) by using the
`--mask` option and giving it a BED file.

## What does this tool do?

This tool will produce a BED file with every locus in a Genbank file, which can
be easily edited and then used to `--mask` plasmids when using `Snippy 4`.

### Installation

```
pip install mask-plasmid
```

### Running

```
mask-plasmid <my_gb.gbk[.gz]> > plasmids.bed
```

## Development

### Pushing to Pypi

The following command will:

- run tests
- clean up the current branch
- bump the version
- generate the distributions
- clean up the current branch
- tag the commit with the version
- push to github
- push to pypi

```
pipenv run inv deploy <new_version_number> [<patch|minor|major>]
```
