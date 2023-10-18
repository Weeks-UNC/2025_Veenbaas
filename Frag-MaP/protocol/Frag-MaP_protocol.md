# Frag-MaP experimental protocol

Seth D. Veenbaas
10/16/2023

## Experiment Summary

Detect the RNA binding site of fully-functionalized fragments in B. subtilis total RNA.

## Protocol Overview:

- Photocrosslink and extract RNA
- Partial Fragmentation of total RNA
- Click Azide-PEG3-Biotin
- Streptavidin bead enrichment (optional)
- Ethanol precipitation
- MaP RT
- Second strand synthesis
- NEB Ultra II adapter ligation kit
- Qubit
- Bioanalyzer
- Pool and dilute library
- Miseq

##  Photocrosslink and extract RNA (3 days)

Prepare ligand crosslinked total RNA for JuMP RT, and sequencing.

### **NOTE: All experiments should start fresh by streaking B. sub on plates.**

* B. sub does not grow well from glycerol stocks or passaged cell pellets. 

* B. sub does not store well at 4 °C because it enters a spore form.

### Day 1: Plate cells

#### Materials:

* B. subtilis str. 168 glycerol stock
* LB Agar plate

#### Protocol:

1. Streak a plate with B. subtilis str. 168 to form single colonies. 
2. Incubate plate at 30 °C overnight.

### Day 2: Overnight culture

#### Materials:

* LB media (5 mL)
* Culture tube

#### Protocol:

1. Inoculate 5 mL LB media with a single colony from plate. 
2. Grow cells overnight at 30 °C, 225 rpm.

### Day 3: Probe cells and extract RNA (~10 hours)

#### Materials:

* LB media (50 mL)
* PBS buffer (100 mL)
* 50 mM ligand stock in DMSO (20 uL per sample)
* Sterile 6-well plastic plate (1 well per sample)
* lysozyme (60 mg)
* 1M Tris pH 7 (180 uL)
* 0.5 M EDTA (120 uL)
* Chloroform
* 100% ethanol
* Qiogen RNAeasy Plus Universial Mini kit

#### Protocol:

3. Inoculate 60 mL LB media with 3 mL cultured cells and grow cells to 0.50 OD600.

    **NOTE: Expect cell growth to take ~2.5 hours.**

    | Time point | #1 OD600 | #2 OD600 |
    | :--------: | :------: | :------: |
    |            |    -     |    -     |
    |            |          |          |
    |            |          |          |

4. Buffer excahnge cells.
    * Gently pellet cells at 3200g for 10 min at 4 °C.
    * Carefully remove supernatant.
    * Wash cell pellet with 50 mL PBS buffer, repeat centrifugation, and carefully remove supernatant.
    * Resuspend cells in 50 mL PBS buffer.

5. Probe cells with functionalized ligands.
    * Combine 4,980 uL of cultured media with 20 uL of photo-reactive ligand (50 mM stock in DMSO) and pipette mix. Avoid prolonged light exposure. 
    
        **NOTE: final [ligand] is 200 uM. 250X dilution.**

    * Incubate ligand-treated cells for 30 minutes at 30 °C and 225 rpm. 
    
        **NOTE: Keep solution in dark**.

6. Cross-link functionalized ligands to RNA.
    * Transfer 5 mL cell solution to a sterile 6-well plastic plate.
    * Place uncover plate and place on ice
    * Irradiate with 365 nm light source and cross-link with 3 J/cm2. 
    
        **NOTE: This is nine minutes (or three max energy hits) 5-6 cm from the light source in a UVP crosslinker.**

7. Create cell pellet. 
    * Centrifuge to pellet the cells. 8,000xg for 10 min. at 4 °C.
    * Discard supernatant.

8. Prepare fresh lysis buffer.
    * (30 mM Tris pH 7, 10 mM EDTA, 10 mg/mL lysozyme):
  
    | Reagent                | Amount       |
    | :--------------------- | :----------- |
    | lysozyme               | 50 mg        |
    | 1M Tris pH 7           | 150 uL       |
    | 0.5M EDTA              | 100 uL       |
    | RNase inhibitor murine | 50 uL        |
    | NF H2O                 | 4700 uL      |
    | **TOTAL**              | **5,000 uL** |


8. Lysis cell pellet with lysozyme buffer.
    * Add 250 uL of buffer lysis to each cell pellet.
    * Incubate for 30 min. at RT.
    
