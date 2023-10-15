# Konversi Temperatur

print('\nPROGRAM KONVERSI SUHU\n')

# Konversi celcius ke satuan lain

celcius = float(input('Masukkan suhu dalam celcius: '))
print('Suhu adalah : ',celcius,'celcius')

#Reamur
reamur = (4/5)*celcius
print('suhu adalah : ',reamur,'reamur')

#Fahrenheit
fahrenheit = ((9/5)*celcius) + 32
print('suhu adalah : ',fahrenheit,'fahrenheit')

#Kelvin
kelvin = celcius + 273
print('suhu adalah : ',kelvin,'kelvin')