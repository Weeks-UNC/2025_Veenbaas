# Frag-MaP Enrich 2 Experiment

Seth D. Veenbaas
05/05/2023

## Experiment Summary

### Goal:

Enrich rRNA photo-crosslinked to fully-functionalized fragments in B. subtilis total RNA.

## Protocol Overview:

- Partial Fragmentation of total RNA
- Click Azide-PEG3-Biotin
- Streptavidin bead enrichment
- RT
- Second strand synthesis
- NEB Ultra II adapter ligation kit
- Miseq

## Sample Details:

RNA provided from Frag-MaP Cell Probing 4 experiment (200 μM).

| Sample ID | Replicate | Ligand | Fragmention | Enrichment | [RNA] (ng/μL) | i7 index | i5 index |
| :-------- | :-------: | :----: | :---------: | :--------: | :-----------: | :------: | :------: |
| 1D        |     1     |  DMSO  |     RNA     |  Enriched  |      500      |   701    |   504    |
| 1M        |     1     | Methyl |     RNA     |  Enriched  |      500      |   702    |   504    |
| 1Z        |     1     |  ZLD   |     RNA     |  Enriched  |      500      |   703    |   504    |
| 1Q        |     1     |   QN   |     RNA     |  Enriched  |      500      |   704    |   504    |
| 1B        |     1     |   BO   |     RNA     |  Enriched  |      500      |   705    |   504    |
| 1H        |     1     |   HO   |     RNA     |  Enriched  |      500      |   706    |   504    |
| 1G        |     1     |   GO   |     RNA     |  Enriched  |      500      |   707    |   504    |
| 1J        |     1     |   JO   |     RNA     |  Enriched  |      500      |   708    |   504    |
| 2D        |     2     |  DMSO  |     RNA     |  Enriched  |      500      |   701    |   505    |
| 2M        |     2     | Methyl |     RNA     |  Enriched  |      500      |   702    |   505    |
| 2Z        |     2     |  ZLD   |     RNA     |  Enriched  |      500      |   703    |   505    |
| 2Q        |     2     |   QN   |     RNA     |  Enriched  |      500      |   704    |   505    |
| 2B        |     2     |   BO   |     RNA     |  Enriched  |      500      |   705    |   505    |
| 2H        |     2     |   HO   |     RNA     |  Enriched  |      500      |   706    |   505    |
| 2G        |     2     |   GO   |     RNA     |  Enriched  |      500      |   707    |   505    |
| 2J        |     2     |   JO   |     RNA     |  Enriched  |      500      |   708    |   505    |


## Optimization: Partial Fragmentation of total RNA

Find conditions to fragment total RNA to around 200 nt average length.

### Materials:

