import time

def skew(genome,i):
    return genome[0:i].count('G')-genome[0:i].count('C')

def minimum_skew(genome):
    min_indices = []
    skew_cache = [0]
    minimum_seen = 0
    min_indices = [0]
    for i in range(1,len(genome)):
        _skew = skew_cache[i-1]+skew(genome[i-1:i],1)
        skew_cache.append(_skew)
        if _skew > minimum_seen:
            continue
        elif _skew == minimum_seen:
            min_indices.append(i)
        else:
            min_indices.clear()
            minimum_seen = _skew
            min_indices.append(i)
    return min_indices
    
##
##start_time = time.time()
##for i in range(0,15):
##    print('{} '.format(skew('GAGCCACCGCGATA',i)))
##exc_time = time.time()-start_time
##print("\n\nexecution time: {} \n".format(exc_time))

f = open('dataset_7_6.txt','r')
genome = f.read()
start_time = time.time()
print("\nMinimum skew indices: {}".format(minimum_skew(genome)))
exc_time = time.time()-start_time
print("\n\nexecution time: {} \n".format(exc_time))
