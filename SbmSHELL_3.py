# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 00:05:53 2020

@author: Carina Afonso (PG40952) e Laura Duro (PG40959)
"""

from cmd import *
from SeqBioManagerENG import SeqBioManagerENG

class SbmSHELL_3(Cmd):
    prompt = 'SeqBioManager> '
    intro = '''                             
                    MENU Eliminar sequências                                
  ===========================================================
    
             1. Eliminar sequências individualmente
             2. Eliminar todas as sequências
       
        
                            M. MENU
    '''  
                        
    def __set_menu__(self):
        '''
        Define o menu a exibir entre cada comando executado
        '''
        global menu
        global menu
        menu = '''                             
                    MENU Eliminar sequências                                
  ===========================================================
    
             1. Eliminar sequências individualmente
             2. Eliminar todas as sequências
       
        
                            M. MENU
    '''                          
    
    def __set_eng__(self, arg):
        '''
        Transporte da instancia da classe SeqBioManagerENG criada na shell principal
        '''
        global eng
        eng = arg
    
    def do_1(self, arg):
        'Comando para eliminar uma sequência do gestor num ficheiro: 1'
        while True:
            id_seq = input('Introduza o ID (do gestor) da sequência:')
            state_id = eng.del_sequence(int(id_seq))
            if state_id:
                print('\nSequência ', id_seq, ' apagada do gestor.', sep = '')
                break
            else:
                print('\n\tID da sequência inválido!')
        print(menu)
    
    def do_2(self, arg):
        'Comando para eliminar todas as sequências do gestor num ficheiro: 2'
        while True:
            aux = input('Pretende eliminar todas as sequências? S ou N').upper()
            if aux == 'S':
                eng.del_all_sequences()
                print('\nTodas as sequências foram apagadas do gestor.')
                break
            elif aux == 'N':
                print('\nOperação abortado.')
                break
            else:
                print('\nOpção inválida!')
        print(menu)
            
    def do_M(self, arg):
        'Comando para retroceder ao MENU: M'
        return True