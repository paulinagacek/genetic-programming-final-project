Zrobione:
- [x] finess jako parametr
- [x] dodać mechanizm zapobiegający wpadaniu w lokalne optimum - dodane patience czyli liczba iteracji po której na nowo jest generowane 40% populacji
- [x] naprawienie błędu OverflowError: integer division result too large for a float
- [x] naprawienie błędu z wyświetlaniem pustej tablicy - okazało się że problem był znowu z kopiowaniem tablic - interpreter 
    działał na orginale i po wczytaniu wartości z tablicy usuwał ją sobie i potem inne programy miały puste inputy

Do Zrobienia:
- [ ] dodać osobne przejście po kodzie sprawdzające składnie, które nie wykonuje kodu jak są błędy
- [ ] zmiana deepcopy tree na bfs
- [ ] podrasowac algorytmy
- [ ] popracowac nad crossoverem
- [ ] dodac w wierzchołakch drzewa informacje o liczbie wszystkich jego dzieci i szansa na mutacje to 1/2^sqrt(liczba dzieci)
- [ ] mutacja całego poddrzewa
- [ ] dynamiczne zmienianie parametrow szansy na mutacje i crossover
- [ ] dodanie opcji, żeby najsilniejszy potomek zawsze przechodził do następnej generacji