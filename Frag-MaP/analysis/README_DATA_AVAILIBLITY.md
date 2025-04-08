
# Data Availability

The NextSeq sequencing files (`.fastq`) and SHAPEMapper output files (`profile.txt` and `log.txt`) used to generate the RNAVigate profiles stored in the`.pkl` files in this repository are available on GEO.

## Run Analysis Notebook (.ipynb)

To execute the `.ipynb` files in this repository, you need to have **RNAvigate** installed. RNAvigate is a powerful tool for RNA analysis and is available at the following GitHub repository:  
[RNAvigate GitHub Repository](https://github.com/Weeks-UNC/RNAvigate)

Please follow the installation instructions provided in the repository to set up RNAvigate before running the notebooks.

## GEO Repository

You can access the data through the Gene Expression Ombibus at:
[GEO Accession GSE276279](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276279)

# GEO Download

A tar file containing all the data can be downloaded directly from:  
[Download Data](https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE276279&format=file)

## Dataset Information

**Status:** Public on Apr 02, 2025  
**Title:** Ligand-binding pockets in RNA, and where to find them [II]  
**Organism:** *Bacillus subtilis*  
**Experiment Type:** Other  

### Summary
RNAs are critical regulators of gene expression, and their functions are often mediated by complex secondary and tertiary structures. Structured regions in RNA can selectively interact with small molecules – via well-defined ligand binding pockets – to modulate the regulatory repertoire of an RNA. 

The broad potential to modulate biological function via RNA-ligand interactions remains unrealized due to challenges in identifying RNA motifs capable of binding ligands with good physiochemical properties (often termed drug-like). Here, we devise **fpocketR**, a computational strategy that accurately detects pockets capable of binding drug-like ligands in RNA structures. 

Remarkably, fewer than 60 such pockets had been previously visualized. We experimentally confirmed the ligandability of novel pockets detected with fpocketR using a fragment-based approach introduced here, **Frag-MaP**, that detects ligand-binding sites in cells. Analysis of pockets detected by fpocketR and validated by Frag-MaP reveals dozens of newly identified sites able to bind drug-like ligands, supports a model for RNA secondary structural motifs able to bind quality ligands, and creates a broad framework for understanding the RNA ligand-ome.

### Overall Design
We used photo-crosslinking fully functionalize fragment (FFF) probes and mutational profiling reverse transcription (MaP-RT) to determine the nucleotide position of RNA-ligand interactions. The FFF probes tested include:  
- A non-selective control (*methyl*)  
- A positive control (*linezolid*)  
- Fragments (*6-aminoquinoxaline* and *Enamine Z4225957206*)  

### Contributor(s)
- Veenbaas SD  
- Koehn JT  
- Irving PS  
- Lama NN  
- Weeks KM  

### Citation(s)
Veenbaas SD, Koehn JT, Irving PS, Lama NN et al. *Ligand-binding pockets in RNA, and where to find them*. bioRxiv 2025 Mar 15. PMID: 40161846
