from testes.fat_diario import *

c = 0
for i in fat_diario:
    if c == 0:
        fat_menor = i['valor']
        fat_maior = i['valor']
    else:
        if fat_menor > i['valor'] and i['valor'] != 0:
            fat_menor = i['valor']
            dia_fat_minimo = i['dia']
        elif fat_maior < i['valor']:
            fat_maior = i['valor']
            dia_fat_maximo = i['dia']
    c += 1

    

soma = 0 
dias = 0
for i in fat_diario:
    if i["valor"] != 0:
        soma += i["valor"]
        dias += 1
media = soma / dias

dias_acima_da_media = 0
for i in fat_diario:
    if i["valor"] > media:
        dias_acima_da_media += 1


print(f'O menor faturamento foi R${fat_menor:.2f}, no dia {dia_fat_minimo}')
print(f'O maior faturamento foi R${fat_maior:.2f}, no dia {dia_fat_maximo}')
print(f'Em {dias_acima_da_media} dias a media de faturamento(R${media:.2f}), foi superada')