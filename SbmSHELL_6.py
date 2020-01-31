# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:37:36 2020

@author: Carina Afonso (PG40952) e Laura Duro (PG40959)
"""

from cmd import *
from SeqBioManagerENG import SeqBioManagerENG

class SbmSHELL_6(Cmd):
    prompt = 'SeqBioManager> '
    intro = '''                             
               MENU Frequência de sub-sequências                                
  ===========================================================
    
         1. Calcular para uma sequência do gestor
         2. Calcular para todas as sequências do gestor
       
        
                            M. MENU
    '''  
                        
    def __set_menu__(self):
        '''
        Define o menu a exibir entre cada comando executado
        '''
        global menu
        global menu
        menu = '''                             
               MENU Frequência de sub-sequências                                
  ===========================================================
    
         1. Calcular para uma sequência do gestor
         2. Calcular para todas as sequências do gestor
       
        
                            M. MENU
    '''                          
    
    def __set_eng__(self, arg):
        '''
        Transporte da instancia da classe SeqBioManagerENG criada na shell principal
        '''
        global eng
        eng = arg
    
    def do_1(self, arg):
        'Comando para calcular a frequência de sub-sequências com tamanho k, introduzido pelo utilizador, numa sequência do gestor: 1'
        try:
            while True:
                id_gestor = input('Introduza o id (do gestor) da sequência: ')
                if eng.check_id_seq(int(id_gestor)):
                    break
                else:
                    print('\nID da sequência inválido!')
            while True:
                k = input('Introduza o tamanho das sub-sequências: ')
                if int(k) > 0 and int(k) <= int(eng.seqs[int(id_gestor)]['size']):
                    break
                else:
                    print('\nValor de k inválido! Escolha um número positivo e com comprimento menor que a sequência escolhida.')    
            sub_seqs = eng.freq_sub_seqs(int(id_gestor), int(k))
            print('\nFrequência de sub-sequências na sequência com ID', id_gestor)
            print('\n\tFrequência\tSub-sequência (k=', k, ')', sep = '')
            for key in sub_seqs.keys():
                print('\n\t  ', sub_seqs[key], '\t', key)
            print(menu)
        except:
            print('Erro: sub-sequência')
            print(menu)
    
    
    def do_2(self, arg):
        'Comando para calcular a frequência de sub-sequências com tamanho k, introduzido pelo utilizador, em todas as sequências do gestor: 2'
        try:
            while True:
                k = input('Introduza o tamanho das sub-sequências: ')
                if int(k) > 0:
                    break_value = True
                    for id_gestor in eng.seqs.keys():
                        if int(k) > int(eng.seqs[int(id_gestor)]['size']):
                            print('\nSub-sequência maior que sequências.')
                            break_value = False
                            break
                    if break_value:
                        break  
                else:
                    print('\nValor de k inválido! Escolha um número positivo.')    
            all_sub_seqs = eng.allseqs_freq_sub_seqs(int(k))
            for id_gestor in all_sub_seqs.keys():
                print('\nFrequência de sub-sequências na sequência com ID', str(id_gestor))
                print('\n\tFrequência\tSub-sequência (k=', k, ')', sep = '')
                for key in all_sub_seqs[id_gestor].keys():
                    print('\n\t  ', all_sub_seqs[id_gestor][key], '\t', key)
            print(menu)
        except:
            print('Erro: sub-sequência')
            print(menu)
        
    def do_M(self, arg):
        'Comando para retroceder ao MENU: M'
        return True
    
    
    
    
    
    