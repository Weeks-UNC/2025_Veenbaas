#!/user/bin/python

# -----------------------------------------------------
# fpocket Optimization Evalution code
# Seth Veenbaas
# Weeks Lab, UNC-CH
# 2021
#
# Version 2.18
# Eval_opt evaluates four parameters: -m -M -i -D
#
# -----------------------------------------------------

from tqdm import tqdm
import datetime
import math
import argparse
import os
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from glob import iglob
import numpy as np
import pandas as pd
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from prody import *
from sklearn.preprocessing import MinMaxScaler


# Set package configurations
confProDy(verbosity='none')
# pd.set_option('precision', 3)

# Creates list of NT from pdb file and sets value to int(0).
# Returns list ([NT_sequence, 0],ect...)


def getPDB_NT_list(pdbcoords):

    PDB_nt_list = []

    if args.align:
        nt_subtract = next(iter(pdbcoords)) - 1
        for nt_id in pdbcoords:

            nt_number = nt_id - nt_subtract
            if nt_number not in PDB_nt_list:
                PDB_nt_list.append([nt_number, 0])
    else:
        for nt_id in pdbcoords:
            nt_number = nt_id
            if nt_number not in PDB_nt_list:
                PDB_nt_list.append([nt_number, 0])

    return PDB_nt_list

# Identifies the sequence position and identiy of NT in binding pocket
# Return: pocket_nt = [ [<nt_seq>, <Pocket Number], ect....]


def getPocketNT(stpcoords, pdbcoords, pdb_nt_list, distancefilter):
    pocket = 1
    pocket_nt = pdb_nt_list

    for a_sphere in stpcoords:

        if a_sphere[0] == pocket:

            x1 = float(a_sphere[1])
            y1 = float(a_sphere[2])
            z1 = float(a_sphere[3])

            # for loop status: Working
            for key, value in pdbcoords.items():

                # For Loop status: Working
                # pdc= dictionary. Keys = integar of nt_seq.
                # Values = nested list with info for each atom composing nucleotide
                # key= nested list with the id and position of all atoms in a nucleotide
                # info= info for a simple atom [<nt_id>,<x1>,<y1>,<z1>]
                for info in value:

                    nt_seq = key
                    x2 = float(info[1])
                    y2 = float(info[2])
                    z2 = float(info[3])
                    distance = calcDist(x1, y1, z1, x2, y2, z2)

                    if distance < distancefilter:

                        for index, pocket_nt_list in enumerate(pocket_nt):
                            nt = pocket_nt_list[0]

                            if nt == nt_seq and pocket_nt[index][1] == 0:
                                # if pocket_nt[index][1] == 0:
                                pocket_nt[index] = [nt_seq, pocket]

        elif a_sphere[0] != pocket:
            pocket += 1
    # print(pocket_nt)
    return pocket_nt


def getLigandOverlap(stp_coords, pdb_coords, ligand_coords, pocket_num=None):
    ligand_overlap = {}
    pocket_count = getPocketCount(stp_coords)
    atom_count = len(ligand_coords)

    for pocket in range(1, pocket_count+1):
        coord_overlap = 0

        for atom in ligand_coords:
            x1 = atom[0]
            y1 = atom[1]
            z1 = atom[2]
            if (pocket == pocket_num or pocket_num is None):
                for a_sphere in stp_coords:
                    if type(a_sphere[0]) == int:
                        poc = int(a_sphere[0])

                        if poc == pocket:
                            x2 = float(a_sphere[1])
                            y2 = float(a_sphere[2])
                            z2 = float(a_sphere[3])
                            distance = calcDist(x1, y1, z1, x2, y2, z2)

                            if distance < 3:
                                coord_overlap += 1
                                break

        if coord_overlap > 0 and atom_count > 0:
            eval_score = float(coord_overlap / atom_count)
            ligand_overlap[pocket] = eval_score

        elif coord_overlap == 0 and atom_count > 0:
            eval_score = 0.0
            ligand_overlap[pocket] = eval_score

    # pocket_eval, dict = {pocket : eval score}
    if pocket_num is None:
        return ligand_overlap
    elif(len(ligand_overlap) != 0):
        return ligand_overlap[pocket_num]


