import os

disk=input("Введите  путь, который вы хотите отскранировать: ")

folder=[]

for i in os.walk(disk):
    folder.append(i)

files=[]
sum=0
for address, dirs, files in folder:
    for file in files:
        sum+=os.path.getsize(address+'\\'+file)

print(sum,'- Б')
print(sum/1024,'- КБ')
print(sum/1024/1024,'- МБ')
print(sum/1024/1024/1024,'- ГБ')
print(sum/1024/1024/1024/1024,'- ТБ')






















# import os
#
# disk=input("Введите диск, который вы хотите отскранировать: ")
#
# print(os.listdir(disk))
# os.chdir(disk)
# print(os.getcwd())
#
# def get_folder_size(path,size=0):
#     print(os.listdir(path))
#
#     os.chdir(path)
#     for i in os.listdir(path):
#
#         cur_path=os.path.abspath(i)
#         print(cur_path)
#         if os.path.isfile(cur_path):
#             size+=os.path.getsize(cur_path)
#             print(size)
#         else:
#             previous_path = path
#             os.chdir(path)
#             size+=get_folder_size(cur_path)
#
#     return size
#
#
#
#
#
#
#
# get_folder_size(os.path.realpath(disk))







































