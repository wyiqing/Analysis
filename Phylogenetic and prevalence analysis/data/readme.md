This collection is a multi-user shareable SnapGene resource.
Files can be added and removed through SnapGene 4.0+ or with a file browser like Finder in macOS, File Explorer in Windows, or Nautilus in Linux.

##  Identification and Filtering of M13 Peptidase Homologs

Protein sequences were searched against the Reference Proteomes (2025-01) dataset using HMM-based searching with an E-value threshold of \(10^{-10}\). Sequences assigned to Bacteria were retained, yielding 4,762 sequences in the `taxonomy` file.

Based on domain architecture, sequences containing both the M13_N and M13 domains were further identified, yielding 3,623 sequences in the `phmmer_M13_N_M13_peptidase` file.

The intersection of the taxonomy-filtered and domain architecture-filtered datasets was extracted to generate the `domain_architecture_filtered_protein` file. 

Redundant protein sequences were subsequently removed to produce the final `deduplication_protein` file for downstream analysis.

**Output files:**
- `taxonomy`: Bacterial protein sequences identified using HMM-based searching (4,762 sequences).
- `phmmer_M13_N_M13_peptidase`: Protein sequences containing both M13_N and M13 domains (3,623 sequences).
- `domain_architecture_filtered_protein`: Intersection of the taxonomy-filtered and domain architecture-filtered datasets (366 sequences).
- `deduplication_protein`: Nonredundant protein sequence dataset (291 sequences).
