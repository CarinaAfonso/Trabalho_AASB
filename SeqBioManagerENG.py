# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 18:00:51 2020

@author: Carina Afonso (PG40952) e Laura Duro (PG40959)
"""

from MySeq import MySeq
from AlignSeq import AlignSeq
from MyAlign import MyAlign
from SubstMatrix import SubstMatrix
from upgma import UPGMA
from MultipleAlign import MultipleAlign
from Bio.ExPASy import ScanProsite
from Bio.Align.Applications import ClustalwCommandline
from Bio import Phylo
from Bio import Entrez
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import re
import math

class SeqBioManagerENG:
    
    def __init__(self):
        self.seqs = {} #{'id_seq': {'seq': MySeq(), 'id' : [bd, id_seq], 'input': input_seq}
        self.last_id = 0 #quando 0, nenhuma sequência adicionada
        
        
        
# ______________________________ GERAL SEQUÊNCIAS _____________________________   

    def check_id_seq(self, id_seq):
        if id_seq > self.last_id or id_seq < 1:
            return False
        else:
            return True
        
        

# _________________________ INPUT E OUTPUT SEQUÊNCIAS _________________________  

## INPUT
        
  ### MANUAL
    
    def add_sequence(self, id_seq, dtbs, seq, input_seq, orgnsm, name):
        '''
        Adiciona uma sequência ao gestor (self.seqs)
        :param id_seq: id da sequencia na base de dados de onde foi retirada
        :param dtbs: base de dados de onde provém a sequência
        :param seq: sequência proteica
        :param input_seq: tipo de input da seq - manual ou automático
        :param orgnsm: organismo da sequência
        :param name: nome da proteína
        :return state: boolenao - indica se a sequência foi adicionada ao gestor
        '''
        state = True
        seq_inst = MySeq(seq, 'protein') #criação de uma instância MySeq
        if seq_inst.valida(): #validação da sequencia 
            self.last_id += 1 #id_interno
            self.seqs[self.last_id] = {'seq': seq_inst, 'name': name, 'id': [dtbs, id_seq], 'orgnsm': orgnsm,'input': input_seq, 'size': len(seq)}
        else:
            state = False
        return state
    
    
  ### AUTOMATIC
  
    #### FICHEIROS
    
    def check_file(self, file_name):
        '''
        Valida o tipo de ficheiro dado pelo utilizador
        :param file_name: nome do ficheiro completo, com extensão
        :return state: booleano - indica se o nome é ou não válido
        '''
        state = False
        input_seq = -1
        types = ['.txt', '.faa'] #txt ou fasta para aminoácidos
        if file_name[-4:] in types:#validar o tipo de ficheiro
            input_seq = file_name[-3:]
            state = True
        elif file_name[-6:] == '.fasta': 
            input_seq = file_name[-5:]
            state = True
        return (state, input_seq)
    
    def load_sequence_faa(self, file_name, input_seq):
        '''
        Adicona uma sequência ao gestor (self.seqs) a partir de um ficheiro fasta
        (.fasta ou .faa)
        :param file_name: nome do ficheiro
        :param input_seq: tipo de ficheiro
        :return state_file: booleano - estado de leitura do ficheiro
        :return state_seq: booleano - indica se a sequência foi adicionada
                           ao gestor
        '''
        try:
            state_file = True
            file = open(file_name, 'r')
            seq = ''
            other = ''
            for line in file.readlines():
                if line[0] == '>':
                    other = line[1:] #informação extra do ficheiro
                else:
                    for symbol in ('\n', ' '): #eliminar todos os caracteres que nao fazem parte da sequencia
                        line = line.replace(symbol, '')
                    seq += line
            file.close()
            seq_inst = MySeq(seq, 'protein') #criação de uma instância MySeq
            state_seq = True
            if seq_inst.valida(): #validação da sequencia 
                self.last_id += 1 #id_interno
                self.seqs[self.last_id] = {'seq': seq_inst, 'input': input_seq, 'size': len(seq), 'others': other}
            else:
                state_seq = False
            return (state_file, state_seq)
        except:
            state_file = False # não abriu o ficheiro
            state_seq = False
            return (state_file, state_seq)
    
    def load_sequence_txt(self, file_name):
        '''
        Adicona sequências ao gestor (self.seqs) a partir de um ficheiro txt
        :param file_name: nome do ficheiro
        :param input_seq: tipo de ficheiro
        :return state_file: booleano - estado de leitura do ficheiro
        :return n_seq_val: número de sequências importadas com sucesso
        :return n_seq_nval: número de sequências não importadas
        '''
        try:
            state_file = True
            n_seq_val = 0
            n_seq_nval = 0
            file = open(file_name)
            input_seq = ''
            seq = ''
            id_dtbs = ''
            dtbs = ''
            orgnsm = ''
            name = ''
            others = ''
            for line in file.readlines():
                if line.find('Input:') != -1:
                    input_seq = line[7:].replace('\n', '')
                elif line.find('Base de Dados:') != -1:
                    dtbs = line[15:].replace('\n', '')
                elif line.find('ID:') != -1:
                    id_dtbs = line[4:].replace('\n', '')
                elif line.find('Organismo:') != -1:
                    orgnsm = line[11:].replace('\n', '')
                elif line.find('Nome:') != -1:
                    name = line[6:].replace('\n', '')
                elif line.find('Outros:') != -1:
                    others = line[8:].replace('\n', '')  
                elif line.find('Seq:') != -1:
                    seq = line[5:].replace('\n', '')
                elif line.find('END') != -1:
                    seq_inst = MySeq(seq, 'protein') #criação de uma instância MySeq
                    if seq_inst.valida(): #validação da sequencia 
                        self.last_id += 1 #id_interno
                        self.seqs[self.last_id] = {'seq': seq_inst, 'input': input_seq, 'size': len(seq), 'others': others, 'id': [dtbs, id_dtbs], 'orgnsm': orgnsm, 'name': name}  
                        n_seq_val += 1
                        input_seq = ''
                        seq = ''
                        id_dtbs = ''
                        dtbs = ''
                        orgnsm = ''
                        name = ''
                        others = ''
                    else:
                        n_seq_nval += 1
            file.close()
            return (state_file, n_seq_val, n_seq_nval)
        except:
            state_file = False # não abriu o ficheiro
            n_seq_val = -1
            n_seq_nval = -1
            return (state_file, n_seq_val, n_seq_nval)
    
    def load_seqs_blast(self, seqs_save, seqs_result):
        '''
        Adicona sequências ao gestor (self.seqs) a partir dos resultados de um blast
        :param seqs_save: numero das sequências a guardar
        :param seqs_result: sequencias resultado do blast
        '''
        for id_result in seqs_save:
            self.last_id += 1
            others = seqs_result[int(id_result)-1][0]
            seq = seqs_result[int(id_result)-1][2]
            seq_inst = MySeq(seq, 'protein')
            self.seqs[self.last_id] = {'others': others, 'seq':seq_inst, 'size':len(seq), 'input':'blast'}
        
    def load_previous_data(self):
        (state_file, n_seq_val, n_seq_nval) = self.load_sequence_txt('DATA_all_SBM.txt')
    
    #### NCBI
    
    def __set_email__(self):
        '''
        Função que define o email para poder usar Entrex do Biopython
        '''
        Entrez.email = 'pg40959@alunos.uminho.pt'
        
    def get_sequence_ncbi(self, id_prot):
        '''
        Função que dado o ID da proteína no NCBI retorna a seq e outra informação
        :param id_prot: ID proteina
        '''
        self.__set_email__()
        record = Entrez.efetch(db = 'protein', id = id_prot, rettype = 'fasta', retmode = 'text')
        info = record.read()
        split = info.find('\n')
        others = info[1:split]
        seq = info[split:].replace('\n', '')
        self.last_id +=1
        seq_inst = MySeq(seq, tipo = 'protein')
        self.seqs[self.last_id] = {'seq': seq_inst, 'others': others, 'size': len(seq), 'input': 'NCBI', 'id': ['NCBI', id_prot]}


## OUTPUT

    def __write_sequence__(self, id_seq, file):
        '''
        Escreve os atributos e a sequência num ficheiro já aberto
        :param id_seq: id interno da sequência
        :param file: ficheiro onde será escrita a informação
        '''
        keys = self.seqs[id_seq].keys()
        if 'input' in keys:
            file.writelines('Input: ' + self.seqs[id_seq]['input'] + '\n')
        if 'id' in keys:
            file.writelines('Base de Dados: ' + self.seqs[id_seq]['id'][0] + '\n')
            file.writelines('ID: ' + self.seqs[id_seq]['id'][1] + '\n')
        if 'orgnsm' in keys:
            file.writelines('Organismo: ' + self.seqs[id_seq]['orgnsm'] + '\n')
        if 'name' in keys:
            file.writelines('Nome: ' + self.seqs[id_seq]['name'] + '\n')
        if 'others' in keys:
            file.writelines('Outros: ' + self.seqs[id_seq]['others'] + '\n')
        file.writelines('Seq: ' + self.seqs[id_seq]['seq'].seq + '\nEND\n\n')   
    
    def save_sequence(self, id_seq, file_name):
        '''
        Guarda os atributos e a sequencia num ficheiro
        :param id_seq: id interno da sequência
        :param file_name: nome do ficheiro onde será guardada a informação
        :return : booleano indicativo do resultado
        '''
        try:
            state_id = False
            state_file = True
            if self.check_id_seq(id_seq):
                state_id = True
                file = open(file_name + '_SBM.txt', 'w+')
                self.__write_sequence__(id_seq, file)
                file.close()
            return (state_id, state_file)
        except:
            state_id = False
            state_file = False
            return (state_id, state_file)
    
    def save_all_sequences(self, file_name):
        '''
        Guarda os atributos e a sequencia, de todas as sequências do gestor, 
        num ficheiro
        :param file_name: nome do ficheiro onde será guardada a informação
        :return : booleano indicativo do resultado
        '''
        try:
            file = open(file_name + '_all_SBM.txt', 'w+')
            for id_seq in self.seqs.keys():
                self.__write_sequence__(id_seq, file)
            file.close()
            return True
        except:
            return False
    
    def save_data(self):
        '''
        Guarda informação toda presente no gestor aquando o seu término
        :return state: indica se a informação foi guardada com sucesso
        '''
        state = self.save_all_sequences('DATA')
        return state
    
    
    
# _____________________ ATRIBUTOS E MANIPULAÇÃO SEQUÊNCIAS ____________________     
    
## DELETAR
    
    def del_sequence(self, id_seq):
        '''
        Apaga a informação referente a sequência do gestor
        :param id_seq: id da sequencia no gestor
        :return state_id: boolenao que indica se a sequência foi ou não apagada
        '''
        state_id = False
        if self.check_id_seq(id_seq):
            state_id = True
            self.seqs.pop(id_seq)
        return state_id
    
    def del_all_sequences(self):
        '''
        Apaga a informação referente a todas as sequências do gestor
        '''
        for id_seq in self.seqs.keys():
            self.del_sequence(id_seq)
        self.last_id = 0 #reset ao contador
    
## CONSULTAR/ALTERAR ATRIBUTOS
        
    def get_atrb_seq(self, id_seq):
        '''
        Retorna os valores dos atributos de uma sequência
        :param id_seq: id da sequência no gestor
        :return state_id: booleano que indica se o id é valido ou não
        :return input_seq: valor referente à maneira de input da sequência 
                           no gestor
        :return dtbs: base de dados de onde foi retirada a sequência
        :return id_dtbs: id da sequência na base de dados
        :return orgnsm: organismo à qual pertence a sequência
        :return name: nome da proteína
        :return others: outra informação da sequência
        :return seq: sequência
        :return size: tamanho da sequência
        '''
        state_id = False
        input_seq = -1
        id_dtbs = -1
        dtbs = -1
        orgnsm = -1
        name = -1
        others = -1
        seq = -1
        size = -1        
        if self.check_id_seq(id_seq):
            state_id = True
            keys = self.seqs[id_seq].keys()
            if 'input' in keys:
                input_seq = self.seqs[id_seq]['input']
            if 'id' in keys:
                dtbs = self.seqs[id_seq]['id'][0]
                id_dtbs = self.seqs[id_seq]['id'][1]
            if 'orgnsm' in keys:
                orgnsm = self.seqs[id_seq]['orgnsm']
            if 'name' in keys:
                name = self.seqs[id_seq]['name']
            if 'others' in keys:
                others = self.seqs[id_seq]['others']
            seq = self.seqs[id_seq]['seq'].seq
            size = self.seqs[id_seq]['size']
        return (state_id, input_seq, id_dtbs, dtbs, orgnsm, name, others, seq, size)
        
    def set_atrb_seq(self, id_seq):
        '''
        Retorna os atributos de uma sequência
        :param id_seq: id da sequência no gestor
        :return atrb: lista de atributos pertencentes à sequência
        '''
        state_id = False
        atrb = []
        if self.check_id_seq(id_seq):
            state_id = True
            atrb = self.seqs[id_seq].keys()   
        return (state_id, atrb)
    
    def change_atrb_seq(self, id_gestor, chng_atrb):
        '''
        Alteração dos valores de atributos de uma sequência pelo utilizador
        :param id_gestor: id da sequência no gestor
        :param chng_atrb: lista de atributos a alterar pelo utilizador
        :return booleano: sucesso/insucesso nas alterações dos atributos
        '''
        try:
            if 'id' in chng_atrb:
                self.seqs[id_gestor]['id'][0] = input('Introduza a nova Base de Dados:')
                self.seqs[id_gestor]['id'][1] = input('Introduza a novo ID:')
            if 'orgnsm' in chng_atrb:
                self.seqs[id_gestor]['orgnsm'] = input('Introduza o novo Organismo:')
            if 'name' in chng_atrb:
                self.seqs[id_gestor]['name'] = input('Introduza o novo Nome:')    
            if 'others' in chng_atrb:
                self.seqs[id_gestor]['others'] = input('Introduza as novas informações adicionais:')    
            return True
        except:
            return False
    
# _________________________ ALINHAMENTO DE SEQUÊNCIAS _________________________

## SEQUÊNCIAS MAIS SEMELHANTES
    
    def make_subs_matrix(self, match, mismatch):
        '''
        Cria matriz de substituição para alinhamentos
        :param match: valor de valorização por correspondência
        :param mismatch: valor de penalização por não correspondência
        :return sm: matriz de substituição
        '''
        sm = SubstMatrix()
        sm.createFromMatchPars(match, mismatch, self.seqs[self.last_id]['seq'].alphabet())
        return sm
    
    def load_subs_matrix(self, file_matrix):
        '''
        Importa matrix de substituição para alinhamentos
        :param file_matrix: nome do ficheiro onde estão guardados os valores
        :return sm: matriz de substituição
        '''
        sm = SubstMatrix()
        sm.loadFromFile(file_matrix, sep = '\t')
        return sm
    
    def align_seqs(self, id_1, id_2, sm, gap):
        '''
        Faz o alinhamento global entre duas sequências
        :param id_1: id do gestor da 1a sequência
        :param id_2: id do gestor da 2a sequência
        :param sm: matrix de substituição
        :param gap: valor de penalização por espaçamentos
        :return myalign: instancia da classe MyAlign - seqs
        :return alignseq: instancia da classe AlignSeq - alinhamento
        '''
        seq_1 = self.seqs[id_1]['seq']
        seq_2 = self.seqs[id_2]['seq']
        myalign = MyAlign([seq_1, seq_2])
        alignseq = AlignSeq(sm, gap)
        alignseq.needlemanWunsch(seq_1, seq_2)
        return (myalign, alignseq)
        
    def best_align(self, id_gestor, sm, gap):
        '''
        Faz o alinhamento global entre uma sequência e todas as outras do 
        gestor, devolvendo aquela com melhor score
        :param id_gestor: id do gestor da sequência escolhida
        :param sm: matrix de substituição
        :param gap: valor de penalização por espaçamentos
        :return 
        '''
        all_align = {}
        for id_2 in self.seqs.keys():
            if id_gestor != id_2:
                (myalign, alignseq) = self.align_seqs(id_gestor, id_2, sm, gap)
                all_align[id_2] = [myalign, alignseq]
        best_score = -math.inf
        best_id = -1
        for id_key in all_align.keys():
            score = all_align[id_key][1].scoreAlin(all_align[id_key][0])
            if best_score < score:
                best_score = score
                best_id = id_key
        return best_id 

## ALINHAMENTO MULTIPLO
    
    def multiple_align(self, ids_seqs, sm, gap):
        '''
        Função que faz o alinhamento múltiplo de sequências do gestor
        :param ids_seq: IDs das sequências a alinhar
        :param sm: matrix de scores para alinhamentos
        :param gap: valor de penalização por espaçamentos para alinhamentos
        :return align_cons: alinhamento múltiplo
        '''
        seqs = []
        for id_gestor in ids_seqs:
            seqs.append(self.seqs[int(id_gestor)]['seq'])
        alseq = AlignSeq(sm, gap)
        multialgn = MultipleAlign(seqs, alseq)
        align_cons = multialgn.alignConsensus()
        return align_cons
    
    
    
# __________________________ PADRÕES E SUB-SEQUÊNCIAS _________________________ 

## FREQUÊNCIA DE SUB-SEQUÊNCIAS
    
    def freq_sub_seqs(self, id_gestor, k):
        '''
        Calcula a frequência de sub-sequências de tamanho k numa sequência
        :param id_gestor: ID da sequência do gestor
        :param k: comprimento das sub-sequências
        :return sub_seqs: dicionário com sub-sequências como chave e valores 
                          das frequências
        '''
        sub_seqs = {}
        seq = self.seqs[id_gestor]['seq'].seq
        total = 0
        for i in range(len(seq)-(k-1)):
            sub_seq = seq[i:i+k]
            if sub_seq in sub_seqs.keys():
                sub_seqs[sub_seq] += 1
            else:
                sub_seqs[sub_seq] = 1
            total += 1
        for key in sub_seqs.keys():
            sub_seqs[key] = sub_seqs[key]/total
        return sub_seqs
    
    def allseqs_freq_sub_seqs(self, k):
        '''
        Calcula a frequência de sub-sequências de tamanho k em todas as 
        sequências do gestor
        :param k: comprimento das sub-sequências
        :return all_sub_seqs: dicionário com ID sequências como chave e como 
                              valor um dicionário com sub-sequências como chave 
                              e valores das frequências
        '''
        all_sub_seqs = {}
        for id_gestor in self.seqs.keys():
            all_sub_seqs[id_gestor] = self.freq_sub_seqs(int(id_gestor), k)
        return all_sub_seqs
    
## OCORRÊNCIAS PADRÃO   
    
    def find_re_pattern(self, id_gestor, expre):
        '''
        Deteta o número e a localização de um padrão, dado na forma de expressão 
        regular, numa sequência
        :param id_gestor: ID da sequência
        :param expre: expressão regular
        :return post: posições onde o padrão foi encontrado na sequência
        :return num: número de vezes que o padrão foi encontrado na sequência
        '''
        post = re.finditer(expre, self.seqs[id_gestor]['seq'].seq)
        num = len(re.findall(expre, self.seqs[id_gestor]['seq'].seq))
        return (post, num)
    
    def find_re_pattern_allseqs(self, expre):
        '''
        Deteta o número e a localização de um padrão, dado na forma de expressão 
        regular, em todas as sequências do gestor
        :param expre: expressão regular
        :return patterns: dicionário onde as chaves são os ID´s das sequências e 
                          os valores uma lista com as posições onde o padrão foi 
                          encontrado naquela sequência e o número de vezes que 
                          esse padrão foi encontrado
        '''
        patterns = {}
        for id_gestor in self.seqs.keys():
            (post, num) = self.find_re_pattern(id_gestor, expre)
            patterns[id_gestor] = [post, num]
        return patterns
    
    
    
# ___________________________ ÁRVORES FILOGENÉTICAS ___________________________        
      
##  ÁRVORES  
    
    def upgma_tree(self, ids_seqs, sm, gap):
        '''
        Cria uma árvore filogenética com todas as sequências do gestor - 
        algoritmo UPGMA
        :param seqs: lista com os ID's do gestor das sequencias para construção 
                     da árvore
        :param sm: matrix de scores para alinhamento múltiplo
        :param gap: valor de penalização para alinhamento múltiplo
        :return arv: instancia da classe Binnary Tree
        '''
        seqs = []
        for id_gestor in ids_seqs:
            seqs.append(self.seqs[int(id_gestor)]['seq'])
        alseq = AlignSeq(sm, gap)
        up = UPGMA(seqs, alseq)
        arv = up.run()
        return arv
    
    def write_fasta(self, ids_seqs, file_name = 'Tree_seqs.fasta'):
        '''
        Escreve sequências do gestor num ficheiro fasta
        :param ids_seqs: lista com os ids
        :param file_name: nome do ficheiro
        '''
        file = open(file_name, 'w+')
        for id_gestor in ids_seqs:
            file.writelines('> ' + id_gestor + '\n')
            file.writelines(self.seqs[int(id_gestor)]['seq'].seq + '\n\n')
        file.close()
            
    def clustal_tree(self, ids_seqs):
        '''
        Função que constrói a árvore filogenética com todas as sequências do 
        gestor com auxilio do programa ClustalW 
        '''
        self.write_fasta(ids_seqs, file_name = 'Tree_seqs.fasta')
        cmdline=ClustalwCommandline('clustalw2', infile = 'Tree_seqs.fasta')
        cmdline()
        tree = Phylo.read('All_seqs.dnd', 'newick')
        Phylo.draw_ascii(tree)
    
    def reorganize_seqs(self, arv, ids_seqs):
        '''
        Funçao que reorganiza os IDs das sequências numa lista com base na 
        similaridade entre elas dada por uma árvore filogenética
        :param arv: árvore filogenética
        :param ids_seqs: IDs das sequencias do gestor
        :return new_ids_seqs: IDs das sequências do gestor na ordem de maior 
                              similaridade dada pela árvore filogenética
        '''
        new_ids_seqs = []
        order = arv.getCluster()
        for pos in order:
            new_ids_seqs.append(ids_seqs[pos])
        return new_ids_seqs
            
# __________________________________ MOTIVOS __________________________________  
        
    def scan_motifs(self, ids_seqs):
        '''
        Funçao para pesquisa de motivos a partir da Prosite
        :param ids_seqs: IDs das sequências do gestor
        :return results: resultados do scan
        '''
        results = []
        for id_seq in ids_seqs:
            handle = ScanProsite.scan(seq = self.seqs[id_seq]['seq'].seq)
            results.append(ScanProsite.read(handle))
        return results
        
    
# ___________________________________ BLAST ___________________________________    
    
    def blast(self, id_gestor, dtbs, hit_size, e_value):
        '''
        Função para realizar um blast com os parametros defenidos pelo utilizador
        :param id_gestor: sequência usada para blast
        :param dtbs: base de dados usada
        :param hit_size: número de resultados máximo retornado
        :param e-value: limite máximo e-value
        :return seqs_result: lista de listas com sequências retornadas
        '''
        result_handle = NCBIWWW.qblast( program = 'blastp', database = dtbs, sequence = self.seqs[id_gestor]['seq'].seq, hitlist_size = hit_size)
        blast_records = NCBIXML.parse(result_handle)
        seqs_result = []
        for blast_record in blast_records:
            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    if hsp.expect < e_value:
                        seqs_result.append([alignment.title, hsp.expect, hsp.sbjct.replace('-', '')])
        return seqs_result
                        
    
        
                        
                  
                    
    
