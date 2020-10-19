import sys
print('kalkulator')
a = int(input('podaj pierwsza liczbe: '))
b = int(input('podaj druga liczbe: '))
c = int(input('wybierz rodzaj dzialania: 1- dodawanie, 2- odejmowanie, 3- mnozenie, 4- dzielenie, 5- potegowanie: '))
if (c == 1):
    wynik = a+b
elif  (c == 2):
    wynik = a-b
elif (c ==3):
    wynik = a*b
elif (c ==5):
    wynik = a**b
elif (c ==4):
        if(b != 0):
            wynik = a/b
        else:
            print('nie wolno dzielic przez zero')
            sys.exit()
else:
        print(' zly wybor')

print('wynik dzialania to: ', wynik)
              
