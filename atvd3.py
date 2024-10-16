# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.
def calcular_area_base(raio):
    area = 3.14 * (raio**2)
    return area

#recebr o valor do raiopara os cálculos.
raioCirculo = float(input("digite o comprimento do raio da base do cilindro: "))

def calcular_volume_cilindro(altura):
    volume = calcular_area_base(raioCirculo) * altura
    return volume

# receber o valor da altura para os cálculos.
alturaCilindro = float(input("para calcular o volume do cilindro, digite a sua altura: "))

# variáveis para retornar os valores.
a = calcular_area_base(raioCirculo)
vol = calcular_volume_cilindro(alturaCilindro)

print (f"""dados o raio da base e a altura do cilindro:
       a área da base: {a:.2f}.
       o volume do cilindro: {vol:.2f}.""")
