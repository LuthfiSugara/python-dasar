import json

makan = { 'pagi': "Bubur", 'siang': "Ayam Goreng", 'malam' : "Mie Ayam" }
harga = { 'nasi' : 3000 , 'ayam' : 5000, 'rujak' : 2000 }

print(makan['pagi'])
print(harga['nasi'])

harga['nasi'] = 1000
print(harga)

harga['es'] = 2000
print(harga)

harga.update({'jeruk': 2000, 'semangka': 4000})
print(harga)

del harga['nasi']
print(harga)

# Nested dictionary having same keys
Dict = {'Dict1': [{'name': 'Ali', 'age': '19'},
                {'name': 'Budi', 'age': '12'}],
        'Dict2': {'name': 'Bob', 'age': '25'}}

# Prints value corresponding to key 'name' in Dict1
print(Dict['Dict1'][1]['name'])

# Prints value corresponding to key 'age' in Dict2
print(Dict['Dict2']['age'])

