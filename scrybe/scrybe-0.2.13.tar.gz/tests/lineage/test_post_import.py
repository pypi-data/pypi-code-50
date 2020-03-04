def load_np_and_print():
    import numpy as np
    print(type(np.zeros(11)))


def load_pd_and_print():
    import pandas as pd
    print(type(pd.Series([0, 1, 2, 3])))
    print(type(pd.DataFrame({"x": [0, 1, 2, 3], "y": [0, 1, 2, 3]})))


load_np_and_print()
load_pd_and_print()


import scrybe


load_np_and_print()
load_pd_and_print()
