import random
import os

def generuj_sekwencje_fasta():
    """Generuje losową sekwencję DNA, zapisuje ją do pliku FASTA i wyświetla statystyki."""

    #ORIGINAL
    """
    try:
        dlugosc = int(input("Podaj długość sekwencji DNA: "))
        if dlugosc <= 0:
            print("Długość sekwencji musi być liczbą dodatnią.")
            return
    except ValueError:
        print("Podano nieprawidłową wartość długości.")
        return
    """
    #MODIFIED (Błąd walidacji podanej długości kończy program, a lepiej gdyby była możliwość ponownego wprowadzenia.)
    dlugosc_poprawna = False
    while(not dlugosc_poprawna):
        try:
            dlugosc = int(input("Podaj długość sekwencji DNA: "))
            if dlugosc <= 0:
                print("Długość sekwencji musi być liczbą dodatnią.")
                continue
        except ValueError:
            print("Podano nieprawidłową wartość długości.")
            continue
        dlugosc_poprawna = True

    identyfikator = input("Podaj ID sekwencji: ")
    opis = input("Podaj opis sekwencji: ")
    imie = input("Podaj imię: ")

    nukleotydy = ['A', 'C', 'G', 'T']
    sekwencja = ''.join(random.choice(nukleotydy) for _ in range(dlugosc))

    pozycja_wstawienia = random.randint(0, len(sekwencja))
    sekwencja_zmodyfikowana = sekwencja[:pozycja_wstawienia] + imie + sekwencja[pozycja_wstawienia:]

    nazwa_pliku = f"{identyfikator}.fasta"
    
    #ORIGINAL
    #nazwa_pliku = f"{identyfikator}.fasta"
    #with open(nazwa_pliku, "w") as plik:
    #MODIFIED (Istniejący plik o identycznej nazwie zostanie nadpisany a zawartość utracona. Warto o tym ostrzec.)
    if(os.path.isfile(nazwa_pliku)):
        print(f"Plik o nazwie {nazwa_pliku} już istnieje. Czy chcesz go nadpisać? (t/n):")
        if(input() != "t"):
            return
    with open(nazwa_pliku, "w") as plik:
        plik.write(f">{identyfikator} {opis}\n")
        #ORIGINAL
        #plik.write(sekwencja_zmodyfikowana + "\n")
        #MODIFIED (W artykule Wikipedia w przykładzie FASTA linikii sekwencji dzielone są co 60 znaków, tu też warto to zaimplementować)
        indeks_sekwencji = 0
        while(indeks_sekwencji <= len(sekwencja_zmodyfikowana)):
            start_liniki = indeks_sekwencji
            indeks_sekwencji += 60
            plik.write(sekwencja_zmodyfikowana[start_liniki:indeks_sekwencji] + "\n")
    print(f"\nSekwencja została zapisana do pliku: {nazwa_pliku}")

    licznik_a = sekwencja.count('A')
    licznik_c = sekwencja.count('C')
    licznik_g = sekwencja.count('G')
    licznik_t = sekwencja.count('T')

    procent_a = (licznik_a / dlugosc) * 100
    procent_c = (licznik_c / dlugosc) * 100
    procent_g = (licznik_g / dlugosc) * 100
    procent_t = (licznik_t / dlugosc) * 100

    stosunek_cg_at = (licznik_c + licznik_g) / (licznik_a + licznik_t) if (licznik_a + licznik_t) > 0 else 0

    print("\nStatystyki sekwencji:")
    print(f"Procent A: {procent_a:.2f}%")
    print(f"Procent C: {procent_c:.2f}%")
    print(f"Procent G: {procent_g:.2f}%")
    print(f"Procent T: {procent_t:.2f}%")
    print(f"Stosunek (C+G)/(A+T): {stosunek_cg_at:.2f}")

if __name__ == "__main__":
    generuj_sekwencje_fasta()
