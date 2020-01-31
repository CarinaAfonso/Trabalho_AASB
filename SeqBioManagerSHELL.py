# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 16:41:47 2020

@author: Carina Afonso (PG40952) e Laura Duro (PG40959)
"""

from cmd import *
from SbmSHELL_1 import SbmSHELL_1
from SbmSHELL_2 import SbmSHELL_2
from SbmSHELL_3 import SbmSHELL_3
from SbmSHELL_4 import SbmSHELL_4
from SbmSHELL_5 import SbmSHELL_5
from SbmSHELL_6 import SbmSHELL_6
from SbmSHELL_7 import SbmSHELL_7
from SbmSHELL_10 import SbmSHELL_10
from SeqBioManagerENG import SeqBioManagerENG

class SeqBioManagerSHELL(Cmd):

    prompt = 'SeqBioManager> '
    menu = '''                             
                          MENU                                  
  ===========================================================
    
            1. Adicionar sequências
            2. Guardar sequências
            3. Eliminar sequências do gestor
            4. Atributos sequências
            5. Sequência mais semelhante
            6. Calcular frequência de sub-sequências
            7. Procurar ocurrências de padrões
            8. Blast
            9. Alinhamento múltiplo
           10. Árvore filogenéticas
           11. Domínios funcionais
           
                
                
                        Q. Sair
    '''                          
    intro = '\nBem-vindo ao Gestor de Sequências Biológicas - proteínas.\nEscolha uma opção do menu para começar.\n' + menu
    
    def __set_menu__(self):
        '''
        Define o menu a exibir entre cada comando executado
        '''
        global menu
        menu = '''                             
                          MENU                                  
  ===========================================================
    
            1. Adicionar sequências
            2. Guardar sequências
            3. Eliminar sequências do gestor
            4. Atributos sequências
            5. Sequência mais semelhante
            6. Calcular frequência de sub-sequências
            7. Procurar ocurrências de padrões
            8. Blast
            9. Alinhamento múltiplo
           10. Árvore filogenética
           11. Domínios funcionais
           
                
                
                        Q. Sair
    '''                          
    
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
    
    def __set_blast_parameters__(self):
        '''
        Função para defenir parametros de blast
        :return dtbs: base de dados contra a qual correrá o blast
        :return hit: número de hits a retornar
        :return evalue: evalue cutoff
        '''

        while True:
            option = input('''
                                      
    1. Não redundante
    2. Sequências de referência de proteínas do NCBI
    3. UniProtKB/SwissProt não-redundante
    4. Base de dados de proteínas PDB
            
    Escolha uma base de dados: ''')
            if int(option) != 1 and int(option) != 2 and int(option) != 3 and int(option) != 4:
                print('\nnOpção inválida!')
            else:
                break
        if int(option) == 1:
            dtbs = 'nr'
        elif int(option) == 2:
            dtbs = 'refseq_protein'
        elif int(option) == 3:
            dtbs = 'swissprot'
        elif int(option) == 4:
            dtbs = 'pdbaa'
        hit = input('\tNúmero de hits: ')
        e_value = input('\tLimite e-value: ')
        return (dtbs, hit, e_value)
    
    def __set_parameters_multi_align__(self):
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
        'Comando para adicionar uma ou mais sequências ao gestor: 1'
        try:
            sh_1 = SbmSHELL_1()
            sh_1.__set_menu__()
            sh_1.__set_eng__(eng)
            sh_1.cmdloop()
            del sh_1
            print(menu)
        except:
            print('\nErro: MENU Adicionar Sequências')
            print(menu)

    def do_2(self, arg):
        'Comando para guardar uma ou mais sequências em ficheiros: 2'
        try:
            sh_2 = SbmSHELL_2()
            sh_2.__set_menu__()
            sh_2.__set_eng__(eng)
            sh_2.cmdloop()
            del sh_2
            print(menu)
        except:
            print('\nErro: MENU Guardar Sequências')
            print(menu)
        
    def do_3(self, arg):
        'Comando para eliminar uma ou mais sequências do gestor: 3'
        try:
            sh_3 = SbmSHELL_3()
            sh_3.__set_menu__()
            sh_3.__set_eng__(eng)
            sh_3.cmdloop()
            del sh_3
            print(menu)
        except:
            print('\nErro: MENU Eliminar Sequências')
            print(menu)
            
    def do_4(self, arg):
        'Comando para consultar ou alterar atributos de uma sequência do gestor: 4'
        try:
            sh_4 = SbmSHELL_4()
            sh_4.__set_menu__()
            sh_4.__set_eng__(eng)
            sh_4.cmdloop()
            del sh_4
            print(menu)
        except:
            print('\nErro: MENU Atributos Sequências')
            print(menu)
            
    def do_5(self, arg):
        'Comando para encontrar, para uma sequência escolhida, a sequência mais similar já existente no gestor: 5'
        try:
            sh_5 = SbmSHELL_5()
            sh_5.__set_menu__()
            sh_5.__set_eng__(eng)
            sh_5.cmdloop()
            del sh_5
            print(menu)
        except:
            print('\nErro: MENU Sequência mais semelhante')
            print(menu)
    
    def do_6(self, arg):
        '''Comando para encontrar, para uma sequência escolhida ou para todas as sequências presentes no gestor,
            as frequências das sub-sequências, com tamanho k, presentes: 6'''
        try:
            sh_6 = SbmSHELL_6()
            sh_6.__set_menu__()
            sh_6.__set_eng__(eng)
            sh_6.cmdloop()
            del sh_6
            print(menu)
        except:
            print('\nErro: MENU Frequência de sub-sequências')
            print(menu)
    
    def do_7(self, arg):
        'Comando para procurar ocorrências de padrôes, dadas na forma de espressão regular, numa sequência do gestor ou em todas: 7'
        try:
            sh_7 = SbmSHELL_7()
            sh_7.__set_menu__()
            sh_7.__set_eng__(eng)
            sh_7.cmdloop()
            del sh_7
            print(menu)
        except:
            print('\nErro: MENU Ocorrências de Padrões')
            print(menu)
    
    def do_8(self, arg):
        'Comando para efetuar Blast (NCBI) de uma sequência do gestor: 8'
        try:
            while True:
                id_gestor = input('Introduza o ID (do gestor) da sequência: ')
                if eng.check_id_seq(int(id_gestor)):
                    break
                else:
                    print('ID inválido!')   
            (dtbs, hit_size, e_value) = self.__set_blast_parameters__()
            print('\nBlast em progresso .........')
            seqs_result = eng.blast(int(id_gestor), dtbs, int(hit_size), float(e_value))
            i = 1
            for result in seqs_result:
                print(i, '.', sep = '')
                for info in result:
                    print('\n', str(info))
                print('\n')
                i += 1
            while True:
                option = input('Deseja importar alguma sequência para o gestor do resultado do blast? S ou N\n').upper()
                if option != 'N' and option != 'S':
                    print('\nOpção inválida')
                else:
                    break
            if option == 'S':
                aux = True
                while aux:
                    seqs_save = input('Introduza os números das sequências que deseja importar: ').split()
                    for id_seq in seqs_save:
                        aux = False
                        if int(id_seq) < 1 or int(id_seq) >= i:
                            aux = True
                            print('\nNúmeros de sequências inválidos!')
                            break
            eng.load_seqs_blast(seqs_save, seqs_result)
            print('\nSequências importadas.')
            print(menu)
        except:
            print('Erro: Blast')
            print(menu)
    
    def do_9(self, arg):
        'Comando para alinhamento múltiplo de diversas sequências do gestor: 9'
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
                (option, file_matrix, gap, match, mismatch) = self.__set_parameters_multi_align__()
                if option == '1':
                    sm = eng.load_subs_matrix(file_matrix)
                else:
                    sm = eng.make_subs_matrix(match, mismatch)
                arv = eng.upgma_tree(ids_seqs, sm, gap)
                ordered_ids_seqs = eng.reorganize_seqs(arv, ids_seqs)
                align_cons = eng.multiple_align(ordered_ids_seqs, sm, gap)
                print(align_cons)
            print(menu)
        except:
            print('Erro: Alinhamento Múltiplo  - algoritmo local')
            print(menu)
    
    def do_10(self, arg):
        'Comando para construção de árvores filogenéticas com as sequências do gestor: 10'
        try:
            sh_10 = SbmSHELL_10()
            sh_10.__set_menu__()
            sh_10.__set_eng__(eng)
            sh_10.cmdloop()
            del sh_10
            print(menu)
        except:
            print('\nErro: MENU Árvore Filogenética')
            print(menu)
        
    def do_11(self, arg):
        'Comando para procurar domínios funcionais para sequências do gestor: 11'
        try:
            ids_seqs = self.__select_sequences__()
            if len(ids_seqs) == 0:
                print('\nNenhuma sequência selecionada!')
            else:
                results = eng.scan_motifs(ids_seqs)             
                for seq in range(len(results)):
                    if results[seq].n_match == 0:
                        print('\nNão foram detetados motifs para a sequência ', ids_seqs[seq])
                    else:
                        print('\n--------- Sequência ',ids_seqs[seq],'---------')
                        print('nº motifs: ', results[seq].n_match)
                        for motif in range(len(results[seq])):
                            if len(results[seq]) != 0:
                                print('Signature ac: ',results[seq][motif]['signature_ac'])
            print(menu)
        except:
            print('\nErro - Scan Prosite')
            print(menu)
    
    def do_Q(self, arg):
        state = eng.save_data()
        print('\nTerminou o gestor.')
        if state:
            print('\nDados guardados com sucesso!')
        else:
            print('\nErro ao guardar dados.')
        return True



if __name__ == '__main__':
    eng = SeqBioManagerENG()
    eng.load_previous_data()
    sh = SeqBioManagerSHELL()
    sh.__set_menu__()
    sh.cmdloop()   