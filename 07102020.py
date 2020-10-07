print("primul meu mesaj")
# a = input("mesaj")
a = input("mesaj")
print("a")
print("Ana are mere \n ion are pere")
print("""
\tAna are multe mere
Petre este la joaca
""")
variabila1 = 1
variabila2 = 2
variabila3 = f"Ana are {variabila1} mar si {variabila2}pere"
print(variabila3)
variabila4 = "Ana are {1}mar si {0}pere".format(variabila1, variabila2)
print(variabila4)
variabila5 = "Ana are {1} mar si {1} pere".format(variabila1, variabila2)
varaibila5 = "Ana are {1} mar si {0} pere".format(variabila1, variabila2)
print(variabila5)
variabila2 = 3
print(type(variabila4))
variabila6 = "Ana are " + str(variabila2) + " mere."
print(variabila6)
print(variabila1 + variabila2)
print(str(variabila1) + str(variabila2))

varaible_number_1 = 3 - 2j
print(varaible_number_1.real)
print(variable_number_1.imag)
