

from atividade1 import gerar_array


def bubble_sort(vetor):

    n = len(vetor)

    for i in range(n):

        for j in range(0, n-i-1):

            if vetor[j] > vetor[j+1]:

                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

 


meu_array = gerar_array()

print("Array não ordenado:")

print(meu_array)

 

bubble_sort(meu_array)

 

print("Array ordenado:")

print(meu_array)