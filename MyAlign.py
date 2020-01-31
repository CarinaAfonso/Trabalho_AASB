class MyAlign:

    def __init__(self, lseqs, tipo="protein"):
        self.listseqs = lseqs
        self.tipo = tipo
    
    def __len__(self):# number of columns
        return len(self.listseqs[0])
    
    def __getitem__(self, n):
        if type(n) is tuple and len(n) ==2: 
            i, j = n
            return self.listseqs[i][j]
        elif type(n) is int: return self.listseqs[n]
        return None
    
    def __str__(self):
        res = ""
        for seq in self.listseqs:
            res += "\n" + seq 
        return res
    
    def numSeqs(self):
        return len(self.listseqs)
    
    def column (self, indice):
        res = []
        for k in range(len(self.listseqs)):
            res.append(self.listseqs[k][indice])
        return res

    def consensus(self):
        cons= ''
        for i in range(len(self)):
            cont= {}
            for k in range(len(self.listseqs)):
                c= self.listseqs[k][i]
                
                if c in cont:
                    cont[c]= cont[c]+ 1
                else:
                    cont[c]=1
                    
            maximum = 0
            cmax= None
            
            for ke in cont.keys():
                if ke != '-' and cont[ke] > maximum:
                        maximum= cont[ke]
                        cmax=ke
            cons= cons + cmax
        return cons  

#ACRESCENTADO
    def consensus_absoluto(self, indice_col):
        listaCar= self.column(indice_col)
        res= True
        i=1
        
        while res and i < len(listaCar):
            if listaCar[i] != listaCar[0]: 
                res= False
            else:
                i+= 1
        return res  
  

    def lista_consenso(self):
        lista_cons= []
        
        for c in range(len(self)):
            if self.consensus_absoluto(c):
                lista_cons.append(c)
        return lista_cons      
    
    
    def column_has_kgaps(self, indice_col, k):
        
        listaCars= self.column(indice_col)
        num_gaps= 0
        
        for c in listaCars:
            if c == '-':
                num_gaps +=1
        
        if num_gaps >= k:
            return True
        else:
            return False

    def column_with_kgaps (self, k):
        res= []
        
        for c in range (len(self)):
            if self.column_has_kgaps(c,k):
                res.append(c)
        return res       
    
    
    def add_gap (self, seq, pos):#seq- linha #pos- posicao
        self.listseqs[seq] = self.listseqs[seq][:pos] + '-' +self.listseqs[seq][pos:] 
        #Basicamente vamos colocar o que esta naquela posicao toda para tras metemos o gap e depois é o que esta a frente
        
    def remove_gap(self, seq, pos):   
    #1º vai tetar encontrar um gap, se tiver vamos troca pelo que esta antes e depois apenas     
       if self.listseqs[seq][pos] == '-' :
           self.listseqs[seq] = self.listseqs[seq][:pos] + self.listseqs[seq][pos +1:]
           
           
    def add_sequence_heuristic(self, newseq):
        newrow= ''
        i=0    #alinhamento
        j=0    #nova seq
        
        while i < len (self) and j < len(newseq):
            carscol= self.column(i)    #carscol - caracteres coluna
            
            if newseq[j] in carscol:
                newrow += newseq[j]
                j+=1                
            else:
                 newrow += '-'
            i+= 1
            
        while j< len (newseq):
            newrow += newseq[j]
            
            for k in range(len(self.listseqs)):
                self.listseqs[k] += '-'
            j+=1    
        
        if i < len(self): # ou len(self.listaseqs[0]) - colunas
            for c in range (i, len(self)):
                newrow += '-'
                
#        while i< len(self):
#            newrow += '-'
#            i+=1
                
        self.listseqs.append(newrow)        

        

if __name__ == "__main__": 
    alig = MyAlign(["ATGA-A","AA-AT-"], "dna")
    print(alig)
    print(len(alig))
    print(alig.column(2))
    print(alig[1,1])
    print(alig[0,2])


# Results
# ATGA-A
# AA-AT-
# 6
# ['G', '-']
# A
# G
