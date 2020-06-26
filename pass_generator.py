import random
numbers='1 2 3 4 5 6 7 8 9 9'.split(' ')
letters='q w e r t y u i o p a s d f g h j k l z x c v b n m'.split(' ')
letters+='q w e r t y u i o p a s d f g h j k l z x c v b n m'.upper().split(' ')
signs='! @ # $ % ^ & * + = - _'.split(" ")

final_list=[]
check_letters=input("Нужны ли буквы в вашем пароле?(y/n) ")
check_numbers=input("Нужны ли цифры в вашем пароле?(y/n) ")
check_signs=input("Нужны ли символы в вашем пароле?(y/n) ")
length=int(input("Введите длину пароля: "))
if check_letters=='y':
    final_list+=letters
if check_numbers=='y':
    final_list+=numbers
if check_signs=='y':
    final_list+=signs

password=[]
for i in range(length):
    password+=random.choice(final_list)
password=''.join(password)
print("Ваш пароль: ", password)