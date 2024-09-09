code =(input("digite o código de conversão"))
if code == "c":
    celsius = int(input("temperatura em graus celcius:"))
    f = ((9 / 5) * celsius) + 32 
    print("Conversão - Temperatura em graus Farenheit=", f)
elif code == "f":
    farenheit = int(input("temperatura em farenheit:"))
    c = (farenheit - 32) / (9 / 5)
    print("Conversão - Temperatura em garus Celsius=", c)
else:
    print("código inválido! por favor digite c ou f.")