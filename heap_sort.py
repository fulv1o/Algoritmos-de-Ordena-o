"""
Algoritmo de ordenação heapsort
"""

import random
import time

# variável global para contar o número de comparações
comp = 0


# ----------------------------------------------------------------------------------------------------------------------
# 'heapfy' converte uma árvore binária em uma estrutura do tipo heap
# n é o tamanho do heap
def heapfy(vetor, heap_tam, i):
    global comp
    maior = i  # Inicializa a maior raiz
    l = 2 * i + 1  # esquerda
    r = 2 * i + 2  # direita

    # Verifica se existe um descendente a esquerda da raiz e se é maior do que a raiz
    if l < heap_tam and vetor[i] < vetor[l]:
        maior = l
        comp+=1

    # Verifica se existe um descendente a direita da raiz e se é maior do que a raiz
    if r < heap_tam and vetor[maior] < vetor[r]:
        maior = r
        comp+=1

    # Troca a raiz se for necessário
    if maior != i:
        vetor[i], vetor[maior] = vetor[maior], vetor[i]  # Executa a troca

        # Converte a raiz
        heapfy(vetor, heap_tam, maior)
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
def heap_sort(vetor):
    tam_heap = len(vetor)
    # Constrói o heap máximo
    for i in range(tam_heap, -1, -1):
        heapfy(vetor, tam_heap, i)

    # Extrai os elementos um por um
    for i in range(tam_heap - 1, 0, -1):
        vetor[i], vetor[0] = vetor[0], vetor[i]  # swap
        heapfy(vetor, i, 0)
# ----------------------------------------------------------------------------------------------------------------------


# main------------------------------------------------------------------------------------------------------------------
# Implementação da lista a ser utilizada para a ordenação
vetor = list(range(0, 1000))
random.shuffle(vetor)

print('O vetor desordenado é: ', end='')
print(vetor)

tI = time.time()
heap_sort(vetor)
tF = time.time()

tempo = (tF-tI)*1000

print(f'O vetor ordenado é: ', end='')
print(vetor)
print(f'O número de comparações é: {comp}')
print(f'O tempo total foi: {round(tempo, 2)} ms')