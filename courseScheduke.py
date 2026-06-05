from collections import defaultdict
from typing import List

# =========================================================================
# PROBLEMA: Course Schedule (LeetCode 207)
# Dado numCourses e uma lista de prerequisitos [a, b] (para fazer 'a'
# preciso antes fazer 'b'), retornar True se eh possivel concluir todos
# os cursos. So eh possivel se NAO existir um ciclo no grafo de dependencias.
# =========================================================================

# -------------------------------------------------------------------------
# BRUTE FORCE (forca bruta):
#
# A ideia ingenua seria, para cada curso, tentar simular TODAS as ordens
# possiveis de conclusao dos cursos (todas as permutacoes/caminhos) e
# verificar se em algum momento conseguimos respeitar todos os prerequisitos.
#
# 1) Para cada curso, seguimos suas dependencias recursivamente.
# 2) A cada passo guardamos o "caminho atual" (cursos que estamos tentando
#    concluir nesta cadeia).
# 3) Se durante a recursao voltarmos a um curso que JA esta no caminho atual,
#    encontramos um ciclo -> impossivel concluir -> retorna False.
#
# O problema do brute force puro (sem marcar nos ja resolvidos) eh que ele
# re-explora os mesmos sub-caminhos varias vezes. No pior caso isso vira
# exponencial: O(V!) / O(2^V), porque visitamos as mesmas dependencias
# repetidamente para cada ponto de partida diferente.
#
# A solucao otimizada abaixo eh exatamente esse mesmo DFS, mas adicionando
# uma marcacao de estado (visited) que evita re-explorar nos ja confirmados,
# baixando a complexidade para O(V + E).
# -------------------------------------------------------------------------


class Solution:
    def canFinish(self, numCourses: int, prerequisits: List[List[int]]) -> bool:
        g = defaultdict(list)              # cria o grafo: curso -> lista de prerequisitos
        courses = prerequisits             # apenas um alias para a lista de arestas
        for a, b in courses:               # para cada par [a, b] (a depende de b)
            g[a].append(b)                 # adiciona a aresta a -> b no grafo

        unvisited = 0                      # estado: no ainda nao foi tocado
        visiting = 1                       # estado: no esta na pilha de recursao atual
        visited = 2                        # estado: no ja foi totalmente resolvido (sem ciclo)
        states = [unvisited] * numCourses  # comeca todos os cursos como 'unvisited'

        def dfs(node):                     # DFS que retorna False se achar ciclo
            state = states[node]           # le o estado atual do no
            if state == visited:           # se ja resolvemos esse no antes...
                return True                # ...nao precisa reprocessar, sem ciclo aqui
            elif state == visiting:        # se o no JA esta no caminho atual...
                return False               # ...achamos um ciclo -> impossivel

            states[node] = visiting        # marca o no como 'em processamento' (na pilha)

            for nei in g[node]:            # percorre todos os prerequisitos do no
                if not dfs(nei):           # desce recursivamente em cada vizinho
                    return False           # se algum vizinho achou ciclo, propaga False

            states[node] = visited         # terminou sem ciclo -> marca como resolvido
            return True                    # esse no esta ok

        for i in range(numCourses):        # tenta iniciar o DFS a partir de cada curso
            if not dfs(i):                 # se qualquer DFS detectar um ciclo...
                return False               # ...nao da pra concluir todos os cursos
        return True                        # nenhum ciclo encontrado -> da pra concluir tudo
