import numpy as np
import pandas as pd
import pysam
from sklearn.preprocessing import MinMaxScaler, StandardScaler, MaxAbsScaler
import matplotlib.pyplot as plt

import multiprocessing as mp
from functools import partial


# Pysamstats warns this
# RuntimeWarning: pysam.libcalignedsegment.PileupColumn size changed,
# may indicate binary incompatibility. Expected 72 from C header, got 88 from PyObject
# I cannot fixed it, don't show it
import warnings

with warnings.catch_warnings(record=True) as w:
    import pysamstats


import os
import re
from tqdm import tqdm

from atpbar import atpbar
from atpbar import register_reporter, find_reporter, flush

import iscard

# import pprint


class IscardError(Exception):
    pass


def func(arg1, arg2):
    """Summary line.

    Extended description of function.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value

    """
    return True


def read_bed(filename: str) -> pd.DataFrame:
    """return a dataFrame from bed bedfile 

    Bedfile must have 4 colonnes : chr, start, end, name.
    Name can be the gene name or any other group name. 
    
    Args:
        filename (str): bed file
    
    Returns:
        pd.DataFrame: a Dataframe with 4 colonnes : chr, start,end, name
    """
    return pd.read_csv(
        filename, sep="\t", header=None, names=["chrom", "start", "end", "name"]
    ).drop_duplicates()


def get_coverage(
    bamfile: str, chrom: str, start: int, end: int, sample_rate=1
) -> pd.DataFrame:
    """Get read depth from from bam files according location  

    Args:
        bamfile (str): a bam file with index
        chrom (str): chromosome name
        start (int): start position of interest
        end (int): end position of interest
      
    Returns:
        pd.DataDrame: A dataframe with chromosom, position and depth for each bam file 
    
    """
    import warnings

    mybam = pysam.AlignmentFile(bamfile)
    df = pd.DataFrame(
        pysamstats.load_coverage(
            mybam,
            chrom=chrom,
            start=start,
            end=end,
            truncate=True,
            pad=True,
            fields=["chrom", "pos", "reads_all"],
        )
    )

    df["chrom"] = df["chrom"].apply(lambda x: x.decode())
    df.rename({"reads_all": "depth"}, inplace=True, axis=1)

    # keep line every sample_rate row
    df = df[df.index % sample_rate == 0]

    return df


def get_coverages_from_bed(
    bamfile: str, bedfile: str, sample_rate=100, show_progress=True
):

    sample_name = os.path.basename(bamfile).replace(".bam", "")
    bed = read_bed(bedfile)

    all_regions = []

    if show_progress:
        generator = tqdm(list(bed.iterrows()))
    else:
        generator = bed.iterrows()

    for i, row in generator:

        chrom, start, end, name = row["chrom"], row["start"], row["end"], row["name"]

        cov = get_coverage(bamfile, chrom, start, end, sample_rate)
        cov["name"] = name
        all_regions.append(cov.values)

    df = pd.DataFrame(
        np.concatenate(all_regions), columns=["chrom", "pos", sample_name, "name"]
    )
    df[sample_name] = df[sample_name].astype(np.uint16)

    return df.set_index(["name", "chrom", "pos"])


def compute_coverage(
    bamfiles: list, bedfile: str, sample_rate=100, threads=None, show_progress=True
):
    """ Compute coverage all all bamfile using multithreading"""
    if threads is None:
        theads = 1

    with mp.Pool(threads) as pool:
        worker = partial(
            get_coverages_from_bed,
            bedfile=bedfile,
            sample_rate=sample_rate,
            show_progress=show_progress,
        )
        data = pd.concat(pool.map(worker, bamfiles), axis=1)

    return data


def scale_dataframe(df):
    new_df = df.copy()
    scaler = MaxAbsScaler()
    # scale data
    scale_df = pd.DataFrame(scaler.fit_transform(new_df), columns=new_df.columns)

    # Need to apply same index for scale_df before updating values
    new_df.update(scale_df.set_index(new_df.index))

    return new_df


def call_region(serie: pd.Series, threshold=2, consecutive_count=100):
    counter = 0
    valid = False

    for index, i in serie.items():
        if abs(i) > threshold:
            counter += 1
            if counter == 1:
                begin = index
        else:
            counter = 0
            if valid == True:
                valid = False
                yield (begin, end)

        if counter > consecutive_count:
            end = index
            valid = True


def print_bedgraph(df: pd.DataFrame, column: str, name=None):

    if not name:
        name = "Iscard data"

    print(
        f"""track type=bedGraph name="{name}" description="BedGraph format" 
        visibility=full color=200,100,0 altColor=0,100,200 priority=20")"""
    )

    for index, row in df.iterrows():
        chrom = row["chrom"]
        start = row["pos"]
        end = row["pos"] + 1
        value = row[column]

        print(chrom, start, end, value, sep="\t")


# def create_model(bamlist: list, bedfile:str, output:str, window = 1, agg="mean"):
#     """ create hdf5 model """

#     #write bam list
#     pd.Series([os.path.abspath(i) for i in bamlist]).to_hdf(output, key="bamlist")

#     # write metadata
#     pd.Series({"window": window, "agg":agg, "region":os.path.abspath(bedfile)}).to_hdf(output, key="metadata")

#     print("compute model")
#     # compute and write raw dataframe
#     raw = get_coverages_from_bed(bamlist,bedfile, window = 1, agg = agg )
#     raw.to_hdf(output, "raw")

