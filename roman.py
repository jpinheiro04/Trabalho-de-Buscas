"""
Revisão de Python - Aula 1
Projeto: Convertendo número inteiro para Romano
"""

def int_to_roman(number: int) -> str:
    """
    Função que recebe um número inteiro e retorna sua representação em algarismos romanos.
    """
    symbols = {
        1000: "M", 900: "CM", 500: "D", 400: "CD",
        100: "C", 90: "XC", 50: "L", 40: "XL",
        10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
    }

    roman = ""

    for symbol in sorted(symbols.keys(), reverse=True):
        while number >= symbol:
            roman += symbols[symbol]
            number -= symbol  

    return roman


number = int(input("Digite um valor inteiro: "))
if number <= 0:
    print("Por favor, insira um número inteiro positivo.")
else:
    roman = int_to_roman(number)
    print(f"Representação em romano: {roman}")
