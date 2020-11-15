#Mengubah Biner ke Desimal
def bin2Dec(a):
    i = 0
    Desimal = 0
    pangkat = len(a) - 1
    for i in range (len(a)):
        b = int(a[i]) * (2 ** pangkat)
        Desimal += b
        i += 1
        pangkat -= 1
    print(Desimal)
a = input('Nilai biner =')
bin2Dec(a)