import random

def gerar_array():

    return [random.randint(-999999, 999999) for _ in range(20000)]

def testar_array(array):

    for valor in array:

        if valor < -999999 or valor > 999999:

            return False

    return True

meu_array = gerar_array()

if testar_array(meu_array):

    print("Todos os valores estão dentro do intervalo.")

else:

    print("Pelo menos um valor está fora do intervalo.")