# ------------------------------------------------------------------
# BRUTE FORCE (forca bruta):
#
# Para cada posicao i, percorremos toda a lista novamente com um
# segundo laco j. Multiplicamos todos os nums[j] em que j != i.
# Assim montamos o produto de "todos menos o atual" no braco.
#
#   def product_brute(self, nums):
#       n = len(nums)
#       answer = [1] * n
#       for i in range(n):            # laco externo: cada posicao
#           prod = 1
#           for j in range(n):        # laco interno: percorre tudo
#               if i != j:            # ignora o proprio elemento
#                   prod *= nums[j]
#           answer[i] = prod
#       return answer
#
# Complexidade:
#   Tempo:  O(n^2)  -> laco dentro de laco (n posicoes * n elementos)
#   Espaco: O(1)    -> so a lista de resposta exigida
#
# A versao otimizada abaixo resolve em O(n) usando prefixo e sufixo,
# sem precisar de divisao.
# ------------------------------------------------------------------
class Solution:
    def product(self, nums:List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        
        sufix = 1
        for i in range(len(nums) -1, -1, -1):
            answer[i] *= sufix
            sufix *= nums[i]
        return answer