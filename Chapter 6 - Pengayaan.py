#Menentukan bilangan prima
def isPrime(x):
    i  = x - 1
    while i > 1:
        print(i, 'Membagi habis 8?', end='')
        if x % i != 0:
            a = False
            print(a)
        elif x % i == 0:
            a = True
            print(a)
            break
        i -= 1
    #Penentuan Kesimpulan
    if a == False:
        print('Kesimpulan :', x, 'prima')
    elif a == True:
        print('Kesimpulan :', x, 'bukan prima')

isPrime(8)
