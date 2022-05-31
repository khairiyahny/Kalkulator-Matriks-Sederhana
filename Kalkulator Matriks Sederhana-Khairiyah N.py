import numpy as n

print("1. Penjumlahan 2 Matriks\n2. Pengurangan 2 Matriks\n3. Perkalian 2 matriks\n4. Transpose\n5. Determinan\n6. Invers\n7. SPL")
m = int(input("Operasi yang ingin dilakukan (tulis angka) = "))

if m==1:
    p = int(input("Masukkan jumlah baris : "))
    q = int(input("Masukkan jumlah kolom : "))
    x1 = (p,q)
    y1 = n.ones(x1)
    x2 = (p,q)
    y2 = n.ones(x2)
    print("Masukkan elemen matriks pertama : ")
    for a in range(p):
        for b in range(q):
            y1[a][b]=float(input("["+str(a+1)+"]["+str(b+1)+"] = "))
    print("Masukkan elemen matriks kedua : ")
    for c in range(p):
        for d in range(q):
            y2[c][d]=float(input("["+str(c+1)+"]["+str(d+1)+"] = ")) 
    print("RESULT")
    print("Matriks pertama : \n"+ str(y1))
    print("Matriks kedua : \n"+ str(y2))
    z = y1+y2
    print("Hasil penjumlahan : \n"+ str(z))

elif m==2:
    p = int(input("Masukkan jumlah baris : "))
    q = int(input("Masukkan jumlah kolom : "))
    x1 = (p,q)
    y1 = n.ones(x1)
    x2 = (p,q)
    y2 = n.ones(x2)
    print("Masukkan elemen matriks pertama : ")
    for a in range(p):
        for b in range(q):
            y1[a][b]=float(input("["+str(a+1)+"]["+str(b+1)+"] = "))
    print("Masukkan elemen matriks kedua : ")
    for c in range(p):
        for d in range(q):
            y2[c][d]=float(input("["+str(c+1)+"]["+str(d+1)+"] = ")) 
    print("RESULT")
    print("Matriks pertama : \n"+ str(y1))
    print("Matriks kedua : \n"+ str(y2))
    z = y1-y2
    print("Hasil pengurangan : \n"+ str(z))

elif m==3:
    print("Untuk matriks pertama")
    p = int(input("Masukkan jumlah baris : "))
    q = int(input("Masukkan jumlah kolom : "))
    x1 = (p,q)
    y1 = n.ones(x1)
    print("Masukkan elemen matriks pertama : ")
    for a in range(p):
        for b in range(q):
            y1[a][b]=float(input("["+str(a+1)+"]["+str(b+1)+"] = "))
    print("Untuk matriks kedua")
    r = int(input("Masukkan jumlah baris : "))
    s = int(input("Masukkan jumlah kolom : "))
    x2 = (r,s)
    y2 = n.ones(x2)
    print("Masukkan elemen matriks kedua : ")
    for c in range(r):
        for d in range(s):
            y2[c][d]=float(input("["+str(c+1)+"]["+str(d+1)+"] = ")) 
    print("RESULT")
    print("Matriks pertama : \n"+ str(y1))
    print("Matriks kedua : \n"+ str(y2))
    z = n.dot(y1,y2)
    print("Hasil perkalian : \n"+ str(z))

elif m==4:
    p = int(input("Masukkan jumlah baris : "))
    q = int(input("Masukkan jumlah kolom : "))
    x = (p,q)
    y = n.ones(x)
    print("Masukkan elemen matriks : ")
    for a in range(p):
        for b in range(q):
            y[a][b]=float(input("["+str(a+1)+"]["+str(b+1)+"] = "))
    z = n.transpose(y)
    print("Matriks input : \n"+ str(y))
    print("Hasil transpose : \n"+ str(z))

elif m==5:
    p = int(input("Masukkan jumlah baris : "))
    q = int(input("Masukkan jumlah kolom : "))
    x = (p,q)
    y = n.ones(x)
    print("Masukkan elemen matriks : ")
    for a in range(p):
        for b in range(q):
            y[a][b]=float(input("["+str(a+1)+"]["+str(b+1)+"] = "))
    z = int(n.linalg.det(y))
    print("Matriks input : \n"+ str(y))
    print("Determinan : \n"+ str(z))

elif m==6:
    p = int(input("Masukkan jumlah baris : "))
    q = int(input("Masukkan jumlah kolom : "))
    x = (p,q)
    y = n.ones(x)
    print("Masukkan elemen matriks : ")
    for a in range(p):
        for b in range(q):
            y[a][b]=float(input("["+str(a+1)+"]["+str(b+1)+"] = "))
    z = n.linalg.inv(y)
    print("Matriks input : \n"+ str(y))
    print("Invers : \n"+ str(z))

elif m==7:
    print("Matriks koefisien")
    p = int(input("Masukkan jumlah baris pada matriks koefisien : "))
    q = int(input("Masukkan jumlah kolom pada matriks koefisien : "))
    x1 = (p,q)
    y1 = n.ones(x1)
    print("Masukkan elemen matriks koefisien : ")
    for a in range(p):
        for b in range(q):
            y1[a][b]=float(input("["+str(a+1)+"]["+str(b+1)+"] = "))
    print("Matriks konstanta")
    x2 = (p,1)
    y2 = n.ones(x2)
    print("Masukkan elemen matriks konstanta : ")
    for c in range(p):
        for d in range(1):
            y2[c][d]=float(input("["+str(c+1)+"]["+str(d+1)+"] = ")) 
    z = n.linalg.solve(y1,y2)
    print("RESULT\n"+ str(z))

else:
    print("ERROR\n Masukkan pilihan yang tersedia!")

input("\n\n\n\n\nTerimakasiihhhhhh")