def getPocketOverlap(stp_coords, pdb_coords, ligand_coords, pocket_num=None):
    pocket_overlap = {}
    pocket_count = getPocketCount(stp_coords)

    for pocket in range(1, pocket_count+1):
        sphere_count = 0
        coord_overlap = 0
        if (pocket == pocket_num or pocket_num is None):
            for a_sphere in stp_coords:
                if type(a_sphere[0]) == int:
                    poc = int(a_sphere[0])
                    x2 = float(a_sphere[1])
                    y2 = float(a_sphere[2])
                    z2 = float(a_sphere[3])

                    if poc == pocket:
                        sphere_count += 1

                        for key in ligand_coords:
                            x1 = key[0]
                            y1 = key[1]
                            z1 = key[2]
                            distance = calcDist(x1, y1, z1, x2, y2, z2)

                            if distance < 3:
                                coord_overlap += 1
                                break

            if coord_overlap > 0 and sphere_count > 0:
                eval_score = float(coord_overlap / sphere_count)
                pocket_overlap[pocket] = eval_score

            elif coord_overlap == 0 and sphere_count > 0:
                eval_score = 0.0
                pocket_overlap[pocket] = eval_score

    # pocket_eval, dict = {pocket : eval score}
    if pocket_num is None:
        return pocket_overlap
    elif(len(pocket_overlap) != 0):
        return pocket_overlap[pocket_num]


# Determines the center (or mean coordinate space) of ligand and pockets.
# Returns float distance (A) between the ligand center and pocket center.
def get_center_offset(stp_coords, ligand_coords, pocket):
    ligand_array = np.array(ligand_coords)
    ligand_center = np.average(ligand_array, axis=0)

    # Returns stp_center. Array of mean coorindates of STP for specified pocket.
    stp_center = get_STP_center(stp_coords, pocket)
    # Calculates euclidean distance between the center of the ligand and pocket.
    center_offset = np.linalg.norm(stp_center - ligand_center)
    # print(center_offset)
    return center_offset

# Calulates the mean x,y,z coordinates of an input pocket (finds the center of a pocket)
# Returns class <numpy.ndarray> called center_offset


def get_STP_center(stp_coords, pocket):
    stp_by_pocket = []

    for stp in stp_coords:
        if stp[0] == pocket:
            stp_by_pocket.append(stp[1:4])
        if stp_by_pocket:
            stp_array = np.array(stp_by_pocket)

    stp_center = np.average(stp_array, axis=0)

    return stp_center

# Calculates float ratio of STP/pocket volume to ligand volume.


def get_volume_ratio(ligand_volume_df, pdb_code, info_txt, pocket):

    # print("get_volume_ratio" + str(pocket))
    # Parses info.txt file outputed by fpocket
    # to retrieve STP/pocket volume for current pocket.
    with open(info_txt, "r") as info:

        for row in info:
            cur_row = row.strip().split()

            if len(cur_row) > 1:
                if cur_row[0] == "Pocket" and int(cur_row[1]) == pocket:
                    for line in range(0, 7):
                        cur_row = info.readline()

                    cur_row = cur_row.strip().split()
                    stp_volume = float(cur_row[2])

        ligand_volume = ligand_volume_df.loc[pdb_code]['ligand_volume']
        volume_ratio = float(stp_volume/ligand_volume)

    return volume_ratio


# Calculated distance in 3D space between two sets of coordinates
# (x1,y1,z1) (x2,y2,z2) returns float of distance between two points.


def calcDist(x1, y1, z1, x2, y2, z2):
    x = (x1 - x2)**2
    y = (y1 - y2)**2
    z = (z1 - z2)**2
    distance = math.sqrt(x + y + z)

    return distance


def getPocketCount(stp_coords):
    pocket_count = []
    for a_sphere in stp_coords:
        pocket = a_sphere[0]
        if pocket not in pocket_count:
            pocket_count.append(pocket)

    return len(pocket_count)


