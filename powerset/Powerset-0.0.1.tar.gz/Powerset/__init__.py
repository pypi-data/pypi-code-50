#Powerset of a List
powerset = lambda s: sorted([[s[j] for j in range(len(s)) if (i & (1 << j))] for i in range(1 << len(s))]
                            , key = lambda y: len(y))

# Lengths of the sublists (subsets), cardinality of the subsets
lengths = lambda x: [len(i) for i in powerset(x)]

#Number of subsets ordered by cardinality
powernums = lambda x: sorted(list(set([(t, lengths(x).count(t)) for t in lengths(x)])), key = lambda y: y[0])