- Total RNA (2 μg) (DMSO NO UV sample from Cell Probing 2)
- [NEBNext® Magnesium RNA Fragmentation Module](https://www.neb.com/products/e6150-nebnext-magnesium-rna-fragmentation-module#Product%20Information)

### Protocol:

1. Mix the following components in a sterile PCR tube:

| Component                           |    Volume |
| :---------------------------------- | --------: |
| DMSO NO UV sample total RNA (~2 μg) |      8 μL |
| NFW                                 |     10 μL |
| RNA Fragmentation Buffer (10X)      |      2 μL |
| **Total**                           | **20 μL** |

2. Incubate in a preheated thermal cycler:

| Condition | Time | Temp |
| --------- | :--: | :--: |
| 0         |  -   |  RT  |
| 1         |  2   | 94°C |
| 2         |  3   | 94°C |
| 3         |  4   | 94°C |
| 4         |  5   | 94°C |
| 5         |  5   | 80°C |
| 6         |  6   | 94°C |
| 7         |  7   | 80°C |
| 8         |  9   | 80°C |
| 9         |  11  | 80°C |


3. Transfer tube to ice immediately.
4. Add 3 μl 10X RNA Fragmentation Stop Solution.

### Notes:

* 94°C produced a tighter distribution
* 80°C had a more pronouced tail of longer produces and inconsistent results
* Best conditions to create ~150-200 nt length fragemnts: 94°C for 3 minutes
* Bioanalyzer data from 5/12/2023

### More Information:

[NEBNext® Magnesium RNA Fragmentation Module Protocol](https://www.neb.com/protocols/0001/01/01/nebnext-magnesium-rna-fragmentation-module-protocol-e6150)


## Partial Fragmentation of total RNA

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

### More Information:

[NEBNext® Magnesium RNA Fragmentation Module Protocol](https://www.neb.com/protocols/0001/01/01/nebnext-magnesium-rna-fragmentation-module-protocol-e6150)

## Monarch RNA Cleanup kit

* Also try: [Separation of Large and Small RNA into Fractions](https://www.neb.com/protocols/2018/06/28/separation-of-large-and-small-rna-into-fractions--using-the-monarch-rna-cleanup-kits)

### Notes:

* The protocol for seperation of Large and Small RNA into Fractions did not produce better results than the standard protocol.

## Click chemistry with alkyne-RNA & azide-oligo primer using 50% DMSO denaturant

This prtocol is intented to add steric bulk to increase MaP-RT mutation efficency at fully functionalized fragment crosslink sites.

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

## Streptavidin bead enrichment

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

## Purify RNA - Ethanol Precipitation

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

## Notes:

- Used Ammonium Acetate and 2 μL of Glycoblue

## More information:

- [Precipitation of RNA with Ethanol](https://cshprotocols.cshlp.org/content/2020/3/pdb.prot101717.full)
 
# Mutational profiling RT (DMS-optimized)

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

## Notes

* xD and xR series of samples used ~15 ng of RNA input
* xU series of samples used ~300 ng of RNA input

## More Information:

* [First-Stand cDNA Synthesis Using SuperScript II RT](https://tools.thermofisher.com/content/sfs/manuals/superscriptII_pps.pdf)

# Purify cDNA: G50 Column

## Materials:

* G-50 column

## Protocol:

1. Prepare column

    * Re-suspend resin by vortexing
    * Loosen cap and twist off bottom
    * Centrifuge at 735 x g for 1 minute

2. Apply sample

    * Place column into an DNase free tube
    * Gently pipette 12-50 uL of sample onto the center of the resin

3. Elute sample

    * Centifuge at 735 x g for 2 minutes
    * Keep eluate

# Second Strand Synthesis

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


# DNA Library Prep (Adapter Ligation) - NEBNEXT Ultra II

## Materials:

* dsDNA (500 pg - 1 μg)
* (green) NEBNext Ultra II End Prep Enzyme Mix
* (green) NEBNext Ultra II End Prep Reaction Buffer
* (red) NEBNext Ultra II Ligation Master Mix
* (red) NEBNext Ligation Enhancer
* (blue) NEBNext Ultra II Q5 Master Mix
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

        | COMPONENT                                  |      VOLUME |
        | :----------------------------------------- | ----------: |
        | End Prep Reaction Mixture                  |       60 µl |
        | (red) NEBNext Adaptor (diluted)            |      2.5 µl |
        | (red) NEBNext Ultra II Ligation Master Mix |       30 µl |
        | (red) NEBNext Ligation Enhancer            |        1 µl |
        | **TOTAL**                                  | **93.5 µL** |

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

    | COMPONENT                             |    VOLUME |
    | :------------------------------------ | --------: |
    | Adaptor Ligated DNA Fragments         |     15 µl |
    | (blue) NEBNext Ultra II Q5 Master Mix |     25 µl |
    | Index Primer/i7 Primer         |      5 µl |
    | Universal PCR Primer/i5 Primer |      5 µl |
    | **TOTAL**                             | **50 µl** |

    * Mix thoroughly and spin down.
    * Choose number of PCR cycles using the table below:

    | INPUT DNA | # OF CYCLES (YIELD ~100 ng) |
    | --------: | :-------------------------: |
    |    100 ng |              3              |
    |     50 ng |             3–4             |
    |     10 ng |             6–7             |
    |      5 ng |             7–8             |
    |      1 ng |            9–10             |
    |    0.5 ng |            10–11            |
 
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

* Lengths are insert + adaptor (60 nt) + primers (60 nt)

## Next Steps:

* Qubit
* Bioanalyzer

# Qubit

Quantify the dscDNA product from second strand synthesis via Qubit HS DNA assay. 

## Material

* Qubit tubes
* Working solution
* Standards 1 & 2

## Protocol

1. Create standards:
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
| 1D        |      5.39      |
| 1M        |      7.80      |
| 1Z        |      3.73      |
| 1Q        |      7.40      |
| 1B        |      0.96      |
| 1G        |      6.93      |
| 1H        |      4.20      |
| 1J        |      9.73      |
| 2D        |      4.47      |
| 2M        |      3.83      |
| 2Z        |      4.73      |
| 2Q        |      1.51      |
| 2B        |      0.95      |
| 2G        |      4.31      |
| 2H        |      3.90      |
| 2J        |      4.01      |


# DNA bioanalyzer

Determine the average length of nextera library.

## Materials

* High sensitivity DNA reagants
* High sensitivity DNA chip
* Chip priming station

## Protocol 

* Follow manfactuer protocol card

## Results

| Sample ID | Avg. bp length | % of total |
| :-------- | :------------: | ---------: |
| 1D        |      241       |         92 |
| 1M        |      243       |         98 |
| 1Z        |      260       |         93 |
| 1Q        |      256       |         98 |
| 1B        |      239       |         84 |
| 1G        |      232       |         97 |
| 1H        |      250       |         95 |
| 1J        |      240       |         91 |
| 2D        |      251       |         99 |
| 2M        |      278       |         98 |
| 2Z        |      282       |         98 |
| 2Q        |      231       |         97 |
| 2B        |      236       |         91 |
| 2G        |      246       |         97 |
| 2H        |      250       |         96 |
| 2J        |      240       |         96 |

# Pool and dilute library

Dilute sample to the same molarity and pool for sequencing.

## Material

* Illumina-mix-calculator.xlsx
* Sample_Sheet.xlsx

## Target library concentration

 2.00 nM -> 10 pM

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
    | 1D        |      33.84       |                1.79 |
    | 1M        |      51.73       |                1.17 |
    | 1Z        |      21.94       |                2.76 |
    | 1Q        |      46.59       |                1.30 |
    | 1B        |       5.55       |               10.93 |
    | 1G        |      47.65       |                1.27 |
    | 1H        |      26.25       |                2.31 |
    | 1J        |      60.67       |                1.00 |
    | 2D        |      29.00       |                2.09 |
    | 2M        |      22.21       |                2.73 |
    | 2Z        |      27.04       |                2.24 |
    | 2Q        |      10.43       |                5.82 |
    | 2B        |       6.02       |               10.07 |
    | 2G        |      27.95       |                2.17 |
    | 2H        |      24.63       |                2.46 |
    | 2J        |      26.38       |                2.30 |

5. Verify concentration via Qubit.

   |          Name          | ng/μL |    nM |
   | :--------------------: | ----: | ----: |
   | FME2 Seq. Lib. Initial | 3.320 | 22.28 |
   |  FME2 Seq. Lib. Final  | 0.296 |  1.99 |


## Next Steps

MiSeq

# MiSeq

  
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
    * Make sure D:drive has at least 100 GB free
    * If not, delete the oldest run from /Illumina-output/
    * Shut-down windows through the start menu
    * Once complete, shut off power to the device for 30 seconds
    * Turn on power switch, device will reboot

3. Thaw reagent cartridge
    * Open MiSeq Reagent Kit Box 1 of 2 (stored at -20)
    * Thaw HT1 buffer on ice (or RT if impatient, then move to ice)
    * Copy the serial number from the reagent cartridge (MS#######-#00V#)
    * Thaw reagent cartridge in a room temperature water bath (30 min -1 hr)
    * Once completely thawed, store at 4C until loading

4. Pool, denature, and dilute libraries (+PhiX control)
    * Prepare a fresh dilution of 0.2 N NaOH by mixing
        * 200 uL 1.0 N NaOH
        * 800 uL nuclease free water
    * Dilute samples to 3 nM and combine in the desired ratio (including PhiX)

        ***Only include PhiX here if it has not already been denatured***

    * In a 1.7 mL tube, combine
        * 5 uL 3 nM library
        * 5 uL 0.2 N NaOH
    * Briefly vortex and quick spin down (280 x g for 1 min)
    * Incubate at room temp for at least 5 min
    * Add 990 uL chilled HT1
    * Sample library is at 10 pM in HT1 with 1mM NaOH
        * IF higher loading concentration is desired, combine samples at 4 nM and dilute accordingly
        * 8-10 pM recommended for V2 kits
        * 15-20 pM recommended for V3 kits

5. Clean flow cell
    * Remove flow cell from MiSeq Reagent Kit Box 2 of 2 (4 C), handle by the edges
    * Wash flow cell with water
    * Carefully clean glass surface with lens paper wet with 100% EtOH
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

## Notes

### Sample details:

* Samples pooled at 2.0 nM -> 10 pM
* Cluster density: 1130

### Kit details: 
    
MiSeq Reagent Kit v3 600

| Box |   Ref    |    Lot    |    Exp     |
| :-: | :------: | :-------: | :--------: |
|  1  | 15043893 | 20733114  | 2024/01/24 |
|  2  | 15043894 | 207436558 | 2024/03/14 |


