#1.	Scrieti un program ce va numara cate caractere are un sir de caractere dat de utilizator.
# Aceasta numarare sa se realizeze cu ajutorul unui for fara a utiliza len().
# La final afisati rezultatul.



string = input("Introduceti o fraza sau un sir de numere: ")
count1 = 0
count2 = 0
for i in string:
    if(i.isdigit()):
        count1 = count1+1
    count2 = count2+1
print("Numarul de cifre sunt:")
print(count1)
print("Numarul de caractere sunt:")
print(count2)
