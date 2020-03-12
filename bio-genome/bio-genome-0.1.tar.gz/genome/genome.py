def frequent_words(text,k):
    """Find the most frequent k-mers in the gene sequence. K-mer is a short sequence of DNA that is 'k' bases long, usually the length needed to encode a protein for some biological process.

    Args:
    text: string. The sequence of DNA where we are trying to find frequent k-mers.
    k: int. The number of bases in our k-mer- our substring of DNA that encodes a protein.

    Returns:
    frequent_words_list: list. A list of the most frequent k-mers in our gene sequence.
    """
    words = {}
    maxOccurrences = 0
    frequent_words_list = []
    for i in range(0, len(text)-k+1):
        key = text[i:i+k]
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

def reverse_complement(pattern):
    """Find the reverse complement of this DNA sequence. Useful to see what the complementary strand should look like after replication (if ignoring the effect of mutations)
    
    Args:
    pattern: string. The sequence of DNA we want to find the complement of.

    Returns:
    reverse_complement: string. The reverse complement of the input DNA sequence, according to base pairing rules.
    """
    reverse_complement = ''
    for i in range(0,len(pattern)):                         #can we vectorize?
        current = pattern[len(pattern)-i-1]
        if(current == 'A'):
            reverse_complement += 'T'
        elif(current == 'T'):
            reverse_complement += 'A'
        elif(current == 'G'):
            reverse_complement += 'C'
        else:
            reverse_complement += 'G'
    return reverse_complement

def pattern_indices(pattern,gene_sequence):
    """ Find the indices within the gene_sequence where pattern begins. """
    indices = []
    pattern_seen = False
    pattern_start_index = 0
    for i in range(0,len(gene_sequence)-len(pattern)+1):
        tmp = gene_sequence[i:i+len(pattern)]
        if(tmp == pattern):
            indices.append(i) 
    return indices

def pattern_count(text,pattern):
    """Find the number of occurrences of the substring 'pattern' in larger string 'text'."""
    count = 0
    for i in range(0,len(text) - len(pattern) + 1):
        if(text[i:i+len(pattern)] == pattern):
            count += 1
    return count

def clump_finder(gene_sequence,k,l,t):
    """Find the k-mers (clumps) that occur at least t times within a window of the DNA that is l bases long.

    Args:
    gene_sequence: string. Entire genome or subset of the genome
    k: int. Length of our k-mer.
    L: int. Length of our 'window'.
    t: int. Number of occurrences of this clump we expect.

    Returns: 
    clumps: list. All k-mers that match our conditions. 
    """
    k_mers = {}                             
    debug = False
    clumps = set([])
    #populate our dictionary of all k-mers
    for i in range(0,len(gene_sequence)-k+1):      
        k_mer = gene_sequence[i:i+k]
        if k_mer in k_mers:
            k_mers[k_mer].append(i)
        else:
            k_mers[k_mer] = [i]

    #find k_mers that occur at least t times in L window
    for k_mer in k_mers:
        indices_list = k_mers[k_mer]
        for i in range(0,len(indices_list)-t+1):
            first_index = indices_list[i]
            last_index = indices_list[i+t-1]+k-1
            if(last_index - first_index < l):
                clumps.add(k_mer)
                break

    return clumps

def skew(gene_sequence,end_index):
    """ Calculate the difference between the quantity of G bases and the quantity of C bases. Helps to determine the effect of deamination and where 'ori' might lie.

    Args:
    gene_sequence: string. The DNA string on which to calculate the skew. Will most likely be the entire genome.
    end_index: int. The stopping point for calculating the skew.

    Returns: 
    skew: int. The difference between G and C bases in this gene_sequence.
    """
    return gene_sequence[0:end_index].count('G')-gene_sequence[0:end_index].count('C')


class Genome():

    def __init__(self,genome,description="",source_file=""):
        self.genome = genome
        self.description = description
        self.source_file = source_file

    def __repr__(self):
        return """==================== Genome ======================\n\n{}\n\nsource: {}\n\ncontains {} nucleotides\n==================================================""".format(self.description,self.source_file,len(self.genome))

    def minimum_skew(self):
        """Find the point in our genome where the skew is minimized- will help in finding 'ori'.

        Args:
        self.genome: string. Our genome.

        Returns:
        min_indices: list. A list of indices where the skew is at a minimum in our genome.
        """
        min_indices = []
        skew_cache = [0]
        minimum_seen = 0
        min_indices = [0]
        for i in range(1,len(self.genome)+1):
            _skew = skew_cache[i-1]+skew(self.genome[i-1:i],1)
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
