def GreedyMotifSearch(Dna, k, t):  
    Dna = Dna.split('\n')
    Dna1 = Dna[0]
    BestMotifs = []
    for row in range(t):
        Dnarow = Dna[row]
        Motif = Dnarow[0:k-1]
        BestMotifs.append(Motif)
    
    for i in range(len(Dna1)- k + 1):
        iter_motif = Dna1[i:i+k-1]
        for j in [1:t]:
            

