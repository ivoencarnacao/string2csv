""" 
Algoritmo em desenvolvimento 
para separar a Clas. Escalão da Clas. Abs. 
de uma lista de resultados desportivos, 
inserindo um espaço em branco entre ambos.

string_original = "1 94 Ricardo Fonseca 00:15:20 00:31:18 00:31:18 1 V55 12 874 Pedro Gaspar 00:15:44 00:32:37 00:32:36 2 Senior 13 221 Hugo Rocha 00:16:27 00:33:44 00:33:44 3 Grupo Desportivo do Estreito Senior 24 356 André Costa 00:16:27 00:34:15 00:34:14 4 Casa do Benfica de Reguengos de Monsaraz Senior 35 202 José Gaspar 00:16:40 00:34:22 00:34:21 5 V45 1"

string_transformada = "
1 94 Ricardo Fonseca 00:15:20 00:31:18 00:31:18 1 V55 1
2 874 Pedro Gaspar 00:15:44 00:32:37 00:32:36 2 Senior 1
3 221 Hugo Rocha 00:16:27 00:33:44 00:33:44 3 Grupo Desportivo do Estreito Senior 2
4 356 André Costa 00:16:27 00:34:15 00:34:14 4 Casa do Benfica de Reguengos de Monsaraz Senior 3
5 202 José Gaspar 00:16:40 00:34:22 00:34:21 5 V45 1
"

Objetivos:
1. Separar a Clas. Escalão da Clas. Abs. 
  inserindo um espaço em branco entre ambos.
2. Fazer mudança de linha entre cada atleta
3. Considerar os atletas com clube
4. Imprimir num ficheiro csv
5. Inserir uma coluna para o género dos atletas

"""

string_original = """1 94 Ricardo Fonseca 00:15:20 00:31:18 00:31:18 1 V55 12 874 Pedro Gaspar 00:15:44 00:32:37 00:32:36 2 Senior 1"""


#print(string_original)


palavras = string_original.split(' ')
#print(palavras)

#print(palavras[9])
print(palavras[0:10])