# Return the coordinates of known ligands in a .pdb file
# returns nested list of coordinates [[<x1>,<y1>,<z1>],....]
def getLigandCoordinates(pdbligand, ligands):

    ligcoords = []
    with open(pdbligand, "r") as f:

        for row in f:

            for ligand_code in ligands:
                if ligand_code in row[17:21] and "HETA" in row[0:6]:

                    # x,y,z = parseCoordinates(row)
                    x1 = float(row[30:38])
                    y1 = float(row[38:46])
                    z1 = float(row[46:54])
                    coords = [x1, y1, z1]
                    ligcoords.append(coords)

    # lc: list of lists with atom coordinates. [[x1,y1,z1],[...]...]
    return ligcoords


def getSTPCoords(pdbs):
    stpcoords = []
    with open(pdbs, "r") as f:

        for row in f:
            if "STP" in row[17:21] and "HETATM" in row[0:6]:
                poc = int(row[22:27])
                x1 = float(row[30:38])
                y1 = float(row[38:46])
                z1 = float(row[46:54])
                stpcoords.append([poc, x1, y1, z1])

    return stpcoords


def getPDBCoords(pdb):
    pdb_coords = {}
    with open(pdb, "r") as f:

        if args.align:
            firstline = f.readline()
            nt_subtract = int(firstline[22:26]) - 1

        for row in f:
            if "ATOM" in row[0:6]:
                if args.align:
                    nt_seq = int(row[22:26]) - nt_subtract
                else:
                    nt_seq = int(row[22:26])

                nt_name = row[16:18]
                x2 = float(row[30:38])
                y2 = float(row[38:46])
                z2 = float(row[46:54])
                pdb_coords.setdefault(nt_seq, [])
                pdb_coords[nt_seq].append([nt_name, x2, y2, z2])

    return pdb_coords


# Generates a dataframe with the volume of a ligand for each PDB_code
# in PDB_Ligand directory.
def get_ligand_volume_df():

    ligand_pdb_list = [f for f in iglob(
        "PDB_Ligand/*igand.pdb", recursive=True) if os.path.isfile(f)]
    ligand_volume_df = pd.DataFrame(columns=['pdb_code', 'ligand_volume'])

    for ligand_file in ligand_pdb_list:
        pdb_name = os.path.basename(ligand_file)
        pdb_code = pdb_name[0:4]

        # If Ligand_Only.pdb file does not exist:
        # Parse Ligand.pdb file, select ligand, and write to .pdb.
        if not os.path.exists(f"PDB_Ligand/{pdb_code}_Ligand_only.pdb"):
            pdb = parsePDB(ligand_file)
            ligand = pdb.select('not nucleotide and not water')
            output_pdb_code = f"PDB_Ligand/{pdb_code}_ligand_only.pdb"
            writePDB(f"{output_pdb_code}", ligand)

        # Load Ligand_Only.pdb as RDkit object
        ligand_object = AllChem.MolFromPDBFile(
            f"PDB_Ligand/{pdb_code}_Ligand_only.pdb", sanitize=True, removeHs=False)

        # Add hydrogen atoms to ligand object and calculate volume.
        Chem.AddHs(ligand_object)
        ligand_volume = float(AllChem.ComputeMolVolume(ligand_object))

        # Append ligand volume to ligand_volume_df
        ligand_volume_df = ligand_volume_df.append(
            {'pdb_code': pdb_code, 'ligand_volume': ligand_volume}, ignore_index=True)

    return ligand_volume_df


def pocket_type(s):

    if args.test_set:
        if (s['Ligand_Overlap'] >= 0.25):
            return 'Known'
        else:
            return 'Novel'

    else:
        if (s['Center_Offset'] <= 8) and (s['Volume_Ratio'] >= 0.5) and (s['Volume_Ratio'] <= 3.5) and (s['Ligand_Overlap'] >= 0.25):
            return 'Known'
        elif (s['Ligand_Overlap'] >= 0.25):
            return 'Overlap'
        else:
            return 'Novel'


