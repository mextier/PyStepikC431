import string
print(string.ascii_letters+string.digits+string.punctuation)



while True:
    c = int(input('Введите число:'))
    if c == 777:
        print('Выхожу из бесконечности...')
        break
    print('Циркулирую от '+str(c)+' до 1:')
    while c!=0:
        print(c)
        c=c-1
    print('Закончен цикл!')
