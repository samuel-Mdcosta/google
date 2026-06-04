from typing import List

# =============================================================================
# PERGUNTAS PARA FAZER ANTES DE CODAR (entrevista de SWE Intern - Google)
# =============================================================================
# Numa entrevista, NUNCA comece a codar direto. Primeiro clarifique o problema.
# Para o 3Sum, as boas perguntas sao:
#
# 1. O array pode ter numeros negativos, zero e positivos? (sim, isso importa
#    para a logica de parar quando nums[i] > 0)
# 2. Preciso retornar os INDICES ou os VALORES dos numeros? (aqui sao valores)
# 3. As triplas precisam ser UNICAS? Ou pode repetir a mesma tripla?
#    (aqui precisam ser unicas -> por isso o "skip de duplicatas")
# 4. A ordem das triplas no resultado importa? E a ordem dos numeros dentro
#    de cada tripla? (geralmente nao importa, posso ordenar)
# 5. Posso modificar/ordenar o array de entrada? (se sim, posso usar sort())
# 6. Qual o tamanho maximo de N? (define se O(n^2) e aceitavel ou nao)
# 7. Os numeros cabem em int? Pode dar overflow na soma? (em Python nao, mas
#    em Java/C++ sim - bom mencionar)
# 8. O alvo e sempre 0 ou pode ser um valor qualquer? (aqui e fixo em 0)
# 9. O que retorno se nao existir nenhuma tripla? (lista vazia)
#
# Dica: tambem diga em voz alta um exemplo manual antes de codar.
# Ex: nums = [-1, 0, 1, 2, -1, -4] -> resposta [[-1,-1,2], [-1,0,1]]
# =============================================================================


# =============================================================================
# BRUTE FORCE (forca bruta) - como seria a solucao ingenua
# =============================================================================
# A ideia mais simples: testar TODAS as combinacoes de 3 numeros usando
# 3 loops aninhados (i, j, k) e ver quais somam 0. Para evitar triplas
# duplicadas, ordenamos o array e usamos um set.
#
# def threeSum_bruteforce(self, nums):
#     nums.sort()                          # O(n log n)
#     n = len(nums)
#     resultado = set()                    # set evita triplas repetidas
#     for i in range(n):                   # 1o numero
#         for j in range(i + 1, n):        # 2o numero
#             for k in range(j + 1, n):    # 3o numero
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     resultado.add((nums[i], nums[j], nums[k]))
#     return [list(t) for t in resultado]
#
# COMPLEXIDADE DE TEMPO: O(n^3)
#   Porque: sao 3 loops aninhados, cada um percorrendo ate n elementos.
#   n * n * n = n^3. O sort O(n log n) e dominado pelo n^3, entao some.
#
# COMPLEXIDADE DE ESPACO: O(n) (ou ate O(n^3) no pior caso do resultado)
#   Porque: alem do output, o set pode guardar muitas triplas. Se ignorarmos
#   o espaco do output, gastamos O(1) extra. Mas contando o set de respostas,
#   no pior caso ha O(n^3) triplas possiveis -> O(n^3) de espaco.
#   O sort em si usa O(n) ou O(log n) de espaco auxiliar dependendo da impl.
# =============================================================================


# =============================================================================
# SOLUCAO OTIMA - Sort + Two Pointers (dois ponteiros)
# =============================================================================
# Estrategia: fixar um numero nums[i] e usar dois ponteiros (beg e end) para
# achar os outros dois que somam -nums[i]. Como o array esta ordenado, da
# para mover os ponteiros de forma inteligente em vez de testar tudo.

class Solution:                                    # convencao: classe com inicial maiuscula
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                                # ordena o array -> O(n log n). Permite usar two pointers e pular duplicatas.
        n = len(nums)                              # guarda o tamanho para nao recalcular len() varias vezes
        answer = []                                # lista que vai acumular as triplas validas (o resultado)

        for i in range(n):                         # 'i' fixa o PRIMEIRO numero da tripla
            if nums[i] > 0:                        # se o menor numero ja e positivo, soma de 3 positivos nunca da 0...
                break                              # ...entao paramos: nao ha mais solucao possivel (array esta ordenado)
            if i > 0 and nums[i] == nums[i - 1]:   # se nums[i] e igual ao anterior, ja exploramos esse valor...
                continue                           # ...pulamos para nao gerar triplas DUPLICADAS

            beg, end = i + 1, n - 1                # dois ponteiros: 'beg' logo apos i, 'end' no final do array
            while beg < end:                       # enquanto os ponteiros nao se cruzarem
                total = nums[i] + nums[beg] + nums[end]   # soma dos 3 numeros atuais (corrigido: variavel unica e clara)
                if total == 0:                     # achamos uma tripla que soma 0
                    answer.append([nums[i], nums[beg], nums[end]])   # guarda a tripla no resultado
                    beg, end = beg + 1, end - 1    # move os DOIS ponteiros para dentro para procurar novas triplas
                    while beg < end and nums[beg] == nums[beg - 1]:   # pula valores repetidos no lado esquerdo...
                        beg += 1                   # ...para nao repetir a mesma tripla
                    while beg < end and nums[end] == nums[end + 1]:   # pula valores repetidos no lado direito...
                        end -= 1                   # ...mesma razao (evitar duplicatas)
                elif total < 0:                    # soma muito pequena (negativa) -> preciso de numeros maiores
                    beg += 1                       # move o ponteiro esquerdo para a direita (valores crescem, array ordenado)
                else:                              # soma muito grande (positiva) -> preciso de numeros menores
                    end -= 1                       # move o ponteiro direito para a esquerda (valores diminuem)
        return answer                             # devolve todas as triplas unicas encontradas

# -----------------------------------------------------------------------------
# COMPLEXIDADE DE TEMPO: O(n^2)
#   Porque: o sort custa O(n log n). Depois o loop 'for i' roda n vezes e, para
#   cada i, o while dos dois ponteiros roda no maximo O(n). Entao n * n = O(n^2).
#   Como n^2 > n log n, a complexidade final e O(n^2).
#
# COMPLEXIDADE DE ESPACO: O(1) auxiliar (sem contar o output e o sort)
#   Porque: so usamos algumas variaveis (i, beg, end, total). Nao criamos
#   estruturas que crescem com n. Observacao: o sort pode usar O(log n) a O(n)
#   de espaco interno, e a lista 'answer' (output) pode chegar a O(n) triplas.