# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:51:30 2020

@author: Carina Afonso (PG40952) e Laura Duro (PG40959)
"""

from cmd import *
from SeqBioManagerENG import SeqBioManagerENG

class SbmSHELL_10(Cmd):
    prompt = 'SeqBioManager> '
    intro = '''                             
                    MENU Árvore Filogenética                                
  ===========================================================
    
              1. Através do algoritmo UPGMA local
              2. Através do Clustal
       
        
                            M. MENU
    '''  
                        
    def __set_menu__(self):
        '''
        Define o menu a exibir entre cada comando executado
        '''
        global menu
        global menu
        menu = '''                             
                    MENU Árvore Filogenética                                
  ===========================================================
    
              1. Através do algoritmo UPGMA local
              2. Através do Clustal
       
        
                            M. MENU
    '''                          
    
    def __set_eng__(self, arg):
        '''
        Transporte da instancia da classe SeqBioManagerENG criada na shell principal
        '''
        global eng
        eng = arg
    
    def __select_sequences__(self):
        ids_seqs = []
        i = 1
        print('\nIntroduza os IDs (do gestor) das sequências (para terminar introduza -1):')
        while i <= eng.last_id:
            while True:
                id_gestor = input(str(i) + 'ª sequência: ')
                if int(id_gestor) == -1 or eng.check_id_seq(int(id_gestor)):
                    break
                else:
                    print('\nID inválido!')
            i += 1
            if int(id_gestor) == -1:
                break
            else:
                ids_seqs.append(int(id_gestor))
        return ids_seqs
    
    def __set_parameters__(self):
        '''
        Permite ao utilizador definir os parametros a usar no alimnhamento
        :return option: se importa matrix ou quer construir
        :return file_matrix: ficheiro para importar matrix
        :return gap: penalização por espaçamento
        :return match: valorização por correspondência de caracteres
        :return mismatch: penalização por não correspondência de caracteres
        '''
        try:
            file_matrix = ''
            match = ''
            mismatch = ''
            while True:
                option = input('Escolha os parametros dos alinhamentos:\n1.Usar matrix\n2.Definir manualmente\n\n')
                if option == '1':
                    while True:
                        matrix = input('1.Blosum62\n2.Outra\n\n')
                        if matrix == '1':
                            file_matrix = 'blosum62.mat'
                            break
                        elif matrix == '2':
                            file_matrix = input('Introduza o nome do ficheiro onde se encontra a matrix de susbtituição a usar:')
                            break
                        else:
                             print('\nOpção inválida!')
                    break
                elif option == '2':
                    match = int(input('Introduza a valorização por correspondência de caracteres:'))
                    mismatch = int(input('Introduza a penalização por não correspondência de caracteres:'))
                else:
                    print('\nOpção inválida!')
            gap = int(input('Introduza a penalização por espaçamento: '))
            return (option, file_matrix, gap, match, mismatch)
        except:
            print('\nParâmetros introduzidos incorretos.')
    
    def do_1(self, arg):
        'Comando que permite construir uma árvore filogenética para as sequências do gestor a partir de um algoritmo de UPGMA: 2'
        try:
            if len(eng.seqs) <= 1:
                print('\nNúmero de sequências no gestor insuficiente|')
            else:
                ids_seqs = self.__select_sequences__()
                (option, file_matrix, gap, match, mismatch) = self.__set_parameters__()
                if option == '1':
                    sm = eng.load_subs_matrix(file_matrix)
                else:
                    sm = eng.make_subs_matrix(match, mismatch)
                arv = eng.upgma_tree(ids_seqs, sm, gap)
                print('\nA árvore obtido é a seguinte:\n')
                arv.printtree()
            print(menu)
        except:
            print('Erro: Construção Árvore - UPGMA')
            print(menu)
    
    def do_2(self, arg):
        'Comando que permite construir uma árvore filogenética para as sequências do gestor a partir do programa Clustal: 1'
        try:
            if len(eng.seqs) <= 1:
                print('\nNúmero de sequências no gestor insuficiente|')
            else:
                while True:
                    ids_seqs = self.__select_sequences__()
                    if len(ids_seqs) <= 1:
                        print('\nNúmero de sequências escolhidas insuficiente!')
                    else:
                        break
                eng.clustal_tree(ids_seqs)
            print(menu)
        except:
            print('Erro: Construção Árvore - Clustal')
            print(menu)
    
    def do_M(self, arg):
        'Comando para retroceder ao MENU: M'
        return True
    
    