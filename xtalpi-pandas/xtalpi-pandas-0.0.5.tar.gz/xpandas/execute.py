import math


def split_func(arr, n):
    for i in range(0, len(arr), n):
        yield arr[i:i + n]


def chunk_func(arr, n):
    m = int(math.ceil(len(arr) / float(n)))
    for i in range(0, len(arr), m):
        yield arr[i:i + m]


def split_csv(df, csv):
    row = df.shape[0]
    print('\ncsv共有%s行' % row)
    n = int(input('每几行分割为一个csv? :'))
    for idx, i in enumerate(split_func([i for i in range(df.shape[0])], n)):
        df.loc[i].to_csv(csv.replace('.csv', '_' + str(idx) + '.csv'), index=False)


def chunk_csv(df, csv):
    row = df.shape[0]
    print('\ncsv共有%s行' % row)
    n = int(input('将csv按行平均分为几份? :'))
    for idx, i in enumerate(chunk_func([i for i in range(df.shape[0])], n)):
        df.loc[i].to_csv(csv.replace('.csv', '_' + str(idx) + '.csv'), index=False)


def top_csv(df, csv):
    col_names = list(df.columns)
    if len(col_names) <= 10:
        print('\n列名:', col_names)
    else:
        print('\n列名:', col_names + ['......'])

    while True:
        col_name = input('想要按照哪一列进行TOP? :')
        if col_name in col_names:
            break
        else:
            print('列名错误，请重新输入')
    while True:
        print('[1.升序(值越小越好)]或[2.降序(值越大越好)]')
        assending_num = input('请输入1或2选择排列方式：')
        if assending_num == '1':
            assending = True
            break
        elif assending_num == '2':
            assending = False
            break
        else:
            print('请从1或2中选择一个')

    row = df.shape[0]
    print('\ncsv共有%s行' % row)
    top_num = int(input('想要Top前多少行？：'))
    top_df = df.sort_values(col_name, ascending=assending)[:top_num]
    top_df.to_csv(csv.replace('.csv', '_top'+str(top_num)+'.csv'), index=False)
