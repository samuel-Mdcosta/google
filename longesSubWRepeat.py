class Solution:
    def longestSub(self, s:str) -> int:
        l = 0
        n = len(s)
        sett = set()
        maior = 0

        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            w = (r - l) + 1
            maior = max(maior, w)
            sett.add(s[r])

        return maior


# =============================================================================
# PERGUNTAS A FAZER NA ENTREVISTA (Google SWE Intern) ANTES DE CODAR
# =============================================================================
# Mostrar que voce esclarece o problema antes de escrever codigo e algo muito
# valorizado pelo Google. Perguntas que voce deveria fazer:
#
# 1. O que conta como "caractere"? Apenas ASCII (a-z, A-Z), ASCII estendido
#    (256) ou Unicode completo? Isso muda a estrutura de dados que vou usar.
# 2. A string pode ser vazia? Se sim, devo retornar 0?
# 3. Espacos, numeros e simbolos contam como caracteres validos?
# 4. Devo retornar o COMPRIMENTO da substring ou a propria substring?
#    (Aqui retornamos o comprimento.)
# 5. Substring x subsequencia: confirmo que e substring (caracteres
#    contiguos), nao subsequencia (pode pular caracteres).
# 6. Qual o tamanho maximo da entrada? Isso ajuda a decidir se uma solucao
#    O(n^2) seria aceitavel ou se preciso de O(n).
# 7. Diferencia maiusculas de minusculas? ("a" e "A" sao diferentes?)
# 8. Se houver empate (varias substrings com o mesmo tamanho), qualquer uma
#    serve? (Importa so se eu tiver que retornar a substring.)
#
# =============================================================================
# COMO SERIA A SOLUCAO POR FORCA BRUTA (BRUTE FORCE)
# =============================================================================
#
# class SolutionBruteForce:
#     def longestSub(self, s: str) -> int:
#         n = len(s)
#         maior = 0
#         # Para cada possivel inicio i da substring...
#         for i in range(n):
#             # ...e para cada possivel fim j...
#             for j in range(i, n):
#                 # ...verifica se a substring s[i..j] tem chars unicos.
#                 sub = s[i:j + 1]
#                 if len(set(sub)) == len(sub):  # sem repeticao
#                     maior = max(maior, j - i + 1)
#         return maior
#
# -----------------------------------------------------------------------------
# POR QUE A FORCA BRUTA E RUIM
# -----------------------------------------------------------------------------
# Ela gera TODAS as substrings possiveis (sao ~n^2/2 substrings) e, para cada
# uma, verifica se tem caracteres repetidos criando um set. Isso significa
# trabalho redundante enorme: a substring s[i..j] reprocessa quase tudo que a
# substring s[i..j-1] ja tinha processado. Nao aproveitamos nada do que ja
# sabemos. A solucao otimizada (sliding window) elimina esse retrabalho.
#
# Complexidade da forca bruta:
#   - Tempo:  O(n^3) -> dois lacos (O(n^2)) para gerar cada substring,
#             mais O(n) para construir/verificar o set em cada uma.
#             (Pode-se otimizar para O(n^2) verificando unicidade de forma
#             incremental, mas ainda e bem pior que O(n).)
#   - Espaco: O(min(n, m)) -> o set usado para checar a substring, onde m e o
#             tamanho do alfabeto.
#
# =============================================================================
# EXPLICACAO PASSO A PASSO DA SOLUCAO OTIMA (class Solution acima)
# =============================================================================
# Tecnica: SLIDING WINDOW (janela deslizante) com um SET.
# Ideia: manter uma "janela" [l, r] que sempre contem apenas caracteres unicos.
# Quando aparece um caractere repetido, encolhemos a janela pela esquerda (l)
# ate ela voltar a ser valida.
#
#   l = 0          -> ponteiro da ESQUERDA (inicio da janela).
#   n = len(s)     -> tamanho da string (evita recalcular len() no laco).
#   sett = set()   -> guarda os caracteres que estao DENTRO da janela atual.
#                     Set da busca/insercao/remocao em O(1) medio.
#   maior = 0      -> maior comprimento de janela valida encontrado ate agora.
#
#   for r in range(n):          -> r e o ponteiro da DIREITA; expande a janela
#                                  um caractere por vez.
#       while s[r] in sett:     -> se o char da direita JA esta na janela, ha
#                                  repeticao; precisamos encolher pela esquerda.
#           sett.remove(s[l])   -> remove o char mais a esquerda do set...
#           l += 1              -> ...e avanca o ponteiro esquerdo. Repete ate
#                                  que s[r] nao esteja mais na janela.
#       w = (r - l) + 1         -> tamanho atual da janela valida.
#       maior = max(maior, w)   -> atualiza a melhor resposta.
#       sett.add(s[r])          -> agora que a janela e valida, adiciona o char
#                                  da direita ao set.
#   return maior                -> retorna o maior comprimento encontrado.
#
# Por que funciona: cada caractere entra no set exatamente uma vez (quando r
# passa por ele) e sai no maximo uma vez (quando l passa por ele). Por isso os
# dois ponteiros andam so para frente, nunca voltam.
#
# Complexidade da solucao otima:
#   - Tempo:  O(n) -> r percorre a string uma vez e l, no total, tambem anda no
#             maximo n vezes. Cada char e adicionado e removido no maximo 1 vez.
#   - Espaco: O(min(n, m)) -> o set guarda no maximo o numero de caracteres
#             distintos da janela, limitado pelo tamanho do alfabeto m
#             (ex.: 26 para letras minusculas, 128 para ASCII).
# =============================================================================