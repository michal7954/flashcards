# flashcards
Aplikacja do wielokrotnego powtarzania słówek.

# Zasady

Aby słówko zostało uznane za nauczone należy zaliczyć je 5 razy z rzędu.
Kiedy pierwszy raz słówko zostanie zaliczone, aplikacja zapyta o nie po 3 dniach. Potem analogicznie po 7, 14 i 31 dniach. Niezaliczenie któregoś z etapów powoduje powrót do poziomu 0 :( Kolejne powtórzenie słówka będzie miało miejsce następnego dnia.

Danego dnia słówka są sortowane od najwyższego poziomu (etapu nauki). Dla słówek o tym samym poziomie jest zachowana kolejność z pliku.

Kiedy wpiszemy słowo błędnie, pojawia się informacja o liczbie różnic względem poprawnego słowa. Jedna różnica oznacza konieczność dodania, usunięcia lub modyfikacji jednej z liter.

Za każdym razem, po podaniu lub wyświetleniu poprawnego słówka, użytkownik podejmuje decyzję czy system ma zaliczyć słówko.


# Obsługa programu:

1. W pliku data.txt (kodowanie UTF-8) wprowadzić listę słówek w formacie
słówko;definicja
angielski;polski
the complete opposite;całkowite przeciwieństwo

Jedna linijka to jedno słówko. Linie bez średników są ignorowane. Aplikacja utworzy dwie dodatkowe kolumny: poziom postępu (0-4) i datę następnego odpytywania.
Plik zawiera już przykładową listę słówkek.

2. Uruchomić flashcards.exe

3. Nie modyfikować pliku data.txt podczas działania aplikacji. Po zamknięciu aplikacji można dodawać, modyfikować i usuwać słówka z listy.
