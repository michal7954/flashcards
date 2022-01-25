# flashcards
Aplikacja do wielokrotnego powtarzania słówek.

Aby słówko zostało uznane za nauczone należy zaliczyć je 5 razy z rzędu.
Kiedy pierwszy raz słówko zostanie zaliczone, aplikacja zapyta o nie po 3 dniach. Potem analogicznie po 7, 14 i 31 dniach. Niezaliczenie któregoś z etapów powoduje powrót do poziomu 0 :(

Obsługa:
1. W pliku data.txt wprowadzić listę słówek w formacie
słówko;definicja
angielski;polski
go for;wybierać, sięgać po
Jedna linijka to jedno słówko. Aplikacja utworzy dwie dodatkowe kolumny: poziom postępu (0-4) i datę następnego odpytywania.
2. Plik powinien być zapisany w kodowaniu ANSI dla prawidłowego wyświetlania polskich znaków. Załączony plik ma właściwe kodowanie. Kodowanie można zmienić w Notantik->Plik->Zapisz jako->Kodowanie
3. Uruchomić flashcards.exe
4. Nie modyfikować pliku data.txt podczas działania aplikacji.
5. Po zamknięciu aplikacji można dodawać, modyfikować i usuwać słówka z listy.