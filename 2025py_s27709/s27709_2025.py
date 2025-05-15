import random #importuje moduł wykorzystywany do wybierania losowych nukleotydów do sekwencji oraz pozycji wstawianego imienia
import os #importuje moduł wykorzystywany do sprawdzenia czy nie istnieje plik o takiej samej nazwie
import matplotlib.pyplot as plt #importuje moduł wykorzystywany do rysowania wykresu

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
    dlugosc_poprawna = False #zmienna przechowuje wartość/flagę poprawnego zwalidowania długości
    while(not dlugosc_poprawna): #pętla trwa aż do pomyślnego zwalidowania długości sekwencji
        try: #początek bloku try-catch, błąd spowoduje przejście do sekcji 'except'
            dlugosc = int(input("Podaj długość sekwencji DNA: ")) #pobranie wartości od użytkownika, próba sparsowania do liczby całkowitej
            if dlugosc <= 0: #sprawdzenie warunku poprawności
                print("Długość sekwencji musi być liczbą dodatnią.") #informacja dla użytkownika
                continue #przerwanie wykonywania tej iteracji pętli, powrót do począktu pętli bez wykonywania pozostałych instrukcji wewnątrz pętli
        except ValueError: #początek bloku obsługującego 'ValueError' mogącego pojawić się w wyniku wykonania int()
            print("Podano nieprawidłową wartość długości.") #informacja dla użytkownika
            continue #przerwanie obecnej iteracji pętli, przejście do kolejnej
        dlugosc_poprawna = True #brak przerwania pętli insturkcją 'continue' oznacza poprawną wartość długości

    identyfikator = input("Podaj ID sekwencji: ")  #pobranie wartości od użytkownika
    opis = input("Podaj opis sekwencji: ") #pobranie wartości od użytkownika
    imie = input("Podaj imię: ") #pobranie wartości od użytkownika

    nukleotydy = ['A', 'C', 'G', 'T'] #deklaracja listy z 4 nukleotydami mogącymi pojawić się w sekwencji DNA

    sekwencja = ''.join(random.choice(nukleotydy) for _ in range(dlugosc)) 
    #Wykonanie metody join() na pustym stringu ('') z podanym argumentem generatora wyrażeń. Generator wyrażeń wybiera losowo spośród nukleotydów 0..długość razy

    pozycja_wstawienia = random.randint(0, len(sekwencja)) #losowy wybór liczby w zakresie 0 - długość sekwencji, przypisanie wartości do zmiennej
    sekwencja_zmodyfikowana = sekwencja[:pozycja_wstawienia] + imie + sekwencja[pozycja_wstawienia:] 
