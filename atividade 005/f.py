#Faça um programa que imprima os números primos entre 0 e 100.


for i in range(2, 101):
    divisor = 0
    for c in range(1, i + 1):
        if i % c == 0:
          
            divisor += 1
                                     
    if divisor == 2:          
        print(f'o numero {c} é um numero primo')