def getOptAnalysis(opt_df):
    # Changes 'PDB_ID' dtype to category to save time and memory.
    opt_df['PDB_ID'].astype('category')

    # Determines the total number of pockets per parameter set.
    pocket_total_series = opt_df.groupby(
        ['Parameters'])['PDB_ID'].count()

    # Determines the total number of PDB structures with any pockets.
    opt_df['PDB_count'] = opt_df['PDB_ID'].nunique()
    PDB_num = opt_df.groupby(['Parameters'])['PDB_count'].max()

    # Creates a seriers with the mean number of pockets per parameter set.
    pocket_mean_series = pocket_total_series / PDB_num

    # Defines multiple index of fpocket parameters and PDB structures.
    opt_df.set_index(['Parameters', 'PDB_ID'], inplace=True)

    # Adds column with the max. number of pockets in each PDB structure by parameter.
    opt_df['PocNum_Max'] = opt_df.groupby(
        ['Parameters', 'PDB_ID'])['Pocket'].max()

    # Min Max Scalar data normalization function.
    min_max_scaler = MinMaxScaler()

    opt_df.insert(1, 'Pocket_Type', "")
    opt_df['Pocket_Type'] = pd.Categorical(
        opt_df['Pocket_Type'], ['Known', 'Overlap', 'Novel'])
    opt_df['Pocket_Type'] = opt_df.apply(pocket_type, axis=1)

    # Saves "raw" version of opt_df before dropping values and final analysis.
    opt_df.sort_values(by=['Parameters', 'PDB_ID', 'Pocket_Type'], ascending=[
        True, True, True], inplace=False).pipe(saveDF, 'OptEval_RAW')

    # Creates final df of ranked parameter sets and adds column for max num of pockets.
    opt_df_rank = pd.DataFrame(opt_df.groupby(
        ['Parameters'])['PocNum_Max'].max())

    # Adds column with the mean number of pockets per PDB.
    opt_df_rank.insert(0, 'PocNum_Mean', pocket_mean_series)

    # Filers opt_df resulting in a dataframe composed only of known pockets.
    opt_df = opt_df[(opt_df.Pocket_Type == 'Known')]

    # Calculates and adds column for sensitivity of known pocket detection.
    true_pos = opt_df.groupby(['Parameters']).Pocket.count()
    pocket_detected_series = opt_df.reset_index(
        level=[0, 1]).groupby(['Parameters'])['PDB_ID'].nunique()
    false_neg = PDB_num - pocket_detected_series
    sens = true_pos / (true_pos + false_neg)
    opt_df_rank.insert(0, 'Sens', sens)

    # Calculates and adds column for PPV of known pockets.
    false_pos = pocket_total_series - true_pos
    PPV_known = true_pos / (true_pos + false_pos)
    opt_df_rank.insert(1, 'PPV', PPV_known)

    # Sorts final ranked dataframe by sensitivity score.
    opt_df_rank.sort_values(['Sens', 'PPV', 'PocNum_Mean', 'PocNum_Max'], ascending=[
                            False, False, True, True], inplace=True)

    return opt_df, opt_df_rank


# Saves pandas dataframe ojbects to .csv files.
def saveDF(df, name, directory=None):

    if directory is None and args.outputName is None:
        df.to_csv(f'{name}.csv',
                  index=True, float_format='%.3g')
    elif directory is None:
        df.to_csv(f'{args.outputName}_{name}.csv',
                  index=True, float_format='%.3g')
    else:
        df.to_csv(f'{directory}/{args.outputName}_{name}.csv',
                  index=True, float_format='%.3g')


def outputPocketNT(pdb_id, stpcoords, pdbcoords, pdb_nt_list, distancefilter):
    if args.align:
        with open("PocketNT/PocketNT_%s_%sA_%s.txt" % (pdb_id, str(distancefilter), "aligned"), "w+") as f:
            for line in getPocketNT(stpcoords, pdbcoords, pdb_nt_list, distancefilter):
                f.write(str(line[0]) + "\t" + str(line[1]) + "\n")
    else:
        with open("PocketNT/PocketNT_%s_%sA.txt" % (pdb_id, str(distancefilter)), "w+") as f:
            for line in getPocketNT(stpcoords, pdbcoords, pdb_nt_list, distancefilter):
                f.write(str(line[0]) + "\t" + str(line[1]) + "\n")


