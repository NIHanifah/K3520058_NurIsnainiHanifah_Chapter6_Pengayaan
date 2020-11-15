#Menghitung bilangan pangkat dalam suatu range
def sqNumber(a, b):
    for i in range (a, b):
        i = i ** 2
        if i in range (10, 50):
            print(i)
sqNumber(1, 10)