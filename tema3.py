#Numar de telefon

n = int(input("Introduceti numarul de telefon:"))
for i in range(n):
    a = str(input("Introduceti numarul de telefon:"))
    if(len(a) == 10):
        if(a.isnumeric()):
            if(a[0] == "0" or a[0] == "7" or a[0] == "+"):
                print("Numarul introdus este valid")
            else:
                print("Numarul introdus nu este valid")
        else:
            print("Numarul introdus nu este valid")
    else:
        print("Numarul introdus nu este valid")
    break