def getcharacteristics(pdb_code, para_all, stp_coords, pdb_out, info_txt, characteristics_out):
    date = datetime.datetime.now()
    df_pc_pdb = pd.DataFrame()

    with open(info_txt, "r") as f:

        poc_count = 1

        for row in f:

            if "Pocket" in row:
                pocket = int(row.split(" ")[1].strip())
            if "Score :" in row:
                if "Druggability" not in row:
                    score = row.split(":")[1].strip()
            if "Druggability Score :" in row:
                drug_score = row.split(":")[1].strip()
            if "Number of Alpha Spheres :" in row:
                a_sphere = row.split(":")[1].strip()
            if "Total SASA :" in row:
                sasa = row.split(":")[1].strip()
            if "Volume :" in row:
                volume = row.split(":")[1].strip()
            if "Mean local hydrophobic density" in row:
                hydrophobic_density = row.split(":")[1].strip()
            if "Apolar alpha sphere proportion" in row:
                apolar_proportion = row.split(":")[1].strip()
            if "Hydrophobicity score" in row:
                hydrophobicity_score = row.split(":")[1].strip()
            if "Polarity score:" in row:
                polarity_score = row.split(":")[1].strip()
            if "Flexibility" in row:

                if poc_count == pocket:
                    poc_count += 1

                    # Returns stp_center.
                    # Array of mean coorindates of STP for specified pocket.
                    stp_center = get_STP_center(stp_coords, pocket)
                    if args.verbose:
                        d = {'Parameters': [para_all],
                             'PDB_ID': [pdb_id],
                             'Pocket': pocket,
                             'Score': [score],
                             'Drug_Score': [drug_score],
                             'a-spheres': [a_sphere],
                             'SASA': [sasa],
                             'Hydrophobic_Density': [hydrophobic_density],
                             'Apolar_Proportion': [apolar_proportion],
                             'Hydrophobicity': [hydrophobicity_score],
                             'Polarity': [polarity_score],
                             'X': ["{:.2f}".format(stp_center[0])],
                             'Y': ["{:.2f}".format(stp_center[1])],
                             'Z': ["{:.2f}".format(stp_center[2])]}
                    else:
                        d = {'Parameters': [para_all],
                             'PDB_ID': [pdb_id],
                             'Pocket': pocket,
                             'Score': [score],
                             'a-spheres': [a_sphere],
                             'X': ["{:.2f}".format(stp_center[0])],
                             'Y': ["{:.2f}".format(stp_center[1])],
                             'Z': ["{:.2f}".format(stp_center[2])]}

                    df_pc_single_pocket = pd.DataFrame(d)
                    df_pc_pdb = pd.concat(
                        [df_pc_pdb, df_pc_single_pocket], axis=0, ignore_index=True)

    # df_pc_pdb.to_csv(
    #    f'Pocket_Characteristics_{pdb_code}_{para_all}_{date.year}-{date.month}-{date.day}.csv', index=True, float_format='%.3g')

    return df_pc_pdb

######################################


