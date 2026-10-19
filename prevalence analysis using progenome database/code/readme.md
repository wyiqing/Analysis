# Local BLASTP Search

## Overview
This pipeline uses NCBI BLAST+ to perform local protein sequence similarity searches against a custom protein database.

## Software and source
- **NCBI BLAST+**: https://blast.ncbi.nlm.nih.gov/
- **Bioconda package**: https://bioconda.github.io/recipes/blast/README.html
- **Conda documentation**: https://docs.conda.io/

## Environment setup
```bash
conda create -n blastp_env -c conda-forge -c bioconda blast -y
conda activate blastp_env
```

## Input files
- `query.fasta`: Query protein sequences.
- `proteins.fasta`: Target protein sequences for the local database.

## Parameters
- E-value: `1e-20`
- Threads: `4`
- Output format: Tabular (format 6)
