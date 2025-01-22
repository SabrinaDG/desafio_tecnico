#Questao3

lancamentoDeFaturamento = [
    {"dia": 1, "faturamento": 400},
    {"dia": 2, "faturamento": 0 },
    {"dia": 3, "faturamento": 650},
    {"dia": 4, "faturamento": 120},
    {"dia": 5, "faturamento": 300},
]

faturamentos = []
for item in lancamentoDeFaturamento:
    if item['faturamento'] > 0:
        faturamentos.append(item['faturamento'])

menorFaturamento = faturamentos[0]
maiorFaturamento = faturamentos[0]
for item in faturamentos:
    if item < menorFaturamento:
        menorFaturamento = item
    if item > maiorFaturamento:
        maiorFaturamento = item

somaTotalDeFaturamento = 0
for item in faturamentos:
    somaTotalDeFaturamento += item

totalDeFaturamento = len(faturamentos)
mediaDoFaturamento = somaTotalDeFaturamento / totalDeFaturamento

diasAcimaMedia = 0
for f in faturamentos:
    if f > mediaDoFaturamento:
        diasAcimaMedia += 1

print(f"O menor faturamento é: {menorFaturamento}")
print(f"O maior faturamento é: {maiorFaturamento}")
print(f"Os dias com faturamento acima da média: {diasAcimaMedia}")
