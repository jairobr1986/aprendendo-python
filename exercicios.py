#jairobr1986@gmail.com
def conversor(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
while True:
    celsius = float(input("Digite a temperatura em graus Celsius: "))
    fahrenheit = conversor(celsius)
    print("Agora faz: %.2f graus Celsius, ou %.2f graus Fahrenheit" % (celsius, fahrenheit))
    meuloop = input("Deseja continuar? (s/n) ")
    if continuar.lower() == 'n':
    break