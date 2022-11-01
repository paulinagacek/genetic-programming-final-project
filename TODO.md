### Zadania 1) 
Przygotować wstępną gramatykę mini języka służącego do wykonywania programów w GP (jest to część projektu końcowego). Gramatyka powinna pozwolić na zapisanie całego programu jako drzewa (analogicznego do drzewa reprezentującego wyrażenia arytmetyczne w regresji symbolicznej np. w TinyGP). Język powinien posiadać m.in.:

- [ ] instrukcję pętli
- [ ] instrukcję warunkową
- [ ] instrukcja złożona/bloku programu (jak blok w nawiasach klamrowych w języku c/c++/Java)
- [ ] zmienne, stałe i operacje arytmetyczne + logiczne
- [ ] operacja wczytywania z wejścia i wypisywania na wyjście

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

pętle, bloki, crossover, funkcja evolve, value do node, nawiasy ( ), operacje logiczne, ignorowanie whitespace w gramatyce
zapisywanie programu i drzewa do pliku, gramatyka, cin/cout

deserializacja na koniec