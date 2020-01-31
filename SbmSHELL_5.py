# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:26:35 2020

@author: Carina Afonso (PG40952) e Laura Duro (PG40959)
"""

from cmd import *
from SbmSHELL_5_1 import SbmSHELL_5_1
from SeqBioManagerENG import SeqBioManagerENG

class SbmSHELL_5(Cmd):
    prompt = 'SeqBioManager> '
    intro = '''                             
                MENU Sequência mais semelhante                                
  ===========================================================
    
  
                Escolha a sequência a usar:
                 
                1. Carregar sequência
                2. Usar uma sequência do gestor
       
        
                            M. MENU
    '''  
                        
    def __set_menu__(self):
        '''
        Define o menu a exibir entre cada comando executado
        '''
        global menu
        global menu
        menu = '''                             
                MENU Sequência mais semelhante                                
  ===========================================================
    
  
                Escolha a sequência a usar:
                 
                1. Carregar sequência
                2. Usar uma sequência do gestor
       
        
                            M. MENU
    '''  
    
    def __set_eng__(self, arg):
        '''
        Transporte da instancia da classe SeqBioManagerENG criada na shell principal
        '''
        global eng
        eng = arg
        
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
                option = input('Escolha os parametros dos alinhamentos:\n1.Usar matrix\n2.Defenir manualmente')
                if option == '1':
                    while True:
                        matrix = input('1.Blosum62\n2.Outra')
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
                gap = int(input('Introduza a penalização por espaçamento:'))
            return (option, file_matrix, gap, match, mismatch)
        except:
            print('\nParâmetros introduzidos incorretos.')
            print(menu)
    
    def do_1(self, arg):
        'Comando para carregar uma sequência manualmente ou a partir de um ficheiro: 1'
        try:
            sh_5_1 = SbmSHELL_5_1()
            sh_5_1.__set_menu__()
            sh_5_1.__set_eng__(eng)
            sh_5_1.cmdloop()
            del sh_5_1
            (option, file_matrix, gap, match, mismatch) = self.__set_parameters__()
            if option == '1':
                sm = eng.load_subs_matrix(file_matrix)
            else:
                sm = eng.make_subs_matrix(match, mismatch)
            best_id = eng.best_align(eng.last_id, sm, gap) #a sequencia foi introduzida, foi a última
            print('\nA sequência que apresenta maior semelhança, com os parmetros escolhidos, com a sequência importada é a sequência com id' + best_id)
            print(menu)
        except:
            print('Erro: MENU opção importe')
            print(menu)
       
    def do_2(self, arg):
        'Comando para escolher uma sequência a partir do gestor: 2'
        try:
            while True:
                id_gestor = int(input('Introduza o ID (do gestor) da sequência:'))
                if eng.check_id_seq(id_gestor):
                    break
                else:
                    print('\nID inválido!')
            (option, file_matrix, gap, match, mismatch) = self.__set_parameters__()
            if option == '1':
                sm = eng.load_subs_matrix(file_matrix)
            else:
                sm = eng.make_subs_matrix(match, mismatch)
            best_id = eng.best_align(eng.last_id, sm, gap) #a sequencia foi introduzida, foi a última
            print('\nA sequência que apresenta maior semelhança, com os parmetros escolhidos, com a sequência importada é a sequência com id' + best_id)
            print(menu)
        except:
            print('Erro: Alinhamento')
            print(menu)
    
    def do_M(self, arg):
        'Comando para retroceder ao MENU: M'
        return True