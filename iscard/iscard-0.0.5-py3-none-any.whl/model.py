import pandas as pd
from sklearn.metrics import pairwise_distances_chunked, pairwise_distances
from itertools import product
import numpy as np
import os
import matplotlib.pyplot as plt
import logging
from iscard import core, __version__


class Model(object):
    """Compute intermodel and intramodel from bam file and serialize it into a hdf5 file 
    
    Attributes:
        bamlist (list): List of bam files 
        bedfile (str): Region bedfile
        inter_model (pd.DataFrame): contains inter_model z-score
        intra_model (pd.DataFrame): contains intra_model z-score
        jobs (int): Description
        model_version (TYPE): Description
        norm_raw (pd.DataFrame): Normalized Raw depth 
        raw (pd.DataFrame): Raw depth
        sample_rate (int): Sampling rate 
    """

    def __init__(self, modelfile=None):
        super().__init__()

        self.raw = None
        self.bamlist = []
        self.bedfile = None
        self.inter_model = None
        self.intra_model = None
        self.model_version = __version__
        self.sample_rate = 100
        self.threads = -1

        if modelfile:
            self.from_hdf5(modelfile)

    def get_group_names(self):
        """Return group name from bedfile as defined in the fouth column
        
        Returns:
            list: list of goup name 
        """
        return list(core.read_bed(self.bedfile)["name"].unique())

    def learn(
        self,
        bamlist: list,
        bedfile: str,
        show_progress=True,
        threads=1,
        sample_rate=100,
    ):
        """Create intrasample and intersample model
        
        Args:
            bamlist (list): List of bam files 
            bedfile (str): Description
            show_progress (bool, optional): Description
        """
        self.threads = threads
        self.sample_rate = sample_rate

        logging.info(
            """
            Model threads: {:>5} 
            Sampling rate: {:>5} 
            training set: {:>5}
            """.format(
                self.threads, self.sample_rate, len(bamlist)
            )
        )

        self.bamlist = bamlist
        self.bedfile = bedfile

        self.raw = core.compute_coverage(
            self.bamlist,
            self.bedfile,
            sample_rate=self.sample_rate,
            show_progress=show_progress,
            threads=self.threads,
        )

        self._compute_super_model()

    def _compute_super_model(self):
        """ compute intra and inter model and merge them into super model """

        if self.raw is None:
            raise IscardError("No depth computed. ")

        logging.info(f"Create super model model")

        self.create_inter_samples_model()
        self.create_intra_samples_model()
        self.super_model = pd.concat(
            (self.intra_model, self.inter_model), axis=1, verify_integrity=True
        )

        logging.info("Super model done with {}".format(len(self.super_model)))

    def create_inter_samples_model(self):
        """Create inter sample model
        This model compute the mean and the standard deviation from training sampling.
        This will be used later to compute a inter z-score in a new sample
        """

        logging.info(f"Create inter model")

        self.norm_raw = core.scale_dataframe(self.raw)
        self.inter_model = pd.DataFrame(
            {
                "mean": self.norm_raw.mean(axis=1),
                "median": self.norm_raw.median(axis=1),
                "std": self.norm_raw.std(axis=1),
                "min": self.norm_raw.min(axis=1),
                "max": self.norm_raw.max(axis=1),
            }
        )

    def create_intra_samples_model(self):
        """Create intra sample model
        This model compute depth correlation within samples. 
        This will be used later to compute a new intra z-score in a new sample
        """
        # Keep row every step line
        # reset index because we are going to work on integer index

        logging.info(f"Create intra model")

        sub_raw = self.raw.reset_index()
        # sub_raw = sub_raw[sub_raw.index % self.sampling == 0]

        # Create Mask index
        # This is used to avoid pairwise comparaison within same name
        # For example, if name is = [A,A,A,B,B,C], it computes the following mask

        #   A A A B B C
        # A 0 0 0 1 1 0
        # A 0 0 0 1 1 0
        # A 0 0 0 1 1 0
        # B 1 1 1 0 0 1
        # B 1 1 1 0 0 1
        # C 1 1 1 1 1 0

        index = sub_raw["name"]
        mask = np.array([i[0] == i[1] for i in product(index, index)]).reshape(
            len(index), len(index)
        )

        # return to multiindex
        sub_raw = sub_raw.set_index(["name", "chrom", "pos"])

        def _reduce(chunk, start):
            """This function is called internally by pairwise_distances_chunked
            @see https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise_distances_chunked.html
            
            This function looks for the maximum correlation  value in the chunk matrix and return the id 
            Same name in pairwise are skiped by the mask 
            
            For example:
                      A   B   C 
                A    NA  0.9  0.8
                B    0.5 NA  0.4
                C    0.3 0.7  NA
            
            Will return a dataframe:
             id   idx  corr 
             A     B    0.9
             B     C    0.4
             C     B    0.9
            
            Args:
                chunk (TYPE): Description
                start (TYPE): Description
            
            Returns:
                TYPE: Description
            
            """
            # skip na value
            chunk[np.isnan(chunk)] = 1
            # correlation metrics from sklearn is 1 - corr
            chunk = 1 - chunk
            rows_size = chunk.shape[0]

            select_mask = mask[start : start + rows_size]
            # looks for id of maximum correlation value
            idx = np.argmax(np.ma.masked_array(chunk, select_mask), axis=1)

            # We only get idx, let's get correlation value
            corr = []
            for i, index in enumerate(idx):
                corr.append(chunk[i][index])

            # Create a dataframe
            return pd.DataFrame(
                {"idx": idx, "corr": corr}, index=range(start, start + rows_size)
            )

        # Perform pairwise correlation by using pairwise_distances_chunked to avoid memory limit

        all_reduce_chunk = []

        # -1 mean all jobs
        for chunk in pairwise_distances_chunked(
            sub_raw, metric="correlation", reduce_func=_reduce, n_jobs=self.threads
        ):
            all_reduce_chunk.append(chunk)

        self.intra_model = pd.concat(all_reduce_chunk)
        ss = sub_raw.reset_index(drop=True)

        # avoid warning : polynomial.py:630: RuntimeWarning: invalid value encountered in true_divide

        with np.errstate(divide="ignore", invalid="ignore"):
            for i, row in self.intra_model.iterrows():

                j = row["idx"]

                x = ss.loc[i, :]
                y = ss.loc[j, :]

                try:
                    coef, intercept = tuple(np.polyfit(x, y, 1))
                    yp = x * coef + intercept
                    error = yp - y
                    std = error.std()
                except:
                    coef, intercept = 0, 0
                    std = np.NaN

                self.intra_model.loc[i, "coef"] = coef
                self.intra_model.loc[i, "intercept"] = intercept
                self.intra_model.loc[i, "std2"] = std

        self.intra_model = self.intra_model.set_index(sub_raw.index)

    def to_hdf5(self, filename: str):
        """Serialize model to hdf5
        
        Args:
            filename (str): hdf5 filename. eg: model.h5
        
        Raises:
            core.IscardError: If model has not been trained 
        """
        if self.raw is None or self.intra_model is None or self.inter_model is None:
            raise core.IscardError("model has not been computed")

        self.raw.to_hdf(filename, "raw")
        # TODO : remove inter and intra model .. because it is already in super_model ?
        # Or maybe keep both model with different sampling size ?

        self.inter_model.to_hdf(filename, "inter_model")
        self.intra_model.to_hdf(filename, "intra_model")
        self.super_model.to_hdf(filename, "super_model")

        pd.Series(self.bamlist).to_hdf(filename, "bamlist")
        metadata = pd.Series(
            {
                "sample_rate": str(self.sample_rate),
                "region": str(os.path.abspath(self.bedfile)),
                "version": self.model_version,
            }
        )

        metadata.to_hdf(filename, "metadata")

    def from_hdf5(self, filename: str):
        """Set the model instance from a hdf5 file
        
        Args:
            filename (str): hdf5 filename. eg: model.h5
        """
        self.raw = pd.read_hdf(filename, "raw")
        self.inter_model = pd.read_hdf(filename, "inter_model")
        self.intra_model = pd.read_hdf(filename, "intra_model")
        self.super_model = pd.read_hdf(filename, "super_model")

        self.bamlist = list(pd.read_hdf(filename, "bamlist"))

        metadata = pd.read_hdf(filename, key="metadata")
        self.sample_rate = int(metadata["sample_rate"])
        self.bedfile = metadata["region"]
        self.model_version = metadata["version"]

    def test_sample(self, bamfile: str, show_progress=True) -> pd.DataFrame:
        """Test a new sample against the current model
        
        model = Model("model.h5")
        data = model.test_sample("sample.bam")
        
        The dataframe contains for each position:
            - depth : the raw depth 
            - depth_norm: the normalized raw depth
            - inter_z: the inter-model z-score
            - depth_mate: the raw depth of the mate 
            - depth_mate_predicted: the raw depth predicted by the intra-model
            - intra_z: the intra-model z-score 
        
        Args:
            bamfile (str): A sample bam file
        
        Returns:
            pd.DataFrame
        """
        del_coverage = core.get_coverages_from_bed(
            bamfile,
            self.bedfile,
            sample_rate=self.sample_rate,
            show_progress=show_progress,
        )
        dd = del_coverage.copy()
        dd.columns = ["depth"]

        # Compute inter model
        dd["depth_norm"] = core.scale_dataframe(dd)["depth"]
        dd["inter_z"] = (
            dd["depth_norm"] - self.super_model["mean"]
        ) / self.super_model["std"]

        # # Compute intra model
        depth_mate = dd.iloc[self.super_model["idx"], :]["depth"].to_list()
        dd["depth_mate"] = depth_mate
        dd["depth_mate_predicted"] = (
            self.super_model["coef"] * dd["depth"]
        ) + self.super_model["intercept"]
        dd["error_intra"] = dd["depth_mate_predicted"] - dd["depth_mate"]
        dd["intra_z"] = dd["error_intra"] / self.super_model["std2"]

        return dd

    def __len__(self) -> int:
        """Return row size of the model
        
        Returns:
            int
        """
        return len(self.raw)

    def print_infos(self):
        """Print description of the model 
        """
        print("Model version: {}".format(self.model_version))
        print("Depth position counts: {}".format(len(self.inter_model)))
        print("bedfile: {}".format(self.bedfile))
        print("sample rate: {}".format(self.sample_rate))

        print("Bam(s) used: {}".format(len(self.bamlist)))
        for bam in self.bamlist:
            print("\t - " + bam)

        gps = self.get_group_names()

        print("Group names(s): {}".format(len(gps)))
        for g in gps:
            print("\t - " + g)

        print("Inter model shape: {}".format(self.inter_model.shape))
        print("Intra model shape: {}".format(self.intra_model.shape))


