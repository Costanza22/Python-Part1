def converter_massa_lunar(massa_terrestre):
    if massa_terrestre < 0:
        raise ValueError("A massa terrestre não pode ser negativa")
    return massa_terrestre / 6

def converter_distancia_marte(metros):
    if metros < 0:
        raise ValueError("A distância em metros não pode ser negativa")
    gravidade_terra = 9.81
    gravidade_marte = 3.71
    return (gravidade_terra / gravidade_marte) * metros


massa_lunar = converter_massa_lunar(12)
print("Massa em lunar:", massa_lunar)

distancia_marte = converter_distancia_marte(100)
print("Distância em Marte:", distancia_marte)


assert converter_massa_lunar(12) == 2.0

tolerancia = 0.01

valor_calculado = converter_distancia_marte(100)
valor_esperado = 268.69
tolerancia = 0.01 

if abs(valor_calculado - valor_esperado) <= tolerancia:
    print("Teste bem-sucedido")
else:
    print("Teste falhou")

