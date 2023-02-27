fat_estadual = [{'estado': 'SP',
                'faturamento': 67836.43},
                {'estado': 'RJ',
                'faturamento':36678.66},
                {'estado': 'MG',
                'faturamento':29229.88},
                {'estado': 'ES',
                'faturamento':27165.48},
                {'estado': 'Outros',
                'faturamento':19849.53}]

soma = 0 
for i in fat_estadual:
    soma += i["faturamento"]

for i in fat_estadual:
    pocentagem_estadual = (i["faturamento"] *100) / soma
    print(f'A representação de {i["estado"]} equivale a {pocentagem_estadual:.2f}% ')
