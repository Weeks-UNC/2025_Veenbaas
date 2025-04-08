# 2025_Veenbaas

This repository contains supplementary data and analysis software for the *fpocketR* and *Frag-MaP* results reported in the manuscript ["RNA ligand binding pockets and where to find them"](https://www.biorxiv.org/content/10.1101/2025.03.13.643147v1).

## Table of Contents

- [Overview](#overview)
- [fpocketR](#fpocketr)
  - [Analysis](#fpocketr-analysis)
  - [Optimization](#fpocketr-optimization)
- [Frag-MaP](#frag-map)
  - [Analysis](#fragmap-analysis)
  - [Protocol Templates](#protocol-templates)
- [Citation](#citation)
- [License](#license)

## Overview

This repository provides access to the data, code, and protocols accompanying our manuscript on RNA ligand-binding pocket identification and characterization. The repository is organized around two key methodologies:

- **fpocketR**: A computational tool for detecting and characterizing ligand-binding pockets in RNA structures
- **Frag-MaP**: An experimental approach for mapping RNA-ligand interactions through chemical probing

## fpocketR

*fpocketR* is a package for detecting, visualizing, and characterizing drug-like small-molecule binding sites in RNAs. The ***fpocketR*** software can be accessed at: https://github.com/Weeks-UNC/fpocketR

### fpocketR Analysis

The `fpocketR/analysis/` directory contains results and example data for various RNA systems analyzed with *fpocketR*:

- **apo_holo (FIG 5)**: Analysis of 10 RNA structures in both holo (ligand-bound) and apo (ligand-free) states
- **dynamic_rna (Fig 5)**: Application of *fpocketR* to RNA structures with conformational dynamics
- **e_coli_ribosome (FIG S7)**: Analysis of pockets the *E. coli* ribosome (PDB: 7K00)
- **group_II_intron (FIG 7)**: Analysis of pockets in the group II intron (PDB: 5G2X)
- **training_test_sets (FIG 1, 2, 6, 8)**: *fpocketR* results (default and optimized) for the small RNA training and test sets

### fpocketR Optimization

The `fpocketR/optimization/` directory contains:

- **code**: Scripts used for parameter optimization and performance evaluation of *fpocketR*
- **data**: Raw data from the multivariate optimization process that assessed 1875 parameter combinations
- **figures**: Visualization of optimization results and performance metrics

## Frag-MaP

Frag-MaP is a chemical probing technique that uses fully functionalized fragment probes, mutational profiling (MaP), and next-generation sequencing to identify ligand binding sites in RNA with nucleotide precision. We analyzed our Frag-Map data with the Fragmapper analysis module in ***RNAvigate*** which is available at: https://github.com/Weeks-UNC/RNAvigate

### Frag-Map Analysis

The `Frag-MaP/analysis/` directory includes:

- **fragmap_azide_enrichment_analysis.ipynb**: Jupyter notebook for analyzing Frag-MaP enrichment data
- **fme3_rnavigate_samples.pkl** and **fme5_rnavigate_samples.pkl**: Processed data files containing RNAVigate samples for each sample
- **images/**: Figures and visualizations derived from Frag-MaP data
- **README_DATA_AVAILIBLITY.md**: Information on accessing additional data (FASTQ and SHAPEMapper profiles) not included in this repository

### Protocol Templates

The `Frag-MaP/protocol_templates/` directory contains detailed protocols for implementing the Frag-MaP methodology:

- **fragmap_probe_cells.md/pdf**: Protocol for probing *B. subtilis* cells with fully functionalized fragment probes
- **fragmap_protocol_with_enrichment.md/pdf**: Enhanced Frag-MaP protocol (with azide beads) for identifying ligand binding sites in RNA

## Citation

If you use the data or methodologies from this repository, please cite our paper:

### Preprint

```
Veenbaas et al. (2025). RNA ligand binding pockets and where to find them. 
bioRxiv 2025.03.13.643147; doi: https://doi.org/10.1101/2025.03.13.643147
```

### PNAS

Accepted March 11 2025



