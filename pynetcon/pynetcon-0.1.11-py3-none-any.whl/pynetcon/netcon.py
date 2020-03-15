import oct2py
import os
import subprocess
import shutil

def netcon(leg_links, verbosity, cost_type, mu_cap, allow_ops, leg_costs):
    """Binding for netcon.m netcon function

    This function is a Python wrapper for the netcon.m netcon function,
    which calculates the optimal contraction order for a tensor network.

    Parameters
    ----------
    leg_links : tuple of list of int
        Each entry of leg_links describes the connectivity of the tensor that
        entry represents.
        Each entry is a list that has an entry for each leg of the corresponding tensor.
        Values ``0,1,2,...`` are labels of contracted legs and should appear
        exactly twice in `leg_links`.
    verbosity : integer representing levels of output for the program
        0: Quiet. 
        1: State final result. 
        2: State intermediate and final results. 
        3: Also display object sizes during pairwise contractions
    cost_type : integer representing cost type of tensor indices
        1: Absolute value. 
        2: Multiple and power of chi
    mu_cap : integer representing initial upper-bound cost of search (recommended value 1)
    allow_ops : boolean dictating search that includes outer products (True) or not (False)
    leg_costs : list of list of int
        For costType==1: nx2 table. A row reading [a b] assigns a dimension of b to index a. Default: 2 for all legs.
        For costType==2: nx3 table. A row reading [a b c] assigns a dimension of bX^c to index a, for unspecified X. Default: 1X^1 for all legs.

    Returns
    -------
    sequence : list of int
        a sequence of leg links yielding an optimal contraction order
    """

    netcon_path = os.path.dirname(__file__) + '/../netcon/'
    
    # generate .mex file
    subprocess.check_output('mkoctfile --mex -O3 ' + netcon_path + 'netcon_nondisj_cpp.cpp', shell=True)

    # remove old .mex file if it exists
    mex_filename = 'netcon_nondisj_cpp.mex'
    if os.path.exists(netcon_path + mex_filename):
        os.remove(netcon_path + mex_filename)

    # move new .mex file
    shutil.move(mex_filename, netcon_path)

    # run netcon
    netcon_file_path = netcon_path + 'netcon.m'
    octave = oct2py.Oct2Py()
    sequence = octave.feval(
                        netcon_file_path,
                        leg_links,
                        verbosity,
                        cost_type,
                        mu_cap,
                        int(allow_ops),
                        leg_costs
                    )

    return sequence.tolist()[0]