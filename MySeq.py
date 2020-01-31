class MySeq:

    def __init__(self, seq, tipo="dna"):
        self.seq = seq.upper()
        self.tipo = tipo

    def __len__(self):
        return len(self.seq)
    
    def __getitem__(self, n):
        return self.seq[n]

    def __getslice__(self, i, j):
        return self.seq[i:j]

    def __str__(self):
        return self.tipo + ":" + self.seq

    def printseq(self):
        print(self.seq)
    
    def alfabeto(self):
        if (self.tipo=="dna"): return "ACGT"
        elif (self.tipo=="rna"): return "ACGU"
        elif (self.tipo=="protein"): return "ACDEFGHIKLMNPQRSTVWY"
        else: return None
    
    def valida(self):
        alf = self.alfabeto()
        res = True
        i = 0
        while i < len(self.seq) and res:
            if self.seq[i] not in alf: 
                res = False
            else: i += 1
        return res 
    
    def transcricao (self):
        if (self.tipo == "dna"):
            return MySeq(self.seq.replace("T","U"), "rna")
        else:
            return None
        
    def compInverso(self):
        if (self.tipo != "dna"): return None
        comp = ""
        for c in self.seq:
            if (c == 'A'):
                comp = "T" + comp 
            elif (c == "T"): 
                comp = "A" + comp 
            elif (c == "G"): 
                comp = "C" + comp
            elif (c== "C"): 
                comp = "G" + comp
        return MySeq(comp)

    def traduzSeq (self, iniPos= 0):
        if (self.tipo != "dna"): return None
        seqM = self.seq
        seqAA = ""
        for pos in range(iniPos,len(seqM)-2,3):
            cod = seqM[pos:pos+3]
            seqAA += self.traduzCodao(cod)
        return MySeq(seqAA, "protein")

    def orfs (self):
        if (self.tipo != "dna"): return None
        res = []
        res.append(self.traduzSeq(0))
        res.append(self.traduzSeq(1))
        res.append(self.traduzSeq(2))
        compinv = self.compInverso()
        res.append(compinv.traduzSeq(0))
        res.append(compinv.traduzSeq(1))
        res.append(compinv.traduzSeq(2))    
        return res

    def traduzCodao (self, cod):
        tc = {"GCT":"A", "GCC":"A", "GCA":"A", "GCC":"A", "TGT":"C", "TGC":"C",
      "GAT":"D", "GAC":"D","GAA":"E", "GAG":"E", "TTT":"F", "TTC":"F",
      "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G","CAT":"H", "CAC":"H",
      "ATA":"I", "ATT":"I", "ATC":"I",
      "AAA":"K", "AAG":"K",
      "TTA":"L", "TTG":"L", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
      "ATG":"M", "AAT":"N", "AAC":"N",
      "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
      "CAA":"Q", "CAG":"Q",
      "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R",
      "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "AGT":"S", "AGC":"S",
      "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
      "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
      "TGG":"W",
      "TAT":"Y", "TAC":"Y",
      "TAA":"_", "TAG":"_", "TGA":"_"}
        if cod in tc:
            aa = tc[cod]
        else: aa = "X" # errors marked with X
        return aa

    def maiorProteina (self):
        if (self.tipo != "protein"):
            return None
        seqAA = self.seq
        protAtual = ""
        maiorprot = ""
        for aa in seqAA:
            if aa == "_":
                if len(protAtual) > len(maiorprot):
                    maiorprot = protAtual
                protAtual = ""
            else:
                if len(protAtual) > 0 or aa == "M":
                    protAtual += aa
        return MySeq(maiorprot, "protein")        

    
    def todasProteinas(self):
        if (self.tipo != "protein"):
            return None
        seqAA = self.seq
        protsAtuais = []
        proteinas = []
        for aa in seqAA:
            if aa == "_":
                if protsAtuais:
                    for p in protsAtuais:
                        proteinas.append(MySeq(p, "protein"))
                    protsAtuais = []
            else:
                if aa == "M":
                    protsAtuais.append("")
                for i in range(len(protsAtuais)):
                    protsAtuais[i] += aa

        return proteinas

    
    def maiorProteinaORFs (self):
        if (self.tipo != "dna"):
            return None
        larg = MySeq("","protein")
        for orf in self.orfs():
            prot = orf.maiorProteina()
            if len(prot.seq)>len(larg.seq):
                larg = prot
        return larg

