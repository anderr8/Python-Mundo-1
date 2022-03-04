# Conversor de Medidas
# Mútiplos:
# Km = Quilômetro => 1000m -> 1 metro x 1000 = 1 quilômetro
# hm = Hectômetro => 100m  -> 1 metro x 100  = 1 hectômetro
# dam = Decâmetro => 10m   -> 1 metro x 10   = 1 decâmetro

# Submútiplos
# mm = Milímitro  => 0,001m -> 1 metro / 1000 = 1 milímetro
# cm = centímetro => 0,01m  -> 1 metro / 100  = 1 centímetro
# dm = Decímetro  => 0,1m   -> 1 metro / 10   = 1 decímetro

medida = float(input('Uma distância em metros: '))
km = medida * 1000
hm = medida * 100
dam = medida * 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a: \n{:.0f}km \n{:.0f}hm \n{:.0f}dam \n{:.0f}dm \n{:.0f}cm  \n{:.0f}mm .'.format(medida, km, hm, dam, dm, cm, mm))