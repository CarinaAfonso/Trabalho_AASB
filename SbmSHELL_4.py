# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 00:37:44 2020

@author: Carina Afonso (PG40952) e Laura Duro (PG40959)
"""

from cmd import *
from SeqBioManagerENG import SeqBioManagerENG

class SbmSHELL_4(Cmd):
    prompt = 'SeqBioManager> '
    intro = '''                             
                   MENU Atributos sequências                                         
  ===========================================================
    
         1. Consultar atributos de uma sequência
         2. Consultar atributos de todas as sequências
         3. Alterar atributos de uma sequência
       
        
                            M. MENU
    '''  
                        
    def __set_menu__(self):
        '''
        Define o menu a exibir entre cada comando executado
        '''
        global menu
        global menu
        menu = '''                             
                   MENU Atributos sequências                                         
  ===========================================================
    
         1. Consultar atributos de uma sequência
         2. Consultar atributos de todas as sequências
         3. Alterar atributos de uma sequência
       
        
                            M. MENU
    '''  
    
    def __set_eng__(self, arg):
        '''
        Transporte da instancia da classe SeqBioManagerENG criada na shell principal
        '''
        global eng
        eng = arg
    
    def __chose_atrb_seq__(self, atrb):
        '''
        Permite ao utilizador escolher quais os atributos que quererá alterar
        :param atrb: lista de atributos pertencentes à sequência
        :return chng_atrb: lista de atributos a alterar pelo utilizador
        '''
        chng_atrb = []      
        if 'id' in atrb:
            while True:
                aux = input('Deseja alterar a Base de Dados e o ID associado? S ou N\n').upper()
                if aux == 'S':
                    chng_atrb.append('id')
                    break
                elif aux == 'N':
                    break
                else:    
                    print('\nOpção inválida!')
        if 'orgnsm' in atrb:
            while True:
                aux = input('Deseja alterar o Organismo? S ou N\n').upper()
                if aux == 'S':
                    chng_atrb.append('orgnsm')
                    break
                elif aux == 'N':
                    break
                else:    
                    print('\nOpção inválida!')
        if 'name' in atrb:
            while True:
                aux = input('Deseja alterar o nome? S ou N\n').upper()
                if aux == 'S':
                    chng_atrb.append('name')
                    break
                elif aux == 'N':
                    break
                else:    
                    print('\nOpção inválida!')
        if 'others' in atrb:
            while True:
                aux = input('Deseja alterar informações adicionais? S ou N\n').upper()
                if aux == 'S':
                    chng_atrb.append('others')
                    break
                elif aux == 'N':
                    break
                else:    
                    print('\nOpção inválida!')
        return chng_atrb
    
    def do_1(self, arg):
        'Comando para consultar os atributos de uma sequência: 1'
        while True:
            id_seq = input('Introduza o ID (do gestor) da sequência:')
            (state_id, input_seq, id_dtbs, dtbs, orgnsm, name, others, seq, size) = eng.get_atrb_seq(int(id_seq))
            if state_id:
                print('\nID gestor:', id_seq)
                if input_seq != -1:
                    print('\nInput: ' + input_seq)
                if dtbs != -1:
                    print('Base de Dados:' + dtbs)
                if id_dtbs != -1:   
                    print('ID:' + id_dtbs)
                if orgnsm != -1:
                    print('Organismo:' + orgnsm)
                if name != -1:
                    print('Nome:' + name)
                if others != -1:
                    print('Outros:' + others)
                print('Tamanho da seq:' + str(size))
                print('Seq:\n' + seq)
                break
            else:
                print('\n\tID da sequência inválido!')
        print(menu)
    
    def do_2(self, arg):
        'Comando para visualizar os atributos de todas as sequências: 2'
        for id_seq in eng.seqs.keys():
            (state_id, input_seq, id_dtbs, dtbs, orgnsm, name, others, seq, size) = eng.get_atrb_seq(int(id_seq))
            if state_id:
                print('\n\nID gestor:', id_seq)
                if input_seq != -1:
                    print('\nInput: ' + input_seq)
                if dtbs != -1:
                    print('Base de Dados:' + dtbs)
                if id_dtbs != -1:   
                    print('ID:' + id_dtbs)
                if orgnsm != -1:
                    print('Organismo:' + orgnsm)
                if name != -1:
                    print('Nome:' + name)
                if others != -1:
                    print('Outros:' + others)
                print('Tamanho da seq:' + str(size))
                print('Seq:\n' + seq)
            else:
                print('\n\tID da sequência inválido!')
        print(menu)
    
    def do_3(self, arg):
        'Comando para alterar os atributos a uma sequência: 3'
        while True:
            id_gestor = input('Introduza o ID (do gestor) da sequência:')
            (state_id, atrb) = eng.set_atrb_seq(int(id_gestor))
            if state_id: 
                chng_atrb = self.__chose_atrb_seq__(atrb)
                if len(chng_atrb) != 0:
                    if eng.change_atrb_seq(int(id_gestor), chng_atrb):
                        print('\nAtributos da sequência ' + id_gestor + ' alterados com sucesso.')
                    else:
                        print('\nAtributos da sequência' + id_gestor + 'não alterados.')
                else:
                    print('\nNão foram selecionados atributos para alterar.')
                break
            else:
                print('\n\tID da sequência inválido!')
        print(menu)

    def do_M(self, arg):
        'Comando para retroceder ao MENU: M'
        return True
