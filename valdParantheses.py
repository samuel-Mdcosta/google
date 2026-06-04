class Solution:
    def validParentheses(self, s: str) -> bool:
        hashmap = {')': '(', ']': '[', '}': '{'}
        stk = []

        for c in s:
            if c not in hashmap:        # c eh um parentese de ABERTURA "( [ {"
                stk.append(c)           # empilha a abertura
            else:                       # c eh um parentese de FECHAMENTO ") ] }"
                if not stk:             # nao ha nada aberto para fechar -> invalido
                    return False
                popped = stk.pop()      # pega a ultima abertura empilhada
                if popped != hashmap[c]:  # ela precisa "casar" com o fechamento atual
                    return False
        return not stk                  # valido apenas se nao sobrou abertura sem fechar

# =============================================================================
# 1) BRUTE FORCE (forca bruta)
# =============================================================================
#
# Ideia: enquanto existir um par valido GRUDADO ("()" , "[]" ou "{}"),
# remove esse par da string repetidamente. Se no final a string ficar
# vazia, os parenteses eram validos.
#
# def validParenthesesBruteForce(s: str) -> bool:
#     while "()" in s or "[]" in s or "{}" in s:
#         s = s.replace("()", "")
#         s = s.replace("[]", "")
#         s = s.replace("{}", "")
#     return s == ""
#
# Exemplo: "([])"
#   "([])" -> remove "[]" -> "()" -> remove "()" -> ""  -> True
#
# =============================================================================
# 2) POR QUE O BRUTE FORCE E RUIM + COMPLEXIDADE
# =============================================================================
#
# - A cada passada do while a gente percorre a string inteira procurando
#   pares e criando uma NOVA string com replace (string em Python e imutavel,
#   entao cada replace gera uma copia O(n)).
# - No pior caso (ex: "(((...)))" com n/2 aberturas) cada volta remove apenas
#   UM par, ou seja precisamos de ~n/2 voltas, e cada volta custa O(n).
#
#   Complexidade de TEMPO:  O(n^2)
#   Complexidade de ESPACO: O(n)   (cada replace cria uma copia da string)
#
# - Resumo: e ruim porque refaz trabalho repetido (re-escaneia tudo a cada
#   volta) e gasta memoria criando varias copias da string. Nao escala.
#
# =============================================================================
# 3) EXPLICACAO DA CLASS SOLUTION (linha a linha)
# =============================================================================
#
# A estrategia certa e usar uma PILHA (stack), pois o ultimo parentese aberto
# precisa ser o primeiro a ser fechado (comportamento LIFO).
#
#   hashmap = {')': '(', ']': '[', '}': '{'}
#       -> mapa que liga cada FECHAMENTO a sua ABERTURA correspondente.
#          Serve para: (a) saber se um char e fechamento (esta no dict?) e
#          (b) descobrir qual abertura ele exige.
#
#   stk = []
#       -> nossa pilha; guarda as aberturas que ainda nao foram fechadas.
#
#   for c in s:
#       -> percorre cada caractere da string uma unica vez.
#
#   if c not in hashmap:
#       -> se c NAO e uma chave do dict, entao c e uma ABERTURA "( [ {".
#
#   stk.append(c)
#       -> empilha essa abertura para fecha-la depois.
#
#   else:  (c e um FECHAMENTO)
#       if not stk:
#           return False
#           -> chegou um fechamento mas a pilha esta vazia: nao ha abertura
#              correspondente -> string invalida.
#
#       popped = stk.pop()
#           -> remove e pega a ULTIMA abertura empilhada (a mais recente).
#
#       if popped != hashmap[c]:
#           return False
#           -> hashmap[c] e a abertura QUE o fechamento c exige. Se a abertura
#              do topo nao bate com ela (ex: abriu "(" e tentou fechar "]"),
#              a ordem esta errada -> invalido.
#
#   return not stk
#       -> terminou de ler tudo. Se a pilha esta VAZIA, todas as aberturas
#          foram fechadas corretamente -> True. Se sobrou algo -> False.
#
# Complexidade de TEMPO:  O(n)  -> passa uma vez por cada caractere; append,
#                                  pop e busca no dict sao O(1).
# Complexidade de ESPACO: O(n)  -> no pior caso (so aberturas "(((((")
#                                  a pilha guarda todos os n caracteres.
#
# =============================================================================
# 4) PERGUNTAS A FAZER ANTES DE CODAR (entrevista Google SWE Intern)
# =============================================================================
#
# Sobre a ENTRADA:
#   - A string pode conter outros caracteres alem de () [] {} (ex: letras,
#     numeros, espacos)? Se sim, eu ignoro ou considero invalido?
#   - A string pode ser vazia? Nesse caso retorno True ou False?
#     (Convencao comum: string vazia = valida = True.)
#   - Qual o tamanho maximo de n? (Ajuda a julgar se O(n^2) seria aceitavel.)
#   - A entrada pode ser None/null?
#
# Sobre o PROBLEMA / DEFINICAO de "valido":
#   - Quais tipos de parenteses preciso suportar? Apenas ()[]{}?
#   - "Valido" significa: todo aberto tem um fechado do mesmo tipo E na ordem
#     correta (aninhamento correto), certo?
#
# Sobre a SAIDA:
#   - Preciso retornar so um booleano (True/False), ou a posicao do erro?
#
# Sobre RESTRICOES / DESEMPENHO:
#   - Existe restricao de memoria? (Posso usar uma pilha auxiliar O(n)?)
#   - Preciso me preocupar com performance para entradas muito grandes?
#
# Casos de borda para confirmar:
#   - ""        -> True
#   - "("       -> False (sobra abertura)
#   - ")"       -> False (fecha sem abrir)
#   - "(]"      -> False (tipo errado)
#   - "([])"    -> True
#   - "([)]"    -> False (ordem de aninhamento errada)
# =============================================================================