#złączenie operatorem '+' części sekwencji 0..pozycja_wstawienia do wczęsniej podanego imienia oraz do części sekwencji od pozycji wstawienia do końca.

    nazwa_pliku = f"{identyfikator}.fasta" #utworzenie literału nazwy pliku .fasta z wykorzystaniem zmiennej identyfikatora
    
    #ORIGINAL
    #nazwa_pliku = f"{identyfikator}.fasta"
    #with open(nazwa_pliku, "w") as plik:
    #MODIFIED (Istniejący plik o identycznej nazwie zostanie nadpisany a zawartość utracona. Warto o tym ostrzec.)
    if(os.path.isfile(nazwa_pliku)): #sprawdzenie czy istnieje plik o nazwie zawartej w zmiennej
        print(f"Plik o nazwie {nazwa_pliku} już istnieje. Czy chcesz go nadpisać? (t/n):") #informacja dla użytkownika
        if(input() != "t"): #pobranie wartości od użytkownika. sprawdzenie pod kątem zgodności z literałem "t"
            return #powrót z obecnej funkcji. ze względu na kontekst wykonywania, oznacza koniec programu.
    with open(nazwa_pliku, "w") as plik: # Otwiera plik o wskazanej nazwie. "w" oznacza tryb zapisu - 'write'. Konstrukcja 'with' oznacza zamknięcie pliku po zakończeniu operacji.
        plik.write(f">{identyfikator} {opis}\n") #zapis do pliku. literał to wcześniej przypisane zmienne.
        #ORIGINAL
        #plik.write(sekwencja_zmodyfikowana + "\n")
        #MODIFIED (W artykule Wikipedia w przykładzie FASTA linijki sekwencji dzielone są co 60 znaków, tu też warto to zaimplementować)
        indeks_sekwencji = 0 # zmienna. będzie oznaczać progresje przez sekwencję w miarę zapisywania do pliku.
        while(indeks_sekwencji < len(sekwencja_zmodyfikowana)): #pętla będzie trwać do momentu przejścia przez całość sekwencji zawierającej wstawione imię. każda iteracja to jedna linijka w pliku
            start_linijki = indeks_sekwencji #start_linijki oznacza indeks w sekwencji zapisywanej do pliku. indeks ten wskazuje na początek obecnie zapisywanej linijki
            indeks_sekwencji += 60 #indeks sekwencji przesunięty jest o 60 znaków od pozycji pierwotnej. odpowiada to 60 znakom które mają być zawarte w linijce
            plik.write(sekwencja_zmodyfikowana[start_linijki:indeks_sekwencji] + "\n") #zapisywany jest fragment sekwencji od indeksu start_linijki do indeks_sekwencji. literał kończy znak nowej linii. przekroczenie długości sekwencji przez indeks nie powoduje błędu, w literale zawarte jest tyle znaków ile jest dostępnych.
    print(f"\nSekwencja została zapisana do pliku: {nazwa_pliku}") #informacja dla użytkownika

    licznik_a = sekwencja.count('A') #metoda count() wykonana na ciągu znaków sekwencji zwraca liczbę wystąpień znaku podanego jako argument. metoda wykonywana jest na sekwencji bez wstawionego imienia.
    licznik_c = sekwencja.count('C')
    licznik_g = sekwencja.count('G')
    licznik_t = sekwencja.count('T')

    procent_a = (licznik_a / dlugosc) * 100 #wyliczenie wartości procentowej udziału wybranego nukleotydu spośród całej sekwencji
    procent_c = (licznik_c / dlugosc) * 100
    procent_g = (licznik_g / dlugosc) * 100
    procent_t = (licznik_t / dlugosc) * 100
    
    #ORIGINAL
    #stosunek_cg_at = (licznik_c + licznik_g) / (licznik_a + licznik_t) if (licznik_a + licznik_t) > 0 else 0
    #MODIFIED (Wartość udziału w procentach CG jest sposobem podawania stosunku w przykładzie w poleceniu.)
    stosunek_cg_at = (licznik_c + licznik_g) / dlugosc * 100

    print("\nStatystyki sekwencji:")
    print(f"Procent A: {procent_a:.2f}%") #wyświetlenie oraz zaokrąglenie do dwóch miejsc po przecinku wyliczonych wartości
    print(f"Procent C: {procent_c:.2f}%")
    print(f"Procent G: {procent_g:.2f}%")
    print(f"Procent T: {procent_t:.2f}%")
    #ORIGINAL
    #print(f"Stosunek (C+G)/(A+T): {stosunek_cg_at:.2f}")
    #MODIFIED (Ponownie, zmiana na sposób wyrażania informacji jak w przykładzie w poleceniu.)
    print(f"%CG: {stosunek_cg_at:.2f}")
    
    #ORIGINAL
    #MODIFIED (Rysowanie wykresu dla lepszej wizualizacji danych)
    plt.title("Udział nukleotydów w sekwencji") #nazwa/nagłówek wykresu
    plt.bar(nukleotydy, [procent_a, procent_c, procent_g, procent_t]) #określenie danych dla wykresu słupkowego (bar): etykiety (nukleotydy)i wartości zmiennych z procentami
    plt.ylabel("Udział (%)") #etykieta osi y
    plt.xlabel("Nukleotyd") #etykieta osi X
    plt.show() #pokazuje wykres
   

if __name__ == "__main__": # w tym miejscu zaczyna się program. warunek sprawdza czy skrypt jest uruchamiony 'samodzielnie' jako program a nie część innego skryptu
    generuj_sekwencje_fasta() #wywołuje główną funkcję