def parseArgs():
    prs = argparse.ArgumentParser()
    prs.add_argument('--directory', type=str, required=True,
                     help="Input file directory for input files.")
    prs.add_argument('-pnt', '--pocketNT', action="store_true",
                     help="Identifies nucleotides within specified distance of a ligand.")
    prs.add_argument('-a', '--align', action="store_true",
                     help="Aligns PocketNT output files to start at nucleotide number 1.")
    prs.add_argument('-opt', '--optEval', action='store_true',
                     help="Evaluate performance of fpocket parameter optimization.")
    prs.add_argument('-pc', '--pocketcharacteristics', action='store_true',
                     help="Output .csv file with pocket charteristics from fpocket output .txt file.")
    prs.add_argument('-v', '--verbose', action="store_true",
                     help="Provides additional pocket characteristics relevant to pocket scores.")
    prs.add_argument('-r', '--ribosome', action='store_true',
                     help='Optimized for ribosome.')
    prs.add_argument('-df', '--distancefilter', type=float,
                     help='Distance filter (in Angstroms) for identifying nucleotides close in space to pockets. Default is 4.5.')
    prs.add_argument('-l', '--ligand', type=str,
                     help='Input disired ligand three-digit code found in the .pdb, otherwise a library of common ligands will be used.')
    prs.add_argument('-pf', '--paraFilter', action="store_true",
                     help="Concatinates parameters listed in output file to a single column.")
    prs.add_argument('-lo', '--ligand_overlap', action='store_true')
    prs.add_argument('-o', '--outputName', type=str, default=None,
                     help='Name of output file')
    prs.add_argument('-an', '--analyze', type=str,
                     help='Only runs getOptAnalysis funcation. Input a string of the path to a .csv file to reanalyze')
    prs.add_argument('-test', '--test_set', action='store_true',
                     help='Removes strict known pocket filters for use on evaluating test sets.')

    args = prs.parse_args()

    return args


