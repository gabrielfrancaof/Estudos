#Escreva um programa em python que obtenha uma temperatura em graus Celsius. calcule e mostre a respectiva temperatura nas escalas Fahrenheit e Kelvin

celsius = float(input("Digite o valor em °C que deja converter: "))
fahrenheit = celsius*1.8 + 32
kelvin = celsius + 273.15

print("A temperatura de ",celsius,"°C em fahrenheit é: ", fahrenheit, "°F", "e em Kelvin é: ", kelvin, "K")