9. Extract and purify total RNA from cells. 
    * Use 1000 uL of Tri-reagent 
    * Mix aggressively to aid in lysis
    * Lyse for 15 minutes
    * Add 250 uL of chloroform
    * Vortex and incubate at RT for 3-5 minutes
    * Centrifuge at 15000xg for 15 minutes at 4 C
    * **NOTE: Keep sample on ice until aqueous layer is recovered**
    * Add 100% ethanol to each recovered aqueous layer in equal parts (1:1)
    * Follow Direct-zol RNA Miniprep Plus Kit instructions.
    * Elute from column with 50 uL of NFW

        **NOTE: Yields of ~50-60 ug total RNA have been achieved per 5 mL culture probed.**

10. Check RNA purity.
    * Measure absorbance ratio (A260/280 and A260/230) on nanodrop.

    | Culture | Sample ID | Yield (μg) | [RNA] (ng/μL) | A260/280 | A260/230 |
    | :-----: | :-------: | :--------: | :-----------: | :------: | -------- |
    |         |           |            |               |          |          |
    |         |           |            |               |          |          |
    |         |           |            |               |          |          |
    |         |           |            |               |          |          |
    |         |           |            |               |          |          |
    |         |           |            |               |          |          |
    |         |           |            |               |          |          |
    |         |           |            |               |          |          |

### NOTES:

* Samples diluted to 500 ng/μL and flash frozen.

### Storage:

* RNA can be stored overnight at 4 °C for ~ 1 week.
* RNA can be flash-frozen in aliquots and stored at -80 °C for ~1 year.

### Next Steps:

* Partial RNA Fragmentation
* MaP-RT

## Sample Details:

RNA provided from Frag-MaP Cell Probing 4 experiment (200 μM).

| Sample ID | Replicate | Ligand | Fragmention | Enrichment | [RNA] (ng/μL) | i7 index | i5 index |
| :-------- | :-------: | :----: | :---------: | :--------: | :-----------: | :------: | :------: |
|           |           |        |             |            |               |          |          |
|           |           |        |             |            |               |          |          |
|           |           |        |             |            |               |          |          |
|           |           |        |             |            |               |          |          |
|           |           |        |             |            |               |          |          |
|           |           |        |             |            |               |          |          |
|           |           |        |             |            |               |          |          |
|           |           |        |             |            |               |          |          |


## Partial Fragmentation of total RNA (~0.5 hour)

Fragment RNA to around 150 nt average length.

### Materials:

