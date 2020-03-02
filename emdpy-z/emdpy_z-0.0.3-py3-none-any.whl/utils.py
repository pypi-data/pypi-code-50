
import pandas as pd

def to_csv(path, imfs, res):

    df = pd.DataFrame()
    # IMF
    for i in range(imfs.shape[0]):
        name = 'imf' + str(i+1)
        df[name] = imfs[i][1, :]
    # Res
    if res.shape != (2,):
        df['res'] = res[1]
    # save
    df.to_csv(path)
    print('==> Finished ...')

