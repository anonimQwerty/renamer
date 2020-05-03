import os


inp=input('Входное разширение изменяемых файлов: ')

exp=input('Исходное разширение изменяемых файлов: ')

dir=os.listdir()
for i in dir:
	name_i=i.replace(inp, exp)
#	new_name =name_i+'.py'
	if inp in i:
		os.rename(i, name_i)
print(os.listdir())
	