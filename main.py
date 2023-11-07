
import pandas as pd

data = []

while True:
    name = input("Write your name please:")
    salary = input("Write your salary please:")
    age = input("Write your age please:")
    choice = input("Do you want to continue add data to your excel file? Y/N")
    data.append([name, salary, age])
    if choice == "Y" or choice == 'y':
        continue
    else:
        break


#Kolumna z danymi w excelu

zapis = pd.DataFrame(data, columns=['Imię', 'Pensja', 'Wiek'])

#Zapisanie do excela

zapis.to_excel('zapisywanie_danych_w_excelu.xlsx', index=False)
