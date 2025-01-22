#Questao 4

def calculoPercentual(percentual, total):
    calculo  = (percentual / total) * 100
    return calculo

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros

percentualSp = calculoPercentual(sp, total)
percentualRj = calculoPercentual(rj, total)
percentualMg = calculoPercentual(mg, total)
percentualEs = calculoPercentual(es, total)
percentualOtros = calculoPercentual(outros, total)

print(f'Percentual SP: {percentualSp:.2f}')
print(f'Percentual RJ: {percentualRj:.2f}')
print(f'Percentual MG: {percentualMg:.2f}')
print(f'Percentual ES: {percentualEs:.2f}')
print(f'Percentual OUTRO: {percentualOtros:.2f}')
