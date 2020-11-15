#Konversi Desimal ke Biner dalam Bentuk String
def dec2Bin(n):
    print(bin(n))
dec2Bin(10)

#Konversi Desimal ke Biner
def dec2Bin2(a):
    b = ''
    while a > 0:
        if a % 2 == 0:
            b = '0' + b
        else:
            b = '1' + b
        a = a / 2 - ((a % 2) / 2)
    print(b)
dec2Bin2(10)