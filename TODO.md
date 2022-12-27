### Zadania 1) 
Przygotować wstępną gramatykę mini języka służącego do wykonywania programów w GP (jest to część projektu końcowego). Gramatyka powinna pozwolić na zapisanie całego programu jako drzewa (analogicznego do drzewa reprezentującego wyrażenia arytmetyczne w regresji symbolicznej np. w TinyGP). Język powinien posiadać m.in.:

- [x] instrukcję pętli
- [x] instrukcję warunkową
- [x] instrukcja złożona/bloku programu (jak blok w nawiasach klamrowych w języku c/c++/Java)
- [x] zmienne, stałe i operacje arytmetyczne + logiczne
- [x] operacja wczytywania z wejścia i wypisywania na wyjście
- [ ] Przetestować gramatykę w programie do generowania parserów, który będzie używany w projekcie (np. w Antlr)

### Zadanie 2) 
Przygotować bibliotekę pozwalającą na generowanie i ewolucję programów w opracowanym mini języku. Biblioteka powinna posiadać funkcje analogiczne do tych z TinyGP m.in.:

- [ ] generowanie losowych programów (drzew) o zadanej wielkości +
- [ ] operację krzyżowania dwóch drzew/programów +
- [x] operację mutacji +
- [x] możliwość testowania programów (obliczenia wartości funkcji przystosowania) na podstawie wektora danych wejściowych i danych wyjściowych. (Na razie nie implementujemy żadnej konkretnej funkcji przystosowania, będzie ona tworzona dla konkretnego problemu) + 
- [x] selekcję osobników (programów) na podstawie wartości funkcji przystosowania (na razie selekcja turniejowa za zadawaną liczbą zawodników np. 2, 5, 10, itd.)
- [ ] serializację i deserializację (zapisanie/wczytanie) zadanego drzewa (programu)

**UWAGA: Na razie nie implementujemy wykonywania programów w mini języku (czyli interpretera, translatora czy kompilatora dla mini języka).**

pętle, bloki, crossover, funkcja evolve, value do node, nawiasy ( ), operacje logiczne,
zapisywanie programu i drzewa do pliku, gramatyka, cin/cout

deserializacja na koniec

corssover:
losujemy z parenta 1 miejsce  do przeszczepu
losujemy z parenta 2 miejsce do przeszeczpu
jesli typy sie nie zgadzaja
jesli w n_parent_2(stała) prob nie uda sie znalezc miejsca to losujemy nowe miejsce z parenta 1
jesli w n_parent_1(stała) prob nie uda sie znalezc miejsca to zwracamy osobnik z lepszym fitness

ewolucja tak jak w tiny gp

Paweł:
- [ ] funkcja evolve
- [ ] crossover
- [ ] zapisywanie programu i drzewa do pliku
- [ ] przetestowac gramatyke w antlr

Paulina:
- [x] pętle
- [x] bloki
- [ ] value do node
- [ ] nawiasy ( )
- [x] operacje logiczne

# Zbudowanie parsera
- [ ] dodać osobne przejście po kodzie sprawdzające składnie, które nie wykonuje kodu jak są błędy


# Problemy
```
    File "C:\Users\pauli\OneDrive\Pulpit\5ty SEM\genetic-programming-vol2\src\Converter.py", line 85, 
    in get_proper_node
        return Converter.get_loop(node)
    File "C:\Users\pauli\OneDrive\Pulpit\5ty SEM\genetic-programming-vol2\src\Converter.py", line 66, 
    in get_loop
    right_child = Converter.get_proper_node(node.children[1])
    File "C:\Users\pauli\OneDrive\Pulpit\5ty SEM\genetic-programming-vol2\src\Converter.py", line 80, 
    in get_proper_node
    output += Converter.get_proper_node(child)
    File "C:\Users\pauli\OneDrive\Pulpit\5ty SEM\genetic-programming-vol2\src\Converter.py", line 85, in get_proper_node
    return Converter.get_loop(node)
    maximum recursion depth exceeded while getting the str of an object
```

- zmiana deepcopy tree na bfs
- podrasowac algorytmy
- popracowac nad crossoverem
- dodac w wierzchołakch drzewa informacje o liczbie wszystkich jego dzieci i szansa na mutacje to 1/2^sqrt(liczba dzieci)
- mutacja poddrzewa
- finess jako parametr
- dynamiczne zmienianie parametrow szansy na mutacje i crossover
- naprawić błąd:
```
C:\Users\gacekpau\OneDrive - Intel Corporation\Desktop\3 ROK ISI\genetyczne-vol2>python runGP.py >> log789_5.txt 
Traceback (most recent call last):
  File "C:\Users\gacekpau\OneDrive - Intel Corporation\Desktop\3 ROK ISI\genetyczne-vol2\runGP.py", line 16, in <module>
    gp.evolve()
  File "C:\Users\gacekpau\OneDrive - Intel Corporation\Desktop\3 ROK ISI\genetyczne-vol2\src\GP.py", line 283, in evolve
    fitness_copy[weakest_idx] = self.compute_fitness(child_str)
  File "C:\Users\gacekpau\OneDrive - Intel Corporation\Desktop\3 ROK ISI\genetyczne-vol2\src\GP.py", line 78, in compute_fitness
    fitness += sum_calculator(prints,
  File "C:\Users\gacekpau\OneDrive - Intel Corporation\Desktop\3 ROK ISI\genetyczne-vol2\src\GP.py", line 25, in sum_calculator
    fitness += -abs((np.min(np.array(received_outs) -
OverflowError: integer division result too large for a float
```

Paulina:
- [x] naprawienie błędu z wyświetlaniem pustej tablicy - okazało się że problem był znowu z kopiowaniem tablic - interpreter 
    działał na orginale i po wczytaniu wartości z tablicy usuwał ją sobie i potem inne programy miały puste inputy
- [ ] dodanie opcji, żeby najsilniejszy potomek zawsze przechodził do następnej generacji
- [x] dodać mechanizm zapobiegający wpadaniu w lokalne optimum - dodane patience czyli liczba iteracji po której na nowo jest generowane 40% populacji
- [x] naprawienie błędu OverflowError: integer division result too large for a float