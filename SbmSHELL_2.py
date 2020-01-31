# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 20:08:01 2020

@author: Carina Afonso (PG40952) e Laura Duro (PG40959)
"""

from cmd import *
from SeqBioManagerENG import SeqBioManagerENG

class SbmSHELL_2(Cmd):
    prompt = 'SeqBioManager> '
    intro = '''                             
                    MENU Guardar sequências                                
  ===========================================================
    
             1. Guardar sequências individualmente
             2. Guardar todas as sequências
       
        
                            M. MENU
    '''  
                        
    def __set_menu__(self):
        '''
        Define o menu a exibir entre cada comando executado
        '''
        global menu
        global menu
        menu = '''                             
                    MENU Guardar sequências                                
  ===========================================================
    
             1. Guardar sequências individualmente
             2. Guardar todas as sequências
       
        
                            M. MENU
    '''                          
    
    def __set_eng__(self, arg):
        '''
        Transporte da instancia da classe SeqBioManagerENG criada na shell principal
        '''
        global eng
        eng = arg
    
    def do_1(self, arg):
        'Comando para guardar uma sequência do gestor num ficheiro: 1'
        while True:
            id_seq = int(input('Introduza o ID, associado ao gestor, da sequência: '))
            file_name = input('Introduza o nome do ficheiro (sem extensão): ')
            (state_id, state_file) = eng.save_sequence(id_seq, file_name)
            if state_id:
                if state_file:
                    print('\nSequência guardada no ficheiro "', file_name + '_SBM.txt".',  sep = '')
                else:
                    print('\nErro ao guardar sequência.')
                break
            else:
                print('\n\tID da sequência inválido!')
        print(menu)
    
    def do_2(self, arg):
        'Comando para guardar todas as sequências do gestor num ficheiro: 2'
        file_name = input('Introduza o nome do ficheiro (sem extensão): ')
        if eng.save_all_sequences(file_name):
            print('Sequência guardada no ficheiro "', file_name + 'all_SBM.txt".',  sep = '')
        else:
            print('Erro ao guardar sequências.')
        print(menu)
        
    def do_M(self, arg):
        'Comando para retroceder ao MENU: M'
        return True
    