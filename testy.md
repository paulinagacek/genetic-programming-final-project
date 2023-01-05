Zadania testowe dla systemu GP
- [x] 1.1.A Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 1. Poza liczbą 1 może też zwrócić inne liczby.
    - znajduje rozwiązanie w pierwszej iteracji

- [x] 1.1.B Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 789. Poza liczbą 789 może też zwrócić inne liczby.
    - znajduje rozwiązanie około 40stej iteracji

- [x] 1.1.C Program powinien wygenerować na wyjściu (na dowolnej pozycji w danych wyjściowych) liczbę 31415. Poza liczbą 3145 może też zwrócić inne liczby.

- [x] 1.1.D Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 1. Poza liczbą 1 może też zwrócić inne liczby.

- [x] 1.1.E Program powinien wygenerować na pierwszej pozycji na wyjściu liczbę 789. Poza liczbą 789 może też zwrócić inne liczby.

1.1.F Program powinien wygenerować na wyjściu liczbę jako jedyną liczbę 1. Poza liczbą 1 NIE powinien nic więcej wygenerować.

- [x] 1.2.A Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9]

- [x] 1.2.B Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby w zakresie [-9,9]

- [x] 1.2.C Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich sumę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]

- [x] 1.2.D Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich różnicę. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]

- [ ] 1.2.E Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) ich iloczyn. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [-9999,9999]

- [ ] 1.3.A Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) większą z nich. Na wejściu mogą być tylko całkowite liczby dodatnie w zakresie [0,9]

- [ ] 1.3.B Program powinien odczytać dwie pierwsze liczy z wejścia i zwrócić na wyjściu (jedynie) większą z nich. Na wejściu mogą być tylko całkowite liczby w zakresie [-9999,9999]

- [ ] 1.4.A Program powinien odczytać dziesięć pierwszych liczy z wejścia i zwrócić na wyjściu (jedynie) ich średnią arytmetyczną (zaokrągloną do pełnej liczby całkowitej). Na wejściu mogą być tylko całkowite liczby w zakresie [-99,99]

- [ ] 1.4.B Program powinien odczytać na początek z wejścia pierwszą liczbę (ma być to wartość nieujemna) a następnie tyle liczb (całkowitych) jaka jest wartość pierwszej odczytanej liczby i zwrócić na wyjściu (jedynie) ich średnią arytmetyczną zaokrągloną do pełnej liczby całkowitej (do średniej nie jest wliczana pierwsza odczytana liczba, która mówi z ilu liczb chcemy obliczyć średnią). Na wejściu mogą być tylko całkowite liczby w zakresie [-99,99], pierwsza liczba może być tylko w zakresie [0,99].


------------------------------------------
Finalne testy
------------------------------------------


Testy systemu
Ostatnim etapem prac nad systemami ewolucji GP jest zaprojektowanie sposobów uczenia (podział na etapy uczenia, zdefiniowanie funkcji dopasowania, itp.) wybranych problemów i przetestowanie możliwości rozwiązywania wybranych problemów przez stworzone przez Państwa systemy ewolucji GP.

Proszę co najmniej przetestować swój system co najmniej na następujących problemach:

Jeden wybrany problem z BenchmarkSuiteGECCO2015 z zakresu 1-5 (strona 9)
Jeden wybrany problem z BenchmarkSuiteGECCO2015 ze zbioru {6, 15, 17, 18, 21}
Jeden wybrany problem z BenchmarkSuiteGECCO2015 ze zbioru {26, 27, 28,}
Regresja symboliczna dla funkcji boolowskiej (opis poniżej)

Regresja symboliczna dla funkcji boolowskiej
Dana jest pewna funkcja boolowska (ang. boolean function) postaci:
f : {0,1}k → {0,1}
Czyli funkcja, której argumentem jest k zmiennych logicznych, a wyjściem jedna liczba logiczna (0/1)

Sprawdzić czy podczas procesu ewolucji GP uda się wygenerować program odtwarzający działanie tej funkcji boolowskiej.
Jako dane uczące (fitness cases) należy podać odwzorowanie wszystkich możliwych wektorów wejściowe (będzie ich 2k) na wartość wyjściową (0/1)

Funkcje boolowskie dla k=1:

D0
NOT(D0)

Przykładowe funkcje boolowskie dla k=2:

D0 AND D1
D0 OR D1
D0 XOR D1

itd.

Proszę sprawdzić czy Państwa system jest w stanie wygenerować programy odtwarzające funkcje boolowskie dla k=1, k=2, k=3,...., k=10

Ponieważ funkcję boolowską można reprezentować jako tabelę prawdy (dla danego k, tabela będzie miała k kolumn reprezentujących poszczególne dane wejściowe D0,D1,...,Dk; jedną kolumnę reprezentującą wynik funkcji 0/1; oraz 2k wierszy reprezentujących poszczególne kombinacje wartości D0,...,Dk), można wygenerować sobie losowo ta tabelę (tzn. kolumnę z wynikami funkcji) i traktować ją jako fitness cases.

[opcjonalnie] Santa fe trail problem


[opcjonalnie] Różne benchmarki
https://geneticprogramming.com/benchmarks/