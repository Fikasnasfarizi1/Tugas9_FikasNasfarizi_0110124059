print('##nomer1##')
def celcius_ke_fahrenheit(celcius):
    fahrenheit=(celcius*9/5)+32
    return fahrenheit

suhu_celcius1 = 0
suhu_celcius2 = 100
suhu_fahrenheit1 = celcius_ke_fahrenheit(suhu_celcius1)
suhu_fahrenheit2 = celcius_ke_fahrenheit(suhu_celcius2)
print('suhu celcius', suhu_celcius1, 'sama dengan', suhu_fahrenheit1)
print('suhu celcius', suhu_celcius2, 'sama dengan', suhu_fahrenheit2)
    