import numpy as np 
import math

def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0


#Entrada
input = 0

#Saida desejada
output_desire = 0

#Peso inicial
input_weight = 0.5

#Texa que define a velocidade com que a ia aprende
learning_rate = 0.1

#Deifine 
error = math.inf


iteration = 0

#Neuronio artifical criado para corrigir os erros em que a soma se tona igual a zero
bias = 1
bias_weight = 0.5

while not error == 0:

    iteration += 1 

    #Função que soma todos os neuronios 
    sum = (input * input_weight) + (bias * bias_weight)

    output = activation(sum)

    error = output_desire - output
    print(f"iteration = {iteration}")
    print(f"Peso = {input_weight}")
    print(f"Entrada = {input} desejado = {output_desire}")
    print(f"Saida = {output}")
    print(f"Erro = {error}")
   

    if not error == 0:
        input_weight = input_weight + (learning_rate * input * error)
        bias_weight = bias_weight + (learning_rate * bias * error)

print ("A IA aprendeu")
