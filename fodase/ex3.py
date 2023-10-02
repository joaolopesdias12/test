import os

path = "C:/Users/heliu/hola/"
for filename in os.listdir(path):
    my_dest = str("hola") + ".txt"
    my_source = path + filename
    my_dest = path + my_dest
    os.rename(my_source, my_dest)