def call_test(
    test_data: pd.DataFrame, column="inter_z", threshold=1.96, consecutive_count=1000
):
    """Call region from self.test_data
    
    Args:
        test_data (pd.DataFrame): Description
        column (str, optional): Description
        threshold (float, optional): Description
        consecutive_count (int, optional): Description
        group_name (str)
    
    Yields:
        TYPE: region 
    """

    for region in core.call_region(test_data[column], threshold, consecutive_count):
        first, last = region
        chrom = test_data["chrom"][first]
        name = test_data["name"][first]

        x1 = test_data["pos"][first]
        x2 = test_data["pos"][last]

        yield (chrom, x1, x2, name)


def plot_test(
    outputfile: str,
    test_data: pd.DataFrame,
    model: Model,
    group_name: str,
    call=True,
    threshold=2,
    consecutive_count=1000,
):

    data = test_data.query("name == @group_name")
    mm = model.inter_model[["min", "max", "mean"]].loc[group_name, :].reset_index()

    figure, ax = plt.subplots(3, 1, figsize=(30, 10))

    figure.suptitle(group_name, fontsize=30)

    ax[0].grid(True)
    ax[0].set_xlabel("position")
    ax[0].set_ylabel("raw depth")
    ax[0].fill_between("pos", "min", "max", color="lightgray", alpha=1, data=mm)
    ax[0].plot(data["pos"], data["depth_norm"], color="#32afa9")

    ax[1].grid(True)
    ax[1].set_xlabel("position")
    ax[1].set_ylabel("Inter z-score")
    ax[1].plot(data["pos"], data["inter_z"], color="lightgray")
    ax[1].plot(data["pos"], data["inter_z"].rolling(500).mean(), color="#32afa9")

    # ax[0].plot(data["pos"], data["inter_z"].rolling(500).mean())

    ax[2].grid(True)
    ax[2].set_ylabel("Intra z-score")
    ax[2].scatter(data["pos"], data["intra_z"], color="#32afa9")

    # Plot region
    if call:
        for region in call_test(data):
            chrom, x1, x2, name = region
            ax[0].axvspan(x1, x2, alpha=0.5, color="red")
            ax[1].axvspan(x1, x2, alpha=0.5, color="red")
            ax[2].axvspan(x1, x2, alpha=0.5, color="red")

    plt.savefig(outputfile)
