import sys,traceback

def PatternCount(Text,pattern):
    count = 0
    for i in range(0,len(Text) - len(pattern) + 1):
        if(Text[i:i+len(pattern)] == pattern):
            count += 1
    return count

def FrequentWords(Text,k):
    words = {}
    maxOccurrences = 0
    frequent_words_list = []
    for i in range(0, len(Text)-k+1):
        key = Text[i:i+k]
        if key in words:
            words[key] += 1
            if words[key] > maxOccurrences:
                maxOccurrences = words[key]
        else:
            words[key] = 1
            if(maxOccurrences <= 1):
                maxOccurrences = 1
    for key in words:
        if(words[key] == maxOccurrences):
            frequent_words_list.append(key)
    return frequent_words_list

def ReverseComplement(Pattern):
    reverseComplement = ''
    for i in range(0,len(Pattern)):
        current = Pattern[len(Pattern)-i-1]
        if(current == 'A'):
            reverseComplement += 'T'
        elif(current == 'T'):
            reverseComplement += 'A'
        elif(current == 'G'):
            reverseComplement += 'C'
        else:
            reverseComplement += 'G'
    return reverseComplement

def PatternIndices(Pattern,Genome):
    indices = []
    pattern_seen = False
    pattern_start_index = 0
    for i in range(0,len(Genome)-len(Pattern)+1):
        tmp = Genome[i:i+len(Pattern)]
        if(tmp == Pattern):
            indices.append(i) 
    return indices

# def ClumpFinder(genome,k,L,t):
#     i = 0
#     debug = False
#     tmp_dict = {}
#     clumps = set([])
#     current_window = ''
#     while i <= len(genome)-L:    
#         current_window = genome[i:i+L]
#         if debug:
#             print('current_window: {}'.format(current_window))
#             input('press enter')
#         for j in range(0,len(current_window)-k+1):
#             k_mer = current_window[j:j+k]
#             if debug:
#                 print('k_mer: {}'.format(k_mer))
#                 input('press enter')
#             if k_mer in tmp_dict:
#                 tmp_dict[k_mer] += 1
#             else:
#                 tmp_dict[k_mer] = 1
#         for key in tmp_dict:
#             if tmp_dict[key] == t:
#                 clumps.add(key)
#         tmp_dict = {}
#         i+=1 
#     return clumps

def ClumpFinder(genome,k,L,t):
    k_mers = {}                             #our dictionary holding all kmers, with list of start indices
    debug = False
    clumps = set([])
    for i in range(0,len(genome)-k+1):      #populate our dictionary
        k_mer = genome[i:i+k]
        if k_mer in k_mers:
            k_mers[k_mer].append(i)
        else:
            k_mers[k_mer] = [i]
    if debug:
        print('kmers: \n\n{}'.format(k_mers))
        input('press enter')
    for k_mer in k_mers:
        indices_list = k_mers[k_mer]
        # if debug:
        #     print('k_mer: {} \t indices_list: {}'.format(k_mer,indices_list))
        #     input('press enter')
        for i in range(0,len(indices_list)-t+1):
            first_index = indices_list[i]
            last_index = indices_list[i+t-1]+k-1
            if(last_index - first_index < L):
                clumps.add(k_mer)
                if debug:
                    print('k_mer "{}" forms a clump between {} and {}'.format(k_mer,first_occurrence,t_occurrence))
                    print('\nindices_list: {}'.format(indices_list))
                    input('press enter')
                break

    return clumps





f = open('E_coli.txt','r')
genome = f.read()
clumps = ClumpFinder(genome,9,500,3)
tmp = ''
for clump in clumps:
    tmp = tmp + ' ' + str(clump) 
print(tmp)
print("\n\n"+str(len(clumps)) + "\n")


