# Sorteador simples
#Uso da biblioteca `random` para selecionar itens aleatoriamente

import random

def sorteador():
    participantes = ["Alice", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda"]
    print("Lista de participantes:")
    for i, participante in enumerate(participantes, start=1):
        print(f"{i}. {participante}")
    
    vencedor = random.choice(participantes)
    print(f"\nO vencedor é: {vencedor}")

sorteador()