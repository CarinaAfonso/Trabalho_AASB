# Trabalho_AASB - Grupo 4 [Carina Afonso (PG40952) e Laura Duro (PG40959)]

Este trabalho foi realizado no âmbito da unidade curricular Algoritmos para Análise de Sequências Biológicas, tendo como objetivo a criação de um programa, interativo com o utilizador através de um menu, que permita armazenar, gerir e manipular um conjunto de sequências de proteínas, cobrindo diversos funcionalidades (Descritas no menu em baixo).

                             
                          MENU                                  
  ===========================================================
    
            1. Adicionar sequências
            2. Guardar sequências
            3. Eliminar sequências do gestor
            4. Atributos sequências
            5. Sequência mais semelhante
            6. Calcular frequência de sub-sequências
            7. Procurar ocorrências de padrões
            8. Blast
            9. Alinhamento múltiplo
           10. Árvore filogenética
           11. Domínios funcionais
           12. Alterações pós-tradução
           

De modo a guardar todas as sequências, inclusive informações sobre esta, criamos um dicionário que segue a seguinte orientação: 
                             {'id_seq': {'seq': MySeq(), 'id' : [bd, id_seq], 'input': input_seq}
                             
Optou-se por colocar um id interno ('id_seq'), para todas as seqências, e caso exista também o id externo ('id' : [bd, id_seq] ).

Uma vez que o programa permite a introdução de sequências de modo manual, assim como automático (através de ficheiros ou NCBI), guardamos o tipo de input realizado no dicionário ('input': input_seq).

Na realização do comando que encontra a sequência mais semelhante (comando 5. no Menu) em vez da realização de um Blast, optou-se por um alinhamento múltipo. Esta escolha foi feita com base no facto do alinamento múltiplo, apesar de menos eficiente ser mais preciso.
