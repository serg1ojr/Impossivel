# Impossivel
from time import sleep
print(' '*15,'Calculo ST', ' '*15)
print(' '*30)
prod = float(input('Valor do produto: R$ '))
bicms = float(input('Base ICMS: '))
print('CALCULANDO....')
sleep(1)
icms = (prod/100)*bicms
print('Valor ICMS: R$ {:.2f}'.format(icms))
sleep(1)
ipi = (prod/100)*10
print('Valor do IPI: R$ {:.2f}'.format(ipi))
sleep(1)
print('Valor do Produto + IPI: R$ {:.2f}'.format(prod + ipi))
sleep(1)
iva = (prod + ipi) * 1.343
print('VC DO IVA: R$ {:.2f}'.format(iva))
sleep(1)
basest = prod + ipi + iva
print('BC ST: R$ {:.2f}'.format(basest))
sleep(1)
icmsst = ((basest/100)*bicms) - icms
print('Valor ICMS ST: R$ {:.2f}'.format(icmsst))
sleep(1)
print('=-=-'*15)
