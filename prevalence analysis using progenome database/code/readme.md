# BLAST+ Installation and Setup on Linux

## 1. Overview

This guide describes how to install and configure NCBI BLAST+ on Linux using Conda for local protein sequence similarity searches.

## 2. Installation

Install BLAST+ in a dedicated Conda environment:

```bash
conda create -n blast_env -c conda-forge -c bioconda blast -y
```

Activate the environment:

```bash
conda activate blast_env
```

## 3. Verify Installation

Check the installed BLASTP version:

```bash
blastp -version
```

Display the available command-line options:

```bash
blastp -help
```

## 4. Usage Example

Run a BLASTP search against a local protein database:

```bash
blastp \
  -query query.fasta \
  -db protein_db \
  -out blastp_results.tsv \
  -evalue 1e-20 \
  -num_threads 8 \
  -outfmt 6
```

**Note:** The local protein database must be formatted using `makeblastdb` before running the search. For example:

```bash
makeblastdb \
  -in protein_sequences.fasta \
  -dbtype prot \
  -out protein_db
```

## 5. References

- [NCBI BLAST+ Command Line Applications User Manual](https://www.ncbi.nlm.nih.gov/books/NBK279690/)
- [Bioconda](https://bioconda.github.io/)
