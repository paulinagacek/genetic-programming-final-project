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