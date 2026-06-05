class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


# =====================================================================
# PROBLEMA: Search in Rotated Sorted Array (LeetCode 33)
# Um array ordenado foi "rotacionado" em algum pivo desconhecido.
# Ex: [0,1,2,4,5,6,7] virou [4,5,6,7,0,1,2]. Achar o indice do target.
# =====================================================================
#
# =====================================================================
# 1) BRUTE FORCE (forca bruta) - como seria
# =====================================================================
#
# class SolutionBruteForce:
#     def search(self, nums: list[int], target: int) -> int:
#         for i in range(len(nums)):   # percorre todos os elementos
#             if nums[i] == target:    # se achar o target...
#                 return i             # ...retorna o indice
#         return -1                    # nao encontrou
#
#   -> Simplesmente varre o array inteiro do inicio ao fim procurando
#      o target, ignorando completamente o fato de que o array esta
#      (quase) ordenado.
#
# =====================================================================
# 2) PORQUE O BRUTE FORCE E RUIM + COMPLEXIDADE
# =====================================================================
#
# Por que e ruim:
#   - Ele joga fora a informacao mais importante do problema: o array
#     e ORDENADO (so que rotacionado). Quando temos ordenacao, da pra
#     usar busca binaria e cortar o espaco de busca pela metade a cada
#     passo, em vez de olhar elemento por elemento.
#   - O enunciado normalmente PEDE solucao em O(log n). O brute force
#     em O(n) seria rejeitado numa entrevista.
#
# Seja n = numero de elementos do array.
#
#   Complexidade de TEMPO:  O(n)
#       - no pior caso (target no fim ou ausente) percorre tudo.
#
#   Complexidade de ESPACO: O(1)
#       - usa so a variavel do loop, nenhuma estrutura extra.
#
# Resumo: o espaco ja e otimo, mas o TEMPO O(n) e o problema.
# Queremos O(log n) -> busca binaria adaptada para o array rotacionado.
#
# =====================================================================
# 3) EXPLICACAO PASSO A PASSO DA SOLUTION (busca binaria modificada)
# =====================================================================
#
# A ideia chave: mesmo rotacionado, se eu pego o meio (mid), pelo menos
# UMA das duas metades [l..mid] ou [mid..r] esta totalmente ordenada.
# Eu descubro qual metade esta ordenada e checo se o target cabe nela.
# Se cabe, busco nessa metade; se nao, busco na outra. Assim continuo
# cortando o array pela metade -> O(log n).
#
#   def search(self, nums: list[int], target: int) -> int:
#
#       l, r = 0, len(nums) - 1
#         -> Dois ponteiros: l no inicio e r no fim do array.
#            Eles delimitam o intervalo onde o target ainda pode estar.
#
#       while l <= r:
#         -> Enquanto o intervalo for valido (ainda ha o que buscar).
#            Quando l passa de r, o intervalo "fechou" sem achar nada.
#
#           mid = (l + r) // 2
#             -> Indice do meio do intervalo atual (divisao inteira).
#
#           if nums[mid] == target:
#               return mid
#             -> Sorte/caso direto: o meio JA e o target. Retorna o indice.
#
#           if nums[l] <= nums[mid]:
#             -> Pergunta: a metade da ESQUERDA (de l ate mid) esta
#                ordenada? Se o valor da esquerda <= valor do meio, sim,
#                essa metade nao tem o "ponto de quebra" da rotacao.
#
#               if target > nums[mid] or target < nums[l]:
#                   l = mid + 1
#                 -> A esquerda esta ordenada e vai de nums[l] ate nums[mid].
#                    Se o target NAO cabe nesse intervalo (ou e maior que
#                    o meio, ou menor que o inicio), entao ele so pode
#                    estar na DIREITA -> joga l para depois do mid.
#               else:
#                   r = mid - 1
#                 -> Caso contrario o target esta dentro da esquerda
#                    ordenada -> busca na esquerda movendo r para antes
#                    do mid.
#
#           else:
#             -> Se a esquerda NAO estava ordenada, entao a DIREITA
#                (de mid ate r) com certeza esta ordenada.
#
#               if target < nums[mid] or target > nums[r]:
#                   r = mid - 1
#                 -> A direita ordenada vai de nums[mid] ate nums[r].
#                    Se o target NAO cabe ai (menor que o meio ou maior
#                    que o fim), ele so pode estar na ESQUERDA -> move r.
#               else:
#                   l = mid + 1
#                 -> Caso contrario o target esta na direita ordenada
#                    -> busca na direita movendo l para depois do mid.
#
#       return -1
#         -> Saiu do while sem encontrar: o target nao esta no array.
#
#   Complexidade de TEMPO:  O(log n)
#       - a cada iteracao descartamos metade do intervalo de busca.
#
#   Complexidade de ESPACO: O(1)
#       - usamos apenas os ponteiros l, r e mid; nada cresce com n.
#
# =====================================================================
# 4) PERGUNTAS PARA FAZER ANTES DE CODAR (entrevista Google Intern)
# =====================================================================
#
#   Sobre a ENTRADA:
#     - O array pode estar vazio? (len == 0 -> retornar -1.)
#     - Os numeros sao todos UNICOS, ou podem ter duplicatas? Isso muda
#       muito: com duplicatas (ex: [1,1,1,0,1]) a busca binaria pode
#       cair para O(n) no pior caso (esse e o LeetCode 81).
#     - O array realmente esta ordenado-e-rotacionado, ou pode estar
#       em ordem qualquer? (A busca binaria depende dessa garantia.)
#     - Qual o range dos valores? Podem ser negativos?
#     - De quanto pode ser a rotacao? (Pode ser 0 = nao rotacionado.)
#
#   Sobre a SAIDA:
#     - Devo retornar o INDICE do target ou apenas True/False se existe?
#     - Se o target nao existir, retorno -1? E o formato esperado?
#     - Se houver duplicatas e o target aparecer varias vezes, qualquer
#       indice serve ou preciso do primeiro/ultimo?
#
#   Sobre RESTRICOES / CASOS DE BORDA:
#     - Existe exigencia de complexidade? (Normalmente exigem O(log n),
#       o que descarta o brute force O(n).)
#     - Array com 1 unico elemento; target igual ao primeiro/ultimo.
#     - Posso modificar o array de entrada? (Aqui nao precisamos.)
#
#   Exemplo para validar entendimento:
#     - nums = [4,5,6,7,0,1,2], target = 0  -> retorna 4
#     - nums = [4,5,6,7,0,1,2], target = 3  -> retorna -1
