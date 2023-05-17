azbuka = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
step = 3
message = input("Введите сообщение для зашифровки: ").upper()
result = ''

for i in message:
    mes = azbuka.find(i)
    new_mes = mes + step
    if i in azbuka:
        result += azbuka[new_mes]
    else:
        result += i
print (result)