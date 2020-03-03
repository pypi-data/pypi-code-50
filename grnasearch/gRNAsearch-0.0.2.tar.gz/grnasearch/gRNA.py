from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import pandas as pd
import re


def search(syn, tag, save=True, output_dir="~", output_name="gRNA"):
    try:
        for record in SeqIO.parse(syn, "fasta"):
            ori_seq = Seq(str(record.seq), IUPAC.unambiguous_dna)
            rev_com_seq = str(ori_seq.reverse_complement())
    except FileNotFoundError:
        print("Sequence file not found!")
        exit(1)
    except:
        print("Sequence file error!")
        exit(1)
    try:
        dic = pd.read_csv(tag, header=0)
    except FileNotFoundError:
        print("PCR Tag file not found!")
        exit(1)
    except:
        print("PCR Tag file error!")
        exit(1)

    total_len = len(ori_seq)
    foundlist = []
    # make WT reference table
    for idx, row in dic.iterrows():
        ori_result = ori_seq.find(row["Forward Syn"])
        if ori_result != -1:
            WT = str(ori_seq[int(ori_result - 25):ori_result] + row['Forward WT'] + ori_seq[int(
                ori_result + len(row["Forward Syn"])):ori_result + len(row["Forward Syn"]) + 26])
            foundlist.append(
                [row["Amplicon"], int(ori_result - 25), int(ori_result + len(row["Forward Syn"]) + 26), "Forward", WT])
        else:
            print(idx, row["Forward Syn"], " not found!")
        com_result = rev_com_seq.find(row["Reverse Syn"])
        if com_result != -1:
            WT = str(rev_com_seq[int(com_result - 25):com_result] + row['Reverse WT'] + rev_com_seq[int(
                com_result + len(row["Reverse Syn"])):com_result + len(row["Reverse Syn"]) + 26])
            foundlist.append([row["Amplicon"], int(total_len - int(com_result + len(row["Reverse Syn"]) + 26)),
                              int(total_len - int(com_result - 25)), "Reverse", WT])
        else:
            print(idx, row["Reverse Syn"], " not found!")
    frames = pd.DataFrame(foundlist, columns=['Amplicon', 'syn_FWD_start', 'syn_FWD_end', 'strand', 'WT_5_to_3'])

    output = []
    for idx, row in frames.iterrows():
        WT = row['WT_5_to_3']
        if row['strand'] == "Forward":
            seq = ori_seq
            start = row["syn_FWD_start"]
            end = row["syn_FWD_end"]
        elif row['strand'] == "Reverse":
            seq = rev_com_seq
            start = total_len - row["syn_FWD_end"]
            end = total_len - row["syn_FWD_start"]
        frame = str(seq[start:end])
        target = [n.start() for n in re.finditer(".GG", frame)]
        if len(target) != 0:  # make sure NGG exists on syn
            for f in target:
                f_abs = f + start
                if row['strand'] == "Forward":
                    newstart = f_abs - 20
                    newend = f_abs + 3
                elif row['strand'] == "Reverse":
                    newstart = total_len - (f_abs + 3)
                    newend = total_len - (f_abs - 20)
                else:
                    print("Deprecated intermediate file at line {}!".format(idx))
                    exit(1)
                GGpos = [n.start() for n in re.finditer("GG", WT)]  # find GG on WT
                if len(GGpos) != 0:  # GG found on WT
                    ce = 0
                    ct = 0
                    for GG in GGpos:
                        eight = WT[GG - 9:GG - 1]  # get -8 to -1
                        if eight == str(seq[f_abs - 8:f_abs]):  # -8 to -1 same
                            twelve = WT[GG - 21:GG - 9]  # get -20 to -9
                            if twelve == str(seq[f_abs - 20:f_abs - 8]):  # -20 to -9 same
                                break
                            else:  # -20 to -9 different for this GG
                                ct += 1
                        else:  # -8 to -1 different for this GG
                            ce += 1
                            ct += 1
                    if ce == len(GGpos) and ct == len(GGpos):  # -8 to -1 different for all GG
                        output.append(
                            [str(seq[f_abs - 20:f_abs + 3]), "8 different", row['strand'], row['Amplicon'], newstart,
                             newend])
                        # print("eight different: " + str(seq[f_abs - 20:f_abs + 3]))
                    elif ct == len(GGpos):  # -20 to -9 different for all GG
                        output.append(
                            [str(seq[f_abs - 20:f_abs + 3]), "12 different", row['strand'], row['Amplicon'], newstart,
                             newend])  # use with causion
                        # print("twelve caution: " + str(seq[f_abs - 20:f_abs + 3]))
                    else:
                        # print("All same found! Do not use!")  # do not use
                        pass
                else:  # GG not found on WT
                    output.append(
                        [str(seq[f_abs - 20:f_abs + 3]), "GG different", row['strand'], row['Amplicon'], newstart,
                         newend])
                    # print("GG not found in WT: " + str(seq[f_abs - 20:f_abs + 3]))
        else:
            print("No NGG found at line {}.".format(idx))

    summary = pd.DataFrame(output,
                           columns=['5_to_3_sequence', 'pattern', 'strand', 'amplicon', 'syn_FWD_start', 'syn_FWD_end'])
    if save:
        frames.to_csv("{}/{}_intermediate.csv".format(output_dir, output_name), index=False)
        summary.to_csv("{}/{}_search.csv".format(output_dir, output_name), index=False)
        print("Done! Results are in {}".format(output_dir))
    return summary, frames


