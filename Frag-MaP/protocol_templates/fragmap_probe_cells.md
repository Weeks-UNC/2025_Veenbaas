#  In-cell UV cross-linking of photo-reactive ligands to RNA

Date: 7/20/2024

Author: Seth D. Veenbaas

Aim: Prepare ligand crosslinked total RNA for JuMP RT, and sequencing.

Logic: Treating cells with photo-reactive ligand and 365 nm UV cross-links ligand to RNA at direct binding sites, which can be subsequently mapped through JuMP RT and sequencing.

**NOTE: All experiments should start fresh by streaking B. sub on plates.**

* B. sub does not grow well from glycerol stocks or passaged cell pellets. 

* B. sub does not store well at 4 °C because it enters a spore form.

## Day 1: Plate cells

### Materials:

* B. subtilis str. 168 glycerol stock
* LB Agar plate

### Protocol:

1. Streak a plate with B. subtilis str. 168 to form single colonies. 
2. Incubate plate at 30 °C overnight.

### Notes:


## Day 2: Overnight culture

### Materials:

* LB media (5 mL)
* Culture tube

### Protocol:

1. Inoculate 5 mL LB media with a single colony from plate. 
2. Grow cells overnight at 30 °C, 225 rpm.

## Day 3: Probe cells and extract RNA (~10 hours)

### Materials:

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

### Protocol:

3. Inoculate 60 mL LB media with 3 mL cultured cells and grow cells to 0.50 OD<sub>600<sub/>.

    **NOTE: Expect cell growth to take ~2.5 hours.**

    | Time point | #1 OD<sub>600<sub/> | #2 OD<sub>600<sub/> | #3 OD<sub>600<sub/> |
    | :--------: | :-----------------: | :-----------------: | :-----------------: |
    |            |          -          |          -          |          -          |
    |            |                     |                     |                     |
    |            |                     |                     |                     |

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
    * Add 200 uL of buffer lysis to each cell pellet.
    * Incubate for 30 min. at RT.
    
9. Extract and purify total RNA from cells. 
    * Use 1000 uL of Tri-reagent 
    * Mix aggressively to aid in lysis
    * Lyse for 15 minutes

        **OPTIONAL PAUSE: store at 4 °C**

    * Add 250 uL of chloroform
    * Vortex and incubate at RT for 3-5 minutes
    * Centrifuge at 15000xg for 15 minutes at 4 °C

        **NOTE: Keep sample on ice until aqueous layer is recovered**

    * Add 100% ethanol to each recovered aqueous layer in equal parts (1:1)
    * Follow [Monarch total RNA miniprep](https://www.neb.com/en-us/-/media/nebus/files/manuals/manualt2010.pdf?rev=175a03b980f84584b7353d73dd6cba54&hash=93B1804F5634464706E58663FCD33B6C) kit instructions. Start at Part 2 step 4.
    * Elute from column with 51.5 uL of NFW

        **NOTE: Yields of ~50-60 ug total RNA have been achieved per 5 mL culture probed.**

10. Check RNA purity.df
    * Measure absorbance ratio (A260/280 and A260/230) on nanodrop.

    | Sample ID | Replicate | Ligand | Yield (μg) | [RNA] (ng/μL) | A260/280 | A260/230 | Vol NFW to 500 ng/μL (μL) |
    | :-------- | :-------: | :----- | :--------: | :-----------: | :------: | :------: | :-----------------------: |
    |           |           |        |            |               |          |          |                           |
    |           |           |        |            |               |          |          |                           |
    |           |           |        |            |               |          |          |                           |
    |           |           |        |            |               |          |          |                           |
    |           |           |        |            |               |          |          |                           |
    |           |           |        |            |               |          |          |                           |
    |           |           |        |            |               |          |          |                           |
    |           |           |        |            |               |          |          |                           |
    |           |           |        |            |               |          |          |                           |
    |           |           |        |            |               |          |          |                           |
    |           |           |        |            |               |          |          |                           |
    |           |           |        |            |               |          |          |                           |
    |           |           |        |            |               |          |          |                           |
    |           |           |        |            |               |          |          |                           |
    |           |           |        |            |               |          |          |                           |

        
## NOTES:


## Storage:

* RNA can be stored overnight at 4 °C for ~ 1 week.
* RNA can be flash-frozen in aliquots and stored at -80 °C for ~1 year.

## Next Steps:

* Partial RNA Fragmentation