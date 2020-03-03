from basemath import *

if __name__=='__main__':
    decimal = 61
    bases   = [2, 8, 16]
    results = [[1,1,1,1,0,1], [7,5], [3, 'D']]
    for i,b in enumerate(bases):
        result = de2array(decimal,b)
        assert result == results[i], 'Need {}, got {}'.format(results[i], result)
        bnum = bNUM(result, b)
        result = bnum.get_decimal()
        assert result == decimal, 'Need {}, got {} in base2de'.format(decimal, result)
    a = bNUM(10, 2, cut=3)
    assert a.array == [0,'1','1'], 'Need {}, got {} in cutdown'.format([0,1,1], a.array)
    a = bNUM(10, 2)
    a = a.to_base(16).to_len(2)
    assert a.array == [0, 'A'], 'Need {}, got {} in to_base to_len'.format([0, 'A'], a.array)
    test = [bNUM('4500', 16, 4), bNUM('0076', 16, 4),
            bNUM('252D', 16, 4), bNUM('4000', 16, 4),
            bNUM('4011', 16, 4), bNUM('C0A8', 16, 4),
            bNUM('010F', 16, 4), bNUM('C1C8', 16, 4),
            bNUM('B708', 16, 4)]
    summ = bNUM(0, 16, 4)
    for ti in test:
        summ += ti
    summ = summ.cutdown(4)
    csip = bNUM('FFFF', 16, 4) - summ
    test.append(csip)
    summ = bNUM(0, 16, 4)
    for ti in test:
        summ += ti
    summ = summ.cutdown(4)
    result = bNUM('FFFF', 16, 4) - summ
    assert result.get_decimal() == 0, 'Need 0, got {} in checksum'.format(result.get_decimal())
    a = bNUM('1010', 2)
    b = bNUM('1011', 2)
    result = a*b
    assert result.get_decimal() == 110, 'Need 110, got {} in mul'.format(result)
    print("ALL DONE")
