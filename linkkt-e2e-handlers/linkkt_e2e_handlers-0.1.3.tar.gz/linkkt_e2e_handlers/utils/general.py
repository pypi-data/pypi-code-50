def merge_lists_of_dicts(L):
    main = []
    for l in L:
        if isinstance(l, list):
            for i in l:
                if i not in main:
                    main.append(i)
    return main