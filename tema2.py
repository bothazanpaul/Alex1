#2.	Creati un program in care utilizatorul sa introduca o adresa de email de formatul litere_sau_cifre@litere_sau_cifre.litere.
#Validati acest sir de caractere si informati utilizatorul de raspuns.
#@ sau .(punct) trebuie sa exista o singura data in sirul de caractere



import re

fromAddress = 'numeresilitere@numeresilitere.com'

rex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'

inputAddress = input('Introduceti o adresa de email pentru a fi verificata:')
addressToVerify = str(inputAddress)

match = re.match(rex, addressToVerify)
if match == None:
	print('Adresa de email nevalida!')
	raise ValueError('Incearca din nou!')
else:
	print('Adresa de email valida!')