- Total RNA (10 μg)
- [NEBNext® Magnesium RNA Fragmentation Module](https://www.neb.com/products/e6150-nebnext-magnesium-rna-fragmentation-module#Product%20Information)

### Protocol:

1. Mix the following components in a sterile PCR tube:

| Component                      |    Volume |
| :----------------------------- | --------: |
| Purified total RNA (~10 μg)    |     18 μL |
| RNA Fragmentation Buffer (10X) |      2 μL |
| **Total**                      | **20 μL** |

2. Incubate in a preheated thermal cycler for 3 minutes at 94°C.
3. Transfer tube to ice immediately.
4. Add 2 μl 10X RNA Fragmentation Stop Solution.
5. Clean up with [Monarch RNA Cleanup kit](https://www.neb.com/en-us/products/t2030-monarch-rna-cleanup-kit-10-ug#Product%20Information)

### More Information:

[NEBNext® Magnesium RNA Fragmentation Module Protocol](https://www.neb.com/protocols/0001/01/01/nebnext-magnesium-rna-fragmentation-module-protocol-e6150)


## Click Azide-PEG3-Biotin (~1 hour)

This prtocol is intented to add a vector to enable biotin-streptavin enrichment for crosslinked RNA.

### Materials:

Multiple reagents amounts by the number of intended samples

| Reagents                  | [Reagent] | [Final] | Amount    |
| :------------------------ | :-------- | :------ | :-------- |
| Total RNA-alkyne – 10X    | ~10 μg    | ~0.1 μM | 18 μL     |
| N3-Cy5 – 25X              | 50 μM     | 2 μM    | 2 μL      |
| HEPES Buffer pH 7.5 – 25X | 250 mM    | 10 mM   | 2 μL      |
| DMSO                      | -         | -       | 25 μL     |
| Ascorbic Acid – 20X       | 10 mM     | 0.5 mM  | 2.5 μL    |
| Cu(II): TBTA – 41.7X      | 10 mM     | 240 μM  | 1.2 μL    |
| **TOTAL**                 | -         | -       | **50 μL** |

### Protocol:

1. Prepare fresh 10 mM Ascorbic acid stock 20X:

   - Combine reagents.
   - Sparge solution with N2 and use immediately.

   | Reagents      | Amount     |
   | :------------ | :--------- |
   | Ascorbic acid | 9.0 mg     |
   | NF Water      | 5.0 mL     |
   | **TOTAL**     | **5.0 mL** |

2. Dilute RNA:

   - Add RNA-alkyne and water to a strip of PCR tubes.

   | Reagents          | [Reagent] | Final [RNA-Alkyne] | Amount      |
   | :---------------- | :-------- | :----------------- | :---------- |
   | RNA-alkyne – 10X  | 75 ng/μL  | ~ 0.01 μM          | 17.3 μL     |
   | Nuclease free H2O | -         | -                  | - μL        |
   | **Subtotal**      | -         | -                  | **17.3 μL** |

3. Heat denature RNA:

   - Incubate RNA at 95 °C for 2 min.
   - Snap cool on ice for 2 min.

4. Add HEPES buffer and N3-PEG3-Biotin to tubes:

   - Add HEPES and N3-PEG3-Biotin.

   | Reagents                  | [Reagent] | [Final] | Amount      |
   | :------------------------ | :-------- | :------ | :---------- |
   | HEPES Buffer pH 7.5 – 25X | 250 mM    | 10 mM   | 2 μL        |
   | N3-PEG3-Biotin – 25X      | 50 μM     | 2 μM    | 2 μL        |
   | **Subtotal**              | -         | -       | **21.3 μL** |

   **NOTE: Batch samples can be kept on ice after HEPES addition.**

5. Denature RNA by adding DMSO:

   - Add DMSO to each sample.
   - Briefly vortex.

     | Reagents     | [Reagent] | [Final] | Amount      |
     | :----------- | :-------- | :------ | :---------- |
     | DMSO         | -         | -       | 25 μL       |
     | **Subtotal** | -         | -       | **46.3 μL** |

6. Start click reaction:

   - Add ascorbic acid and Cu(II)/TBTA mix to samples.

     | Reagents             | [Reagent] | [Final] | Amount      |
     | :------------------- | :-------- | :------ | :---------- |
     | Ascorbic Acid – 20X  | 10 mM     | 0.5 mM  | 2.5 μL      |
     | Cu(II): TBTA – 41.7X | 10 mM     | 240 uM  | 1.2 μL      |
     | **Total**            | -         | -       | **50.0 μL** |

     **NOTE: Initiate reaction within 5 minutes of adding DMSO (RNA stays denatured for ~30 minutes).**

7. Incubate reaction.

   - Cover reaction.
   - Incubate at 40 °C for ~20 minutes.

     **NOTE: No further conversion after 1 h and more RNA degradation occurs.**

8. Quench reaction.

   - Add 1.0 μL of 0.5 M EDTA to each sample (50 μL).

9. Remove DMSO.

   - Dilute to ~500 μL with NF water (final [DMSO] is 5%).
   - Concentrate with Amicon Ultra 0.5mL Centrifugal filter spin column (10-50K NMWL cut off). Spin for 10 min at 14,000 g and 4 °C.

   **OPTIONAL:**

   - Wash column with ~500 μL of cold TE buffer
   - Spin for 10 min at 14,000 g and 4 °C.


### Results - Nanodrop:

| Sample ID | [RNA] (ng/μL) | A260/280 | A260/230 |
| :-------- | :-----------: | :------: | :------: |
| 1D        |               |          |          |
| 1M        |               |          |          |
| 1Z        |               |          |          |
| 1Q        |               |          |          |
| 1B        |               |          |          |
| 1H        |               |          |          |
| 1G        |               |          |          |
| 1J        |               |          |          |
| 2D        |               |          |          |
| 2M        |               |          |          |
| 2Z        |               |          |          |
| 2Q        |               |          |          |
| 2B        |               |          |          |
| 2H        |               |          |          |
| 2G        |               |          |          |
| 2J        |               |          |          |

## Streptavidin bead enrichment (~1 hour)

Enrich crosslinked RNA via Biotin-Streptavidin pull-down.

### Before starting:

- click Azide-3PEG-biotin to Alkyne-RNA and purify (RNAeasy Minelute)

### Materials:

- 0.5M Tris pH 7.5
- 2M NaCl
- 10% Tween-20
- [Streptavidin Magnetic Beads](https://www.neb.com/products/s1420-streptavidin-magnetic-beads#Product%20Information)
- Formamide
- 0.5M EDTA

### Protocol:

1. Prepare Bind Buffer (2X):

    | Component   | [reagant] |  [2X]  | [Final] | Amount (μL) |
    | :---------- | :-------: | :----: | :-----: | ----------: |
    | Tris pH 7.5 |    1 M    | 100 mM |  50mM   |       1,000 |
    | KCl         |    2 M    | 200 mM | 100 mM  |       2,000 |
    | TWEEN-20    |    10%    | 0.02%  |  0.01%  |          20 |
    | NFW         |     -     |   -    |    -    |       6,980 |
    | **TOTAL**   |   **-**   | **-**  |  **-**  |  **10,000** |

2. Prepare Wash Buffer:

   | Component   | [reagant] | [Final] | Amount (μL) |
   | :---------- | :-------: | ------: | ----------: |
   | Bind Buffer |    2X     |      1X |       7,000 |
   | NFW         |     -     |       - |       7,000 |
   | **TOTAL**   |   **-**   |   **-** |  **14,000** |

3. Prepare Elution Buffer:

    | Component     | Concentration | [Final] | Amount (μL) |
    | :------------ | :-----------: | :-----: | ----------: |
    | Formamide     |      99%      |   95%   |         960 |
    | EDTA (pH 8.2) |     0.5M      |  10 mM  |          20 |
    | NFW           |       -       |    -    |          20 |
    | **TOTAL**     |     **-**     |  **-**  |    **1000** |

4. Wash NEB Streptavidin Magnatic Beads.

   * Vortex beads until comletely suspended.
   * Add 50 μL of beads to a PCR strip.
   * Incubaute at RT for 5 minutes.
   * Apply magnet to beads and remove supernatant.
   * Resuspend beads in 100 μL of Wash Buffer (1X).
   * Apply magnet to beads and remove supernatant.
   * Repeat wash with Wash Buffer (1X).

5. Bind RNA to beads:

   - Add RNA-biotin to a strip of PCR tubes.
   - Add Bind Buffer (2X).
   - Add NEB Streptavidin Magnatic Beads.

   | Component          | Concentration | [Final] | Amount (μL) |
   | :----------------- | :-----------: | :-----: | ----------: |
   | RNA-Biotin         |       -       |  5 μg   |          25 |
   | Bind Buffer        |      2X       |   1X    |          25 |
   | Streptavidin Beads |       -       |    -    |          50 |
   | **TOTAL**          |     **-**     |  **-**  |     **100** |

6. Incubate RNA-Biotin and Streptavidin Beads for at least 30 minutes at RT.
   * < 10 minutes for short oligios (~ 30 nucleotides).
   * ~ 15 minutes for fragmented total RNA.
   * ~ 30 minutes for full length total RNA.

7. Pull-down:

   - Immobilize beads with magnetic rack.
   - Remove and discard supernatant.

8. Wash beads 4 times:

   - Resuspend beads in 150 μL of Wash Buffer (1X).
   - Immobilize beads with magnetic rack.
   - Remove and discard supernatant.

9. Elute RNA:

   - Add 50 μL of Elution Buffer.
   - Heat tubes at 95 °C for 4 minutes.
   - Quickly transfer tubes to magnetic rack and immobilize beads.
   - Transfer RNA-biotin solution into a new tube. 

### More information:

- [*A chemical probe based on the PreQ1 metabolite enables transcriptome-wide mapping of binding sites*](https://www.nature.com/articles/s41467-021-25973-x)

### Next steps:

- [Ethanol precipitation](ethanol-rna-precipitation.md)

## Purify RNA - Ethanol Precipitation (~2 hours)

Purified RNA may need to be concentrated by precipitation for downstream
applications. Precipitation of RNA with ethanol (or isopropanol) is the
standard method to recover RNA from aqueous solutions.

### Materials:

- RNA (> 10 ng/μL)\*
- 100% Ethanol (or isopropanol)
- 70% Ethanol
- A salt from TABLE 1.

  TABLE 1. Salt solutions for precipitating RNA

  | Salt             |  Stock (M) | [Final] (M) | Comments                                         |
  | :--------------- | ---------: | ----------: | ------------------------------------------------ |
  | Sodium Acetate   | 3 (pH 5.2) |         0.3 | Recommended.                                     |
  | Ammonium acetate |          5 |         0.5 | Use with isopropanol to remove free nucleotides. |
  | Lithium Chloride |          8 |         0.8 | Avoid for downstream IVT or RT.                  |

**NOTE: Avoid Potassium salts if RNA will be exposed to dodecyl sulfate (SDS).**

### Protocol:

1. Combined components:

   - Add RNA to appropriately sized tube.
   - Add one of the salt solutions shown in Table 1.
   - Add 2.5–3.0 volumes of ice-cold ethanol (or 1 volume of isopropanol).
   - Mix the solution well.

   | Component            | Concentration | Equivalents |
   | :------------------- | ------------: | ----------: |
   | RNA                  |   >10 ng/μL\* |           1 |
   | Salt                 |           10X |         0.1 |
   | Ethanol              |          100% |         2.9 |
   | Glycogen (*optional) |          100X |           - |
   | **TOTAL**            |         **-** |       **4** |

   \*If [RNA] is < 10 ng/μL, add glycogen (final concentration of 50–150 μg/mL)
   to facilitate low concentration precipitation.

2. Precipitate RNA:

   - Store the ethanolic solution for 1 h to overnight at −20 °C.
   - RNA precipitation is faster and more complete at higher RNA concentrations.

3. Recover the RNA:

   - Centrifugation RNA solution at 12,000g–14,000g for 10 min at 4 °C to form pellet.
   - RNA pellet is is often invisible.
   - Decant the supernatant without disturbing the RNA pellet.
   - Carefully remove remaining traces of the supernatant with a disposable pipette tip.

4. Wash the RNA pellet (x2):

   - Add 0.5 mL of ice-cold 70% ethanol to pellet.
   - Centrifuge at maximum speed for 10min at 4 °C.
   - Repeat ethanol wash.

5. Dry RNA pellet:

   - Leave tube open at room temperature until the last traces of fluid have evaporated.
   - Do not dry the RNA pellet completely; otherwise, it can be difficult to dissolve the RNA.

6. Dissolve the RNA pellet:
   - Dissolve RNA in the desired volume of an RNase-free buffer (usually TE; pH between 6 and 7).
   - Rinse the walls of the tube well with the buffer.

## Storage:

- RNA can be stored for up to 1 yr at −80 °C.

## More information:

- [Precipitation of RNA with Ethanol](https://cshprotocols.cshlp.org/content/2020/3/pdb.prot101717.full)
 
# Mutational profiling RT (~3 hours)

This is protocol is based on Smola et.al., 2015. It has been optimized for the
synthesis of long cDNA from DMS modified RNA.

## Before starting:

[Modify RNA](../chemical-reactions/)
[Purify RNA](../purification/)

## Materials:

* 0.5 M Tris pH 8.0
* 0.75 M KCl
* 0.1 M DTT
* RNA (1 ng to 5 μg of total RNA)
* 2 µM RT primer (50 to 250 ng random primer)
* 10 mM dNTP mix
* 5 M betaine
* 40 mM MnCl2
* SuperScript II

## Protocol:

1. Create fresh 10X NTP minus:

    | Reagent           | Amount       |
    | :-------------    | :----------- |
    | 1 M Tris ph 8.0   | 20 uL        |
    | 2 M KCl           | 15 uL        |
    | 1 M DTT           | 4 uL         |
    | NF Water          | 1 uL         |
    |**TOTAL**          | **40 uL**    |

2. For each RNA sample combine:

    | Reagent           | Amount    |
    | :---------------- | :-------- |
    | RNA (~15 ng)      | 7.5 uL    |
    | nonamer (~100 ng) | 0.5 uL    |
    | 10 mM dNTPs       | 2 uL      |
    | **TOTAL**         | **10 µL** |

3. Denature and anneal ribosome by incubating at 90°C for 5 min, then cool on ice.
4. Create the following master mix:

    ***(multiply by number of samples+1)***

    | Reagent        | Amount   |
    | :------------- | :------- |
    | 10X NTP minus  | 2 uL     |
    | 5 M Betaine    | 4 uL     |
    | 40 mM MnCl2    | 3 uL     |
    | **TOTAL**      | **9 uL** |

5. Add 9 µL of master mix to each sample.
6. Incubate at 25°C for 2 min.
7. Add 1 µL of SuperScript II.
8. Set Thermocycler to this program:
   * Incubate at 25°C for 10 min.
   * Incubate at 42°C for 90 min.
   * 10 cycles of 50°C for 2 min and 42°C for 2 min.
   * Deactivate at 70°C for 10 min.
   * Hold at 4°C.
9. Purify cDNA with [G-50 column](https://www.cytivalifesciences.com/en/us/shop/molecular-and-immunodiagnostics/pcr-cleanup-and-size-selection/illustra-microspin-g-50-columns-p-00056?s_kwcid=AL!14612!3!675381046559!!!g!!&dtid=semp_google_20584436769_152358921965&ps_kw=&extcmp=G-SE-PAID-CY23072-GLOBAL-ALL-Research-matters-Google-Ads-Microspin-G-50-Columns&adgrp=&gclid=Cj0KCQjw4bipBhCyARIsAFsieCx4oBgd-ebx6sMs5pbFPAENOKxupyYOSkLWZ0s7ugzSo3WgdScv5nAaAkZpEALw_wcB#related-documents)



## More Information:

* [First-Stand cDNA Synthesis Using SuperScript II RT](https://tools.thermofisher.com/content/sfs/manuals/superscriptII_pps.pdf)


# Second Strand Synthesis (~2 hours)

From first strand synthesis product, a mix of enzymes polymerizes a second
cDNA from the first cDNA of a DNA-RNA hybrid, then digests away the RNA.

## Before starting:

* [first strand synthesis](map-rt-dms.md)
* [cDNA purification](../purification/spri-bead-purification.md)

## Materials:

* NEBNext second strand synthesis enzyme mix
* NEBNext second strand synthesis 10x buffer
* Fresh 80% EtOH

## Protocol:

**Always keep 2nd Strand Enzyme cold (below 16°C)**

1. Into a tube combine:

    | Reagent                           | Amount        |
    | :-------------------------------- | :------------ |
    | sscDNA                            | 20 μL         |
    | nucleotide-free water             | 48 μL         |
    | 10X 2nd Strand Reaction Buffer    | 8 μL          |
    | 2nd Strand Enzyme Mix             | 4 μL          |
    | **TOTAL**                         | **80 μL**     |

2. Mix by pipetting.
3. Incubate at 16°C for 60 min.

## Next Steps:

* [Purify DNA](../purification/spri-bead-purification.md)
* [HS DNA Qubit assay](../assays/hs-dna.md)
* [Nextera XT](nextera-xt.md)


# DNA Library Prep (Adapter Ligation) - NEBNEXT Ultra II (~2 hours)

## Materials:

* dsDNA (500 pg - 1 μg)
* NEBNext Ultra II End Prep Enzyme Mix
* NEBNext Ultra II End Prep Reaction Buffer
* NEBNext Ultra II Ligation Master Mix
* NEBNext Ligation Enhancer
* NEBNext Ultra II Q5 Master Mix
* NEBNext Oligo Kit
* 80% Ethanol

## Protocol:

1. Prepare Ends.

    * Add the following components into a PCR tube:

        | Components               |    Volume |
        | :----------------------- | --------: |
        | dsDNA                    |     50 μL |
        | End Prep Reaction Buffer |      7 μL |
        | End Prep Enzyme Mix      |      3 μL |
        | **TOTAL**                | **60 μL** |

    * Mix thoroughly and spin down.
    * Inbucate in thermal cycler with lid set to > 75 °C:

        | Step      | Time (min.) | Temperature (°C) |
        | :-------- | :---------: | :--------------: |
        | Prep ends |     30      |        20        |
        | Denature  |     30      |        65        |
        | End       |    HOLD     |        4         |

2. Adapter Ligation. (Adds ~60 nt)

    * Dilute adaptors based on input DNA quantity (from NEBNext Oligo Kit):

        | Input DNA   | Adpator Dilution | Working [Adapter] |
        | :---------- | :--------------: | :---------------: |
        | 101-1000 ng |   No Dilution    |       15 μM       |
        | 5 - 100 ng  |       1:10       |      1.5 μM       |
        | 0.5 - 5 ng  |       1:25       |      0.6 μM       |
    
    * Add the following components directly into the End Prep Reaction Mixture:

        * **NOTE: Do NOT premix Adapter with Master Mix or Ligation Enhancer.**

        | COMPONENT                            |      VOLUME |
        | :----------------------------------- | ----------: |
        | End Prep Reaction Mixture            |       60 µl |
        | NEBNext Adaptor (diluted)            |      2.5 µl |
        | NEBNext Ultra II Ligation Master Mix |       30 µl |
        | NEBNext Ligation Enhancer            |        1 µl |
        | **TOTAL**                            | **93.5 µL** |

    * Mix thoroughly and spin down.
    * Incubate at 20 °C for 15 minutes with lid heater off.
    * Add 3 µl of (red) USER enzyme.
    * Mix throughly.
    * Incubate at 37 °C for 15 minutes with the lid heater set to > 47 °C

3. Cleanup of Adaptor-ligated DNA - SPRI beads

    **Bead Ratio: 1.4x**

    1. Beads added to reaction mixture (1.4X)
    2. Incubate at room temp. for 5 min.
    3. Place in magnetic holder for 5 min.
    4. Remove most of the supernatant
    5. Wash beads with 80% ethanol (30 seconds) twice.
    6. Add 17 μL of water, resuspend pellet, and incubate for 5 minutes.
    7. Remove and keep supernatant.

4. PCR Amplification (Adds ~60 nt)

    * Add the following components to a PCR strip:

    | COMPONENT                      |    VOLUME |
    | :----------------------------- | --------: |
    | Adaptor Ligated DNA Fragments  |     15 µl |
    | NEBNext Ultra II Q5 Master Mix |     25 µl |
    | Index Primer/i7 Primer         |      5 µl |
    | Universal PCR Primer/i5 Primer |      5 µl |
    | **TOTAL**                      | **50 µl** |

    * Mix thoroughly and spin down.
    * Choose number of PCR cycles using the table below:

    | INPUT DNA | # OF CYCLES (YIELD ~100 ng) |
    | --------: | :-------------------------: |
    |    100 ng |              3              |
    |     50 ng |             3–4             |
    |     10 ng |             6–7             |
    |      5 ng |             7–8             |
    |      1 ng |            9–10             |
    |    0.5 ng |            10–13            |
 
    * Perform PCR amplification using the following PCR cycling conditions:

    | STEP                 | PCR Cycle Step      | TEMP  | TIME       | CYCLES |
    | :------------------- | ------------------- | ----- | ---------- | ------ |
    | Initial Denaturation |                     | 98 °C | 30 seconds | 1      |
    | PCR cycles:          |                     |       |            |        |
    |                      | Denaturation        | 98 °C | 10 seconds | 3-15   |
    |                      | Annealing/Extension | 65 °C | 75 seconds | 3-15   |
    | Final Extension      |                     | 65 °C | 5 minutes  | 1      |
    | HOLD                 |                     | 4 °C  | Hold       | 1      |

5. Cleanup of PCR Reaction - SPRI beads

    **Bead Ratio: 1.2x**

    1. Beads added to reaction mixture (1.2X)
    2. Incubate at room temp. for 5 min.
    3. Place in magnetic holder for 5 min.
    4. Remove most of the supernatant
    5. Wash beads with 80% ethanol (30 seconds) twice.
    6. Add 20 μL of water, resuspend pellet, and incubate for 5 minutes.
    7. Remove and keep supernatant.

## Notes:

* 12 cycles of PCR used
* Lengths are insert + adaptor (60 nt) + primers (60 nt)

## Next Steps:

* Qubit
* Bioanalyzer

# Qubit (~0.5 hours)

Quantify the dscDNA product from second strand synthesis via Qubit HS DNA assay. 

## Material

* [Qubit 1X dsDNA HS kit](https://www.thermofisher.com/order/catalog/product/Q33230)
    * Qubit tubes
    * 1X working solution
    * Standards 1 & 2

## Protocol

1. Create standard 1 & 2:
    * Add 190 μL of working solution into Qubit tube
    * Add 10 μL of standard
    * Equalibrate to RT
2. Create samples:
    * Add 196 μL of working solution into Qubit tube
    * Add 4 μL of cDNA
    * Equalibrate to RT
3. Incubate for 2 minutes before reading concentrations

## Results

| Sample ID | [dscDNA] ng/μL |
| :-------- | :------------: |
|           |                |
|           |                |
|           |                |
|           |                |
|           |                |
|           |                |
|           |                |
|           |                |


# Bioanalyzer (~1 hour)

Determine the average length of nextera library.

## Materials

* High sensitivity DNA reagants
* High sensitivity DNA chip
* Chip priming station

## Protocol 

* Follow Agilent [protocol](https://www.agilent.com/cs/library/usermanuals/Public/G2938-90321_SensitivityDNA_KG_EN.pdf)

## Results

| Sample ID | Avg. bp length | % of total |
| :-------- | :------------: | ---------: |
|           |                |            |
|           |                |            |
|           |                |            |
|           |                |            |
|           |                |            |
|           |                |            |
|           |                |            |
|           |                |            |


# Pool and dilute library (~1 hour)

Dilute sample to the same molarity and pool for sequencing.

## Material

* [Illumina-mix-calculator.xlsx](https://github.com/Weeks-UNC/2023_Veenbaas_PNAS_fpocketR_Frag-MaP/blob/main/Frag-MaP/protocol/Illumina-mix-calculator.xlsx)
* [Sample_Sheet.xlsx](https://github.com/Weeks-UNC/2023_Veenbaas_PNAS_fpocketR_Frag-MaP/blob/main/Frag-MaP/protocol/SAMPLE_SHEET.xlsx)

## Target library concentration for illumina v3 chemistry

 2.00 nM [library] -> 10 pM [final]

## Protocol 

1. Input data into illumina-mix-calculator.xlsx
    * Avg. bp length (Bioanalyzer)
    * ng/μL (Qubit)
    * % Non-dimer (bioanalyzer)
    * Target library concentration (nM)

    **NOTE: Recomended minimum volume: 3 μL**

2. Pool sample library using the volumes calculated by illumina-mix-calculator.xlsx

3. Quantify the concentration of the pooled sample library using Qubit

4. Dilute the pooled library to the final concentration (ng/μL) calculated by illumina-mix-calculator.xlsx

    | Sample ID | [non-dimer] (nM) | Amount to pool (μL) |
    | :-------- | :--------------: | ------------------: |
    |           |                  |                     |
    |           |                  |                     |
    |           |                  |                     |
    |           |                  |                     |
    |           |                  |                     |
    |           |                  |                     |
    |           |                  |                     |
    |           |                  |                     |

5. Verify concentration via Qubit.

   | Sample ID | ng/μL |  nM |
   | :-------: | ----: | --: |
   |           |       |     |
   |           |       |     |
   |           |       |     |
   |           |       |     |
   |           |       |     |
   |           |       |     |
   |           |       |     |
   |           |       |     |


## Next Steps

MiSeq


# MiSeq (~2 hours)

Normalized DNA sequencing libraries are pooled, denatured, diluted, loaded into a MiSeq reagent kit, and ran on the MiSeq

1. Post-run wash (if not already completed)
    * After the run, discard waste, reagent cartridge and PR2 bottle
        * Formamide must be removed from the reagent cartridge (Well #8)
    * Fill an empty PR2 bottle with 500 mL 0.5% Tween 20:
        * 25 mL 10% Tween 20
        * 475 MilliQ water
    * From PR2 bottle, put 5 mL of 0.5% Tween 20 into each well of the wash tray
    * Load wash tray, wash bottle, and waste bottle
    * Start post-run wash

2. Reboot computer and clear disk space
    * Make drive has at least 100 GB free
    * Shut-down windows through the start menu
    * Once complete, shut off power to the device for 30 seconds
    * Turn on power switch, device will reboot

3. Thaw reagent cartridge
    * Open MiSeq Reagent Kit Box 1 of 2 (stored at -20)
    * Thaw HT1 buffer on ice (or RT if impatient, then move to ice)
    * Copy the serial number from the reagent cartridge (MS#######-#00V#)
    * Thaw reagent cartridge in a room temperature water bath (~1 hr)
    * Once completely thawed, store at 4C until loading

4. Pool, denature, and dilute libraries
    * Prepare a fresh dilution of 0.2 N NaOH by mixing
        * 200 uL 1.0 N NaOH
        * 800 uL nuclease free water
    * Dilute samples to 2.0 nM and combine in the desired ratio
    * In a 1.7 mL tube, combine
        * 5 uL 2.0 nM library
        * 5 uL 0.2 N NaOH
    * Briefly vortex and quick spin down (280 x g for 1 min)
    * Incubate at room temp for at least 5 min
    * Add 990 uL chilled HT1
    * Sample library is at 10 pM in HT1 with 1mM NaOH

5. Clean flow cell
    * Remove flow cell from MiSeq Reagent Kit Box 2 of 2 (4 C), handle by the edges
    * Wash flow cell with water
    * Carefully clean glass surface with lens paper
    * Repeat until surface is free of smudges
    * Wrap in lens paper until needed

6. Load cartridge and start run (load within 1 hour of denaturing samples)
    * Flip cartridge 10x to ensure proper mixing
    * Using a 1000 uL tip, poke open the hole for the sample
    * Load 600 uL sample (avoid air bubbles), gently tap cartridge so libraries pool at bottom
    * Follow the on-screen directions to insert the flow cell, reagent cartridge, and PR2 bottle

7. Post-run wash (perform ASAP, within 24 hours of run completion)
    * After the run, discard waste, reagent cartridge and PR2 bottle
        * Formamide must be removed from the reagent cartridge (Well #8)
    * Fill an empty PR2 bottle with 500 mL 0.5% Tween 20:
        * 25 mL 10% Tween 20
        * 475 MilliQ water
    * From PR2 bottle, put 5 mL of 0.5% Tween 20 into each well of the wash tray
    * Load wash tray, wash bottle, and waste bottle
    * Start post-run wash

### Sample details:

* Final library concentration should be ~10 pM
* Cluster density should be ~1000-1200

### Kit details: 

| Box | Ref | Lot | Exp |
| :-: | :-: | :-: | :-: |
|  1  |     |     |     |
|  2  |     |     |     |
