from mcrp_utils.utils import zip_columns

c1 = tuple('1234')
c2 = tuple('56')
for va in 'bct':
    print('valign', va)
    for s in zip_columns(c1, c2, valign=va):
        print(s)
    for s in zip_columns(c2, c1, valign=va):
        print(s)
