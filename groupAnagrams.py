
class Solution:
    def group(self, strs: List[str]) -> List[List[str]]:
        anagramsDict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            anagramsDict[key].append(s)

        return list(anagramsDict.values())


# =====================================================================
# 1) BRUTE FORCE (forca bruta) - como seria
# =====================================================================
#
# class SolutionBruteForce:
#     def group(self, strs: List[str]) -> List[List[str]]:
#         result = []          # lista final de grupos
#         used = [False] * len(strs)   # marca quais strings ja foram agrupadas
#
#         for i in range(len(strs)):
#             if used[i]:
#                 continue                 # ja foi colocada em um grupo, pula
#             group = [strs[i]]            # comeca um grupo novo com a string i
#             used[i] = True
#             for j in range(i + 1, len(strs)):
#                 if used[j]:
#                     continue
#                 # checa se strs[j] e anagrama de strs[i].
#                 # forma mais ingenua: ordenar as duas e comparar
#                 if sorted(strs[i]) == sorted(strs[j]):
#                     group.append(strs[j])
#                     used[j] = True
#             result.append(group)
#         return result
#
# =====================================================================
# 2) PORQUE O BRUTE FORCE E RUIM + COMPLEXIDADE
# =====================================================================
#
# Por que e ruim:
#   - Ele compara CADA string com TODAS as outras (dois loops aninhados).
#     Isso e um padrao O(n^2) de comparacoes.
#   - Para cada comparacao ainda ordena as duas strings (sorted), o que
#     custa O(k log k), onde k = tamanho da string.
#   - Ou seja, ele repete muito trabalho: a mesma string pode ser
#     ordenada varias vezes, uma vez para cada comparacao.
#
# Seja n = numero de strings e k = tamanho maximo de uma string.
#
#   Complexidade de TEMPO:  O(n^2 * k log k)
#       - n^2 por causa dos dois loops comparando todos com todos
#       - k log k por causa do sorted() dentro da comparacao
#
#   Complexidade de ESPACO: O(n * k)
#       - precisamos guardar todas as strings na lista de resultado
#       - (o array "used" e O(n))
#
# O problema central: O(n^2) nao escala. Com 10.000 strings ja sao
# ~100 milhoes de comparacoes. Precisamos de uma forma de agrupar
# anagramas SEM comparar par a par -> usar um dicionario (hash map).
#
# =====================================================================
# 3) EXPLICACAO PASSO A PASSO DA SOLUTION (a otimizada acima)
# =====================================================================
#
# A ideia chave: dois strings sao anagramas se e somente se tem a
# mesma CONTAGEM de cada letra. Entao usamos essa contagem como uma
# "assinatura" (chave) e jogamos no dicionario. Anagramas caem na
# mesma chave automaticamente -> sem comparar par a par.
#
#   def group(self, strs: List[str]) -> List[List[str]]:
#
#       anagramsDict = defaultdict(list)
#         -> Cria um dicionario onde o valor padrao de qualquer chave
#            nova e uma lista vazia. Assim podemos dar .append direto
#            sem precisar checar "se a chave existe".
#
#       for s in strs:
#         -> Percorre cada string da entrada uma unica vez.
#
#           count = [0] * 26
#             -> Array de 26 posicoes (uma por letra a-z), todas em 0.
#                Vai contar quantas vezes cada letra aparece em s.
#
#           for c in s:
#               count[ord(c) - ord('a')] += 1
#             -> Para cada caractere c, ord(c) - ord('a') transforma
#                a letra num indice 0..25 ('a'->0, 'b'->1, ...).
#                Incrementa a contagem daquela letra.
#
#           key = tuple(count)
#             -> Transforma a lista de contagem numa tupla.
#                Listas NAO podem ser chave de dicionario (sao mutaveis),
#                mas tuplas SIM (sao imutaveis e "hashaveis").
#                Essa tupla e a assinatura do anagrama.
#
#           anagramsDict[key].append(s)
#             -> Coloca a string s no grupo correspondente aquela
#                assinatura. Todos os anagramas compartilham a mesma
#                key, entao vao para a mesma lista.
#
#       return list(anagramsDict.values())
#         -> Retorna todos os grupos (os valores do dicionario) como
#            uma lista de listas.
#
#   Complexidade de TEMPO:  O(n * k)
#       - n strings, e para cada uma percorremos seus k caracteres.
#       - montar a chave de tamanho 26 e custo constante O(26) = O(1).
#       - bem melhor que O(n^2 * k log k) do brute force.
#
#   Complexidade de ESPACO: O(n * k)
#       - guardamos todas as strings dentro do dicionario.
#       - (cada chave e O(26) = O(1), entao as chaves nao dominam.)
#
# =====================================================================
# 4) PERGUNTAS PARA FAZER ANTES DE CODAR (entrevista Google Intern)
# =====================================================================
#
#   Sobre a ENTRADA:
#     - As strings contem apenas letras minusculas (a-z)? Ou tambem
#       maiusculas, numeros, espacos, acentos, unicode? (Isso decide se
#       posso usar o array de 26 posicoes ou preciso de algo mais geral.)
#     - O array de entrada pode ser vazio? Pode conter strings vazias ""?
#     - Pode haver strings duplicadas na entrada?
#     - Qual o tamanho maximo de n (quantidade de strings) e de k
#       (tamanho de cada string)? Isso ajuda a escolher a complexidade.
#
#   Sobre a SAIDA:
#     - A ordem dos grupos importa? E a ordem dentro de cada grupo?
#       (Em geral nao importa, mas e bom confirmar.)
#     - Preciso retornar como lista de listas? Algum formato especifico?
#
#   Sobre RESTRICOES / CASOS DE BORDA:
#     - Como tratar maiusculas vs minusculas? "Abc" e "bca" sao anagramas?
#     - Diferencas de memoria/tempo importam (otimizar para qual)?
#     - Existe garantia de caracteres ASCII apenas?
#
#   Exemplo para validar entendimento:
#     - Entrada: ["eat","tea","tan","ate","nat","bat"]
#       Saida esperada: [["eat","tea","ate"],["tan","nat"],["bat"]]
