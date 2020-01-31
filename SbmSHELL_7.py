# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 19:19:05 2020

@author: Carina Afonso (PG40952) e Laura Duro (PG40959)
"""

from cmd import *
from SeqBioManagerENG import SeqBioManagerENG

class SbmSHELL_7(Cmd):
    prompt = 'SeqBioManager> '
    intro = '''                             
                  MENU Ocorrências de Padrões                                
  ===========================================================
    
        1. Encontrar para uma sequência do gestor
        2. Encontrar para todas as sequências do gestor
       
        
                            M. MENU
    '''  
                        
    def __set_menu__(self):
        '''
        Define o menu a exibir entre cada comando executado
        '''
        global menu
        global menu
        menu = '''                             
                  MENU Ocorrências de Padrões                                
  ===========================================================
    
        1. Encontrar para uma sequência do gestor
        2. Encontrar para todas as sequências do gestor
       
        
                            M. MENU
    '''                          
    
    def __set_eng__(self, arg):
        '''
        Transporte da instancia da classe SeqBioManagerENG criada na shell principal
        '''
        global eng
        eng = arg
    
    def do_1(self, arg):
        'Comando para encontrar padrões, dados na forma de expressão regular introduzidos pelo utilizador, numa sequência do gestor: 1'
        try:
            while True:
                id_gestor = input('Introduza a ID (do gestor) da sequência:')
                if eng.check_id_seq(int(id_gestor)):
                    break
                else:
                    print('ID inválido!')
            expre = input('Introduza, na forma de expressão regular, um padrão: ')
            (post, num) = eng.find_re_pattern(int(id_gestor), expre)
            if num == 0:
                print('\nNão foram encontradas ocurrências do padrão', expre, 'na sequência com ID', id_gestor)
            else:
                print('\nForam encontradas', num, 'ocorrência(s) do padrão', expre, 'na sequência com ID', id_gestor)
                print('\nPosições na sequência:\n   Início\tFim')
                for pos in post:
                    print('\n     ', pos.span()[0], '\t', pos.span()[1])
            print(menu)
        except:
            print('Erro: encontrar padrões')
            print(menu)
    
    def do_2(self, arg):
        'Comando para encontrar padrões, dados na forma de expressão regular introduzidos pelo utilizador, numa todas as sequências do gestor: 2'
        try:
            expre = input('Introduza, na forma de expressão regular, um padrão: ')
            patterns = eng.find_re_pattern_allseqs(expre)
            for id_gestor in patterns.keys():
                if patterns[id_gestor][1] == 0:
                    print('\nNão foram encontradas ocurrências do padrão "', expre, '" na sequência com ID', str(id_gestor), sep = '')
                else:
                    print('\nForam encontradas ', patterns[id_gestor][1], ' ocorrência(s) do padrão "', expre, '" na sequência com ID', str(id_gestor), sep = '')
                    print('\nPosições na sequência:\n   Início\tFim')
                    for pos in patterns[id_gestor][0]:
                        print('\n     ', pos.span()[0], '\t', pos.span()[1])
            print(menu)
        except:
            print('Erro: encontrar padrões')
            print(menu)  
        
    def do_M(self, arg):
        'Comando para retroceder ao MENU: M'
        return True
    
    
    
    