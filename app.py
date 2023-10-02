""" 
Algoritmo em desenvolvimento para separar a Clas. Escalão da Clas. Abs.,
de uma lista de resultados desportivos, inserindo um espaço em branco entre ambos.
"""

results = """1 94 Ricardo Fonseca 00:15:20 00:31:18 00:31:18 1 V55 12 874 Pedro Gaspar 00:15:44 00:32:37 00:32:36 2 Senior 19"""


age_group = ["Junior", "Senior", "V55"]


words = results.split()

for word in words:
    if word in age_group:
        word_index = words.index(word)
        next_word = words[word_index + 1]
        splitted_word = next_word.replace(next_word[1], " " + next_word[1])
        words[word_index + 1] = splitted_word

print(f"{words}")
