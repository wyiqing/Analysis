# mNEP Homolog Identification and Phylogenetic Analysis

## 1. Overview

This workflow identifies candidate mNEP homologs using phmmer, intersects the search results, filters sequences based on taxonomic information from gut microbe, and constructs a phylogenetic tree using MAFFT, trimAl, and IQ-TREE 3.

## 2. Workflow

### Step 1. phmmer Search and Intersection

- Search protein sequences using phmmer with an E-value threshold of \(10^{-10}\).
- Retain hits annotated with both M13N and M13 domains and assigned to the taxonomic group Bacteria.
- Identify the intersection of sequences satisfying these criteria.

### Step 2. Filter Taxa Using 16S Sequencing Data from GreenGene2

Identify genus-level taxonomic annotations in the 16S sequencing dataset. 

### Step 3. Multiple Sequence Alignment with MAFFT

Perform multiple sequence alignment using the selected MAFFT high-accuracy strategy.

### Step 4. Alignment Trimming with trimAl

Remove poorly aligned and gap-rich positions using the `gappyout` method.

### Step 5. Phylogenetic Tree Construction with IQ-TREE 3

Construct a maximum-likelihood phylogenetic tree using the LG substitution model, with 1,000 ultrafast bootstrap replicates and 1,000 SH-aLRT replicates.

Final tree file:

`mafft_L_trim_gappy.fasta_restored.treefile`