#     # Scale
#     scale_raw = scale_dataframe(raw)
#     model = pd.DataFrame(
#     {
#         "mean":scale_raw.mean(axis=1),
#         "median":scale_raw.median(axis=1),
#         "std": scale_raw.std(axis=1),
#         "min": scale_raw.min(axis=1),
#         "max": scale_raw.max(axis=1),
#     })

#     model.to_hdf(output,key="model")


# def test_sample(bam: str, model: str, output: str):

#     metadata = pd.read_hdf(model, "metadata")

# #    print(model)
#     model = pd.read_hdf(model, "model")

#     region = metadata["region"]
#     window = metadata["window"]
#     agg = metadata["agg"]

#     sample_df = get_coverages_from_bed([bam],region, window = window, agg = agg )

#     depth = sample_df.iloc[:,0]
#     sample_df = scale_dataframe(sample_df)

#     model = model.reset_index()

#     model["depth"] = depth.reset_index(drop=True)
#     model["depth_scale"] = sample_df.reset_index(drop=True).iloc[:,0]
#     model["z"]  = ( model["depth_scale"] - model["mean"]) / model["std"]
#     model["zscore"] = model["z"].rolling(300).mean()

#     model.to_hdf(output, key="sample")

# def bedgraph_sample(testfile:str, column = "sample_z"):

#     sample_df = pd.read_hdf(testfile, "sample")

#     if column not in sample_df.columns:
#         print("select another column")
#         return

#     #sample_df[column] = sample_df[column].apply(round)

#     with open("/dev/stdout","w") as file:
#         header = f"track type=bedGraph name=\"Iscard sample\" description=\"Iscard sample\" visibility=full color=200,100,0 altColor=0,100,200 priority=20"
#         file.write(header + "\n")
#         sample_df[["chrom","pos","pos",column]].to_csv(file , sep="\t", header=False, index=False)


# def detect_outside_region(sample_df, threshold = 2, times = 100):
#     counter = 0
#     valid = False
#     for index, i in sample_df.items():
#         if abs(i) > threshold:
#             counter+= 1
#             if counter == 1:
#                 begin = index[1]
#         else:
#             counter = 0
#             if valid == True:
#                 valid =  False
#                 yield (begin,end)

#         if counter > times:
#             end = index[1]
#             valid = True


# def plot_sample(testfile: str, name:str, coordinate:str, output:str):

#     if not name:
#         print("select a gene name ")
#         return

#     match = re.search(r'(chr\w+)\:(\d+)-(\d+)', coordinate )

#     if  match:
#         (chrom,start, end) = match.groups()
#         print(chrom,start, end)

#     sample_df = pd.read_hdf(testfile, "sample")

#     df = sample_df.query("name == @name")

#     if match:
#         df = query("pos >@start & pos < @end ")


#     figure, ax = plt.subplots(2,1, figsize=(30,10))
#     plt.subplots_adjust(hspace = 0.3)

#     figure.suptitle("PKD1", fontsize=30)

#     ax[0].grid(True)
#     ax[0].set_xlabel('position')
#     ax[0].set_ylabel('raw depth')

#     ax[0].plot("pos", "sample", data = df, color="red")
#     ax[0].plot("pos", "mean", data = df, color="#455c7c", ls='--', lw=1)
#     ax[0].fill_between("pos","min", "max", color="blue", alpha=0.2, data = df)
#     handles, labels = ax[0].get_legend_handles_labels()
#     ax[0].legend(handles, labels)

#     ax[1].grid(True)
#     ax[1].set_xlabel('position')
#     ax[1].set_ylabel('z-score')

#     ax[1].plot("pos", "sample_z", data = df, color="#ff6961")
#     ax[1].plot("pos", "sample_zsmooth", data = df, color="green", linewidth=2)

#     ax[1].set_ylim(-10,10)
#     handles, labels = ax[1].get_legend_handles_labels()
#     ax[1].legend(handles, labels)

#     d = sample_df.set_index(["chrom","pos"])


#     # detect region
#     outside_regions = detect_outside_region(df.set_index(["chrom","pos"])["sample_z"], threshold=2, times=500)

#     for region in outside_regions:
#         ax[0].axvspan(*region, alpha=0.5, color='lightgray')
#         ax[1].axvspan(*region, alpha=0.5, color='lightgray')


#     figure.savefig(output)


# def print_model_info(model_file:str):

#     pp = pprint.PrettyPrinter(indent=4)

#     bamlist = list(pd.read_hdf(model_file, key="bamlist"))

#     model = pd.read_hdf(model_file,key="model")

#     print("Regions scanned:\n")
#     print("{} position(s)".format(model.shape[0]))

#     print("\n")

#     print("{} Bam(s) used for the model: \n".format(len(bamlist)))
#     print("\n".join(list(pd.read_hdf(model_file, key="bamlist"))))

#     print("\n")

#     print("Model arguments: \n")
#     for key, value in dict(pd.read_hdf(model_file, key="metadata")).items():
#         print("{:<10}{:<10}".format(key+":",str(value)))


# # write metadata
# pd.Series({"window": window, "agg":agg, "region":os.path.abspath(bedfile)}).to_hdf(output, key="metadata")

# print("compute model")
# # compute and write raw dataframe
# raw = get_coverages_from_bed(bamlist,bedfile, window = 1, agg = agg )
# raw.to_hdf(output, "raw")

# # Scale
# scale_raw = scale_dataframe(raw)
# model = pd.DataFrame(
# {
#     "mean":scale_raw.mean(axis=1),
#     "median":scale_raw.median(axis=1),
#     "std": scale_raw.std(axis=1),
#     "min": scale_raw.min(axis=1),
#     "max": scale_raw.max(axis=1),
# })

# model.to_hdf(output,key="model")
