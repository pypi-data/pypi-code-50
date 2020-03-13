def func(listTemp, n):
    for i in range(0, len(listTemp), n):
        yield listTemp[i:i + n]


def split_csv(df, csv):
    for i in func([i for i in range(df.shape[0])], n):

    pass

def cut_csv(df, csv):
    row = df.shape[0]
    print('csv共有%s行' % row)
    n = int(input('每几行分割为一个csv?：'))
    for idx, i in enumerate(func([i for i in range(df.shape[0])], n)):
        df.loc[i].to_csv(csv.replace('.csv', '_' + str(idx) + '.csv'), index=False)