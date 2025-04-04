# 2025_Veenbaas_PNAS_fpocketR_Frag-MaP

This repository contains the raw data, processed data, and Jupyter notebooks used in the analysis of fpocketR and Frag-MaP data for the manuscript "Ligand-binding pocket in RNA, and where to find them".


## *fpocketR*

### Software

Install instructions for the pocket detection, characterization, and visualization package used in the manuscript can be found at the [*fpocketR* repository](https://github.com/Weeks-UNC/fpocketR).

*fpocketR* use instructions can be found in the [*fpocketR* repository demo](https://github.com/Weeks-UNC/fpocketR/blob/main/Demo/fpocketR_demo.md)

### Results

*fpocketR* results using [default parameters](https://github.com/Weeks-UNC/2023_Veenbaas_PNAS_fpocketR_Frag-MaP/tree/main/fpocketR/analysis/default). 

*fpocketR* results using optimized parameters are available for the [training set](https://github.com/Weeks-UNC/2023_Veenbaas_PNAS_fpocketR_Frag-MaP/tree/main/fpocketR/analysis/training) and [test set](https://github.com/Weeks-UNC/2023_Veenbaas_PNAS_fpocketR_Frag-MaP/tree/main/fpocketR/analysis/test).


## Frag-MaP

### Protocol

Step-by-step [printable protocol](https://github.com/Weeks-UNC/2023_Veenbaas_PNAS_fpocketR_Frag-MaP/blob/main/Frag-MaP/protocol/Frag-MaP_protocol.pdf) for Frag-MaP. Steps are included for cell culture through Illumina sequencing.

### Data

Raw sequencing data can be obtained at the [GEO repository](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE245321).

### Analysis

There are two options to view the analysis notebooks:

### Static web page in browser

These are view-only versions of Jupyter Notebooks. 

Frag-Mapper analysis used for:

[Figure 3 and SI Figure 3](https://github.com/Weeks-UNC/2023_Veenbaas_PNAS_fpocketR_Frag-MaP/blob/main/Frag-MaP/analysis/frag-MaP_notebook.ipynb)

### Interactive notebooks on your local machine

Download this repository. In order to view the Jupyter notebooks, you will need
Jupyter installed. In order to run them, you will need a Jupyter kernel with
RNAvigate installed.

In future versions of RNAvigate, syntax changes may prevent these notebooks
from running properly. If that is the case, here is the hard link to the
version of RNAvigate used in these notebooks.

- [RNAvigate (0.2.0) source code](https://github.com/Weeks-UNC/RNAvigate/tree/48d6c1b9477b52120ce48ac0dacba0071ddf86d9)
