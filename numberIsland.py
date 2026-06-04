from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])  

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)

        numberIsland = 0 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    numberIsland += 1  
                    dfs(i, j)
        return numberIsland


# ============================================================================
# 1) COMO SERIA O BRUTE FORCE (FORÇA BRUTA)
# ============================================================================
#
# A ideia "ingênua" de força bruta seria, para CADA célula de terra, descobrir
# a qual ilha ela pertence sem "afundar" o terreno. Uma forma comum é usar um
# conjunto 'visited' e, para cada célula '1' ainda não visitada, fazer uma
# busca (BFS/DFS) que marca o grupo. Mas a versão *realmente* força bruta é
# tentar comparar/agrupar células repetidamente, por exemplo:
#
# def numIslands_bruteforce(grid):
#     if not grid:
#         return 0
#     m, n = len(grid), len(grid[0])
#     # cada célula de terra começa como sua própria "ilha" (id único)
#     ids = {}
#     next_id = 0
#     for i in range(m):
#         for j in range(n):
#             if grid[i][j] == '1':
#                 ids[(i, j)] = next_id
#                 next_id += 1
#
#     # repetidamente varremos a grade inteira juntando vizinhos que tenham
#     # ids diferentes, até nada mais mudar (ponto fixo).
#     changed = True
#     while changed:
#         changed = False
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] != '1':
#                     continue
#                 for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
#                     ni, nj = i + di, j + dj
#                     if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
#                         # se o vizinho tem id menor, copiamos -> propaga o menor id
#                         if ids[(ni, nj)] < ids[(i, j)]:
#                             ids[(i, j)] = ids[(ni, nj)]
#                             changed = True
#     # o número de ilhas é a quantidade de ids distintos que sobraram
#     return len(set(ids.values()))
#
# ============================================================================
# 2) POR QUE O BRUTE FORCE É RUIM + COMPLEXIDADE
# ============================================================================
#
# - Ele NÃO visita cada célula uma única vez. Ele varre a grade inteira
#   várias vezes ("while changed") até os ids pararem de mudar. No pior caso,
#   a informação do menor id precisa "atravessar" toda a ilha célula por célula,
#   e cada passada propaga o id apenas para os vizinhos imediatos.
# - Isso gera trabalho redundante enorme: reprocessamos células que já
#   estavam corretas só para confirmar que nada mudou.
#
# Complexidade de TEMPO: O((m*n)^2) no pior caso.
#   -> Cada varredura completa custa O(m*n) e podemos precisar de até O(m*n)
#      varreduras para um id se propagar por uma ilha bem comprida (em forma
#      de "cobra"/espiral). Multiplicando, chega a O((m*n)^2). Muito lento.
#
# Complexidade de ESPAÇO: O(m*n).
#   -> O dicionário 'ids' guarda um id para cada célula de terra.
#
# Resumo: a força bruta desperdiça tempo refazendo o mesmo trabalho. A solução
# com DFS resolve isso visitando cada célula NO MÁXIMO uma vez.
#
# ============================================================================
# 3) EXPLICAÇÃO PASSO A PASSO DA SOLUÇÃO (class Solution) + COMPLEXIDADE
# ============================================================================
#
# if not grid: return 0
#   -> Trata o caso de grade vazia para não dar erro no len(grid[0]).
#
# m, n = len(grid), len(grid[0])
#   -> Guarda dimensões: m linhas e n colunas. Usadas para checar limites.
#
# def dfs(i, j):
#   -> Função recursiva que, a partir de uma célula de terra, visita TODA a
#      ilha conectada a ela.
#
#   if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1': return
#     -> Condição de parada. Para a recursão se:
#        * saiu da grade (índices inválidos), ou
#        * a célula é água ('0') ou já foi visitada (também vira '0').
#
#   grid[i][j] = '0'
#     -> Marca a célula como visitada "afundando" a terra. Evita loops
#        infinitos e revisita. (Faz o papel de um conjunto 'visited', mas
#        modificando a própria grade -> O(1) de espaço extra por marca.)
#
#   dfs(i, j+1); dfs(i, j-1); dfs(i+1, j); dfs(i-1, j)
#     -> Expande para os 4 vizinhos (direita, esquerda, baixo, cima),
#        cobrindo toda a região de terra conectada.
#
# numberIsland = 0
#   -> Contador de ilhas.
#
# for i in range(m): for j in range(n):
#   -> Percorre cada célula exatamente uma vez no laço principal.
#
#   if grid[i][j] == '1':
#       numberIsland += 1
#       dfs(i, j)
#     -> Achou terra ainda não visitada = começo de uma NOVA ilha.
#        Soma 1 no contador e chama o DFS para afundar a ilha inteira,
#        garantindo que ela não seja contada de novo.
#
# return numberIsland
#   -> Devolve o total de ilhas encontradas.
#
# Complexidade de TEMPO: O(m*n).
#   -> Cada célula é visitada no máximo uma vez pelo laço e no máximo uma vez
#      pelo DFS (depois vira '0' e é ignorada). Trabalho linear no tamanho da
#      grade.
#
# Complexidade de ESPAÇO: O(m*n) no pior caso.
#   -> Não usamos estrutura 'visited' extra (marcamos na própria grade), mas a
#      RECURSÃO usa a pilha de chamadas. Se a grade inteira for terra, o DFS
#      pode empilhar até m*n chamadas. (Se não pudermos modificar a grade,
#      precisaríamos de O(m*n) extra para o 'visited' de qualquer forma.)
#
# ============================================================================
# 4) PERGUNTAS A FAZER NA ENTREVISTA (Software Engineer Intern - Google)
# ============================================================================
#
# Antes de codar, demonstre que você esclarece o problema:
#
# - Entrada/formato: a grade é de strings '0'/'1' ou de inteiros 0/1?
# - A grade pode estar vazia ou ser None? E linhas de tamanhos diferentes?
# - O que conta como "conectado"? Apenas 4 direções (cima/baixo/esq/dir) ou
#   também as diagonais (8 direções)?
# - Posso MODIFICAR a grade de entrada (afundar as ilhas), ou ela precisa
#   permanecer intacta? (Isso muda a estratégia de 'visited' e o espaço.)
# - Qual o tamanho máximo da grade? (Importa para riservar profundidade da
#   recursão / risco de stack overflow -> talvez usar BFS iterativo.)
# - Pode haver caracteres diferentes de '0' e '1'?
# - O que devo retornar para uma grade vazia? (0, presumo.)
# - Há restrições de memória/tempo? (Define se DFS recursivo serve ou se
#   preciso de BFS com fila para evitar estouro de pilha.)
