from function import addition, division, multiplication, subtraction, squared #importer från funcion

while True:
    print("Välkommen till miniräknaren!")
    print("Tillgängliga operatörer:")
    print("1: Addition")
    print("2: Subtraktion")
    print("3: Multiplikation")
    print("4: Division")
    print("5: Upphöjmed")
    print("KLicka på X för att avsluta")

    choice = input("Skriv in operatören: ")
    if choice == 'x' or choice == 'X':
        break
#Nedan sparas de nummer i variabler
num1 = float(input("Skriv in det första numret")) 
num2 = float(input("Skriv in det andra numret"))

if choice == '1':
    addition(num1, num2) 
elif choice == '2':
    subtraction(num1,num2)
elif choice == '3':
    multiplication(num1, num2)
elif choice == '4':
    division(num1, num2)
elif choice == '5':
    squared(num1, num2)
else:
    print("Oidentfierat val")

print("\n")
