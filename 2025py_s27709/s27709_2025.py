import random

def generuj_sekwencje_fasta():
    """Generuje losową sekwencję DNA, zapisuje ją do pliku FASTA i wyświetla statystyki."""

    try:
        dlugosc = int(input("Podaj długość sekwencji DNA: "))
        if dlugosc <= 0:
            print("Długość sekwencji musi być liczbą dodatnią.")
            return
    except ValueError:
        print("Podano nieprawidłową wartość długości.")
        return

    identyfikator = input("Podaj ID sekwencji: ")
    opis = input("Podaj opis sekwencji: ")
    imie = input("Podaj imię: ")

    nukleotydy = ['A', 'C', 'G', 'T']
    sekwencja = ''.join(random.choice(nukleotydy) for _ in range(dlugosc))

    # Wstawienie imienia w losowym miejscu
    pozycja_wstawienia = random.randint(0, len(sekwencja))
    sekwencja_zmodyfikowana = sekwencja[:pozycja_wstawienia] + imie + sekwencja[pozycja_wstawienia:]

    # Zapis do pliku FASTA
    nazwa_pliku = f"{identyfikator}.fasta"
    with open(nazwa_pliku, "w") as plik:
        plik.write(f">{identyfikator} {opis}\n")
        plik.write(sekwencja_zmodyfikowana + "\n")

    print(f"\nSekwencja została zapisana do pliku: {nazwa_pliku}")

    # Obliczenie statystyk (bez uwzględnienia wstawionego imienia i nazwiska)
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
