# BLASTP Search and BioSample Statistics

## 1. Overview

This workflow identifies mNEP homologs in *Lactobacillus* and *Ligilactobacillus* using BLASTP and summarizes BioSample information from the ProGenomes database.

## 2. Workflow

### Step 1. BLASTP Search

Install BLAST+ using Conda:

```bash
conda install -c bioconda blast
```

BLASTP searches were performed against local protein databases using an E-value threshold of \(10^{-20}\). Redundant records with identical sequence IDs and protein sequences were removed, and column headers were added to the output files.

**Output files:**
- `blastp_lac_e20_results_plusHeaderCol.tsv`
- `blastp_lig_e20_results_plusHeaderCol.tsv`

Records with complete BioSample information:
- *Lactobacillus*: 2,155
- *Ligilactobacillus*: 565

### Step 2. BioSample Extraction from ProGenomes

BioSample identifiers were extracted and summarized from the following contig FASTA files obtained from the ProGenomes database [1]:

- `genus-Lactobacillus.all_contigs.fasta`
- `genus-Ligilactobacillus.all_contigs.fasta`

**Output files:**
- `genus-Lactobacillus_all_headers_twoStepFinal`
- `genus-Ligilactobacillus_all_headers_twoStepFinal`

Records with complete BioSample information:
- *Lactobacillus*: 2,372
- *Ligilactobacillus*: 576

Detailed counting results are provided in the accompanying report file.

## Reference

1. Fullam A, et al. proGenomes4: providing 2 million accurately and consistently annotated high-quality prokaryotic genomes. *Nucleic Acids Research*. 2025; gkaf1208.