if __name__ == "__main__":

    args = parseArgs()

    # Changes working directory to user inputed directory (--directory).
    os.chdir(args.directory)

    if not args.analyze:
        # Recursively creates list of paths for all *_out.pdb files from fpocket.
        out_pdb = [f for f in iglob(
            "fpocketOutput*/*out/*_out.pdb", recursive=True) if os.path.isfile(f)]

        # Set ligand varible based on user input (-l) or predefined list.
        if args.ligand:
            ligands = args.ligand
        else:
            ligands = ["SAM", "SAH", "3AY", "TPS", "LYS", "PYI", "FMN", "6GO",
                       "5AZ", "GLY", "C2E", "6AP", "2QB", "PRF", "ADE", "ZMP",
                       "GLN", "6YG", "GAI", "PRP", "G4P", "AMZ", "H4B", "TPP",
                       "BTN", "MGR", "DAI", "GTP", "GLP", "GNG", "VIB", "4PQ",
                       "51B", "GUN", "XAN", "QAX", "V4J", "YO3", "J8F", "X5R",
                       "V6T", "NNR", "1TU", "29G", "2ZY", "FH8", "53D", "ISH",
                       "UYS", "PMZ", "QSY"]

        # Defines the distance filter from user input (-df) or a default value of 4.5A.
        if args.distancefilter:
            distancefilter = args.distancefilter
        else:
            distance_filter = 4.5

        if args.optEval:
            print("Hang back and relax this might take a while \U0001F919.")
            print()

            # Creates dataframe which will be appended with the evaluation scores
            # for each parameter set, PDB, and pocket.
            opt_df = pd.DataFrame(columns=['Parameters', 'PDB_ID', 'Pocket',
                                           'Ligand_Overlap', 'Pocket_Overlap',
                                           'Center_Offset', 'Volume_Ratio'])

            # Generates a dateframe with the volume of each ligand indexed PDB code.
            print('Measuring ligand volumes \U0001F4D0...')
            ligand_volume_df = get_ligand_volume_df()
            ligand_volume_df.set_index("pdb_code", inplace=True)

        if args.optEval:
            total_out_pdb = len(out_pdb)
            progress_increment = 100 / total_out_pdb
            print()
            print(f"Evaluating {total_out_pdb} fpocket outputs...")
            pbar = tqdm(
                total=100, bar_format="{desc}: {percentage:.2f}%|{bar}| [{elapsed} < {remaining}]")

        # Iterate through *_out.pdb files and store PDB code.
        for pdb_out in out_pdb:
            pdb_path = os.path.basename(pdb_out)
            pdb_code = pdb_path[0:4]
            pdbName = pdb_path[0:-8]

            # Split pdb path to obtain optimization parameters
            if args.optEval or args.pocketNT or args.pocketcharacteristics:
                pdb_split1 = pdb_out.split("/")
                pdb_split2 = pdb_split1[0].split("-")
                para_m = pdb_split2[1].split("_")[1]
                para_M = pdb_split2[2].split("_")[1]
                para_i = pdb_split2[3].split("_")[1]
                para_D = pdb_split2[4].split("_")[1]

                para_all = f"m{para_m}_M{para_M}_i{para_i}_D{para_D}"
            # Changes the method for obtaining pdb_id based on file naming skeem
            # for riboswitches or the ribosome.
            if args.ribosome:
                pdb_id = pdbName
            else:
                pdb_id = pdb_code

            # Defines varibles for the paths to *_info.txt and *_ligand.pdb files
            # which match the optimization parameters and PDB_id to the *_out.pdb.
            info_txt = f"{pdb_split1[0]}/{pdb_split1[1]}/{pdbName}_info.txt"
            pdb_ligand = f"PDB_Ligand/{pdb_code}_Ligand.pdb"

            # Runs pocketNT. Determines nucleotides that are near a-spheres based
            # on distance filter. Returns a list of lists containing a nucleotide
            # number and the number of the highest ranked nearby pocket.
            # list of lists: [[<nucleotide #, pocket #],...]
            if args.pocketNT:
                print(f"PocketNT PDB: {pdb_code}")
                pdb_coords = getPDBCoords(pdb_out)
                stp_coords = getSTPCoords(pdb_out)
                pdb_nt_list = getPDB_NT_list(pdb_coords)

                pocketnt_path = os.path.join(args.directory, "PocketNT")
                if not os.path.isdir(pocketnt_path):
                    os.mkdir(pocketnt_path)

                outputPocketNT(pdb_id, stp_coords, pdb_coords,
                               pdb_nt_list, distance_filter)

            # Gathers pocket characteristics from fpocket output into a pandas dataframe and outputs as a .csv file.
            if args.pocketcharacteristics:
                #print(f"pocketcharacteristics: {pdb_code}")
                characteristics_out = f"{pdb_split1[0]}/{pdb_split1[1]}/"
                stp_coords = getSTPCoords(pdb_out)
                df_pc_pdb = getcharacteristics(pdb_id, para_all, stp_coords, pdb_out,
                                               info_txt, characteristics_out)
                saveDF(
                    df_pc_pdb, f'{pdb_code}_pocket_characteristics_out', characteristics_out)

            # Evaluates the performance of fpocket parameters based on
            # ligand overlap, pocket overlap, center, and volume criteria.
            # Activated by flag (-opt).
            if args.optEval:
                pdb_coords = getPDBCoords(pdb_out)
                stp_coords = getSTPCoords(pdb_out)
                pockets = getPocketCount(stp_coords)
                ligand_coords = getLigandCoordinates(pdb_ligand, ligands)

                # Runs evaluation methods for each pocket in the current PDB.
                for pocket in range(1, pockets + 1):
                    ligand_overlap = getLigandOverlap(
                        stp_coords, pdb_coords, ligand_coords, pocket)
                    pocket_overlap = getPocketOverlap(
                        stp_coords, pdb_coords, ligand_coords, pocket)
                    center_offset = get_center_offset(
                        stp_coords, ligand_coords, pocket)
                    volume_ratio = get_volume_ratio(
                        ligand_volume_df, pdb_code, info_txt, pocket)

                    # Dictionary 'd' stores evaluation scores for the current pocket.
                    d = {'Parameters': [para_all],
                         'PDB_ID': [pdb_id],
                         'Pocket': pocket,
                         'Ligand_Overlap': [ligand_overlap],
                         'Pocket_Overlap': [pocket_overlap],
                         'Center_Offset': [center_offset],
                         'Volume_Ratio': [volume_ratio]}

                    opt_df2 = pd.DataFrame(d)
                    opt_df = opt_df.append(opt_df2, ignore_index=True)
            if args.optEval:
                pbar.update(progress_increment)
        if args.optEval:
            pbar.close()

if args.analyze:
    opt_df = pd.read_csv(args.analyze)

if args.optEval or args.analyze:

    # Finds best pocket for each PDB for each parameter set.
    opt_df_known, opt_df_rank = getOptAnalysis(opt_df)

    saveDF(opt_df_known, 'OptEval_Known')
    saveDF(opt_df_rank, 'OptEval_Rank')
    print()
    print('Done! \U0001F973')
