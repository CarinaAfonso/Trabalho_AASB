# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:05:42 2020

@author: Carina Afonso (PG40952) e Laura Duro (PG40959)
"""

from cmd import *
from SeqBioManagerENG import SeqBioManagerENG #não sei se necessário


class SbmSHELL_5_1(Cmd):
    prompt = 'SeqBioManager> '
    intro = '''                                 
       1. Adicionar manualmente
       2. Adicionar a partir de um ficheiro
                
                
                    M. MENU Sequência semelhante
    '''     
                     
    def __set_menu__(self):
        '''
        Define o menu a exibir entre cada comando executado
        '''
        global menu
        global menu
        menu = '''                             
       1. Adicionar manualmente
       2. Adicionar a partir de um ficheiro
                
                
                    M. MENU Sequência semelhante
    '''     
    
    def __set_eng__(self, arg):
        '''
        Transporte da instancia da classe SeqBioManagerENG criada na shell principal
        '''
        global eng
        eng = arg
        
    def do_1(self, arg):
        'Comando para adicionar uma sequência ao gestor manualmente: 1' 
        try:
            id_seq = input('Introduza o ID da sequência: ')
            dtbs = input('Introduza a base de dados de onde foi retirada: ')
            orgnsm = input('Introduza o organismo: ')
            name = input('Introduza o nome da proteína: ')
            seq = input('Introduza a sequência de aminoácidos: ').upper()
            input_seq = 'manual'
            state = eng.add_sequence(id_seq, dtbs, seq, input_seq, orgnsm, name)
            if state:
                print('\nSequencia adicionada com sucesso!\nID da sequência: ', eng.last_id)
            else:
                print('\nSequência não adicionada - não é válida.')
            print(menu)
        except:
            print('\nErro ao adicionar sequência.')
            print(menu)
    
    def do_2(self, arg):
        'Comando para adicionar uma sequência ao gestor a partir de um ficheiro: 2'
        try:
            file_name = input('Introduza o nome do ficheiro (com extensão): ')
            (state, input_seq) = eng.check_file(file_name)
            if state:
                if input_seq == 'fasta' or input_seq == 'faa':
                    (state_file, state_seq) = self.load_sequence_faa(file_name, 'file_' + input_seq)
                    if state_file:
                        if state_seq:
                            print('\nSequencia adicionada com sucesso.\nNúmero da sequência: ', eng.last_id)
                        else:
                            print('\nSequência não adicionada.')
                    else:
                        print('\nFicheiro não encontrado.\nVerifique o nome do ficheiro e a diretoria.')            
                else:
                    (state_file, n_seq_val, n_seq_nval) = self.load_sequence_txt(file_name)
                    if state_file:
                        print('\n', n_seq_val, ' Sequência(s) adicionada(s) com sucesso.', sep = '')
                        print('\n', n_seq_nval, ' Sequência(s) não adicionada(s).', sep = '')
                    else:
                        print('\nFicheiro não encontrado.\nVerifique o nome do ficheiro e a diretoria.')
            else:
                print('\nNome do ficheiro introduzido inválido.\nVerifique se o ficheiro que pretende apresenta extensão ".txt", ".faa" ou ".fasta"')
            print(menu)  
        except:
            print('\nErro ao adicionar sequência.')
            print(menu)
    

    def do_M(self, arg):
        'Comando para retroceder ao MENU Sequência mais semelhante: M'
        return True